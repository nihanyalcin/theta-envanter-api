# -*- coding: utf-8 -*-
"""Puanlama: cevap sözlüğünden sonuç yapısına.

cevaplar: {"i1": 0-4, ..., "i6": "a".."d", ..., "r1": 0-4, "r2": "a".."c", "z1": "a"/"b", ..., "cumle": str}
"""
from .sorular import F, S, Z, ALANLAR, ALAN_SIRA, TIPLER, RISK_KELIMELER

BANTLAR = [(70, "Akıyor"), (45, "Takılıyor"), (20, "Tıkanıyor"), (0, "Donmuş")]
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
    return "Donmuş"


def _sik(cevaplar, kod):
    return str(cevaplar.get(kod, "") or "").strip().lower()[:1]


def puanla(cevaplar):
    sizinti = {a: 0 for a in ALANLAR}
    tip_ham = {t: 0 for t in TIPLER}
    alan_tip = {a: {t: 0 for t in TIPLER} for a in ALANLAR}
    soru_puan = {}

    for kod, alan, ters, _ in F:
        try:
            v = int(cevaplar.get(kod, 0) or 0)
        except (TypeError, ValueError):
            v = 0
        v = max(0, min(4, v))
        if ters:
            v = 4 - v
        soru_puan[kod] = v
        sizinti[alan] += v

    for kod, alan, _, harita in S:
        hedef = harita.get(_sik(cevaplar, kod))
        if hedef is None or hedef == "TUTAR":
            soru_puan[kod] = 0
            continue
        soru_puan[kod] = 2
        sizinti[alan] += 2
        tip_ham[hedef] += 2
        alan_tip[alan][hedef] += 2

    for kod, harita in Z:
        hedef = harita.get(_sik(cevaplar, kod))
        if hedef:
            tip_ham[hedef] += 1

    yuzde = {a: int(round(100 * (1 - sizinti[a] / PAYDA))) for a in ALANLAR}
    tip_yuzde = {t: int(round(100 * tip_ham[t] / TIP_MAKS[t])) for t in TIPLER}
    sira = sorted(TIPLER, key=lambda t: -tip_yuzde[t])
    baskin, ikinci = sira[0], sira[1]
    cift_tip = (tip_yuzde[baskin] - tip_yuzde[ikinci]) < 10
    serbest = all(v < 35 for v in tip_yuzde.values())

    alan_baskin = {}
    for a in ALANLAR:
        d = alan_tip[a]
        alan_baskin[a] = max(d, key=lambda t: d[t]) if max(d.values()) > 0 else None

    a_sira = sorted(ALAN_SIRA, key=lambda a: yuzde[a])
    zayif, guclu = a_sira[0], a_sira[-1]
    liste_yuku = int(round((yuzde[a_sira[0]] + yuzde[a_sira[1]]) / 2))
    agir_liste = liste_yuku < 30

    # örüntüler
    oruntu = []
    if {baskin, ikinci} == {"M", "G"} and abs(tip_yuzde["M"] - tip_yuzde["G"]) < 15:
        oruntu.append("mukemmel_kacis")
    if baskin == "S" and sum(1 for a in ALANLAR if 45 <= yuzde[a] <= 69) >= 3:
        oruntu.append("son_dakika")
    if yuzde[guclu] - yuzde[zayif] > 30:
        oruntu.append("secici")
    if zayif == "B" and yuzde["B"] <= 44:
        oruntu.append("beden_sonda")
    if yuzde["P"] <= 44 and tip_yuzde["G"] >= 50:
        oruntu.append("para_kacinma")
    if yuzde["K"] <= 44:
        oruntu.append("iletisim_borcu")
    if baskin == "D" and "I" in a_sira[:2]:
        oruntu.append("otorite_direnc")
    if sum(1 for a in ALANLAR if yuzde[a] <= 44) >= 3:
        oruntu.append("yaygin")

    # risk
    try:
        r1 = max(0, min(4, int(cevaplar.get("r1", 0) or 0)))
    except (TypeError, ValueError):
        r1 = 0
    r2 = _sik(cevaplar, "r2")
    cumle = str(cevaplar.get("cumle", "") or "")
    bayraklar = {
        "anhedoni": r1 >= 3,
        "artis": r2 in ("b", "c"),
        "ciddi": r2 == "c",
        "metin": any(k in cumle.lower() for k in RISK_KELIMELER),
    }
    genis_durustce = bayraklar["anhedoni"] or bayraklar["ciddi"]
    incele = bayraklar["anhedoni"] and bayraklar["artis"]
    rapor_yok = bayraklar["metin"]

    alan_en = {}
    for a in ALANLAR:
        kodlar = [k for k, al, _, _ in F if al == a] + [k for k, al, _, _ in S if al == a]
        kodlar = sorted(kodlar, key=lambda k: -soru_puan.get(k, 0))
        alan_en[a] = [k for k in kodlar[:2] if soru_puan.get(k, 0) >= 2]

    return {
        "alan_yuzde": yuzde,
        "alan_bant": {a: bant(yuzde[a]) for a in ALANLAR},
        "alan_baskin": alan_baskin,
        "alan_en": alan_en,
        "alan_sira": a_sira,
        "tip_yuzde": tip_yuzde,
        "tip_sira": sira,
        "baskin": baskin,
        "ikinci": ikinci,
        "cift_tip": cift_tip,
        "serbest": serbest,
        "zayif": zayif,
        "guclu": guclu,
        "liste_yuku": liste_yuku,
        "agir_liste": agir_liste,
        "oruntu": oruntu,
        "bayraklar": bayraklar,
        "incele": incele,
        "rapor_yok": rapor_yok,
        "genis_durustce": genis_durustce,
        "soru_puan": soru_puan,
        "r": {"r1": r1, "r2": r2},
        "cumle": cumle.strip(),
        "cevaplar": {k: cevaplar.get(k) for k in cevaplar if k != "cumle"},
    }
