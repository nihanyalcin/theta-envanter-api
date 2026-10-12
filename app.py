"""
==========================================================
THETA KAPISI — ENVANTER RAPOR SERVİSİ (Python / Flask)
==========================================================
POST /rapor/yasam-dengesi
  Gövde: Sheets'ten gelen JSON
  Dönüş: PDF

Neden Playwright?
  Rapordaki radar grafiği ve tüm hesaplamalar JavaScript ile
  çiziliyor. WeasyPrint gibi araçlar JS çalıştırmadığı için
  grafik boş çıkar. Playwright gerçek bir Chromium açıyor.

Dosya yapısı (ikisi de çalışır):
  app.py
  requirements.txt
  yasam-dengesi.html             ← düz yapı
    veya
  templates/yasam-dengesi.html   ← klasörlü yapı
==========================================================
"""

import os
import io
import json
from flask import Flask, request, send_file, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

KOK = os.path.dirname(os.path.abspath(__file__))
RAPOR_ANAHTARI = os.environ.get("RAPOR_ANAHTARI")  # boşsa yetki kontrolü yapılmaz

# Şablonları bir kez okuyup bellekte tut
_sablonlar = {}


def sablon_al(ad):
    """Şablonu önce kök klasörde, bulamazsa templates/ içinde arar.
       Böylece dosyaları nasıl yüklediğinden bağımsız çalışır."""
    if ad not in _sablonlar:
        adaylar = [
            os.path.join(KOK, f"{ad}.html"),
            os.path.join(KOK, "templates", f"{ad}.html"),
        ]
        for yol in adaylar:
            if os.path.exists(yol):
                with open(yol, "r", encoding="utf-8") as f:
                    _sablonlar[ad] = f.read()
                break
        else:
            raise FileNotFoundError(
                f"{ad}.html bulunamadı. Aranan yerler: " + " · ".join(adaylar)
            )
    return _sablonlar[ad]


def yetki_var_mi(req):
    if not RAPOR_ANAHTARI:
        return True
    return req.headers.get("x-api-key") == RAPOR_ANAHTARI


def veri_gecerli_mi(v):
    if not isinstance(v, dict):
        return "Gövde JSON nesnesi değil"
    if not v.get("ad"):
        return "ad alanı eksik"
    alanlar = v.get("alanlar")
    if not isinstance(alanlar, list) or not alanlar:
        return "alanlar dizisi eksik"
    for a in alanlar:
        if not isinstance(a.get("mem"), (int, float)):
            return f"{a.get('ad')} alanında mem sayı değil"
        if not isinstance(a.get("one"), (int, float)):
            return f"{a.get('ad')} alanında one sayı değil"
    return None


def pdf_uret(html):
    """HTML'den A4 PDF üretir."""
    with sync_playwright() as p:
        tarayici = p.chromium.launch(
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        sayfa = tarayici.new_page()
        sayfa.set_content(html, wait_until="networkidle")

        # Google Fonts yüklensin
        sayfa.wait_for_timeout(1200)

        pdf = sayfa.pdf(
            format="A4",
            print_background=True,   # mor bloklar ve renkli çubuklar için şart
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=True,
        )
        tarayici.close()
        return pdf


def dosya_adi_yap(ad, ek="yasam-dengesi"):
    temiz = "".join(c for c in (ad or "rapor") if c.isalnum() or c in " -_ÇĞİÖŞÜçğıöşü")
    return f"{temiz.strip().replace(' ', '-')}-{ek}.pdf"


# ==========================================================
#  YAŞAM DENGESİ HARİTASI
# ==========================================================
@app.route("/rapor/yasam-dengesi", methods=["POST"])
def yasam_dengesi():
    if not yetki_var_mi(request):
        return jsonify({"hata": "Yetkisiz istek"}), 401

    try:
        veri = request.get_json(force=True, silent=True)
    except Exception:
        veri = None

    hata = veri_gecerli_mi(veri)
    if hata:
        app.logger.error("Geçersiz veri: %s", hata)
        return jsonify({"hata": hata}), 400

    try:
        html = sablon_al("yasam-dengesi").replace(
            "{{VERI_JSON}}", json.dumps(veri, ensure_ascii=False)
        )
        pdf = pdf_uret(html)
        app.logger.info("Rapor üretildi: %s", veri.get("ad"))

        return send_file(
            io.BytesIO(pdf),
            mimetype="application/pdf",
            as_attachment=True,
            download_name=dosya_adi_yap(veri.get("ad")),
        )
    except Exception as e:
        app.logger.exception("Rapor hatası")
        return jsonify({"hata": "Rapor üretilemedi", "detay": str(e)}), 500


# ==========================================================
#  ÖNİZLEME — tarayıcıda HTML olarak gör (test için)
#  /rapor/onizleme?veri=<url-encoded json>
# ==========================================================
@app.route("/rapor/onizleme", methods=["GET"])
def onizleme():
    try:
        veri = json.loads(request.args.get("veri", "{}"))
        html = sablon_al("yasam-dengesi").replace(
            "{{VERI_JSON}}", json.dumps(veri, ensure_ascii=False)
        )
        return html, 200, {"Content-Type": "text/html; charset=utf-8"}
    except Exception as e:
        return f"Geçersiz veri parametresi: {e}", 400


# ==========================================================
#  SAĞLIK KONTROLÜ
# ==========================================================
@app.route("/rapor/saglik", methods=["GET"])
def saglik():
    return jsonify({"durum": "çalışıyor"})

# Sinir Haritasi envanteri (sinir_haritasi/sinir_haritasi/route.py)
try:
    from sinir_haritasi.sinir_haritasi import bp as sinir_bp
    app.register_blueprint(sinir_bp)
except Exception as _e:
    print("sinir_haritasi yuklenemedi:", _e)

# Iliski Mesafesi envanteri (iliski_mesafesi/route.py)
try:
    from iliski_mesafesi.route import bp as mesafe_bp
    app.register_blueprint(mesafe_bp)
except Exception as _e:
    print("iliski_mesafesi yuklenemedi:", _e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
