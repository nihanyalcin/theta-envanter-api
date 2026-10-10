# -*- coding: utf-8 -*-
"""Sınır Haritası rapor PDF'i (ReportLab, telefon boyu 9:16)."""
import os
from datetime import date
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, Table, TableStyle, NextPageTemplate, KeepTogether, Flowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from .sorular import ALANLAR, TIPLER, KISA
from . import metinler as M

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
if not os.path.exists(os.path.join(FONT_DIR, "DejaVuSans.ttf")):
    FONT_DIR = "/usr/share/fonts/truetype/dejavu"
_registered = False


def _fonts():
    global _registered
    if _registered:
        return
    for ad, dosya in [("Serif", "DejaVuSerif.ttf"), ("SerifB", "DejaVuSerif-Bold.ttf"),
                      ("SerifI", "DejaVuSerif-Italic.ttf"), ("Sans", "DejaVuSans.ttf"),
                      ("SansB", "DejaVuSans-Bold.ttf")]:
        pdfmetrics.registerFont(TTFont(ad, os.path.join(FONT_DIR, dosya)))
    _registered = True


MOR = HexColor("#2A1640"); MOR2 = HexColor("#4A2A6B"); MOR3 = HexColor("#6B3FA0")
ALTIN = HexColor("#C9A24D"); ALTIN2 = HexColor("#E6C77A"); KREM = HexColor("#F6F0E6")
KREM2 = HexColor("#FFFBF4"); SOLUK = HexColor("#7A6A8C"); CIZGI = HexColor("#EADFCB")
BANT_RENK = {"Tutuyor": HexColor("#5C8A5C"), "Esniyor": HexColor("#C9A24D"),
             "Sızıyor": HexColor("#C76B3F"), "Kapı yok": HexColor("#9B3B3B")}

W, H, MARJ = 420, 746, 26


def _styles():
    return {
        "ust": ParagraphStyle("ust", fontName="SansB", fontSize=7.5, leading=10, textColor=ALTIN, spaceAfter=4),
        "h1": ParagraphStyle("h1", fontName="SerifB", fontSize=24, leading=29, textColor=MOR, spaceAfter=8),
        "h2": ParagraphStyle("h2", fontName="SerifB", fontSize=14.5, leading=18, textColor=MOR, spaceBefore=6, spaceAfter=4),
        "p": ParagraphStyle("p", fontName="Sans", fontSize=9.8, leading=15, textColor=MOR, spaceAfter=8),
        "pi": ParagraphStyle("pi", fontName="SerifI", fontSize=11, leading=16, textColor=MOR2, spaceAfter=8),
        "cumle": ParagraphStyle("cumle", fontName="Serif", fontSize=12.5, leading=18, textColor=MOR, spaceAfter=6),
        "not": ParagraphStyle("not", fontName="Sans", fontSize=8.5, leading=12.5, textColor=SOLUK, spaceAfter=6),
        "num": ParagraphStyle("num", fontName="SerifB", fontSize=30, leading=34, textColor=ALTIN),
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
    """Yüzde çubuğu: etiket, çubuk, yüzde."""
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


def _bg_krem(c, doc):
    c.setFillColor(KREM); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(SOLUK); c.setFont("Sans", 7)
    c.drawCentredString(W / 2, 14, "Sınır Haritası · Theta Kapısı · %d" % doc.page)


def _bg_mor(c, doc):
    c.setFillColor(MOR); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(MOR2); c.circle(W * 0.85, H * 0.85, 140, fill=1, stroke=0)
    c.setFillColor(MOR); c.circle(W * 0.85, H * 0.85, 100, fill=1, stroke=0)
    c.setStrokeColor(ALTIN); c.setLineWidth(0.8); c.rect(14, 14, W - 28, H - 28, fill=0, stroke=1)


def _kutu(flow, genislik=W - 2 * MARJ, zemin=KREM2, sol=ALTIN):
    t = Table([[flow]], colWidths=[genislik])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), zemin), ("BOX", (0, 0), (-1, -1), 0.6, CIZGI),
                           ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                           ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                           ("LINEBEFORE", (0, 0), (0, -1), 2.2, sol)]))
    return t


