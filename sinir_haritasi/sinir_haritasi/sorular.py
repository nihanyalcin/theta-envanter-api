# -*- coding: utf-8 -*-
"""Sınır Haritası soru bankası.

Kanal F: 0-4 ölçek, puan Tip sütunundaki sızıntı tipine yazılır.
Kanal S: şık -> tip (S/K/G/T) ya da "TUTAR". E8'de "e" = yok (paydadan düşer).
Kanal Z: şık -> tip, 1 puan.
"""

ALANLAR = {
    "A": "Aile",
    "I": "İş",
    "R": "Arkadaş ve çevre",
    "E": "Eş ve partner",
    "N": "Kendine",
}

TIPLER = {
    "S": "Suçluluk kapısı",
    "K": "Çatışma kaçınması",
    "G": "Görünmezlik",
    "T": "Tek başına taşıma",
}

F_SIKLAR = [
    "Hiç olmadı",
    "Oldu ama yormadı",
    "Oldu, biraz yordu",
    "Sık oldu ve yordu",
    "Neredeyse hep oldu ve çok yordu",
]

# F soruları: (kod, alan, tip, metin)
F = [
    ("a1", "A", "S", "Annem ya da babam bir şey istediğinde, istemesem de \"tamam\" dedim."),
    ("a2", "A", "K", "Ailede bir konu beni rahatsız etti ama tartışma çıkmasın diye sustum."),
    ("a3", "A", "G", "Aileme bir şeyi açıkça söylemedim, anlamalarını bekledim; anlamayınca kırıldım."),
    ("a4", "A", "T", "Aile organizasyonunu, bakımını ya da işini kimse istemeden ben üstlendim."),
    ("a5", "A", "S", "Aileden gelen son dakika isteklere planımı bozarak evet dedim."),
    ("i1", "I", "S", "Mesai bitiminde gelen işe, kendi planımı bozarak evet dedim."),
    ("i2", "I", "K", "İşte haksızlık olduğunu düşündüğüm bir durumda sesimi çıkarmadım."),
    ("i3", "I", "G", "Yaptığım işin fark edilmemesine içerledim ama dile getirmedim."),
    ("i4", "I", "T", "Başkasının işini \"daha hızlı olur\" diye kendim yaptım."),
    ("i5", "I", "S", "İş saatleri dışında gelen mesajlara hemen cevap verdim."),
    ("r1", "R", "S", "Arkadaş ya da çevreden gelen isteklere, istemediğim halde evet dedim."),
    ("r2", "R", "K", "Bir arkadaşımın beni üzen davranışını ona söylemedim."),
    ("r3", "R", "G", "Hep ben aradım, hep ben dinledim; dengesizliği dile getirmedim."),
    ("r4", "R", "T", "Grup işini (organizasyon, veli grubu, apartman) ben üstlendim."),
    ("r5", "R", "S", "Borç, ürün, aracılık gibi bir isteği reddedemedim."),
    ("e1", "E", "S", "Partnerimin isteğine, kendi ihtiyacımı erteleyerek evet dedim."),
    ("e2", "E", "K", "İlişkide rahatsız olduğum bir konuyu kavga çıkmasın diye açmadım."),
    ("e3", "E", "G", "Partnerimin ne hissettiğimi anlamasını bekledim, anlamayınca kırıldım."),
    ("e4", "E", "T", "Ev ve ilişki yükünü \"ben hallederim\" diyerek tek başıma taşıdım."),
    ("e5", "E", "S", "Partnerime hayır dediğimde tepkisinden çekindim."),
    ("n1", "N", "S", "Kendim için ayırdığım zamanı, başkası istedi diye iptal ettim."),
    ("n2", "N", "K", "Yorgun olduğumu söylemek yerine \"iyiyim\" dedim."),
    ("n3", "N", "G", "Bir ihtiyacımı kimseye söylemedim, fark etmelerini beklerim."),
    ("n4", "N", "T", "Dinlenmek yerine \"bitirmeden rahat edemem\" diye devam ettim."),
    ("n5", "N", "S", "Kendime bir şey alırken suçluluk duydum ya da vazgeçtim."),
]

