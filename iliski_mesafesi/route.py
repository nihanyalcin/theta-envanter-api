# -*- coding: utf-8 -*-
"""Flask blueprint: POST /iliski-mesafesi (site formu JSON).

Ortam değişkenleri (Sınır Haritası ile ortak): BREVO_API_KEY veya SMTP_*, NIHAN_EMAIL, WHATSAPP_LINK, CORS_ORIGIN
  URUN_KODU_MESAFE  (erişim kodları; varsayılan MESAFE2026,IKILI2026)

Form alanları: ad, eposta, kod, durum (a/b), y1..y8, u1..u8, s1..s8, o1..o8, r1 (0-4), r2 (a-c), r3 (a-d), z1..z8, cumle, kvkk
Risk akışı: 1 bayrak -> inceleme (rapor Nihan'a, danışana bekleme maili);
            fiziksel (r3=d) ya da 2+ bayrak -> rapor üretilmez, danışana kısa destek maili, Nihan'a ham cevaplar + koç notu.
"""
import os, re, tempfile, logging
from flask import Blueprint, request, jsonify

from .puanla import puanla
from .rapor import rapor_pdf, koc_notu_pdf
from .sorular import F_SIKLAR
try:
    from sinir_haritasi.sinir_haritasi.route import mail_gonder   # repo yerleşimi
except ImportError:  # yerel test
    from sinir_haritasi.route import mail_gonder

bp = Blueprint("iliski_mesafesi", __name__)
log = logging.getLogger("iliski_mesafesi")

KODLAR = re.compile(r"^(y[1-8]|u[1-8]|s[1-8]|o[1-8]|z[1-8]|r[1-3]|durum)$")

DESTEK_MAIL = """Merhaba {ad},

Cevapların ulaştı; teşekkür ederim, bunları yazmak kolay değil.

Yazdıklarında, bir raporun değil bir insanın okuması gereken şeyler var. Bu yüzden bu envanter için otomatik rapor üretmedim; onun yerine ben okuyorum ve istersen seninle konuşmak isterim. Bu maile tek kelime cevap yazman yeter.

Eğer şu an güvende hissetmiyorsan:
· 183 Sosyal Destek Hattı (7/24)
· 155 Polis İmdat
· KADES uygulaması (tek dokunuşla konum bildirir)

Bunları yazmak görevim; gerisi senin kararın ve bu kararda yalnız değilsin.

Nihan
thetakapisi.com.tr"""


def normalize(raw):
    cev = {}
    for k, v in raw.items():
        if not KODLAR.match(k):
            continue
        s = str(v or "").strip()
        if (k[0] in "yuso" and int(k[1]) <= 5) or k == "r1":   # F ölçeği
            idx = next((i for i, m in enumerate(F_SIKLAR) if s.lower().startswith(m.lower()[:12])), None)
            if idx is None and s.isdigit():
                idx = int(s)
            cev[k] = idx if idx is not None else 0
        else:
            cev[k] = s[:1].lower()
    cev["cumle"] = str(raw.get("cumle", "") or "")
    return cev


def _ham_metin(ad, eposta, cev):
    satir = ["%s <%s>" % (ad, eposta), ""]
    for k in sorted(cev):
        satir.append("%s: %s" % (k, cev[k]))
    return "\n".join(satir)


@bp.after_request
def _cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = os.environ.get("CORS_ORIGIN", "https://thetakapisi.com.tr")
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return resp


