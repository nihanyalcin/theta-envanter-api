# -*- coding: utf-8 -*-
"""İlişki Mesafesi Haritası rapor PDF'i (ReportLab, telefon boyu 9:16)."""
import os
from datetime import date
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, NextPageTemplate, KeepTogether, Flowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from .sorular import BOYUTLAR, TIPLER, KISA, S as S_SORULAR, S_SIK, Z as Z_SORULAR, Z_SORU, R_SORU, F_SIKLAR
from . import metinler as M
from .mesajlar import mesaj as hazir_mesaj
from .cumle import cumle_coz

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
_FONT_URL = "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/"


def _font_yolu(dosya):
    kardes = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sinir_haritasi", "sinir_haritasi", "fonts", dosya)
    adaylar = [os.path.join(FONT_DIR, dosya), kardes, os.path.join("/usr/share/fonts/truetype/dejavu", dosya),
               os.path.join("/usr/share/fonts/dejavu", dosya), os.path.join("/tmp/sh_fonts", dosya)]
    for y in adaylar:
        if os.path.exists(y):
            return y
    try:
        import urllib.request
        os.makedirs("/tmp/sh_fonts", exist_ok=True)
        urllib.request.urlretrieve(_FONT_URL + dosya, adaylar[-1])
        return adaylar[-1]
    except Exception as e:  # pragma: no cover
        raise RuntimeError("Font bulunamadı: %s (%s)" % (dosya, e))


_registered = False


def _fonts():
    global _registered
    if _registered:
        return
    for ad, dosya in [("Serif", "DejaVuSerif.ttf"), ("SerifB", "DejaVuSerif-Bold.ttf"),
                      ("SerifI", "DejaVuSerif-Italic.ttf"), ("Sans", "DejaVuSans.ttf"),
                      ("SansB", "DejaVuSans-Bold.ttf")]:
        pdfmetrics.registerFont(TTFont(ad, _font_yolu(dosya)))
    _registered = True


MOR = HexColor("#2A1640"); MOR2 = HexColor("#4A2A6B"); MOR3 = HexColor("#6B3FA0")
ALTIN = HexColor("#C9A24D"); ALTIN2 = HexColor("#E6C77A"); KREM = HexColor("#F6F0E6")
KREM2 = HexColor("#FFFBF4"); SOLUK = HexColor("#7A6A8C"); CIZGI = HexColor("#EADFCB")
BANT_RENK = {"Akıyor": HexColor("#5C8A5C"), "Takılıyor": HexColor("#C9A24D"),
             "Tıkanıyor": HexColor("#C76B3F"), "Kapalı": HexColor("#9B3B3B")}
TIP_RENK = {"T": "#C76B3F", "C": "#4A6FA5", "B": "#8A6FA0", "D": "#C9A24D", "TUTAR": "#5C8A5C"}
BOYUT_SIRA = ["Y", "U", "S", "O"]
W, H, MARJ = 420, 746, 26


