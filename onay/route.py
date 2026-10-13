# -*- coding: utf-8 -*-
"""Flask blueprint: POST /onay-haritasi (site formu JSON).

Ortam değişkenleri (diğer envanterlerle ortak): BREVO_API_KEY veya SMTP_*, NIHAN_EMAIL, CORS_ORIGIN
  URUN_KODU_ONAY  (erişim kodları; varsayılan ONAY2026)

Form alanları: ad, eposta, kod, i1..i8, a1..a8, p1..p8, c1..c8, g1..g8, r1 (0-4), r2 (a-c), z1..z8, cumle, kvkk
Risk akışı: değersizlik ya da donma -> rapor gider, dürüstçe bölümü genişler;
            değersizlik + donma ya da güvensizlik -> inceleme (rapor Nihan'a, danışana bekleme maili);
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

bp = Blueprint("onay", __name__)
log = logging.getLogger("onay")

KODLAR = re.compile(r"^([iapcg][1-8]|z[1-8]|r[1-2])$")

DESTEK_MAIL = """Merhaba {ad},

Cevapların ulaştı; teşekkür ederim.

Yazdığın cümlede, bir raporun değil bir insanın duyması gereken bir şey var. Bu yüzden otomatik rapor üretmedim; cevaplarını ben okuyorum ve sana bizzat yazacağım. İstersen bu maile tek kelime cevap vermen yeter.

Eğer şu an kendini ya da başkası yüzünden güvende hissetmiyorsan lütfen beklemeden 112'yi ara, güvendiğin birine haber ver ya da en yakın sağlık kuruluşuna git. Bunu söylemek görevim; bu anda yalnız olmak zorunda değilsin.

Nihan
thetakapisi.com.tr"""


def normalize(raw):
    cev = {}
    for k, v in raw.items():
        if not KODLAR.match(k):
            continue
        s = str(v or "").strip()
        if (k[0] in "iapcg" and int(k[1]) <= 5) or k == "r1":   # F ölçeği
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


@bp.route("/onay-haritasi", methods=["POST", "OPTIONS"])
def onay_haritasi():
    if request.method == "OPTIONS":
        return ("", 204)
    payload = request.get_json(force=True, silent=True) or {}
    raw = {str(k).lower(): v for k, v in payload.items()}
    ad = str(raw.get("ad", "") or "").strip() or "Sen"
    eposta = str(raw.get("eposta", "") or "").strip()
    kod = str(raw.get("kod", "") or "").strip().upper()
    gecerli = [k.strip().upper() for k in os.environ.get("URUN_KODU_ONAY", "ONAY2026").split(",") if k.strip()]
    nihan = os.environ.get("NIHAN_EMAIL", "nihan@thetakapisi.com.tr")

    if not eposta:
        return jsonify({"ok": False, "hata": "eposta yok"}), 400
    if not (os.environ.get("SMTP_PASS") or os.environ.get("BREVO_API_KEY")):
        log.error("Mail ayarları eksik; rapor üretilmedi (%s)", eposta)
        return jsonify({"ok": False, "hata": "smtp"}), 500
    if gecerli and kod not in gecerli:
        mail_gonder(eposta, "Onay İhtiyacı Haritası: erişim kodu geçersiz",
                    "Merhaba %s,\n\nGirdiğin erişim kodu tanınmadı. Shopier'den gelen erişim kartındaki kodu kontrol edip formu yeniden doldurabilirsin. Sorun sürerse bu maile cevap yaz.\n\nNihan" % ad)
        return jsonify({"ok": False, "hata": "kod"}), 200

    cev = normalize(raw)
    sonuc = puanla(cev)
    tmp = tempfile.mkdtemp()
    koc_yolu = os.path.join(tmp, "koc-notu.pdf")
    koc_notu_pdf(ad, eposta, sonuc, koc_yolu)

    if sonuc["rapor_yok"]:
        mail_gonder(eposta, "Onay İhtiyacı Haritası: cevapların ulaştı", DESTEK_MAIL.format(ad=ad))
        mail_gonder(nihan, "ACİL · RAPOR ÜRETİLMEDİ · Onay İhtiyacı Haritası · %s" % ad,
                    "Serbest cümlede risk ifadesi var. Danışana destek maili gitti; rapor üretilmedi. Mümkünse bugün ulaş.\n\nCümle: %s\n\nHam cevaplar:\n\n%s" % (sonuc["cumle"], _ham_metin(ad, eposta, cev)),
                    ekler=[(koc_yolu, "koc-notu.pdf")])
        return jsonify({"ok": True, "durum": "destek"}), 200

    rapor_yolu = os.path.join(tmp, "onay-haritasi-%s.pdf" % re.sub(r"[^a-z0-9]+", "-", ad.lower()))
    rapor_pdf(ad, sonuc, rapor_yolu, whatsapp_link=os.environ.get("WHATSAPP_LINK_ONAY", "https://wa.me/905324944692?text=Onay%20%C4%B0htiyac%C4%B1%20Haritas%C4%B1%20g%C3%B6r%C3%BC%C5%9Fmesi%20istiyorum"))

    if sonuc["incele"]:
        mail_gonder(eposta, "Onay İhtiyacı Haritası raporun hazırlanıyor",
                    "Merhaba %s,\n\nCevapların ulaştı. Raporunu bizzat gözden geçiriyorum; 24 saat içinde bu adrese gelecek.\n\nNihan" % ad)
        mail_gonder(nihan, "İNCELEME BEKLİYOR · Onay İhtiyacı Haritası · %s" % ad,
                    "Değersizlik + donma ya da güvensizlik işaretlendi. Rapor ve koç notu ekte (güvenlik notuna bak). Onaylarsan raporu danışana sen gönder: %s" % eposta,
                    ekler=[(rapor_yolu, "onay-haritasi.pdf"), (koc_yolu, "koc-notu.pdf")])
        return jsonify({"ok": True, "durum": "inceleme"}), 200

    mail_gonder(eposta, "Onay İhtiyacı Haritası raporun hazır",
                "Merhaba %s,\n\nOnay İhtiyacı Haritası raporun ekte. İki kere oku: ilkinde sadece bak, ikincisinde en çok rahatsız eden cümlenin altını çiz. Sonra bu hafta rapordaki küçük deneylerden birini seç ve bir kez dene.\n\nRaporu birlikte okumak istersen son sayfadaki linkten yaz.\n\nSevgiyle,\nNihan\nthetakapisi.com.tr" % ad,
                ekler=[(rapor_yolu, "onay-haritasi.pdf")])
    mail_gonder(nihan, "Yeni Onay İhtiyacı Haritası · %s" % ad, "Rapor gönderildi: %s\nKoç notu ekte.%s" % (eposta, "\nNot: dürüstçe bölümü genişletildi (risk işareti)." if sonuc["genis_durustce"] else ""),
                ekler=[(rapor_yolu, "onay-haritasi.pdf"), (koc_yolu, "koc-notu.pdf")])
    return jsonify({"ok": True, "durum": "gonderildi"}), 200