# S soruları: (kod, alan, metin, {şık: tip})
S = [
    ("a6", "A", "Annen hafta sonu yemeğe çağırdı, sen bitkinsin.",
     {"a": "S", "b": "TUTAR", "c": "K", "d": "G"}),
    ("a7", "A", "Kardeşin yine çocuğuna bakmanı istedi, bu ay üçüncü.",
     {"a": "T", "b": "TUTAR", "c": "G", "d": "S"}),
    ("a8", "A", "Bayramda herkesin sende toplanması bekleniyor.",
     {"a": "T", "b": "K", "c": "TUTAR", "d": "S"}),
    ("i6", "I", "Yöneticin saat 18:00'de \"yarın sabaha\" diye iş verdi.",
     {"a": "S", "b": "TUTAR", "c": "K", "d": "G"}),
    ("i7", "I", "İş arkadaşın işini sana yıkıyor.",
     {"a": "K", "b": "TUTAR", "c": "T", "d": "G"}),
    ("i8", "I", "Müşteri kapsam dışı iş istiyor, bedava.",
     {"a": "S", "b": "TUTAR", "c": "K", "d": "G"}),
    ("r6", "R", "Arkadaşın gece 23:30'da uzun bir dert mesajı attı, sen uyuyacaktın.",
     {"a": "S", "b": "TUTAR", "c": "K", "d": "G"}),
    ("r7", "R", "Veli grubunda sınıf annesi olman isteniyor.",
     {"a": "T", "b": "TUTAR", "c": "K", "d": "S"}),
    ("r8", "R", "Arkadaşın borç istedi; geçen borç dönmedi.",
     {"a": "S", "b": "TUTAR", "c": "K", "d": "G"}),
    ("e6", "E", "Partnerin sana sormadan akşam planı yaptı.",
     {"a": "S", "b": "TUTAR", "c": "G", "d": "K"}),
    ("e7", "E", "Ev işi yine sende kaldı.",
     {"a": "T", "b": "TUTAR", "c": "G", "d": "K"}),
    ("e8", "E", "Partnerin telefonunu, paranı ya da kiminle görüştüğünü kontrol etmek istiyor.",
     {"a": "S", "b": "TUTAR", "c": "K", "d": "G", "e": "YOK"}),
    ("n6", "N", "Hastasın, ziyaretçi gelmek istiyor.",
     {"a": "S", "b": "TUTAR", "c": "T", "d": "G"}),
    ("n7", "N", "Boş bir cumartesi öğleden sonran var.",
     {"a": "T", "b": "TUTAR", "c": "S", "d": "K"}),
    ("n8", "N", "Gece 3'te uyandın, kafanda yarının listesi.",
     {"a": "T", "b": "TUTAR", "c": "S", "d": "G"}),
]

# Z soruları: (kod, {şık: tip})
Z = [
    ("z1", {"a": "S", "b": "K"}),
    ("z2", {"a": "G", "b": "T"}),
    ("z3", {"a": "S", "b": "G"}),
    ("z4", {"a": "K", "b": "T"}),
    ("z5", {"a": "S", "b": "T"}),
    ("z6", {"a": "K", "b": "G"}),
    ("z7", {"a": "T", "b": "S"}),
    ("z8", {"a": "K", "b": "G"}),
]

BAGLAM_CIFTLERI = [("a5", "i1", "S"), ("a2", "i2", "K"), ("a3", "i3", "G")]

# Soru kısa etiketleri (raporda "özellikle ... ve ..." için)
KISA = {
    "a1": "anne-babanın istekleri", "a2": "aile içi suskunluk", "a3": "ailede anlaşılmayı beklemek",
    "a4": "aile işini üstlenmek", "a5": "aileden son dakika istekler",
    "a6": "yemek daveti", "a7": "çocuk bakımı isteği", "a8": "bayram organizasyonu",
    "i1": "mesai sonrası iş", "i2": "işte haksızlığa sessiz kalmak", "i3": "fark edilmeyen emek",
    "i4": "başkasının işini yapmak", "i5": "mesai dışı mesajlar",
    "i6": "akşam gelen acil iş", "i7": "yıkılan iş", "i8": "kapsam dışı istek",
    "r1": "çevreden gelen istekler", "r2": "üzen arkadaşa susmak", "r3": "tek taraflı arkadaşlık",
    "r4": "grup işini üstlenmek", "r5": "borç ve aracılık istekleri",
    "r6": "gece gelen dert mesajı", "r7": "sınıf annesi isteği", "r8": "dönmeyen borç",
    "e1": "partnerin isteklerinde kendini ertelemek", "e2": "ilişkide konuyu açmamak",
    "e3": "partnerin anlamasını beklemek", "e4": "ev yükünü tek taşımak", "e5": "hayır deyince çekinmek",
    "e6": "sorulmadan yapılan plan", "e7": "ev işi", "e8": "telefon ve para kontrolü",
    "n1": "kendi zamanını iptal etmek", "n2": "yorgunken iyiyim demek", "n3": "ihtiyacını söylememek",
    "n4": "bitirmeden dinlenememek", "n5": "kendine alırken suçluluk",
    "n6": "hastayken ziyaretçi", "n7": "boş cumartesi", "n8": "gece üç listesi",
}

RISK_KELIMELER = [
    "bağır", "vur", "tehdit", "korku", "kork", "şiddet", "döv", "kıskanç",
    "yasak", "izin vermiyor", "intihar", "ölmek istiyorum", "ölmek isti",
]