def _styles():
    return {
        "ust": ParagraphStyle("ust", fontName="SansB", fontSize=7.5, leading=10, textColor=ALTIN, spaceAfter=4),
        "h1": ParagraphStyle("h1", fontName="SerifB", fontSize=24, leading=29, textColor=MOR, spaceAfter=8),
        "h2": ParagraphStyle("h2", fontName="SerifB", fontSize=14.5, leading=18, textColor=MOR, spaceBefore=6, spaceAfter=4),
        "p": ParagraphStyle("p", fontName="Sans", fontSize=9.8, leading=15, textColor=MOR, spaceAfter=8),
        "pi": ParagraphStyle("pi", fontName="SerifI", fontSize=11, leading=16, textColor=MOR2, spaceAfter=8),
        "cumle": ParagraphStyle("cumle", fontName="Serif", fontSize=12.5, leading=18, textColor=MOR, spaceAfter=6),
        "pk": ParagraphStyle("pk", fontName="Sans", fontSize=8.5, leading=12, textColor=MOR, spaceAfter=0),
        "not": ParagraphStyle("not", fontName="Sans", fontSize=8.5, leading=12.5, textColor=SOLUK, spaceAfter=6),
        "kapak_h": ParagraphStyle("kapak_h", fontName="SerifB", fontSize=30, leading=35, textColor=KREM2, alignment=TA_CENTER),
        "kapak_p": ParagraphStyle("kapak_p", fontName="SerifI", fontSize=12.5, leading=18, textColor=ALTIN2, alignment=TA_CENTER),
        "kapak_u": ParagraphStyle("kapak_u", fontName="SansB", fontSize=8, leading=10, textColor=ALTIN2, alignment=TA_CENTER),
        "bolum_h": ParagraphStyle("bolum_h", fontName="SerifB", fontSize=26, leading=31, textColor=KREM2),
        "bolum_p": ParagraphStyle("bolum_p", fontName="SerifI", fontSize=12, leading=17, textColor=ALTIN2),
        "bolum_n": ParagraphStyle("bolum_n", fontName="SansB", fontSize=8, leading=10, textColor=ALTIN2),
    }


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Cubuk(Flowable):
    def __init__(self, etiket, yuzde, bant, genislik=W - 2 * MARJ):
        super().__init__()
        self.etiket, self.yuzde, self.bant, self.genislik = etiket, yuzde, bant, genislik
        self.height = 34

    def wrap(self, aw, ah):
        return self.genislik, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(MOR); c.setFont("SerifB", 11); c.drawString(0, 20, self.etiket)
        c.setFillColor(SOLUK); c.setFont("Sans", 8); c.drawRightString(self.genislik, 20, "%d · %s" % (self.yuzde, self.bant))
        c.setFillColor(CIZGI); c.roundRect(0, 6, self.genislik, 8, 4, fill=1, stroke=0)
        c.setFillColor(BANT_RENK[self.bant]); c.roundRect(0, 6, max(8, self.genislik * self.yuzde / 100), 8, 4, fill=1, stroke=0)


class Ibre(Flowable):
    """Mesafe ibresi: -100 (uzak) … 0 … +100 (yapışık)."""
    def __init__(self, mesafe, genislik=W - 2 * MARJ):
        super().__init__()
        self.mesafe, self.genislik = max(-100, min(100, mesafe)), genislik
        self.height = 58

    def wrap(self, aw, ah):
        return self.genislik, self.height

    def draw(self):
        c = self.canv; g = self.genislik
        c.setFillColor(SOLUK); c.setFont("Sans", 7.5)
        c.drawString(0, 44, "UZAK"); c.drawCentredString(g / 2, 44, "DENGEDE"); c.drawRightString(g, 44, "YAPIŞIK")
        c.setFillColor(CIZGI); c.roundRect(0, 22, g, 10, 5, fill=1, stroke=0)
        c.setFillColor(HexColor("#DCE8DC")); c.rect(g * 0.375, 22, g * 0.25, 10, fill=1, stroke=0)
        c.setStrokeColor(SOLUK); c.setLineWidth(0.6); c.line(g / 2, 18, g / 2, 36)
        x = g / 2 + (self.mesafe / 100.0) * (g / 2)
        c.setFillColor(MOR); c.circle(x, 27, 7, fill=1, stroke=0)
        c.setFillColor(ALTIN); c.circle(x, 27, 3.5, fill=1, stroke=0)
        c.setFillColor(MOR); c.setFont("SansB", 8)
        c.drawCentredString(max(14, min(g - 14, x)), 6, "%+d" % self.mesafe)


def _bg_krem(c, doc):
    c.setFillColor(KREM); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(SOLUK); c.setFont("Sans", 7)
    c.drawCentredString(W / 2, 14, "İlişki Mesafesi Haritası · Theta Kapısı · %d" % doc.page)


def _bg_mor(c, doc):
    c.setFillColor(MOR); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(MOR2); c.circle(W * 0.85, H * 0.85, 140, fill=1, stroke=0)
    c.setFillColor(MOR); c.circle(W * 0.85, H * 0.85, 100, fill=1, stroke=0)
    c.setStrokeColor(ALTIN); c.setLineWidth(0.8); c.rect(14, 14, W - 28, H - 28, fill=0, stroke=1)


def _kutu(flow, genislik=W - 2 * MARJ, zemin=KREM2, sol=ALTIN, pad=10):
    t = Table([[flow]], colWidths=[genislik])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), zemin), ("BOX", (0, 0), (-1, -1), 0.6, CIZGI),
                           ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                           ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
                           ("LINEBEFORE", (0, 0), (0, -1), 2.2, sol)]))
    return t


