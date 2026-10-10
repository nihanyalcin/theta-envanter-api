# -*- coding: utf-8 -*-
"""Flask blueprint: POST /sinir-haritasi (Tally webhook).

Ortam değişkenleri:
  SMTP_HOST, SMTP_PORT (465), SMTP_USER (nihan@thetakapisi.com.tr), SMTP_PASS
  NIHAN_EMAIL   (varsayılan nihan@thetakapisi.com.tr)
  URUN_KODU     (erişim kartındaki kod; birden fazlaysa virgülle)
  WHATSAPP_LINK (örn. https://wa.me/90XXXXXXXXXX?text=...)
  SH_SHEET_ID   (isteğe bağlı; gspread ile satır ekler)
  MAILERLITE_API_KEY, MAILERLITE_GROUP_ID (isteğe bağlı)
  TALLY_SIGNING_SECRET (isteğe bağlı; Tally webhook imzası)
"""
import os, re, json, hmac, hashlib, smtplib, tempfile, logging
from email.message import EmailMessage
from datetime import datetime
from flask import Blueprint, request, jsonify

from .puanla import puanla
from .rapor import rapor_pdf, koc_notu_pdf

bp = Blueprint("sinir_haritasi", __name__)
log = logging.getLogger("sinir_haritasi")

ALAN_KODLARI = re.compile(r"^(a[1-8]|i[1-8]|r[1-8]|e[1-8]|n[1-8]|z[1-8])$")


def tally_cevaplari(payload):
    """Tally webhook JSON'unu {label: value} sözlüğüne çevirir.
    Multiple choice: value = seçilen option id(leri); options listesinden metne çevrilir.
    Etiket (label) formdaki alan adıdır: ad, eposta, kod, a1..n8, z1..z8, cumle, kvkk."""
    fields = payload.get("data", {}).get("fields", [])
    out = {}
    for f in fields:
        label = (f.get("label") or "").strip().lower()
        val = f.get("value")
        opts = f.get("options") or []
        if isinstance(val, list) and opts:
            metin = [o.get("text", "") for o in opts if o.get("id") in val]
            val = metin[0] if metin else ""
        out[label] = val
    return out


def normalize(raw):
    """Etiketli ham cevapları puanlama sözlüğüne çevirir."""
    cev = {}
    for k, v in raw.items():
        if not ALAN_KODLARI.match(k):
            continue
        s = str(v or "").strip()
        if k[0] in "airen" and int(k[1]) <= 5:          # F: ölçek, sıradan oku
            # Tally metni gelir; indeksini bul
            from .sorular import F_SIKLAR
            idx = next((i for i, m in enumerate(F_SIKLAR) if s.lower().startswith(m.lower()[:12])), None)
            if idx is None and s.isdigit():
                idx = int(s)
            cev[k] = idx if idx is not None else 0
        else:                                           # S ve Z: "a) ..." ilk harf
            cev[k] = s[:1].lower()
    cev["cumle"] = str(raw.get("cumle", "") or "")
    return cev


def mail_gonder(kime, konu, metin, ekler=(), bcc=None):
    host = os.environ["SMTP_HOST"]; port = int(os.environ.get("SMTP_PORT", "465"))
    user = os.environ["SMTP_USER"]; pw = os.environ["SMTP_PASS"]
    msg = EmailMessage()
    msg["From"] = "Nihan · Theta Kapısı <%s>" % user
    msg["To"] = kime
    if bcc:
        msg["Bcc"] = bcc
    msg["Subject"] = konu
    msg.set_content(metin)
    for yol, ad in ekler:
        with open(yol, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=ad)
    with (smtplib.SMTP_SSL(host, port, timeout=30) if port == 465 else smtplib.SMTP(host, port, timeout=30)) as s:
        (port == 465 or s.starttls()); s.login(user, pw)
        s.send_message(msg)


def sheets_satir(satir):
    sid = os.environ.get("SH_SHEET_ID")
    if not sid:
        return
    try:
        import gspread
        gc = gspread.service_account(filename=os.environ.get("GOOGLE_SA_JSON", "service_account.json"))
        ws = gc.open_by_key(sid).worksheet("sinir")
        ws.append_row(satir, value_input_option="USER_ENTERED")
    except Exception as e:
        log.warning("Sheets yazılamadı: %s", e)


def mailerlite_ekle(eposta, ad):
    key = os.environ.get("MAILERLITE_API_KEY"); grp = os.environ.get("MAILERLITE_GROUP_ID")
    if not key or not grp:
        return
    try:
        import requests
        requests.post("https://connect.mailerlite.com/api/subscribers",
                      headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
                      json={"email": eposta, "fields": {"name": ad}, "groups": [grp]}, timeout=15)
    except Exception as e:
        log.warning("MailerLite eklenemedi: %s", e)