@bp.route("/iliski-mesafesi", methods=["POST", "OPTIONS"])
def iliski_mesafesi():
    if request.method == "OPTIONS":
        return ("", 204)
    payload = request.get_json(force=True, silent=True) or {}
    raw = {str(k).lower(): v for k, v in payload.items()}
    ad = str(raw.get("ad", "") or "").strip() or "Sen"
    eposta = str(raw.get("eposta", "") or "").strip()
    kod = str(raw.get("kod", "") or "").strip().upper()
    gecerli = [k.strip().upper() for k in os.environ.get("URUN_KODU_MESAFE", "MESAFE2026,IKILI2026").split(",") if k.strip()]
    nihan = os.environ.get("NIHAN_EMAIL", "nihan@thetakapisi.com.tr")

    if not eposta:
        return jsonify({"ok": False, "hata": "eposta yok"}), 400
    if not (os.environ.get("SMTP_PASS") or os.environ.get("BREVO_API_KEY")):
        log.error("Mail ayarları eksik; rapor üretilmedi (%s)", eposta)
        return jsonify({"ok": False, "hata": "smtp"}), 500
    if gecerli and kod not in gecerli:
        mail_gonder(eposta, "İlişki Mesafesi Haritası: erişim kodu geçersiz",
                    "Merhaba %s,\n\nGirdiğin erişim kodu tanınmadı. Shopier'den gelen erişim kartındaki kodu kontrol edip formu yeniden doldurabilirsin. Sorun sürerse bu maile cevap yaz.\n\nNihan" % ad)
        return jsonify({"ok": False, "hata": "kod"}), 200

    cev = normalize(raw)
    sonuc = puanla(cev)
    tmp = tempfile.mkdtemp()
    koc_yolu = os.path.join(tmp, "koc-notu.pdf")
    koc_notu_pdf(ad, eposta, sonuc, koc_yolu)

    if sonuc["rapor_yok"]:
        mail_gonder(eposta, "İlişki Mesafesi Haritası: cevapların ulaştı", DESTEK_MAIL.format(ad=ad))
        mail_gonder(nihan, "RAPOR ÜRETİLMEDİ · İlişki Mesafesi · %s" % ad,
                    "Güvenlik kuralı tetiklendi (fiziksel ya da 2+ bayrak). Danışana destek maili gitti; rapor üretilmedi.\n\nHam cevaplar:\n\n" + _ham_metin(ad, eposta, cev),
                    ekler=[(koc_yolu, "koc-notu.pdf")])
        return jsonify({"ok": True, "durum": "destek"}), 200

    rapor_yolu = os.path.join(tmp, "iliski-mesafesi-%s.pdf" % re.sub(r"[^a-z0-9]+", "-", ad.lower()))
    rapor_pdf(ad, sonuc, rapor_yolu, whatsapp_link=os.environ.get("WHATSAPP_LINK_MESAFE", "https://wa.me/905324944632?text=%C4%B0li%C5%9Fki%20Mesafesi%20g%C3%B6r%C3%BC%C5%9Fmesi%20istiyorum"))

    if sonuc["incele"]:
        mail_gonder(eposta, "İlişki Mesafesi Haritası raporun hazırlanıyor",
                    "Merhaba %s,\n\nCevapların ulaştı. Raporunu bizzat gözden geçiriyorum; 24 saat içinde bu adrese gelecek.\n\nNihan" % ad)
        mail_gonder(nihan, "İNCELEME BEKLİYOR · İlişki Mesafesi · %s" % ad,
                    "Risk kuralı tetiklendi (1 bayrak). Rapor ve koç notu ekte. Onaylarsan raporu danışana sen gönder: %s" % eposta,
                    ekler=[(rapor_yolu, "iliski-mesafesi-haritasi.pdf"), (koc_yolu, "koc-notu.pdf")])
        return jsonify({"ok": True, "durum": "inceleme"}), 200

    mail_gonder(eposta, "İlişki Mesafesi Haritası raporun hazır",
                "Merhaba %s,\n\nİlişki Mesafesi Haritası raporun ekte. İki kere oku: ilkinde sadece bak, ikincisinde en çok rahatsız eden cümlenin altını çiz.\n\nRaporu birlikte okumak istersen son sayfadaki linkten yaz.\n\nSevgiyle,\nNihan\nthetakapisi.com.tr" % ad,
                ekler=[(rapor_yolu, "iliski-mesafesi-haritasi.pdf")])
    mail_gonder(nihan, "Yeni İlişki Mesafesi · %s" % ad, "Rapor gönderildi: %s\nKoç notu ekte." % eposta,
                ekler=[(rapor_yolu, "iliski-mesafesi-haritasi.pdf"), (koc_yolu, "koc-notu.pdf")])
    return jsonify({"ok": True, "durum": "gonderildi"}), 200
