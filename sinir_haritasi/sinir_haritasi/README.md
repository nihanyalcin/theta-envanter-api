# Sınır Haritası — Render entegrasyonu

1. Bu klasörü theta-envanter-api deposuna `sinir_haritasi/` olarak kopyala.
2. `app.py` içinde:
   ```python
   from sinir_haritasi import bp as sinir_bp
   app.register_blueprint(sinir_bp)
   ```
3. requirements.txt'e ekle (yoksa): `reportlab`, `gspread` (isteğe bağlı), `requests`.
4. Render > Environment: SMTP_HOST, SMTP_PORT=465, SMTP_USER=nihan@thetakapisi.com.tr, SMTP_PASS,
   NIHAN_EMAIL, URUN_KODU, WHATSAPP_LINK; isteğe bağlı SH_SHEET_ID (+ service_account.json), MAILERLITE_API_KEY, MAILERLITE_GROUP_ID, TALLY_SIGNING_SECRET.
5. Form: https://thetakapisi.com.tr/sinir-haritasi-form/ (site formu doğrudan POST /sinir-haritasi çağırır; Tally webhook da desteklenir). CORS_ORIGIN varsayılan https://thetakapisi.com.tr
6. Yerel test: `python -m sinir_haritasi.test` örnek raporları `ornek/` klasörüne üretir.