def imza_gecerli(req):
    secret = os.environ.get("TALLY_SIGNING_SECRET")
    if not secret:
        return True
    gelen = req.headers.get("Tally-Signature", "")
    beklenen = hmac.new(secret.encode(), req.get_data(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(gelen, beklenen)


@bp.after_request
def _cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = os.environ.get("CORS_ORIGIN", "https://thetakapisi.com.tr")
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return resp


@bp.route("/sinir-haritasi", methods=["POST", "OPTIONS"])
def sinir_haritasi():
    if request.method == "OPTIONS":
        return ("", 204)
    payload = request.get_json(force=True, silent=True) or {}
    if "data" in payload and "fields" in payload.get("data", {}):      # Tally webhook
        if not imza_gecerli(request):
            return jsonify({"ok": False, "hata": "imza"}), 401
        raw = tally_cevaplari(payload)
    else:                                                               # site formu (JSON: {ad, eposta, kod, a1.., cumle})
        raw = {str(k).lower(): v for k, v in payload.items()}
    ad = str(raw.get("ad", "") or "").strip() or "Sen"
    eposta = str(raw.get("eposta", "") or "").strip()
    kod = str(raw.get("kod", "") or "").strip().upper()
    gecerli = [k.strip().upper() for k in os.environ.get("URUN_KODU", "").split(",") if k.strip()]
    nihan = os.environ.get("NIHAN_EMAIL", "nihan@thetakapisi.com.tr")

    if not eposta:
        return jsonify({"ok": False, "hata": "eposta yok"}), 400
    if gecerli and kod not in gecerli:
        mail_gonder(eposta, "Sınır Haritası: erişim kodu geçersiz",
                    "Merhaba %s,\n\nGirdiğin erişim kodu tanınmadı. Shopier'den gelen erişim kartındaki kodu kontrol edip formu yeniden doldurabilirsin. Sorun sürerse bu maile cevap yaz.\n\nNihan" % ad)
        return jsonify({"ok": False, "hata": "kod"}), 200

    cev = normalize(raw)
    sonuc = puanla(cev)
    tmp = tempfile.mkdtemp()
    rapor_yolu = os.path.join(tmp, "sinir-haritasi-%s.pdf" % re.sub(r"[^a-z0-9]+", "-", ad.lower()))
    koc_yolu = os.path.join(tmp, "koc-notu.pdf")
    rapor_pdf(ad, sonuc, rapor_yolu, whatsapp_link=os.environ.get("WHATSAPP_LINK", "https://wa.me/"))
    koc_notu_pdf(ad, eposta, sonuc, koc_yolu)

    y = sonuc["alan_yuzde"]; t = sonuc["tip_yuzde"]
    sheets_satir([datetime.now().strftime("%Y-%m-%d %H:%M"), ad, eposta, kod,
                  y["A"], y["I"], y["R"], y["E"], y["N"], t["S"], t["K"], t["G"], t["T"],
                  sonuc["baskin"], ",".join(sonuc["oruntu"]), "İNCELE" if sonuc["incele"] else "", ""])
    mailerlite_ekle(eposta, ad)

    if sonuc["incele"]:
        mail_gonder(eposta, "Sınır Haritası raporun hazırlanıyor",
                    "Merhaba %s,\n\nCevapların ulaştı. Raporunu bizzat gözden geçiriyorum; 24 saat içinde bu adrese gelecek.\n\nNihan" % ad)
        mail_gonder(nihan, "İNCELEME BEKLİYOR · Sınır Haritası · %s" % ad,
                    "Risk kuralı tetiklendi. Rapor ve koç notu ekte. Onaylarsan raporu danışana sen gönder: %s" % eposta,
                    ekler=[(rapor_yolu, "sinir-haritasi.pdf"), (koc_yolu, "koc-notu.pdf")])
        return jsonify({"ok": True, "durum": "inceleme"}), 200

    mail_gonder(eposta, "Sınır Haritası raporun hazır",
                "Merhaba %s,\n\nSınır Haritası raporun ekte. İki kere oku: ilkinde sadece bak, ikincisinde en çok rahatsız eden cümlenin altını çiz.\n\nRaporu birlikte okumak istersen son sayfadaki linkten yaz.\n\nSevgiyle,\nNihan\nthetakapisi.com.tr" % ad,
                ekler=[(rapor_yolu, "sinir-haritasi.pdf")])
    mail_gonder(nihan, "Yeni Sınır Haritası · %s" % ad, "Rapor gönderildi: %s\nKoç notu ekte." % eposta,
                ekler=[(rapor_yolu, "sinir-haritasi.pdf"), (koc_yolu, "koc-notu.pdf")])
    return jsonify({"ok": True, "durum": "gonderildi"}), 200
