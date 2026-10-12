# -*- coding: utf-8 -*-
"""Üç örnek: takip eden (Selin), çekilen (Mert), risk (Zeynep). python -m iliski_mesafesi.test"""
import os, sys
from .puanla import puanla
from .rapor import rapor_pdf, koc_notu_pdf

OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/im_test"
os.makedirs(OUT, exist_ok=True)

SELIN = {"durum": "a", "y1": 3, "y2": 2, "y3": 1, "y4": 4, "y5": 2, "u1": 3, "u2": 4, "u3": 2, "u4": 0, "u5": 1,
         "s1": 2, "s2": 3, "s3": 2, "s4": 1, "s5": 2, "o1": 1, "o2": 2, "o3": 2, "o4": 1, "o5": 3,
         "y6": "d", "y7": "c", "y8": "b", "u6": "b", "u7": "b", "u8": "c", "s6": "c", "s7": "d", "s8": "a",
         "o6": "a", "o7": "d", "o8": "b", "r1": 1, "r2": "c", "r3": "b",
         "z1": "a", "z2": "a", "z3": "a", "z4": "a", "z5": "a", "z6": "a", "z7": "a", "z8": "b",
         "cumle": "Mesaj attım saatlerdir görüldü ama cevap yok, üst üste yazdım sonra kendime kızdım"}

MERT = {"durum": "a", "y1": 2, "y2": 3, "y3": 4, "y4": 0, "y5": 1, "u1": 0, "u2": 0, "u3": 1, "u4": 4, "u5": 3,
        "s1": 3, "s2": 2, "s3": 3, "s4": 4, "s5": 1, "o1": 3, "o2": 1, "o3": 3, "o4": 2, "o5": 1,
        "y6": "c", "y7": "b", "y8": "c", "u6": "c", "u7": "a", "u8": "b", "s6": "d", "s7": "a", "s8": "c",
        "o6": "d", "o7": "c", "o8": "d", "r1": 0, "r2": "c", "r3": "a",
        "z1": "b", "z2": "b", "z3": "b", "z4": "b", "z5": "b", "z6": "b", "z7": "a", "z8": "a",
        "cumle": "Kavga çıkmasın diye bir konuyu aylardır açmıyorum, uzaklaşıyorum, o da fark etmiyor"}

ZEYNEP = {"durum": "a", "y1": 4, "y2": 3, "y3": 3, "y4": 2, "y5": 0, "u1": 4, "u2": 2, "u3": 4, "u4": 2, "u5": 0,
          "s1": 4, "s2": 4, "s3": 3, "s4": 4, "s5": 0, "o1": 3, "o2": 0, "o3": 4, "o4": 1, "o5": 0,
          "y6": "b", "y7": "d", "y8": "d", "u6": "b", "u7": "c", "u8": "d", "s6": "b", "s7": "b", "s8": "d",
          "o6": "b", "o7": "b", "o8": "d", "r1": 4, "r2": "a", "r3": "c",
          "z1": "b", "z2": "a", "z3": "a", "z4": "b", "z5": "b", "z6": "b", "z7": "b", "z8": "a",
          "cumle": "Telefonumu kontrol ediyor, bağırınca susuyorum, söylemeye korkuyorum"}

for ad, cev in [("Selin", SELIN), ("Mert", MERT), ("Zeynep", ZEYNEP)]:
    s = puanla(cev)
    print(ad, s["boyut_yuzde"], "tip", s["tip_yuzde"], "baskin", s["baskin"], "mesafe", s["mesafe"], s["mesafe_ad"],
          "oruntu", s["oruntu"], "bayrak", s["bayrak_sayisi"], "incele", s["incele"], "rapor_yok", s["rapor_yok"])
    koc_notu_pdf(ad, ad.lower() + "@ornek.com", s, os.path.join(OUT, "koc-%s.pdf" % ad.lower()))
    if not s["rapor_yok"]:
        rapor_pdf(ad, s, os.path.join(OUT, "rapor-%s.pdf" % ad.lower()))
print("OK", OUT)
