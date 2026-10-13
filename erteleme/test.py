# -*- coding: utf-8 -*-
"""Örnekler: mükemmeliyetçi (Defne), kaygılı (Burak), direnen + inceleme (Ece), risk cümlesi (Can).
python -m erteleme.test [çıktı klasörü]"""
import os, sys
from .sorular import S, Z
from .puanla import puanla
from .rapor import rapor_pdf, koc_notu_pdf

OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/er_test"
os.makedirs(OUT, exist_ok=True)


def sik(kod, tip):
    harita = next(h for k, _, _, h in S if k == kod)
    bul = [harf for harf, t in harita.items() if t == tip]
    return bul[0] if bul else next(harf for harf, t in harita.items() if t != "TUTAR")


def zsik(kod, tip):
    harita = next(h for k, h in Z if k == kod)
    return next((harf for harf, t in harita.items() if t == tip), "a")


def kisi(f, s_tipleri, z_tipi, r1, r2, cumle):
    """f: alan -> 5 F puanı (5. ters soru ham cevap); s_tipleri: alan -> 3 tip."""
    c = {}
    for alan, puanlar in f.items():
        for i, v in enumerate(puanlar, 1):
            c["%s%d" % (alan.lower(), i)] = v
    for alan, tipler in s_tipleri.items():
        for i, t in enumerate(tipler, 6):
            c["%s%d" % (alan.lower(), i)] = sik("%s%d" % (alan.lower(), i), t)
    for kod, _ in Z:
        c[kod] = zsik(kod, z_tipi.get(kod, ""))
    c.update(r1=r1, r2=r2, cumle=cumle)
    return c


DEFNE = kisi({"I": [3, 1, 2, 0, 1], "E": [3, 1, 1, 0, 2], "B": [2, 3, 1, 0, 1], "P": [1, 0, 3, 0, 3], "K": [2, 1, 3, 0, 1]},
             {"I": ["M", "M", "M"], "E": ["M", "TUTAR", "M"], "B": ["M", "M", "TUTAR"], "P": ["TUTAR", "M", "M"], "K": ["M", "TUTAR", "M"]},
             {"z1": "M", "z3": "M", "z4": "M", "z8": "M", "z2": "S", "z5": "S", "z6": "S", "z7": "G"},
             1, "a", "Kitabımı yazmaya başlayamıyorum çünkü hazır değilim, her şeyin kusursuz olmasını istiyorum")

BURAK = kisi({"I": [1, 3, 1, 0, 2], "E": [1, 2, 0, 0, 3], "B": [1, 1, 1, 4, 1], "P": [3, 4, 2, 0, 1], "K": [3, 2, 2, 0, 1]},
             {"I": ["G", "G", "TUTAR"], "E": ["TUTAR", "G", "G"], "B": ["G", "G", "G"], "P": ["G", "G", "G"], "K": ["G", "G", "TUTAR"]},
             {"z1": "G", "z3": "G", "z6": "G", "z7": "G", "z2": "D", "z4": "S", "z5": "S", "z8": "S"},
             2, "b", "Tahlil sonuçlarına bakmaktan korkuyorum, doktor randevusunu aylardır almıyorum")

ECE = kisi({"I": [2, 1, 3, 4, 0], "E": [1, 1, 2, 4, 2], "B": [1, 1, 3, 0, 2], "P": [3, 1, 1, 4, 1], "K": [2, 2, 1, 4, 1]},
           {"I": ["TUTAR", "D", "D"], "E": ["D", "D", "D"], "B": ["TUTAR", "D", "D"], "P": ["S", "D", "D"], "K": ["D", "D", "TUTAR"]},
           {"z2": "D", "z5": "D", "z7": "D", "z1": "M", "z3": "M", "z4": "S", "z6": "S", "z8": "S"},
           3, "c", "Yöneticimin dayattığı raporu yazmak istemiyorum, neden hep ben yapıyorum")

CAN = kisi({"I": [3, 3, 3, 3, 0], "E": [3, 3, 3, 3, 0], "B": [3, 3, 3, 3, 0], "P": [3, 3, 3, 3, 0], "K": [3, 3, 3, 3, 0]},
           {a: ["G", "G", "G"] for a in "IEBPK"}, {}, 4, "c",
           "Hiçbir şeye başlayamıyorum, artık yaşamak istemiyorum")

for ad, cev in [("Defne", DEFNE), ("Burak", BURAK), ("Ece", ECE), ("Can", CAN)]:
    s = puanla(cev)
    print(ad, s["alan_yuzde"], "tip", s["tip_yuzde"], "baskin", s["baskin"], "yuk", s["liste_yuku"],
          "oruntu", s["oruntu"], "incele", s["incele"], "genis", s["genis_durustce"], "rapor_yok", s["rapor_yok"])
    koc_notu_pdf(ad, ad.lower() + "@ornek.com", s, os.path.join(OUT, "koc-%s.pdf" % ad.lower()))
    if not s["rapor_yok"]:
        rapor_pdf(ad, s, os.path.join(OUT, "rapor-%s.pdf" % ad.lower()))
print("OK", OUT)