def _mor_sayfa(S, ust, baslik, alt):
    return [NextPageTemplate("mor"), PageBreak(), Spacer(1, 250), Paragraph(ust, S["bolum_n"]), Spacer(1, 8),
            Paragraph(esc(baslik), S["bolum_h"]), Spacer(1, 14), Paragraph(esc(alt), S["bolum_p"]),
            NextPageTemplate("krem"), PageBreak()]


def _mesaj_kutusu(S, no, baslik=None):
    m = hazir_mesaj(no)
    if not m:
        return []
    durum, metin, geri = m
    ust = baslik or M.MESAJ_KUTU_UST.format(no=no)
    ic = ("<font name='SansB' color='#C9A24D' size='7'>%s</font><br/>"
          "<font color='#7A6A8C' size='8'>%s</font><br/>" % (esc(ust), esc(durum)) +
          "<font name='Serif' size='11'>%s</font><br/>" % esc(metin) +
          "<font color='#7A6A8C' size='8'>%s</font> <font name='SerifI' size='9.5'>%s</font>" % (esc(M.MESAJ_GERI_UST), esc(geri)))
    return [KeepTogether(_kutu(Paragraph(ic, S["p"]), zemin=white))]


def _senaryolar(S, boyut, cevaplar):
    out = []
    sira = -1
    for kod, b, durum, harita in S_SORULAR:
        if b != boyut:
            continue
        sira += 1
        sik = str(cevaplar.get(kod, "") or "").strip().lower()[:1]
        if sik not in harita:
            continue
        hedef = harita[sik]
        secilen = S_SIK.get(kod, {}).get(sik, "").replace('"', "")
        tutan = next((S_SIK[kod][h] for h, t in harita.items() if t == "TUTAR"), "").replace('"', "")
        tip_ad = TIPLER.get(hedef, "Adım aktı")
        renk = TIP_RENK[hedef]
        ic = ("<font color='#7A6A8C' size='7.5'>%s</font><br/>" % esc(durum) +
              "<font name='SerifI' size='10.5'>Sen: “%s”</font> "
              "<font name='SansB' color='%s' size='7'>· %s</font><br/>" % (esc(secilen), renk, esc(tip_ad)) +
              "<font size='8.5'>%s</font>" % esc(M.S_TIP_YORUM[hedef][sira % 3]))
        if hedef != "TUTAR" and tutan:
            ic += "<br/><font color='#7A6A8C' size='8'>%s</font> <font name='Serif' size='9.5'>“%s”</font>" % (esc(M.S_TUTAN_GIRIS), esc(tutan))
        out.append(_kutu(Paragraph(ic, S["pk"]), zemin=KREM2, sol=HexColor(renk), pad=7))
        out.append(Spacer(1, 4))
    return out


def _ikilemler(S, sonuc):
    cev = sonuc.get("cevaplar", {})
    sayac = {t: 0 for t in TIPLER}
    satirlar = []
    for kod, harita in Z_SORULAR:
        sik = str(cev.get(kod, "") or "").strip().lower()[:1]
        if sik not in harita:
            continue
        sayac[harita[sik]] += 1
        soru, sikler = Z_SORU[kod]
        satirlar.append((soru, sikler[sik], harita[sik]))
    if not satirlar:
        return []
    F = [PageBreak(), Paragraph("İKİLEMLER", S["ust"]), Paragraph("Zorlandığında hangi adımı atıyorsun", S["h1"]),
         Paragraph(esc(M.Z_GIRIS), S["p"])]
    for soru, secim, tip in satirlar:
        F.append(Paragraph("<font color='#7A6A8C' size='8'>%s</font>&nbsp;&nbsp;<font name='SerifI' size='10.5'>%s</font> "
                           "<font color='%s' size='7.5'>· %s</font>" % (esc(soru), esc(secim), TIP_RENK[tip], esc(TIPLER[tip].lower())), S["p"]))
    enb = max(sayac, key=lambda t: sayac[t])
    F.append(Spacer(1, 6))
    if sayac[enb] >= 3 and list(sayac.values()).count(sayac[enb]) == 1:
        F.append(_kutu(Paragraph(esc(M.Z_YORUM[enb]), S["p"])))
    else:
        F.append(_kutu(Paragraph(esc(M.Z_DENGELI), S["p"])))
    ozel = []
    for kod in ("z3", "z5", "z8"):
        sik = str(cev.get(kod, "") or "").strip().lower()[:1]
        if (kod, sik) in M.Z_OZEL:
            ozel.append(M.Z_OZEL[(kod, sik)])
    for p in ozel[:2]:
        F.append(Spacer(1, 6)); F.append(Paragraph(esc(p), S["pi"]))
    return F


