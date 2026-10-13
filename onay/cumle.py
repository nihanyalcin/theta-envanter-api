# -*- coding: utf-8 -*-
"""Serbest cümleyi işler: beklenen onay hangi alana (I/A/P/C/G) ve hangi tipe (U/K/S/T) düşüyor.

cumle_coz("Annemi kırmaktan korktuğum için taşınamıyorum")
 -> {"alan": "A", "tip": "U", "ipucu": "kırmak", "no": "A1", "guven": 2}
"""
import re
from .baslaticilar import no_bul

ALAN_IPUCU = [
    ("P", ["eşim", "eşimi", "eşime", "eşimin", "sevgili", "partner", "kocam", "karım", "nişanlı", "flört", "ilişkim"]),
    ("A", ["annem", "babam", "annemi", "babamı", "anneme", "babama", "anne", "baba", "kardeş", "ailem", "aile",
           "kayınval", "kaynan", "abla", "abi", "teyze", "dayı", "hala", "amca", "oğlum", "kızım", "çocuklar"]),
    ("I", ["patron", "yönetici", "müdür", " iş ", " işte", " işim", "hoca", "öğretmen", "şirket", "ekip", "toplantı",
           "müşteri", "terfi", "mesai", "meslektaş", "çalışma arkadaş"]),
    ("C", ["arkadaş", "dost", "grup", "çevrem", "komşu", "kankam"]),
    ("G", ["instagram", "takipçi", "beğeni", "paylaşım", "sosyal medya", "görünüş", "kilo", "yorum",
           "insanlar ne", "elalem", "el alem", "herkes", "youtube", "tiktok"]),
]

TIP_IPUCU = [
    ("U", ["hayır diyemi", "hayır deme", "kırılır", "kırmak", "kırmaktan", "üzülür", "üzmek", "üzmekten", "küser",
           "darıl", "memnun", "idare", "evet de", "gönlünü"]),
    ("K", ["başar", "kanıtla", "ispat", "yeterli", "yetersiz", "takdir", "gurur", "hak et", "değerli", "mükemmel",
           "fark edil", "beğenilmek", "aferin"]),
    ("S", ["sessiz", "susuyorum", "susarım", "söyleyemi", "görünmez", "yük olmak", "rahatsız etmek", "kendimi geri",
           "isteyemi", "isteğimi"]),
    ("T", ["ne düşün", "kızgın", "kızar", "tepki", "sessizleş", "mesaj", "yüzü", "bakış", "tavır", "tavr", "soğuk",
           "cevap vermi"]),
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
                m = re.search(r"\w*" + re.escape(w.strip()) + r"\w*", s)
                tip, ipucu = t, (m.group(0) if m else w.strip())
                break
        if tip:
            break
    no = no_bul(alan, tip) if alan else None
    guven = (1 if alan else 0) + (1 if tip else 0)
    return {"alan": alan, "tip": tip, "ipucu": ipucu, "no": no, "guven": guven}
