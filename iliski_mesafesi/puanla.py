# -*- coding: utf-8 -*-
"""Puanlama: cevap sözlüğünden sonuç yapısına.

cevaplar: {"durum": "a"/"b", "y1": 0-4, ..., "y6": "a".."d", ..., "r1": 0-4, "r2": "a".."c", "r3": "a".."d",
           "z1": "a"/"b", ..., "cumle": str}
"""
from .sorular import F, S, Z, BOYUTLAR, TIPLER, RISK_KELIMELER

BANTLAR = [(70, "Akıyor"), (45, "Takılıyor"), (20, "Tıkanıyor"), (0, "Kapalı")]
PAYDA = 5 * 4 + 3 * 2  # 26


def _tip_maks():
    m = {t: 0 for t in TIPLER}
    for _, _, _, harita in S:
        for t in set(harita.values()):
            if t in m:
                m[t] += 2
    for _, harita in Z:
        for t in set(harita.values()):
            m[t] += 1
    return m


TIP_MAKS = _tip_maks()


def bant(yuzde):
    for esik, ad in BANTLAR:
        if yuzde >= esik:
            return ad
    return "Kapalı"


def _sik(cevaplar, kod):
    return str(cevaplar.get(kod, "") or "").strip().lower()[:1]


def puanla(cevaplar):
    sizinti = {b: 0 for b in BOYUTLAR}
    tip_ham = {t: 0 for t in TIPLER}
    boyut_tip = {b: {t: 0 for t in TIPLER} for b in BOYUTLAR}
    soru_puan = {}

    for kod, boyut, ters, _ in F:
        v = int(cevaplar.get(kod, 0) or 0)
        v = max(0, min(4, v))
        if ters:
            v = 4 - v
        soru_puan[kod] = v
        sizinti[boyut] += v

    for kod, boyut, _, harita in S:
        hedef = harita.get(_sik(cevaplar, kod))
        if hedef is None or hedef == "TUTAR":
            soru_puan[kod] = 0
            continue
        soru_puan[kod] = 2
        sizinti[boyut] += 2
        tip_ham[hedef] += 2
        boyut_tip[boyut][hedef] += 2

    for kod, harita in Z:
        hedef = harita.get(_sik(cevaplar, kod))
        if hedef:
            tip_ham[hedef] += 1

    yuzde = {b: int(round(100 * (1 - sizinti[b] / PAYDA))) for b in BOYUTLAR}
    tip_yuzde = {t: int(round(100 * tip_ham[t] / TIP_MAKS[t])) for t in TIPLER}
    sira = sorted(TIPLER, key=lambda t: -tip_yuzde[t])
    baskin, ikinci = sira[0], sira[1]
    cift_adim = (tip_yuzde[baskin] - tip_yuzde[ikinci]) < 10
    serbest = all(v < 35 for v in tip_yuzde.values())

    boyut_baskin = {}
    for b in BOYUTLAR:
        d = boyut_tip[b]
        boyut_baskin[b] = max(d, key=lambda t: d[t]) if max(d.values()) > 0 else None

    b_sira = sorted(BOYUTLAR, key=lambda b: yuzde[b])
    zayif, guclu = b_sira[0], b_sira[-1]

    mesafe = yuzde["Y"] - yuzde["U"]
    mesafe_ad = "yapışık" if mesafe > 25 else ("uzak" if mesafe < -25 else "dengeli")

    # örüntüler
    oruntu = []
    if {baskin, ikinci} == {"T", "C"} and abs(tip_yuzde["T"] - tip_yuzde["C"]) < 15:
        oruntu.append("takip_cekilme")
    if yuzde["S"] <= 44 and baskin == "B":
        oruntu.append("soylemeden_bekleyen")
    if baskin == "D" and yuzde["O"] >= 70:
        oruntu.append("idare_eden")
    if mesafe_ad == "yapışık":
        oruntu.append("yapisik")
    if mesafe_ad == "uzak":
        oruntu.append("uzak")
    if yuzde["O"] <= 19:
        oruntu.append("onarim_yok")
    if sum(1 for b in BOYUTLAR if yuzde[b] <= 44) >= 3:
        oruntu.append("yaygin")

    # güvenlik
    r1 = max(0, min(4, int(cevaplar.get("r1", 0) or 0)))
    r2 = _sik(cevaplar, "r2")
    r3 = _sik(cevaplar, "r3")
    cumle = str(cevaplar.get("cumle", "") or "")
    bayraklar = {
        "korku": r1 >= 3,
        "kontrol": r2 == "a",
        "siddet": r3 in ("c", "d"),
        "fiziksel": r3 == "d",
        "metin": any(k in cumle.lower() for k in RISK_KELIMELER),
    }
    if bayraklar["korku"] and yuzde["S"] <= 44:
        oruntu.append("korku_golgesi")
    bayrak_sayisi = sum(1 for k in ("korku", "kontrol", "siddet", "metin") if bayraklar[k])
    rapor_yok = bayraklar["fiziksel"] or bayrak_sayisi >= 2
    incele = bayrak_sayisi >= 1
    genis_durustce = incele

    boyut_en = {}
    for b in BOYUTLAR:
        kodlar = [k for k, bo, _, _ in F if bo == b] + [k for k, bo, _, _ in S if bo == b]
        kodlar = sorted(kodlar, key=lambda k: -soru_puan.get(k, 0))
        boyut_en[b] = [k for k in kodlar[:2] if soru_puan.get(k, 0) > 0]

    return {
        "durum": _sik(cevaplar, "durum") or "a",
        "gecmis": _sik(cevaplar, "durum") == "b",
        "boyut_yuzde": yuzde,
        "boyut_bant": {b: bant(yuzde[b]) for b in BOYUTLAR},
        "boyut_baskin": boyut_baskin,
        "boyut_en": boyut_en,
        "tip_yuzde": tip_yuzde,
        "tip_sira": sira,
        "baskin": baskin,
        "ikinci": ikinci,
        "cift_adim": cift_adim,
        "serbest": serbest,
        "zayif": zayif,
        "guclu": guclu,
        "mesafe": mesafe,
        "mesafe_ad": mesafe_ad,
        "oruntu": oruntu,
        "bayraklar": bayraklar,
        "bayrak_sayisi": bayrak_sayisi,
        "incele": incele,
        "rapor_yok": rapor_yok,
        "genis_durustce": genis_durustce,
        "soru_puan": soru_puan,
        "r": {"r1": r1, "r2": r2, "r3": r3},
        "cumle": cumle.strip(),
        "cevaplar": {k: cevaplar.get(k) for k in cevaplar if k != "cumle"},
    }
