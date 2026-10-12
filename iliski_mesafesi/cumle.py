# -*- coding: utf-8 -*-
"""Serbest cümleyi işler: partnerine söyleyemediği şey hangi boyuta (Y/U/S/O) ve hangi adıma (T/C/B/D) düşüyor.

cumle_coz("Sarılmak istiyorum ama söylersem muhtaç gibi olurum diye bekliyorum")
 -> {"boyut": "Y", "kisi": "E", "tip": "B", "ipucu": "bekli", "mesaj_no": "Y2", "guven": 3}
"""
import re

# kime: E = partnere, N = kendine
KISILER = [
    ("N", ["kendime", "kendim", "kendi ihtiyac", "yalnız kal", "tek başıma kal", "dinlenmek"]),
    ("E", ["eşim", "kocam", "karım", "sevgilim", "partnerim", "partner", "nişanlım", "erkek arkadaşım", "kız arkadaşım", " ona ", " onun ", " o "]),
]

# boyut ipuçları (sıra önemli: önce özgül olanlar)
BOYUTLAR_IPUCU = [
    ("O", ["kavga", "küs", "özür", "barış", "tartışmadan sonra", "haklı", "geçti dedim", "konuşmuyoruz"]),
    ("U", ["yalnız kal", "kendime zaman", "kendime vakit", "boğul", "nefes", "alan", "bir saat", "arkadaşlarıyla", "mesafe", "uzaklaş", "ara ist"]),
    ("Y", ["sarıl", "dokun", "yanıma", "yanımda", "yakınlık", "gel otur", "sevdiğini", "sevildiğimi", "ilgi", "cevap verm", "görüldü", "baş başa", "vakit geçir", "zaman geçir"]),
    ("S", ["söyle", "kırıl", "üzül", "rahatsız", "ihtiyac", "iste", "ev iş", "bulaşık", "ima", "anlamalı", "anlasın", "fark etm", "konuyu aç"]),
]

# adım ipuçları
TIPLER_IPUCU = [
    ("T", ["ısrar", "üst üste", "mesaj attım", "aradım", "peşinden", "neden cevap", "sen zaten", "hiç sormuyor", "sorguladım", "sordum durdum"]),
    ("C", ["uzaklaş", "odaya kapan", "çekildim", "sustum", "konuşmadım", "kaçtım", "kapıyı çarp", "cevap vermedim", "görsün", "zaten ilgilenmiyor"]),
    ("B", ["bekle", "anlamalı", "anlasın", "fark etm", "fark eder", "ima", "söylemedim", "söyleyemedim", "söyleyemiyorum", "belli etmedim", "içimde tut", "soğudum", "küstüm", "muhtaç"]),
    ("D", ["idare et", "hallettim", "hallederim", "boş ver dedim", "tamam dedim", "haklısın dedim", "kapattım", "onun istediği", "ben yaptım", "ben hazırla", "büyümesin"]),
]

# boyut × tip -> hazır cümle no (yoksa boyutun ilk cümlesi)
MESAJ_ESLE = {
    ("Y", "T"): "Y4", ("Y", "C"): "Y1", ("Y", "B"): "Y2", ("Y", "D"): "Y3",
    ("U", "T"): "U2", ("U", "C"): "U3", ("U", "B"): "U1", ("U", "D"): "U4",
    ("S", "T"): "S1", ("S", "C"): "S3", ("S", "B"): "S2", ("S", "D"): "S4",
    ("O", "T"): "O2", ("O", "C"): "O1", ("O", "B"): "O3", ("O", "D"): "O4",
}
# konu özel eşlemeleri
KONULAR = [
    (["cinsel", "yatak", "sevişme"], "S5"), (["sevdiğini söyle", "seviyor mu"], "Y5"), (["pazar", "kahve", "kitap"], "U4"),
    (["üç gün", "günlerdir", "konuşmuyoruz"], "O5"), (["geçti dedim", "geçmedi"], "O4"), (["özür diledi"], "O3"),
    (["arkadaşlarıyla", "arkadaşlarına"], "U2"), (["ara ist", "mola"], "U3"), (["ev iş", "bulaşık", "çamaşır"], "S4"),
    (["cevap verm", "görüldü", "okudu"], "Y4"), (["hafta sonu", "baş başa"], "Y3"), (["sarıl", "dokun"], "Y2"),
]


def _temiz(s):
    s = (s or "").lower().replace("i̇", "i")
    return " " + re.sub(r"\s+", " ", s) + " "


def cumle_coz(cumle):
    s = _temiz(cumle)
    if len(s.strip()) < 4:
        return None
    kisi = None
    for k, kelimeler in KISILER:
        if any(w in s for w in kelimeler):
            kisi = k
            break
    boyut = None
    for b, kelimeler in BOYUTLAR_IPUCU:
        if any(w in s for w in kelimeler):
            boyut = b
            break
    tip, ipucu = None, None
    for t, kelimeler in TIPLER_IPUCU:
        for w in kelimeler:
            if w in s:
                tip, ipucu = t, w.strip()
                break
        if tip:
            break
    mesaj_no = None
    for kelimeler, no in KONULAR:
        if any(w in s for w in kelimeler):
            mesaj_no = no
            break
    if not mesaj_no and boyut:
        mesaj_no = MESAJ_ESLE.get((boyut, tip or "B"), boyut + "1")
    guven = (1 if boyut else 0) + (1 if tip else 0) + (1 if mesaj_no else 0)
    return {"boyut": boyut, "kisi": kisi, "tip": tip, "ipucu": ipucu, "mesaj_no": mesaj_no, "guven": guven}