def _cumle_sayfasi(S, sonuc):
    c = sonuc.get("cumle", "")
    if not c:
        return []
    F = [PageBreak(), Paragraph("SENİN CÜMLEN", S["ust"]), Paragraph("Söyleyemediğin şey", S["h1"]),
         _kutu(Paragraph("“" + esc(c) + "”", S["cumle"]), zemin=white), Spacer(1, 12)]
    coz = cumle_coz(c) or {}
    boyut, tip = coz.get("boyut"), coz.get("tip")
    y = sonuc["boyut_yuzde"]
    if coz.get("kisi") in M.CUMLE_KISI:
        F.append(Paragraph(esc(M.CUMLE_KISI[coz["kisi"]]), S["p"]))
    if boyut:
        F.append(Paragraph(esc(M.CUMLE_BOYUT[boyut]), S["p"]))
        zayif_mi = y[boyut] <= 44 or boyut in sorted(BOYUT_SIRA, key=lambda k: y[k])[:2]
        F.append(Paragraph(esc(M.CUMLE_BOYUT_UYUM[zayif_mi]), S["p"]))
    if tip:
        F.append(Paragraph(esc(M.CUMLE_TIP[tip].format(ipucu=coz["ipucu"])), S["p"]))
        F.append(Paragraph(esc(M.CUMLE_TIP_UYUM[tip == sonuc["baskin"]]), S["p"]))
    if not boyut and not tip:
        F.append(Paragraph(esc(M.CUMLE_BELIRSIZ), S["p"]))
    b_sec = boyut or sonuc["zayif"]
    t_sec = tip or sonuc["baskin"]
    _adim, no = M.BOYUT_ADIM[b_sec][t_sec]
    if coz.get("mesaj_no"):
        no = coz["mesaj_no"]
    F.append(Spacer(1, 6))
    F.append(Paragraph(esc(M.CUMLE_KARSI_GIRIS.format(no=no)), S["not"]))
    F += _mesaj_kutusu(S, no, baslik="SANA ÖZEL · YAKINLIK CÜMLESİ %s" % no)
    F.append(Spacer(1, 10))
    F.append(Paragraph(esc(M.CUMLE_KAPANIS), S["pi"]))
    return F


