# -*- coding: utf-8 -*-
"""Serbest cümleyi işler: en çok ertelenen şey hangi alana (I/E/B/P/K) ve hangi motora (M/G/S/D) düşüyor.

cumle_coz("Doktor randevusunu sonuç kötü çıkar diye almıyorum")
 -> {"alan": "B", "tip": "G", "ipucu": "kötü çıkar", "no": "B2", "guven": 3}
"""
import re
from .baslaticilar import no_bul

ALAN_IPUCU = [
    ("B", ["doktor", "diş", "randevu", "kontrol", "tahlil", "spor", "yürüyüş", "egzersiz", "diyet", "kilo", "uyku", "uyu", "sağlık", "ilaç", "check-up", "spor salon"]),
    ("P", ["fatura", "ödeme", "vergi", "borç", "kredi", "hesab", "bütçe", "para", "banka", "evrak", "başvuru", "belge", "sigorta", "kira", "e-devlet", "noter", "maaş"]),
    ("K", ["mesaj", "mail", "arama", "aramak", "aramadım", "konuşma", "konuşmak", "cevap", "annem", "babam", "arkadaş", "eşim", "sevgilim", "partner", "özür", "tebrik", "taziye", "whatsapp"]),
    ("E", ["dolap", " ev ", " evi", " evde", " evin", "temizlik", "bulaşık", "çamaşır", "tamir", "taşınma", " oda", " odam", "mutfak", "düzen", "arşiv", "fotoğraf", "eşya", "balkon", "garaj"]),
    ("I", [" iş ", " işi", " işe", " işte", " işim", " işler", "rapor", "proje", "tez", "ödev", "sunum", "ders", "sınav", "teslim", "müşteri", "toplantı", "kitap yaz", "yazı", "makale", "cv", "özgeçmiş", "kurs", "eğitim"]),
]

TIP_IPUCU = [
    ("G", ["kork", "kaygı", "endişe", "çekin", "utan", "kötü çık", "kötü bir şey", "bakamıyorum", "bakmak istemiyorum", "yüzleş", "gerg", "panik", "sıkış"]),
    ("M", ["mükemmel", "kusursuz", "hazır değil", "hazır olunca", "tam olsun", "düzgün", "iyi olmalı", "doğru zaman", "doğru kelime", "planlay", "sistem"]),
    ("S", ["son dakika", "son güne", "son gece", "son ana", "sonra yaparım", "vakit var", "acele", "baskı", "deadline", "yetiştir"]),
    ("D", ["zorunda", "neden ben", "neden hep ben", "dayat", "istemiyorum", "saçma", "inat", "karışmasın", "kimse bana", "haksız", "önce o"]),
]


def _temiz(s):
    s = (s or "").lower().replace("i̇", "i")
    return " " + re.sub(r"\s+", " ", s) + " "


def cumle_coz(cumle):
    s = _temiz(cumle)
    if len(s.strip()) < 4:
        return None
    alan = None
    for a, kelimeler in ALAN_IPUCU:
        if any(w in s for w in kelimeler):
            alan = a
            break
    tip, ipucu = None, None
    for t, kelimeler in TIP_IPUCU:
        for w in kelimeler:
            if w in s:
                tip, ipucu = t, w.strip()
                break
        if tip:
            break
    no = no_bul(alan, tip) if alan else None
    guven = (1 if alan else 0) + (1 if tip else 0)
    return {"alan": alan, "tip": tip, "ipucu": ipucu, "no": no, "guven": guven}
