# -*- coding: utf-8 -*-
"""Puanlama: cevap sözlüğünden sonuç yapısına.

cevaplar: {"a1": 0-4, ..., "a6": "a".."d", ..., "z1": "a"/"b", "cumle": str}
"""
from .sorular import F, S, Z, ALANLAR, TIPLER, BAGLAM_CIFTLERI, RISK_KELIMELER

BANTLAR = [
    (70, "Tutuyor"),
    (45, "Esniyor"),
    (20, "Sızıyor"),
    (0, "Kapı yok"),
]

TIP_MAKS = {"S": 66, "K": 54, "G": 54, "T": 53}


def bant(yuzde):
    for esik, ad in BANTLAR:
        if yuzde >= esik:
            return ad
    return "Kapı yok"


def puanla(cevaplar):
    alan_sizinti = {k: 0 for k in ALANLAR}
    alan_payda = {k: 26 for k in ALANLAR}
    tip_ham = {k: 0 for k in TIPLER}
    alan_tip = {a: {t: 0 for t in TIPLER} for a in ALANLAR}
    soru_puan = {}

    for kod, alan, tip, _ in F:
        v = int(cevaplar.get(kod, 0) or 0)
        v = max(0, min(4, v))
        soru_puan[kod] = v
        alan_sizinti[alan] += v
        tip_ham[tip] += v
        alan_tip[alan][tip] += v

    for kod, alan, _, harita in S:
        sik = str(cevaplar.get(kod, "")).strip().lower()[:1]
        hedef = harita.get(sik)
        if hedef == "YOK":
            alan_payda[alan] -= 2
            soru_puan[kod] = 0
            continue
        if hedef == "TUTAR" or hedef is None:
            soru_puan[kod] = 0
            continue
        soru_puan[kod] = 2
        alan_sizinti[alan] += 2
        tip_ham[hedef] += 2
        alan_tip[alan][hedef] += 2

    for kod, harita in Z:
        sik = str(cevaplar.get(kod, "")).strip().lower()[:1]
        hedef = harita.get(sik)
        if hedef:
            tip_ham[hedef] += 1

    alan_yuzde = {}
    for a in ALANLAR:
        payda = max(1, alan_payda[a])
        alan_yuzde[a] = int(round(100 * (1 - alan_sizinti[a] / payda)))

    tip_yuzde = {t: int(round(100 * tip_ham[t] / TIP_MAKS[t])) for t in TIPLER}
    sira = sorted(TIPLER, key=lambda t: -tip_yuzde[t])
    baskin, ikinci = sira[0], sira[1]
    cift_kapi = (tip_yuzde[baskin] - tip_yuzde[ikinci]) < 10
    tutuyor = all(v < 35 for v in tip_yuzde.values())

    alan_baskin = {}
    for a in ALANLAR:
        d = alan_tip[a]
        alan_baskin[a] = max(d, key=lambda t: d[t]) if max(d.values()) > 0 else None

    alan_sira = sorted(ALANLAR, key=lambda a: alan_yuzde[a])
    zayif, guclu = alan_sira[0], alan_sira[-1]
    secici = (alan_yuzde[guclu] - alan_yuzde[zayif]) > 25

    # bağlam çiftleri
    baglam = []
    for a_kod, i_kod, tip in BAGLAM_CIFTLERI:
        fark = soru_puan.get(a_kod, 0) - soru_puan.get(i_kod, 0)
        if abs(fark) >= 2:
            baglam.append({"tip": tip, "yon": "aile" if fark > 0 else "is", "fark": abs(fark)})

    # örüntüler
    oruntu = []
    y = alan_yuzde
    digerler = [y[a] for a in ALANLAR if a != "N"]
    if y["N"] == min(y.values()) and all(y["N"] <= d - 20 for d in digerler):
        oruntu.append("herkese_var_kendine_yok")
    if y["A"] <= 44 and y["I"] >= 70:
        oruntu.append("evde_siziyor_iste_tutuyor")
    if y["I"] <= 44 and y["A"] >= 70:
        oruntu.append("iste_siziyor_evde_tutuyor")
    if set(sira[:2]) == {"K", "G"}:
        oruntu.append("sessiz_tasiyici_ikilisi")
    if set(sira[:2]) == {"S", "T"}:
        oruntu.append("sucluluk_ustlenme_sarmali")
    dusuk = [a for a in ALANLAR if y[a] <= 19]
    if len(dusuk) == 1 and all(y[a] >= 45 for a in ALANLAR if a != dusuk[0]):
        oruntu.append("tek_alan_cokusu")
    if sum(1 for a in ALANLAR if y[a] <= 44) >= 4:
        oruntu.append("yaygin_sizinti")

    # risk bayrakları
    e5 = soru_puan.get("e5", 0)
    e8 = str(cevaplar.get("e8", "")).strip().lower()[:1]
    cumle = str(cevaplar.get("cumle", "") or "").lower()
    bayrak_korku = e5 >= 3
    bayrak_kontrol = e8 in ("a", "c", "d")
    bayrak_metin = any(k in cumle for k in RISK_KELIMELER)
    if y["E"] <= 44 and e5 >= 3:
        oruntu.append("partner_golgesi")
    incele = (bayrak_korku and bayrak_kontrol) or bayrak_metin
    genis_durustce = bayrak_korku or bayrak_kontrol or bayrak_metin

    # her alanda en yüksek iki soru
    alan_en = {}
    for a in ALANLAR:
        kodlar = [k for k, al, _, _ in F if al == a] + [k for k, al, _, _ in S if al == a]
        kodlar = sorted(kodlar, key=lambda k: -soru_puan.get(k, 0))
        alan_en[a] = [k for k in kodlar[:2] if soru_puan.get(k, 0) > 0]

    return {
        "alan_yuzde": alan_yuzde,
        "alan_bant": {a: bant(alan_yuzde[a]) for a in ALANLAR},
        "alan_sizinti": alan_sizinti,
        "alan_baskin": alan_baskin,
        "alan_en": alan_en,
        "tip_yuzde": tip_yuzde,
        "tip_sira": sira,
        "baskin": baskin,
        "ikinci": ikinci,
        "cift_kapi": cift_kapi,
        "tutuyor": tutuyor,
        "zayif": zayif,
        "guclu": guclu,
        "secici": secici,
        "baglam": baglam,
        "oruntu": oruntu,
        "bayraklar": {"korku": bayrak_korku, "kontrol": bayrak_kontrol, "metin": bayrak_metin},
        "incele": incele,
        "genis_durustce": genis_durustce,
        "soru_puan": soru_puan,
        "cumle": str(cevaplar.get("cumle", "") or "").strip(),
    }