def _doc(yol, baslik, ilk="krem"):
    doc = BaseDocTemplate(yol, pagesize=(W, H), leftMargin=MARJ, rightMargin=MARJ, topMargin=30, bottomMargin=30,
                          title=baslik, author="Theta Kapısı")
    fr = Frame(MARJ, 30, W - 2 * MARJ, H - 60, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    sablonlar = [PageTemplate(id="krem", frames=[fr], onPage=_bg_krem), PageTemplate(id="mor", frames=[fr], onPage=_bg_mor)]
    if ilk == "mor":
        sablonlar.reverse()
    doc.addPageTemplates(sablonlar)
    return doc


def rapor_pdf(ad, sonuc, yol, whatsapp_link="https://wa.me/", tarih=None):
    _fonts(); S = _styles()
    tarih = tarih or date.today().strftime("%d.%m.%Y")
    y, b = sonuc["boyut_yuzde"], sonuc["boyut_bant"]
    bask = sonuc["baskin"]; T = M.TIP[bask]
    doc = _doc(yol, "İlişki Mesafesi Haritası · " + ad, ilk="mor")
    F = []
    # 1 Kapak
    F += [NextPageTemplate("krem"), Spacer(1, 180), Paragraph("THETA KAPISI", S["kapak_u"]), Spacer(1, 14),
          Paragraph("İlişki Mesafesi<br/>Haritası", S["kapak_h"]), Spacer(1, 16),
          Paragraph(esc(ad) + " için hazırlandı", S["kapak_p"]), Paragraph(tarih, S["kapak_p"]), Spacer(1, 270),
          Paragraph("thetakapisi.com.tr", S["kapak_u"]), PageBreak()]
    # 2 Tek bakışta
    F += [Paragraph("TEK BAKIŞTA", S["ust"]), Paragraph("Haritan", S["h1"])]
    for k in BOYUT_SIRA:
        F.append(Cubuk(BOYUTLAR[k], y[k], b[k])); F.append(Spacer(1, 6))
    F += [Spacer(1, 6), Paragraph("Mesafe ibren", S["h2"]), Ibre(sonuc["mesafe"]),
          Paragraph(esc(M.MESAFE_METIN[sonuc["mesafe_ad"]]), S["not"]), Spacer(1, 4)]
    if sonuc["serbest"]:
        ozet = "Dört adım da düşük; refleksin tek kalıba yığılmamış."
    elif sonuc["cift_adim"]:
        ozet = "Baskın adımların: <b>%s</b> ve <b>%s</b>." % (T["ad"], M.TIP[sonuc["ikinci"]]["ad"])
    else:
        ozet = "Baskın adımın: <b>%s</b>." % T["ad"]
    F.append(_kutu(Paragraph(ozet + " En zayıf boyutun <b>%s</b> (%d), en güçlü boyutun <b>%s</b> (%d)." % (
        BOYUTLAR[sonuc["zayif"]], y[sonuc["zayif"]], BOYUTLAR[sonuc["guclu"]], y[sonuc["guclu"]]), S["cumle"])))
    if sonuc.get("gecmis"):
        F.append(Paragraph("Bu haritayı son ilişkini düşünerek doldurdun; adımlar ilişkiden ilişkiye taşınır, o yüzden rapor bugünkü sana da söz söyler.", S["not"]))
    F += [Spacer(1, 4), Paragraph("Yüzde, o boyutun ne kadar aktığını gösterir: 100 tam akıyor, 0 kapalı. Bantlar: Akıyor 70+, Takılıyor 45-69, Tıkanıyor 20-44, Kapalı 0-19. Mesafe ibresi Yaklaşma ile Alan arasındaki fark.", S["not"])]
    # 3 Ne ne değil
    F += [PageBreak(), Paragraph("BAŞLAMADAN", S["ust"]), Paragraph("Bu rapor ne, ne değil", S["h1"])]
    F += [Paragraph(esc(p), S["p"]) for p in M.NE_NE_DEGIL]
    # 4 Baskın adım
    F += _mor_sayfa(S, "BASKIN ADIMIN", T["ad"], T["karsi"])
    if sonuc["serbest"]:
        F += [Paragraph("ADIMIN SERBEST", S["ust"]), Paragraph("Dört adım da düşük", S["h1"]), Paragraph(esc(M.SERBEST), S["p"])]
    F += [Paragraph("NASIL ÇALIŞIYOR", S["ust"]), Paragraph(esc(T["ad"]), S["h1"]), Paragraph(esc(T["mekanizma"]), S["p"]),
          Paragraph(esc(T["his"]), S["p"]), Paragraph("Nereden gelmiş olabilir", S["h2"]), Paragraph(esc(T["koken"]), S["p"]),
          Paragraph("Bu adımın erdemi", S["h2"]), Paragraph(esc(T["erdem"]), S["p"]),
          Paragraph("Partnerinde ne tetikliyor", S["h2"]), Paragraph(esc(T["partner"]), S["p"])]
    if sonuc["cift_adim"] and not sonuc["serbest"]:
        T2 = M.TIP[sonuc["ikinci"]]
        F += [Spacer(1, 4), _kutu(Paragraph(esc(M.CIFT_ADIM.format(t1=T["ad"], t2=T2["ad"])), S["p"]))]
        F += [PageBreak(), Paragraph("İKİNCİ ADIMIN", S["ust"]), Paragraph(esc(T2["ad"]), S["h1"]),
              Paragraph(esc(T2["mekanizma"]), S["p"]), Paragraph(esc(T2["his"]), S["p"]),
              Paragraph("Bu adımın erdemi", S["h2"]), Paragraph(esc(T2["erdem"]), S["p"]),
              Paragraph("Partnerinde ne tetikliyor", S["h2"]), Paragraph(esc(T2["partner"]), S["p"])]
    # 5-8 Boyutlar
    for k in BOYUT_SIRA:
        F += [PageBreak(), Paragraph("BOYUT · %d · %s" % (y[k], b[k].upper()), S["ust"]), Paragraph(BOYUTLAR[k], S["h1"]),
              Cubuk("", y[k], b[k]), Spacer(1, 8), Paragraph(esc(M.BOYUT_BANT[k][b[k]]), S["p"])]
        bt = sonuc["boyut_baskin"][k]
        if bt and b[k] != "Akıyor":
            F.append(Paragraph(esc(M.BOYUT_TIP[k][bt]), S["pi"]))
        en = [KISA[q] for q in sonuc["boyut_en"][k]]
        if en:
            F.append(Paragraph("Özellikle: " + esc(" ve ".join(en)) + ".", S["not"]))
        adim, no = M.BOYUT_ADIM[k][bt or bask]
        F += [Spacer(1, 6), _kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>BU HAFTA TEK ADIM</font><br/>" + esc(adim), S["p"]))]
        sen = _senaryolar(S, k, sonuc.get("cevaplar", {}))
        if sen:
            F += [Spacer(1, 6), Paragraph("Üç anda ne yaptın", S["h2"])] + sen
        F += [Spacer(1, 2)] + _mesaj_kutusu(S, no)
    # 9 İkilemler
    F += _ikilemler(S, sonuc)
    # 10 Örüntüler
    oruntu = [M.ORUNTU[o] for o in sonuc["oruntu"] if o in M.ORUNTU]
    F += [PageBreak(), Paragraph("ÖRÜNTÜLER", S["ust"]), Paragraph("Boyutların birbirine söylediği", S["h1"])]
    if not oruntu:
        F.append(Paragraph("Belirgin bir örüntü çıkmadı; boyutlar birbirine yakın. Bu iyi haber: tek bir adımı tanımak yetiyor.", S["p"]))
    for p in oruntu:
        F.append(_kutu(Paragraph(esc(p), S["p"]))); F.append(Spacer(1, 8))
    # 11 Senin cümlen
    F += _cumle_sayfasi(S, sonuc)
    # 12 Plan
    sira = sorted(BOYUT_SIRA, key=lambda k: -y[k])
    F += [PageBreak(), Paragraph("30 GÜN", S["ust"]), Paragraph("Küçük plan", S["h1"]),
          Paragraph("Haftada bir boyut, her hafta tek davranış. En güçlü boyuttan başlıyor, en zayıfa son hafta geliyorsun; kas önce kolay yerde çalışır.", S["p"])]
    for i, k in enumerate(sira):
        _adim, _no = M.BOYUT_ADIM[k][sonuc["boyut_baskin"][k] or bask]
        _m = hazir_mesaj(_no)
        ek = ("<br/><font color='#7A6A8C' size='8'>Cümlen hazır (%s):</font> <font name='Serif' size='9.5'>%s</font>" % (_no, esc(_m[1]))) if _m else ""
        F.append(_kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>HAFTA %d · %s</font><br/>" % (i + 1, esc(BOYUTLAR[k].upper())) + esc(M.PLAN_HAFTA[k]) + ek, S["p"])))
        F.append(Spacer(1, 6))
    F.append(Paragraph("Dört hafta sonra envanteri yeniden doldur; fark genellikle ilk ayda ibrede görünür.", S["not"]))
    # 13 Dürüstçe
    F += [PageBreak(), Paragraph("DÜRÜSTÇE", S["ust"]), Paragraph("Bu raporun sınırları", S["h1"])]
    F += [Paragraph(esc(p), S["p"]) for p in M.DURUSTCE]
    if sonuc["genis_durustce"]:
        F.append(_kutu(Paragraph(esc(M.DURUSTCE_GENIS), S["p"]), sol=HexColor("#9B3B3B")))
    # 14 Sonraki
    F += [PageBreak(), Paragraph("SONRAKİ ADIM", S["ust"]), Paragraph("İstersen", S["h1"])]
    for h, p in M.SONRAKI:
        F += [Paragraph(esc(h), S["h2"]), Paragraph(esc(p), S["p"])]
    F += [Spacer(1, 10), Paragraph("<a href='%s' color='#6B3FA0'>Görüşme için WhatsApp'tan yaz →</a>" % whatsapp_link, S["cumle"]),
          Spacer(1, 20), Paragraph("Bu rapor %s için üretildi; başkasına uymaz. Kendine iyi bak. Sev ve sevgi ver." % esc(ad), S["not"])]
    doc.build(F)
    return yol


def koc_notu_pdf(ad, eposta, sonuc, yol):
    """Nihan'a giden ayrı sayfa (rapor üretilmese de üretilir)."""
    _fonts(); S = _styles()
    doc = _doc(yol, "Koç notu · " + ad)
    y = sonuc["boyut_yuzde"]; t = sonuc["tip_yuzde"]
    F = [Paragraph("KOÇ NOTU · DANIŞANA GİTMEZ", S["ust"]), Paragraph(esc(ad), S["h1"]), Paragraph(esc(eposta), S["not"])]
    if sonuc["rapor_yok"]:
        F.append(_kutu(Paragraph("<b>RAPOR ÜRETİLMEDİ.</b> Danışana destek maili gitti. Ham cevaplar aşağıda; mümkünse bir insan ulaşsın.", S["p"]), sol=HexColor("#9B3B3B")))
    F.append(Paragraph("Durum: %s" % ("son ilişki" if sonuc["gecmis"] else "mevcut ilişki"), S["not"]))
    rows = [["Boyut", "%", "Bant", "Baskın adım"]] + [[BOYUTLAR[k], str(y[k]), sonuc["boyut_bant"][k], TIPLER.get(sonuc["boyut_baskin"][k], "-") if sonuc["boyut_baskin"][k] else "-"] for k in BOYUT_SIRA]
    tb = Table(rows, colWidths=[120, 36, 70, 140])
    tb.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), "Sans"), ("FONTSIZE", (0, 0), (-1, -1), 8.5), ("FONTNAME", (0, 0), (-1, 0), "SansB"),
                            ("LINEBELOW", (0, 0), (-1, -1), 0.4, CIZGI), ("TEXTCOLOR", (0, 0), (-1, -1), MOR), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    F += [tb, Spacer(1, 10)]
    F.append(Paragraph("Adımlar: " + ", ".join("%s %d" % (TIPLER[k], t[k]) for k in sonuc["tip_sira"]) + ". Çift adım: %s. Mesafe: %+d (%s)." % (
        "evet" if sonuc["cift_adim"] else "hayır", sonuc["mesafe"], sonuc["mesafe_ad"]), S["p"]))
    bay = sonuc["bayraklar"]; r = sonuc["r"]
    F.append(_kutu(Paragraph("<b>Güvenlik</b> · r1 korku: %d/4 · r2 kontrol: %s · r3 kavga: %s<br/>Bayraklar: korku %s · kontrol %s · şiddet %s · fiziksel %s · metin %s · <b>%s</b>" % (
        r["r1"], R_SORU["r2"][1].get(r["r2"], "-"), R_SORU["r3"][1].get(r["r3"], "-"),
        "EVET" if bay["korku"] else "hayır", "EVET" if bay["kontrol"] else "hayır", "EVET" if bay["siddet"] else "hayır",
        "EVET" if bay["fiziksel"] else "hayır", "EVET" if bay["metin"] else "hayır",
        "RAPOR YOK" if sonuc["rapor_yok"] else ("İNCELEME GEREKLİ" if sonuc["incele"] else "inceleme gerekmiyor")), S["p"]),
        sol=HexColor("#9B3B3B") if sonuc["incele"] else ALTIN))
    F += [Spacer(1, 8), Paragraph("Örüntüler: " + (", ".join(sonuc["oruntu"]) or "yok"), S["p"])]
    ust3 = sorted(sonuc["soru_puan"], key=lambda k: -sonuc["soru_puan"][k])[:3]
    F.append(Paragraph("En yüksek üç soru: " + ", ".join("%s (%s, %d)" % (k, KISA.get(k, k), sonuc["soru_puan"][k]) for k in ust3), S["p"]))
    if sonuc["cumle"]:
        F.append(Paragraph("Açık uçlu: “" + esc(sonuc["cumle"]) + "”", S["pi"]))
    F.append(Paragraph("Görüşme olursa üç soru", S["h2"]))
    T = M.TIP[sonuc["baskin"]]
    F += [Paragraph("1. %s boyutundaki en yüksek soruyu anlat: o an ne oldu, ne yaptın, sonra ne hissettin?" % BOYUTLAR[sonuc["zayif"]], S["p"]),
          Paragraph("2. %s adımını ilk nerede öğrendiğini hatırlıyor musun? Tek bir sahne yeter." % T["ad"], S["p"]),
          Paragraph("3. Bu ay tek bir yakınlık cümlesi söylesen ve karşılık gelse, ne değişirdi?", S["p"])]
    tema = {"T": "terk edilme", "B": "terk edilme / görülmeme", "C": "boğulma", "D": "kontrol / yük"}[sonuc["baskin"]]
    F.append(Paragraph("Önerilen paket: ThetaHealing odak programı (3-4 seans, tema: %s)" % tema, S["pi"]))
    doc.build(F)
    return yol
