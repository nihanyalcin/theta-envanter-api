# -*- coding: utf-8 -*-
"""Onay İhtiyacı Haritası rapor PDF'i (ReportLab, telefon boyu 9:16)."""
import os
from datetime import date
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, NextPageTemplate, KeepTogether, Flowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from .sorular import ALANLAR, ALAN_SIRA, TIPLER, KISA, S as S_SORULAR, S_SIK, Z as Z_SORULAR, Z_SORU, R_SORU
from . import metinler as M
from .baslaticilar import baslatici, no_bul
from .cumle import cumle_coz

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
_FONT_URL = "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/"


def _font_yolu(dosya):
    kok = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    adaylar = [os.path.join(FONT_DIR, dosya),
               os.path.join(kok, "sinir_haritasi", "sinir_haritasi", "fonts", dosya),
               os.path.join(kok, "iliski_mesafesi", "fonts", dosya),
               os.path.join("/usr/share/fonts/truetype/dejavu", dosya),
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
BANT_RENK = {"Kendinde": HexColor("#5C8A5C"), "Dalgalı": HexColor("#C9A24D"),
             "Dışarıda": HexColor("#C76B3F"), "Kaybolmuş": HexColor("#9B3B3B")}
TIP_RENK = {"U": "#8A6FA0", "K": "#C76B3F", "S": "#7A8A9C", "T": "#4A6FA5", "TUTAR": "#5C8A5C"}
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
        "kapak_h": ParagraphStyle("kapak_h", fontName="SerifB", fontSize=32, leading=37, textColor=KREM2, alignment=TA_CENTER),
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


class Yuk(Flowable):
    """Onay yükü göstergesi: 100 hafif ... 0 ağır, işaretçi ile."""
    def __init__(self, deger, genislik=W - 2 * MARJ):
        super().__init__()
        self.deger, self.genislik = max(0, min(100, deger)), genislik
        self.height = 50

    def wrap(self, aw, ah):
        return self.genislik, self.height

    def draw(self):
        c = self.canv; g = self.genislik
        c.setFillColor(SOLUK); c.setFont("Sans", 7.5)
        c.drawString(0, 38, "AĞIR"); c.drawRightString(g, 38, "HAFİF")
        renkler = ["#9B3B3B", "#C76B3F", "#C9A24D", "#5C8A5C"]
        sinir = [0, 20, 45, 70, 100]
        for i in range(4):
            c.setFillColor(HexColor(renkler[i]))
            c.rect(g * sinir[i] / 100, 18, g * (sinir[i + 1] - sinir[i]) / 100, 9, fill=1, stroke=0)
        x = g * self.deger / 100
        c.setFillColor(MOR); c.circle(x, 22.5, 7, fill=1, stroke=0)
        c.setFillColor(KREM2); c.circle(x, 22.5, 3, fill=1, stroke=0)
        c.setFillColor(MOR); c.setFont("SansB", 8)
        c.drawCentredString(max(10, min(g - 10, x)), 4, "%d" % self.deger)


def _bg_krem(c, doc):
    c.setFillColor(KREM); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(SOLUK); c.setFont("Sans", 7)
    c.drawCentredString(W / 2, 14, "Onay İhtiyacı Haritası · Theta Kapısı · %d" % doc.page)


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


def _baslatici_kutusu(S, no, baslik=None):
    b = baslatici(no)
    if not b:
        return []
    durum, eylem, geri = b
    ust = baslik or M.BASLATICI_UST.format(no=no)
    ic = ("<font name='SansB' color='#C9A24D' size='7'>%s</font><br/>"
          "<font color='#7A6A8C' size='8'>%s</font><br/>" % (esc(ust), esc(durum)) +
          "<font name='SansB' size='8'>%s</font> <font name='Serif' size='10.5'>%s</font><br/>" % (esc(M.BASLATICI_ILK), esc(eylem)) +
          "<font color='#7A6A8C' size='8'>%s</font> <font name='SerifI' size='9.5'>%s</font>" % (esc(M.BASLATICI_GERI), esc(geri)))
    return [KeepTogether(_kutu(Paragraph(ic, S["p"]), zemin=white))]


def _senaryolar(S, alan, cevaplar):
    out = []
    sira = -1
    for kod, a, durum, harita in S_SORULAR:
        if a != alan:
            continue
        sira += 1
        sik = str(cevaplar.get(kod, "") or "").strip().lower()[:1]
        if sik not in harita:
            continue
        hedef = harita[sik]
        secilen = S_SIK.get(kod, {}).get(sik, "").replace('"', "")
        tutan = next((S_SIK[kod][h] for h, t in harita.items() if t == "TUTAR"), "").replace('"', "")
        tip_ad = TIPLER.get(hedef, "Kendinde")
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
    F = [PageBreak(), Paragraph("İKİLEMLER", S["ust"]), Paragraph("Onaya ihtiyaç duyduğunda", S["h1"]),
         Paragraph(esc(M.Z_GIRIS), S["p"])]
    for soru, secim, tip in satirlar:
        F.append(Paragraph("<font color='#7A6A8C' size='8'>%s</font>&nbsp;&nbsp;<font name='SerifI' size='10.5'>%s</font> "
                           "<font color='%s' size='7.5'>· %s</font>" % (esc(soru), esc(secim.replace('"', '')), TIP_RENK[tip], esc(TIPLER[tip].lower())), S["p"]))
    enb = max(sayac, key=lambda t: sayac[t])
    F.append(Spacer(1, 6))
    if sayac[enb] >= 3 and list(sayac.values()).count(sayac[enb]) == 1:
        F.append(_kutu(Paragraph(esc(M.Z_YORUM[enb]), S["p"])))
    else:
        F.append(_kutu(Paragraph(esc(M.Z_DENGELI), S["p"])))
    ozel = []
    for kod in ("z2", "z3", "z5"):
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
    F = [PageBreak(), Paragraph("SENİN CÜMLEN", S["ust"]), Paragraph("Beklenen onay", S["h1"]),
         _kutu(Paragraph("“" + esc(c) + "”", S["cumle"]), zemin=white), Spacer(1, 12)]
    coz = cumle_coz(c) or {}
    alan, tip = coz.get("alan"), coz.get("tip")
    y = sonuc["alan_yuzde"]
    if alan:
        F.append(Paragraph(esc(M.CUMLE_ALAN[alan]), S["p"]))
        zayif_mi = y[alan] <= 44 or alan in sonuc["alan_sira"][:2]
        F.append(Paragraph(esc(M.CUMLE_ALAN_UYUM[zayif_mi]), S["p"]))
    if tip:
        F.append(Paragraph(esc(M.CUMLE_TIP[tip].format(ipucu=coz["ipucu"])), S["p"]))
        F.append(Paragraph(esc(M.CUMLE_TIP_UYUM[tip == sonuc["baskin"]]), S["p"]))
    if not alan and not tip:
        F.append(Paragraph(esc(M.CUMLE_BELIRSIZ), S["p"]))
    no = no_bul(alan or sonuc["zayif"], tip or sonuc["baskin"])
    b = baslatici(no)
    F.append(Spacer(1, 6))
    if b:
        F.append(_kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>BU HAFTA</font><br/>" +
                                 esc(M.CUMLE_YARIN.format(eylem=b[1])), S["p"]), sol=MOR3))
        F.append(Spacer(1, 8))
    F.append(Paragraph(esc(M.CUMLE_KARSI_GIRIS.format(no=no)), S["not"]))
    F += _baslatici_kutusu(S, no, baslik="SANA ÖZEL · DENEY %s" % no)
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
    y, b = sonuc["alan_yuzde"], sonuc["alan_bant"]
    bask = sonuc["baskin"]; T = M.TIP[bask]
    doc = _doc(yol, "Onay İhtiyacı Haritası · " + ad, ilk="mor")
    F = []
    # 1 Kapak
    F += [NextPageTemplate("krem"), Spacer(1, 190), Paragraph("THETA KAPISI", S["kapak_u"]), Spacer(1, 14),
          Paragraph("Onay İhtiyacı Haritası", S["kapak_h"]), Spacer(1, 16),
          Paragraph(esc(ad) + " için hazırlandı", S["kapak_p"]), Paragraph(tarih, S["kapak_p"]), Spacer(1, 290),
          Paragraph("thetakapisi.com.tr", S["kapak_u"]), PageBreak()]
    # 2 Tek bakışta
    F += [Paragraph("TEK BAKIŞTA", S["ust"]), Paragraph("Haritan", S["h1"])]
    for a in ALAN_SIRA:
        F.append(Cubuk(ALANLAR[a], y[a], b[a])); F.append(Spacer(1, 4))
    F += [Spacer(1, 4), Paragraph("Onay yükün", S["h2"]), Yuk(sonuc["onay_yuku"]),
          Paragraph(esc(M.YUK_METIN[sonuc["agir_yuk"]]), S["not"]), Spacer(1, 2)]
    if sonuc["serbest"]:
        ozet = "Dört tipin de düşük; onay ihtiyacın tek bir stratejiye yığılmamış."
    elif sonuc["cift_tip"]:
        ozet = "Baskın tiplerin: <b>%s</b> ve <b>%s</b>." % (T["ad"], M.TIP[sonuc["ikinci"]]["ad"])
    else:
        ozet = "Baskın tipin: <b>%s</b>." % T["ad"]
    F.append(_kutu(Paragraph(ozet + " En zayıf alanın <b>%s</b> (%d), en güçlü alanın <b>%s</b> (%d)." % (
        ALANLAR[sonuc["zayif"]], y[sonuc["zayif"]], ALANLAR[sonuc["guclu"]], y[sonuc["guclu"]]), S["cumle"])))
    F += [Spacer(1, 4), Paragraph("Yüzde, o alanda ne kadar kendinde kalabildiğini gösterir: 100 tamamen kendinde, 0 tamamen başkalarının onayında. Bantlar: Kendinde 70+, Dalgalı 45-69, Dışarıda 20-44, Kaybolmuş 0-19. Onay yükü, en zayıf iki alanının ortalaması.", S["not"])]
    # 3 Ne ne değil
    F += [PageBreak(), Paragraph("BAŞLAMADAN", S["ust"]), Paragraph("Bu rapor ne, ne değil", S["h1"])]
    F += [Paragraph(esc(p), S["p"]) for p in M.NE_NE_DEGIL]
    # 4 Baskın tip
    F += _mor_sayfa(S, "BASKIN TİPİN", T["ad"], T["karsi"])
    if sonuc["serbest"]:
        F += [Paragraph("TİPİN SERBEST", S["ust"]), Paragraph("Dört tip de düşük", S["h1"]), Paragraph(esc(M.SERBEST), S["p"])]
    F += [Paragraph("NASIL ÇALIŞIYOR", S["ust"]), Paragraph(esc(T["ad"]), S["h1"]), Paragraph(esc(T["mekanizma"]), S["p"]),
          Paragraph(esc(T["his"]), S["p"]), Paragraph("Nereden gelmiş olabilir", S["h2"]), Paragraph(esc(T["koken"]), S["p"]),
          Paragraph("Bu tipin erdemi", S["h2"]), Paragraph(esc(T["erdem"]), S["p"]),
          Spacer(1, 4), _kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>KÜÇÜK DENEY</font><br/>" + esc(T["kural"]), S["p"]), sol=MOR3)]
    if sonuc["cift_tip"] and not sonuc["serbest"]:
        T2 = M.TIP[sonuc["ikinci"]]
        F += [Spacer(1, 6), _kutu(Paragraph(esc(M.CIFT_TIP.format(t1=T["ad"], t2=T2["ad"])), S["p"]))]
        F += [PageBreak(), Paragraph("İKİNCİ TİPİN", S["ust"]), Paragraph(esc(T2["ad"]), S["h1"]),
              Paragraph(esc(T2["mekanizma"]), S["p"]), Paragraph(esc(T2["his"]), S["p"]),
              Paragraph("Bu tipin erdemi", S["h2"]), Paragraph(esc(T2["erdem"]), S["p"]),
              Spacer(1, 4), _kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>KÜÇÜK DENEY</font><br/>" + esc(T2["kural"]), S["p"]), sol=MOR3)]
    # 5-9 Alanlar
    for a in ALAN_SIRA:
        F += [PageBreak(), Paragraph("ALAN · %d · %s" % (y[a], b[a].upper()), S["ust"]), Paragraph(ALANLAR[a], S["h1"]),
              Cubuk("", y[a], b[a]), Spacer(1, 8), Paragraph(esc(M.ALAN_BANT[a][b[a]]), S["p"])]
        at = sonuc["alan_baskin"][a]
        if at and b[a] != "Kendinde":
            F.append(Paragraph(esc(M.ALAN_TIP[a][at]), S["pi"]))
        en = [KISA[q] for q in sonuc["alan_en"][a]]
        if en:
            F.append(Paragraph("Özellikle: " + esc(" ve ".join(en)) + ".", S["not"]))
        adim_tip = at or bask
        F += [Spacer(1, 6), _kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>BU HAFTA TEK ADIM</font><br/>" + esc(M.ALAN_ADIM[a][adim_tip]), S["p"]))]
        sen = _senaryolar(S, a, sonuc.get("cevaplar", {}))
        if sen:
            F += [Spacer(1, 6), Paragraph("Üç anda ne yaptın", S["h2"])] + sen
        F += [Spacer(1, 2)] + _baslatici_kutusu(S, no_bul(a, adim_tip))
    # 10 İkilemler
    F += _ikilemler(S, sonuc)
    # 11 Örüntüler
    oruntu = [M.ORUNTU[o] for o in sonuc["oruntu"] if o in M.ORUNTU]
    F += [PageBreak(), Paragraph("ÖRÜNTÜLER", S["ust"]), Paragraph("Alanların birbirine söylediği", S["h1"])]
    if not oruntu:
        F.append(Paragraph("Belirgin bir örüntü çıkmadı; alanlar birbirine yakın. Bu iyi haber: tek bir tipi tanımak yetiyor.", S["p"]))
    for p in oruntu:
        F.append(_kutu(Paragraph(esc(p), S["p"]))); F.append(Spacer(1, 8))
    # 12 Senin cümlen
    F += _cumle_sayfasi(S, sonuc)
    # 13 Plan: 21 gün, üç hafta
    sira = sorted(ALAN_SIRA, key=lambda k: -y[k])
    haftalar = [sira[0], sira[2], sira[-1]]
    F += [PageBreak(), Paragraph("21 GÜN", S["ust"]), Paragraph("Küçük plan", S["h1"]), Paragraph(esc(M.PLAN_GIRIS), S["p"])]
    for i, a in enumerate(haftalar):
        t = sonuc["alan_baskin"][a] or bask
        no = no_bul(a, t)
        bb = baslatici(no)
        ek = ("<br/><font color='#7A6A8C' size='8'>Deney (%s):</font> <font name='Serif' size='9.5'>%s</font>" % (no, esc(bb[1]))) if bb else ""
        F.append(_kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>HAFTA %d · %s</font><br/>" % (i + 1, esc(ALANLAR[a].upper())) +
                                 esc(M.ALAN_ADIM[a][t]) + ek, S["p"])))
        F.append(Spacer(1, 6))
    F.append(Paragraph(esc(M.PLAN_KAPANIS), S["not"]))
    # 14 Dürüstçe
    F += [PageBreak(), Paragraph("DÜRÜSTÇE", S["ust"]), Paragraph("Bu raporun sınırları", S["h1"])]
    F += [Paragraph(esc(p), S["p"]) for p in M.DURUSTCE]
    if sonuc["genis_durustce"]:
        F.append(_kutu(Paragraph(esc(M.DURUSTCE_GENIS), S["p"]), sol=HexColor("#9B3B3B")))
    # 15 Sonraki
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
    y = sonuc["alan_yuzde"]; t = sonuc["tip_yuzde"]
    F = [Paragraph("KOÇ NOTU · DANIŞANA GİTMEZ", S["ust"]), Paragraph(esc(ad), S["h1"]), Paragraph(esc(eposta), S["not"])]
    if sonuc["rapor_yok"]:
        F.append(_kutu(Paragraph("<b>RAPOR ÜRETİLMEDİ.</b> Serbest cümlede risk ifadesi var. Danışana destek maili gitti; mümkünse bugün bir insan ulaşsın.", S["p"]), sol=HexColor("#9B3B3B")))
    rows = [["Alan", "%", "Bant", "Baskın tip"]] + [[ALANLAR[a], str(y[a]), sonuc["alan_bant"][a], TIPLER.get(sonuc["alan_baskin"][a], "-") if sonuc["alan_baskin"][a] else "-"] for a in ALAN_SIRA]
    tb = Table(rows, colWidths=[140, 36, 70, 120])
    tb.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), "Sans"), ("FONTSIZE", (0, 0), (-1, -1), 8.5), ("FONTNAME", (0, 0), (-1, 0), "SansB"),
                            ("LINEBELOW", (0, 0), (-1, -1), 0.4, CIZGI), ("TEXTCOLOR", (0, 0), (-1, -1), MOR), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    F += [tb, Spacer(1, 10)]
    F.append(Paragraph("Tipler: " + ", ".join("%s %d" % (TIPLER[k], t[k]) for k in sonuc["tip_sira"]) +
                       ". Çift tip: %s. Onay yükü: %d%s." % ("evet" if sonuc["cift_tip"] else "hayır", sonuc["onay_yuku"], " (AĞIR)" if sonuc["agir_yuk"] else ""), S["p"]))
    bay = sonuc["bayraklar"]; r = sonuc["r"]
    durum = "RAPOR YOK" if sonuc["rapor_yok"] else ("İNCELEME GEREKLİ" if sonuc["incele"] else ("geniş dürüstçe" if sonuc["genis_durustce"] else "bayrak yok"))
    F.append(_kutu(Paragraph("<b>Risk</b> · r1 değersizlik: %d/4 · r2 yakının tepkisi: %s<br/>Bayraklar: değersizlik %s · donma %s · güvensizlik %s · metin %s · <b>%s</b>" % (
        r["r1"], R_SORU["r2"][1].get(r["r2"], "-"),
        "EVET" if bay["degersizlik"] else "hayır", "EVET" if bay["donma"] else "hayır",
        "EVET" if bay["guvensiz"] else "hayır", "EVET" if bay["metin"] else "hayır", durum), S["p"]),
        sol=HexColor("#9B3B3B") if (sonuc["incele"] or sonuc["rapor_yok"] or sonuc["genis_durustce"]) else ALTIN))
    if bay["guvensiz"]:
        F += [Spacer(1, 6), _kutu(Paragraph("<b>Güvenlik notu.</b> Danışan bir yakınının yanında kendini duygusal ya da fiziksel olarak güvende hissetmediğini işaretledi. Rapordaki \"sesini kullan\" deneyleri o ilişki için uygun olmayabilir; göndermeden önce bunu konuşmayı düşün.", S["p"]), sol=HexColor("#9B3B3B"))]
    F += [Spacer(1, 8), Paragraph("Örüntüler: " + (", ".join(sonuc["oruntu"]) or "yok"), S["p"])]
    ust3 = sorted(sonuc["soru_puan"], key=lambda k: -sonuc["soru_puan"][k])[:3]
    F.append(Paragraph("En yüksek üç soru: " + ", ".join("%s (%s, %d)" % (k, KISA.get(k, k), sonuc["soru_puan"][k]) for k in ust3), S["p"]))
    if sonuc["cumle"]:
        F.append(Paragraph("Beklenen onay: “" + esc(sonuc["cumle"]) + "”", S["pi"]))
    F.append(Paragraph("Görüşme olursa üç soru", S["h2"]))
    T = M.TIP[sonuc["baskin"]]
    F += [Paragraph("1. %s alanında en çok kimin onayını bekliyorsun? O kişi bir gün hiç onaylamasa ne olurdu?" % ALANLAR[sonuc["zayif"]], S["p"]),
          Paragraph("2. %s stratejisini ilk nerede öğrendiğini hatırlıyor musun? Tek bir sahne yeter." % T["ad"], S["p"]),
          Paragraph("3. Kimse görmese, kimse yorum yapmasa bu ay neyi farklı yapardın?", S["p"])]
    oneri = {"U": "Bireysel Koçluk + Sınır Haritası (hayır diyebilme, 6 seans)",
             "K": "Bireysel Koçluk (değeri başarıdan ayırma, 6-8 seans)",
             "S": "Bireysel Koçluk (ihtiyacı ve sesi görünür kılma, 6 seans)",
             "T": "ThetaHealing odak programı (tetikte olma ve güven, 3-4 seans)"}[sonuc["baskin"]]
    F.append(Paragraph("Önerilen paket: " + oneri, S["pi"]))
    doc.build(F)
    return yol