def _mor_sayfa(S, ust, baslik, alt):
    return [NextPageTemplate("mor"), PageBreak(), Spacer(1, 250), Paragraph(ust, S["bolum_n"]), Spacer(1, 8),
            Paragraph(esc(baslik), S["bolum_h"]), Spacer(1, 14), Paragraph(esc(alt), S["bolum_p"]),
            NextPageTemplate("krem"), PageBreak()]


def rapor_pdf(ad, sonuc, yol, whatsapp_link="https://wa.me/", tarih=None):
    _fonts(); S = _styles()
    tarih = tarih or date.today().strftime("%d.%m.%Y")
    y, b = sonuc["alan_yuzde"], sonuc["alan_bant"]
    bask = sonuc["baskin"]; T = M.TIP[bask]
    doc = BaseDocTemplate(yol, pagesize=(W, H), leftMargin=MARJ, rightMargin=MARJ, topMargin=30, bottomMargin=30,
                          title="Sınır Haritası · " + ad, author="Theta Kapısı")
    fr = Frame(MARJ, 30, W - 2 * MARJ, H - 60, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="krem", frames=[fr], onPage=_bg_krem),
                          PageTemplate(id="mor", frames=[fr], onPage=_bg_mor)])
    F = []
    # 1 Kapak
    F += [NextPageTemplate("mor"), Spacer(1, 190), Paragraph("THETA KAPISI", S["kapak_u"]), Spacer(1, 14),
          Paragraph("Sınır Haritası", S["kapak_h"]), Spacer(1, 16),
          Paragraph(esc(ad) + " için hazırlandı", S["kapak_p"]), Paragraph(tarih, S["kapak_p"]), Spacer(1, 290),
          Paragraph("thetakapisi.com.tr", S["kapak_u"]), NextPageTemplate("krem"), PageBreak()]
    # 2 Tek bakışta
    F += [Paragraph("TEK BAKIŞTA", S["ust"]), Paragraph("Haritan", S["h1"])]
    for a in ["A", "I", "R", "E", "N"]:
        F.append(Cubuk(ALANLAR[a], y[a], b[a])); F.append(Spacer(1, 6))
    F += [Spacer(1, 10)]
    if sonuc["tutuyor"]:
        ozet = "Dört kapı da düşük açılıyor; sınırın büyük ölçüde tutuyor."
    elif sonuc["cift_kapi"]:
        ozet = "Baskın kapıların: <b>%s</b> ve <b>%s</b>." % (T["ad"], M.TIP[sonuc["ikinci"]]["ad"])
    else:
        ozet = "Baskın kapın: <b>%s</b>." % T["ad"]
    F.append(_kutu(Paragraph(ozet + " En zayıf alanın <b>%s</b> (%d), en güçlü alanın <b>%s</b> (%d)." % (
        ALANLAR[sonuc["zayif"]], y[sonuc["zayif"]], ALANLAR[sonuc["guclu"]], y[sonuc["guclu"]]), S["cumle"])))
    F += [Spacer(1, 10), Paragraph("Yüzde, o alanda sınırın ne kadar tuttuğunu gösterir: 100 tam tutuyor, 0 hiç tutmuyor. Bantlar: Tutuyor 70+, Esniyor 45-69, Sızıyor 20-44, Kapı yok 0-19.", S["not"])]
    # 3 Ne ne değil
    F += [PageBreak(), Paragraph("BAŞLAMADAN", S["ust"]), Paragraph("Bu rapor ne, ne değil", S["h1"])]
    F += [Paragraph(esc(p), S["p"]) for p in M.NE_NE_DEGIL]
    # 4 Baskın tip
    F += _mor_sayfa(S, "BASKIN KAPIN", T["ad"], T["karsi"])
    if sonuc["tutuyor"]:
        F += [Paragraph("SINIRIN TUTUYOR", S["ust"]), Paragraph("Dört kapı da düşük", S["h1"]), Paragraph(esc(M.TUTUYOR), S["p"])]
    else:
        F += [Paragraph("NASIL ÇALIŞIYOR", S["ust"]), Paragraph(esc(T["ad"]), S["h1"]), Paragraph(esc(T["mekanizma"]), S["p"]),
              Paragraph(esc(T["his"]), S["p"]), Paragraph("Nereden gelmiş olabilir", S["h2"]), Paragraph(esc(T["koken"]), S["p"]),
              Paragraph("Bu kapının erdemi", S["h2"]), Paragraph(esc(T["erdem"]), S["p"])]
        if sonuc["cift_kapi"]:
            T2 = M.TIP[sonuc["ikinci"]]
            F += [Spacer(1, 4), _kutu(Paragraph(esc(M.CIFT_KAPI.format(t1=T["ad"], t2=T2["ad"])), S["p"]))]
            F += [PageBreak(), Paragraph("İKİNCİ KAPIN", S["ust"]), Paragraph(esc(T2["ad"]), S["h1"]),
                  Paragraph(esc(T2["mekanizma"]), S["p"]), Paragraph(esc(T2["his"]), S["p"]),
                  Paragraph("Bu kapının erdemi", S["h2"]), Paragraph(esc(T2["erdem"]), S["p"])]
    # 5-9 Alanlar
    for a in ["A", "I", "R", "E", "N"]:
        F += [PageBreak(), Paragraph("ALAN · %d · %s" % (y[a], b[a].upper()), S["ust"]), Paragraph(ALANLAR[a], S["h1"]),
              Cubuk("", y[a], b[a]), Spacer(1, 8), Paragraph(esc(M.ALAN_BANT[a][b[a]]), S["p"])]
        at = sonuc["alan_baskin"][a]
        if at and b[a] != "Tutuyor":
            F.append(Paragraph(esc(M.ALAN_TIP[a][at]), S["pi"]))
        en = [KISA[k] for k in sonuc["alan_en"][a]]
        if en:
            F.append(Paragraph("Özellikle: " + esc(" ve ".join(en)) + ".", S["not"]))
        adim_tip = at or bask
        adim, no = M.ALAN_ADIM[a][adim_tip]
        F += [Spacer(1, 6), _kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>BU HAFTA TEK ADIM</font><br/>" + esc(adim) +
                                             "<br/><font color='#7A6A8C' size='8'>Hazır cümle: Hayır Deme Cümleleri, mesaj %s</font>" % no, S["p"]))]
    # 10 Örüntüler
    oruntu = [M.ORUNTU[o] for o in sonuc["oruntu"] if o in M.ORUNTU]
    baglam = [M.BAGLAM[(bg["tip"], bg["yon"])] for bg in sonuc["baglam"] if (bg["tip"], bg["yon"]) in M.BAGLAM]
    F += [PageBreak(), Paragraph("ÖRÜNTÜLER", S["ust"]), Paragraph("Alanların birbirine söylediği", S["h1"])]
    if sonuc["secici"]:
        F.append(Paragraph("Alanların arasında 25 puandan fazla fark var: sınırın yok değil, seçici. Kime koyup kime koyamadığına bak; cevap genellikle en eski ilişkide.", S["pi"]))
    if not oruntu and not baglam:
        F.append(Paragraph("Belirgin bir örüntü çıkmadı; alanlar birbirine yakın. Bu iyi haber: tek bir kapıyı tanımak yetiyor.", S["p"]))
    for p in oruntu + baglam:
        F.append(_kutu(Paragraph(esc(p), S["p"]))); F.append(Spacer(1, 8))
    # 11 Senin cümlen
    if sonuc["cumle"]:
        F += [PageBreak(), Paragraph("SENİN CÜMLEN", S["ust"]), Paragraph("Hayır demek istediğin an", S["h1"]),
              _kutu(Paragraph("“" + esc(sonuc["cumle"]) + "”", S["cumle"]), zemin=white), Spacer(1, 14),
              Paragraph("Bu cümleyi bir daha oku. İçinde \"peki\" dediğin an var; o an senin kapın. Rapordan çıkan karşı cümle:", S["p"]),
              Paragraph(esc(T["karsi"]), S["pi"])]
    # 12 Plan
    sira = sorted(ALANLAR, key=lambda k: -y[k])
    F += [PageBreak(), Paragraph("30 GÜN", S["ust"]), Paragraph("Küçük plan", S["h1"]),
          Paragraph("Haftada bir alan, her hafta tek davranış. En güçlü alandan başlıyor, en zayıfa son hafta geliyorsun; kas önce kolay yerde çalışır.", S["p"])]
    for i, a in enumerate(sira[:4] if sira[-1] in sira[:4] else sira[:3] + [sira[-1]]):
        F.append(_kutu(Paragraph("<font name='SansB' color='#C9A24D' size='7'>HAFTA %d</font><br/>" % (i + 1) + esc(M.PLAN_HAFTA[a]), S["p"])))
        F.append(Spacer(1, 6))
    F.append(Paragraph("Beşinci alan bu ay dinleniyor. Dört hafta sonra envanteri yeniden doldur; fark genellikle ilk ayda görünür.", S["not"]))
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
    """Nihan'a giden ayrı sayfa."""
    _fonts(); S = _styles()
    doc = BaseDocTemplate(yol, pagesize=(W, H), leftMargin=MARJ, rightMargin=MARJ, topMargin=30, bottomMargin=30, title="Koç notu · " + ad)
    fr = Frame(MARJ, 30, W - 2 * MARJ, H - 60, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="krem", frames=[fr], onPage=_bg_krem)])
    y = sonuc["alan_yuzde"]; t = sonuc["tip_yuzde"]
    F = [Paragraph("KOÇ NOTU · DANIŞANA GİTMEZ", S["ust"]), Paragraph(esc(ad), S["h1"]), Paragraph(esc(eposta), S["not"])]
    rows = [["Alan", "%", "Bant", "Baskın tip"]] + [[ALANLAR[a], str(y[a]), sonuc["alan_bant"][a], TIPLER.get(sonuc["alan_baskin"][a], "-") if sonuc["alan_baskin"][a] else "-"] for a in ALANLAR]
    tb = Table(rows, colWidths=[120, 36, 70, 140])
    tb.setStyle(TableStyle([("FONTNAME", (0, 0), (-1, -1), "Sans"), ("FONTSIZE", (0, 0), (-1, -1), 8.5), ("FONTNAME", (0, 0), (-1, 0), "SansB"),
                            ("LINEBELOW", (0, 0), (-1, -1), 0.4, CIZGI), ("TEXTCOLOR", (0, 0), (-1, -1), MOR), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    F += [tb, Spacer(1, 10)]
    F.append(Paragraph("Tipler: " + ", ".join("%s %d" % (TIPLER[k], t[k]) for k in sonuc["tip_sira"]) + ". Çift kapı: %s. Seçici: %s." % ("evet" if sonuc["cift_kapi"] else "hayır", "evet" if sonuc["secici"] else "hayır"), S["p"]))
    bay = sonuc["bayraklar"]
    F.append(_kutu(Paragraph("<b>Bayraklar</b> · korku: %s · kontrol: %s · metin: %s · <b>İnceleme: %s</b>" % (
        "EVET" if bay["korku"] else "hayır", "EVET" if bay["kontrol"] else "hayır", "EVET" if bay["metin"] else "hayır",
        "GEREKLİ" if sonuc["incele"] else "gerekmiyor"), S["p"]), sol=HexColor("#9B3B3B") if sonuc["incele"] else ALTIN))
    F += [Spacer(1, 8), Paragraph("Örüntüler: " + (", ".join(sonuc["oruntu"]) or "yok"), S["p"])]
    ust3 = sorted(sonuc["soru_puan"], key=lambda k: -sonuc["soru_puan"][k])[:3]
    F.append(Paragraph("En yüksek üç soru: " + ", ".join("%s (%s, %d)" % (k, KISA.get(k, k), sonuc["soru_puan"][k]) for k in ust3), S["p"]))
    if sonuc["cumle"]:
        F.append(Paragraph("Açık uçlu: “" + esc(sonuc["cumle"]) + "”", S["pi"]))
    F.append(Paragraph("Görüşme olursa üç soru", S["h2"]))
    T = M.TIP[sonuc["baskin"]]
    F += [Paragraph("1. %s alanındaki en yüksek soruyu anlat: o an ne oldu, ne dedin, sonra ne hissettin?" % ALANLAR[sonuc["zayif"]], S["p"]),
          Paragraph("2. %s kapısını ilk nerede öğrendiğini hatırlıyor musun? Tek bir sahne yeter." % T["ad"], S["p"]),
          Paragraph("3. Bu ay tek bir sınır koysan ve tutsa, hayatında ne değişirdi?", S["p"])]
    oneri = "ThetaHealing odak programı (3-4 seans, tema: %s)" % T["ad"] if sonuc["baskin"] in ("S", "G") else "Bireysel Koçluk (haftalık, 6-8 seans, sınır ve devretme)"
    F.append(Paragraph("Önerilen paket: " + oneri, S["pi"]))
    doc.build(F)
    return yol
