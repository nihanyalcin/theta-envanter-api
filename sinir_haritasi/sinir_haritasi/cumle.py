# -*- coding: utf-8 -*-
"""Serbest cümleyi işler: kime hayır diyemedi (alan) ve hangi kapıdan (tip).

cumle_coz("Annem bayramda bizde toplanalım dedi, ayıp olur diye evet dedim")
 -> {"alan": "A", "kisi": "annen", "tip": "S", "ipucu": "ayıp", "guven": 2}
"""
import re

# kişi kelimesi -> (alan, raporda kullanılacak hitap)
KISILER = [
    ("A", "annen", ["annem", "anne ", "anneannem", "babaannem", "annemin", "anneme"]),
    ("A", "baban", ["babam", "babamın", "babama", "baba "]),
    ("A", "kardeşin", ["kardeşim", "kardeşimin", "abim", "ablam", "abla", "abi ", "kız kardeş", "erkek kardeş"]),
    ("A", "ailen", ["ailem", "ailemin", "akraba", "teyzem", "halam", "dayım", "amcam", "yengem", "eniştem", "kuzen"]),
    ("A", "kayınvaliden", ["kayınvalide", "kaynana", "kayınpeder", "kayınbirader", "görümce", "elti"]),
    ("A", "çocuğun", ["oğlum", "kızım", "çocuğum", "çocuklarım"]),
    ("I", "yöneticin", ["patron", "müdür", "yönetici", "amirim", "şefim", "genel müdür", "ceo"]),
    ("I", "müşterin", ["müşteri", "danışan", "öğrenci velisi"]),
    ("I", "iş arkadaşın", ["iş arkadaş", "mesai arkadaş", "ekip", "takım arkadaş", "meslektaş", "ortağım"]),
    ("I", "işin", ["işte ", "işyeri", "iş yeri", "ofis", "toplantı", "mesai", "proje", "şirket"]),
    ("R", "arkadaşın", ["arkadaşım", "arkadaş", "dostum", "kanka", "ahbap"]),
    ("R", "komşun", ["komşu", "apartman", "site yönetimi"]),
    ("R", "veli grubu", ["veli grubu", "sınıf annesi", "okul grubu", "whatsapp grubu", "grup"]),
    ("E", "eşin", ["eşim", "kocam", "karım", "hanımım", "beyim", "sevgilim", "partnerim", "partner", "nişanlım", "erkek arkadaşım", "kız arkadaşım"]),
    ("N", "kendin", ["kendime", "kendim", "kendi ihtiyac", "dinlenmek", "uyumak"]),
]

# konu kelimesi -> mesaj no (cümledeki duruma en yakın hazır mesaj)
KONULAR = [
    (["bayram"], "05"), (["yemeğe", "yemek", "sofra"], "01"), (["çocuğuna bak", "çocuk bak", "bebeğe bak", "torun"], "04"),
    (["akıl ver", "karış"], "02"), (["habersiz", "kapıya gel"], "09"), (["düğün"], "07"), (["miras"], "52"),
    (["vakit ayır", "aramıyorsun", "gelmiyorsun"], "06"), (["para", "borç"], "21"), (["kefil"], "50"),
    (["ev iş", "bulaşık", "çamaşır", "temizlik"], "12"), (["plan yap", "planlamış", "program yap"], "11"),
    (["telefon", "şifre"], "16"), (["yakınlık", "ilişkiye gir"], "14"),
    (["mesai", "akşam altı", "yarın sabah", "gece yap"], "27"), (["hafta sonu çalış", "cumartesi çalış"], "28"),
    (["işini bana", "işini yık", "benim üstüme"], "29"), (["toplantı"], "30"), (["bedava", "ücretsiz", "danışma"], "34"),
    (["gece mesaj", "gece yazıyor", "gece arıyor"], "32"), (["terfi"], "33"), (["eleştir", "performans"], "37"),
    (["sınıf annesi", "veli"], "39"), (["kek", "etkinlik"], "40"), (["komşu"], "42"), (["apartman", "yönetici ol"], "45"),
    (["araba", "bırak"], "46"), (["satış", "ürün", "destek ol"], "47"), (["hediye", "liste"], "49"), (["indirim"], "51"),
    (["hasta", "ziyaret"], "53"), (["yas", "cenaze", "vefat"], "54"), (["organize", "düzenle"], "55"),
    (["doğum", "bebek", "loğusa"], "56"), (["terapi", "ne oldu"], "57"), (["kimse sormuyor", "bana soran yok"], "58"),
    (["kahve", "son dakika", "buluşalım"], "19"), (["geç kal"], "22"), (["tatil"], "23"), (["dert", "gece gündüz"], "25"),
    (["haksız yere", "hemen cevap", "kavgada"], "17"),
]


# kapı ipuçları: (tip, [kelimeler])
KAPILAR = [
    ("S", ["suçlu", "üzül", "kırıl", "ayıp", "kıyamad", "kötü", "vicdan", "mahcup", "sevilme", "incin", "gönlü", "hayal kırıklığı", "yüzüne bakamam"]),
    ("K", ["kavga", "tartış", "gerginlik", "gerilim", "bozulmasın", "bozulur", "sorun çıkmasın", "huzur", "sessiz kald", "konuyu kapat", "ses çıkarmad", "surat", "küs"]),
    ("G", ["anlamalı", "anlasın", "fark etm", "görmüyor", "görülm", "kimse sormuyor", "değer verm", "takdir", "beklerdim", "ima", "hissettirdim", "belli ettim", "söylemedim ama"]),
    ("T", ["ben yapar", "ben hallettim", "hallederim", "kimse yapamaz", "kimse yapmaz", "başkası yapamaz", "devredemed", "benden başka", "üstlendim", "yüklendim", "yine ben", "her zamanki gibi ben", "tek başıma"]),
]


def _temiz(s):
    s = (s or "").lower().replace("i̇", "i")
    return " " + re.sub(r"\s+", " ", s) + " "


def cumle_coz(cumle):
    s = _temiz(cumle)
    if len(s.strip()) < 4:
        return None
    alan, kisi, tip, ipucu = None, None, None, None
    for a, hitap, kelimeler in KISILER:
        for k in kelimeler:
            if k in s:
                alan, kisi = a, hitap
                break
        if alan:
            break
    for t, kelimeler in KAPILAR:
        for k in kelimeler:
            if k in s:
                tip, ipucu = t, k.strip()
                break
        if tip:
            break
    konu_no = None
    for kelimeler, no in KONULAR:
        if any(k in s for k in kelimeler):
            konu_no = no
            break
    guven = (1 if alan else 0) + (1 if tip else 0) + (1 if konu_no else 0)
    return {"alan": alan, "kisi": kisi, "tip": tip, "ipucu": ipucu, "konu_no": konu_no, "guven": guven}
