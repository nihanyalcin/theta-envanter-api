# -*- coding: utf-8 -*-
"""Flask blueprint: POST /erteleme-haritasi (site formu JSON).

Ortam değişkenleri (diğer envanterlerle ortak): BREVO_API_KEY veya SMTP_*, NIHAN_EMAIL, CORS_ORIGIN
  URUN_KODU_ERTELE  (erişim kodları; varsayılan ERTELE2026,UCLU2026)

Form alanları: ad, eposta, kod, i1..i8, e1..e8, b1..b8, p1..p8, k1..k8, r1 (0-4), r2 (a-c), z1..z8, cumle, kvkk
Risk akışı: keyif kaybı ya da ciddi artış -> rapor gider, dürüstçe bölümü genişler;
            keyif kaybı + artış -> inceleme (rapor Nihan'a, danışana bekleme maili);
            serbest cümlede risk ifadesi -> rapor üretilmez, danışana kısa destek maili, Nihan'a ham cevaplar + koç notu.
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

bp = Blueprint("erteleme", __name__)
log = logging.getLogger("erteleme")

KODLAR = re.compile(r"^([iebpk][1-8]|z[1-8]|r[1-2])$")

DESTEK_MAIL = """Merhaba {ad},

Cevapların ulaştı; teşekkür ederim.

Yazdığın cümlede, bir raporun değil bir insanın duyması gereken bir şey var. Bu yüzden otomatik rapor üretmedim; cevaplarını ben okuyorum ve sana bizzat yazacağım. İstersen bu maile tek kelime cevap vermen yeter.

Eğer şu an kendini güvende hissetmiyorsan lütfen beklemeden 112'yi ara, güvendiğin birine haber ver ya da en yakın sağlık kuruluşuna git. Bunu söylemek görevim; bu anda yalnız olmak zorunda değilsin.

Nihan
thetakapisi.com.tr"""


def normalize(raw):
    cev = {}
    for k, v in raw.items():
        if not KODLAR.match(k):
            continue
        s = str(v or "").strip()
        if (k[0] in "iebpk" and int(k[1]) <= 5) or k == "r1":   # F ölçeği
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


@bp.route("/erteleme-haritasi", methods=["POST", "OPTIONS"])
def erteleme_haritasi():
    if request.method == "OPTIONS":
        return ("", 204)
    payload = request.get_json(force=True, silent=True) or {}
    raw = {str(k).lower(): v for k, v in payload.items()}
    ad = str(raw.get("ad", "") or "").strip() or "Sen"
    eposta = str(raw.get("eposta", "") or "").strip()
    kod = str(raw.get("kod", "") or "").strip().upper()
    gecerli = [k.strip().upper() for k in os.environ.get("URUN_KODU_ERTELE", "ERTELE2026,UCLU2026").split(",") if k.strip()]
    nihan = os.environ.get("NIHAN_EMAIL", "nihan@thetakapisi.com.tr")

    if not eposta:
        return jsonify({"ok": False, "hata": "eposta yok"}), 400
    if not (os.environ.get("SMTP_PASS") or os.environ.get("BREVO_API_KEY")):
        log.error("Mail ayarları eksik; rapor üretilmedi (%s)", eposta)
        return jsonify({"ok": False, "hata": "smtp"}), 500
    if gecerli and kod not in gecerli:
        mail_gonder(eposta, "Erteleme Haritası: erişim kodu geçersiz",
                    "Merhaba %s,\n\nGirdiğin erişim kodu tanınmadı. Shopier'den gelen erişim kartındaki kodu kontrol edip formu yeniden doldurabilirsin. Sorun sürerse bu maile cevap yaz.\n\nNihan" % ad)
        return jsonify({"ok": False, "hata": "kod"}), 200

    cev = normalize(raw)
    sonuc = puanla(cev)
    tmp = tempfile.mkdtemp()
    koc_yolu = os.path.join(tmp, "koc-notu.pdf")
    koc_notu_pdf(ad, eposta, sonuc, koc_yolu)

    if sonuc["rapor_yok"]:
        mail_gonder(eposta, "Erteleme Haritası: cevapların ulaştı", DESTEK_MAIL.format(ad=ad))
        mail_gonder(nihan, "ACİL · RAPOR ÜRETİLMEDİ · Erteleme Haritası · %s" % ad,
                    "Serbest cümlede risk ifadesi var. Danışana destek maili gitti; rapor üretilmedi. Mümkünse bugün ulaş.\n\nCümle: %s\n\nHam cevaplar:\n\n%s" % (sonuc["cumle"], _ham_metin(ad, eposta, cev)),
                    ekler=[(koc_yolu, "koc-notu.pdf")])
        return jsonify({"ok": True, "durum": "destek"}), 200

    rapor_yolu = os.path.join(tmp, "erteleme-haritasi-%s.pdf" % re.sub(r"[^a-z0-9]+", "-", ad.lower()))
    rapor_pdf(ad, sonuc, rapor_yolu, whatsapp_link=os.environ.get("WHATSAPP_LINK_ERTELE", "https://wa.me/905324944692?text=Erteleme%20Haritas%C4%B1%20g%C3%B6r%C3%BC%C5%9Fmesi%20istiyorum"))

    if sonuc["incele"]:
        mail_gonder(eposta, "Erteleme Haritası raporun hazırlanıyor",
                    "Merhaba %s,\n\nCevapların ulaştı. Raporunu bizzat gözden geçiriyorum; 24 saat içinde bu adrese gelecek.\n\nNihan" % ad)
        mail_gonder(nihan, "İNCELEME BEKLİYOR · Erteleme Haritası · %s" % ad,
                    "Keyif kaybı + erteleme artışı işaretlendi. Rapor ve koç notu ekte. Onaylarsan raporu danışana sen gönder: %s" % eposta,
                    ekler=[(rapor_yolu, "erteleme-haritasi.pdf"), (koc_yolu, "koc-notu.pdf")])
        return jsonify({"ok": True, "durum": "inceleme"}), 200

    mail_gonder(eposta, "Erteleme Haritası raporun hazır",
                "Merhaba %s,\n\nErteleme Haritası raporun ekte. İki kere oku: ilkinde sadece bak, ikincisinde en çok rahatsız eden cümlenin altını çiz. Sonra yarın sabahın ilk 10 dakikasını rapordaki başlatıcıya ver.\n\nRaporu birlikte okumak istersen son sayfadaki linkten yaz.\n\nSevgiyle,\nNihan\nthetakapisi.com.tr" % ad,
                ekler=[(rapor_yolu, "erteleme-haritasi.pdf")])
    mail_gonder(nihan, "Yeni Erteleme Haritası · %s" % ad, "Rapor gönderildi: %s\nKoç notu ekte.%s" % (eposta, "\nNot: dürüstçe bölümü genişletildi (risk işareti)." if sonuc["genis_durustce"] else ""),
                ekler=[(rapor_yolu, "erteleme-haritasi.pdf"), (koc_yolu, "koc-notu.pdf")])
    return jsonify({"ok": True, "durum": "gonderildi"}), 200
