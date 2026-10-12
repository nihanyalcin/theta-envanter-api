# -*- coding: utf-8 -*-
"""İlişki Mesafesi Haritası soru bankası.

Kanal F: 0-4 ölçek; sızıntı puanı boyuta yazılır (ters sorular 4-v).
Kanal S: şık -> döngü tipi (T/C/B/D) ya da "TUTAR".
Kanal R: güvenlik soruları, puanlamaya girmez.
Kanal Z: şık -> döngü tipi, 1 puan.
"""

BOYUTLAR = {
    "Y": "Yaklaşma",
    "U": "Alan alabilme",
    "S": "Söyleyebilme",
    "O": "Onarım",
}

TIPLER = {
    "T": "Takip eden",
    "C": "Çekilen",
    "B": "Bekleyen",
    "D": "Düzenleyen",
}

BANT_ADLARI = ["Akıyor", "Takılıyor", "Tıkanıyor", "Kapalı"]

F_SIKLAR = [
    "Hiç olmadı",
    "Oldu ama yormadı",
    "Oldu, biraz yordu",
    "Sık oldu ve yordu",
    "Neredeyse hep oldu ve çok yordu",
]

DURUM_SIKLARI = {"a": "Şu an bir ilişkim var", "b": "Son ilişkimi düşünerek dolduruyorum"}

# F soruları: (kod, boyut, ters_mi, metin)
F = [
    ("y1", "Y", False, "Yakınlık istedim ama söylemek yerine bekledim."),
    ("y2", "Y", False, "Sarılmak, dokunmak istedim ama ilk adımı atamadım."),
    ("y3", "Y", False, "\"Gel, biraz otur yanıma\" demek bana muhtaçlık gibi geldi."),
    ("y4", "Y", False, "Yakınlaşmak istediğimde karşılık alamayınca ısrar ettim; mesaj üstüne mesaj attım."),
    ("y5", "Y", True, "İhtiyacım olduğunda \"bana ihtiyacın var mı\" diye sormadan yanına gidebildim."),
    ("u1", "U", False, "Kendime zaman ayırdığımda suçlu hissettim."),
    ("u2", "U", False, "Partnerim kendine zaman ayırdığında bunu bana mesafe olarak okudum."),
    ("u3", "U", False, "Yalnız kalmak istedim ama \"ne der\" diye isteyemedim."),
    ("u4", "U", False, "Gerginlikte tek rahatladığım yer uzaklaşmak oldu; yakınlık boğdu."),
    ("u5", "U", True, "\"Bu akşam kendime ihtiyacım var\" diyebildim ve bunu açıklamak zorunda kalmadım."),
    ("s1", "S", False, "Bir şeye kırıldım, söylemedim, soğuk davrandım."),
    ("s2", "S", False, "İhtiyacımı doğrudan istemek yerine ima ettim."),
    ("s3", "S", False, "\"Söylemem gerekiyorsa zaten anlamı yok\" diye düşündüm."),
    ("s4", "S", False, "Kavga çıkmasın diye bir konuyu açmadım."),
    ("s5", "S", True, "Rahatsız olduğum bir şeyi aynı gün sakin bir cümleyle söyleyebildim."),
    ("o1", "O", False, "Kavgadan sonra günlerce küs kaldım ya da ilk adımı hep o attı."),
    ("o2", "O", False, "Haklı olduğumu kanıtlamak uzlaşmaktan önemli geldi."),
    ("o3", "O", False, "\"Tamam geçti\" dedim ama geçmemişti; içimde tuttum."),
    ("o4", "O", False, "Özür dilemek bana yenilgi gibi geldi."),
    ("o5", "O", True, "Kavgadan sonra 24 saat içinde \"ikimiz de üzüldük, konuşalım\" diyebildim."),
]

# S soruları: (kod, boyut, durum, {şık: tip})  — şık metinleri S_SIK'ta
S = [
    ("y6", "Y", "Zor bir gün geçirdin, eve geldin, o telefonda.", {"a": "TUTAR", "b": "B", "c": "C", "d": "T"}),
    ("y7", "Y", "Hafta sonu baş başa vakit istiyorsun, o arkadaşlarıyla plan yapmış.", {"a": "TUTAR", "b": "C", "c": "T", "d": "B"}),
    ("y8", "Y", "Mesaj attın, üç saattir görüldü ama cevap yok.", {"a": "TUTAR", "b": "T", "c": "C", "d": "B"}),
    ("u6", "U", "Pazar sabahı tek başına kahve içip kitap okumak istiyorsun.", {"a": "TUTAR", "b": "B", "c": "C", "d": "D"}),
    ("u7", "U", "Partnerin \"bu hafta sonu arkadaşlarımla gidiyorum\" dedi.", {"a": "TUTAR", "b": "T", "c": "B", "d": "D"}),
    ("u8", "U", "Tartışma kızıştı, sakinleşmek için ara istiyorsun.", {"a": "TUTAR", "b": "C", "c": "T", "d": "D"}),
    ("s6", "S", "Doğum gününü unuttu.", {"a": "TUTAR", "b": "B", "c": "T", "d": "C"}),
    ("s7", "S", "Ev işi dağılımı seni yoruyor.", {"a": "TUTAR", "b": "B", "c": "D", "d": "T"}),
    ("s8", "S", "Cinsel yakınlıkta bir şey istiyorsun ya da istemiyorsun.", {"a": "TUTAR", "b": "B", "c": "C", "d": "D"}),
    ("o6", "O", "Kavga ettiniz, ertesi sabah.", {"a": "TUTAR", "b": "B", "c": "D", "d": "C"}),
    ("o7", "O", "Haksız olduğunu fark ettin.", {"a": "TUTAR", "b": "D", "c": "C", "d": "T"}),
    ("o8", "O", "O özür diledi.", {"a": "TUTAR", "b": "T", "c": "B", "d": "D"}),
]

S_SIK = {
    "y6": {"a": "Yanına oturup \"bugün kötüydü, biraz sarıl\" derim", "b": "Bir şey demem, yorgunluğumu belli ederim",
           "c": "Odaya çekilirim, zaten ilgilenmiyor", "d": "\"Hiç sormuyorsun bile\" diye başlarım"},
    "y7": {"a": "\"Cumartesi sana ayrılsın istiyorum\" derim", "b": "Gider, ben de kendi programımı doldururum, söylemem",
           "c": "Planını iptal ettirmeye çalışırım", "d": "Giderken ses çıkarmam, dönünce soğuk olurum"},
    "y8": {"a": "Meşguldür der, akşam konuşurum", "b": "Üst üste yazar, ararım",
           "c": "Ben de cevap vermem, görsün", "d": "Bir şey demem ama \"değer vermiyor\" diye düşünürüm"},
    "u6": {"a": "\"Bir saat kendime ayırıyorum\" der, okurum", "b": "Okurum ama aklım onda, suçlu hissederim",
           "c": "Söylemeden odaya kapanırım", "d": "Ona kahvaltı hazırlarım, kitabı unuturum"},
    "u7": {"a": "\"İyi eğlen, dönünce bana anlat\" derim", "b": "\"Benimle vakit geçirmek istemiyor musun\" derim",
           "c": "Tamam der, hafta sonu boyunca soğuk olurum", "d": "Onun gideceği yerin planını ben yaparım"},
    "u8": {"a": "\"Yirmi dakika ara, sonra devam\" derim", "b": "Kapıyı çarpıp çıkarım, saatlerce dönmem",
           "c": "Ara isteyemem, bitene kadar kalırım", "d": "Konuyu ben kapatırım: \"tamam haklısın\""},
    "s6": {"a": "\"Üzüldüm, benim için önemliydi\" derim", "b": "Hatırlamasını beklerim, hatırlamazsa küserim",
           "c": "\"Sen zaten hiçbir şeyi önemsemiyorsun\" derim", "d": "Boş ver, ben de kendime hediye alırım"},
    "s7": {"a": "\"Bu hafta bulaşık sende\" derim", "b": "Yapar, içimden söylenirim",
           "c": "Yapar, zaten o yapamıyor", "d": "Yapmam, birikir, kavga çıkar"},
    "s8": {"a": "Söylerim", "b": "Söylemem, zamanla anlar",
           "c": "Söylemem, uzaklaşırım", "d": "Onun istediği gibi olsun, idare ederim"},
    "o6": {"a": "\"Dün ikimiz de yorulduk, konuşalım mı\" derim", "b": "O konuşana kadar beklerim",
           "c": "Hiçbir şey olmamış gibi davranırım", "d": "Odaya kapanırım, günlerce"},
    "o7": {"a": "\"Haklıydın, özür dilerim\" derim", "b": "Özür dilemem, davranışımla telafi ederim",
           "c": "Konuyu kapatır, bir daha açmam", "d": "\"Ama sen de…\" ile başlarım"},
    "o8": {"a": "\"Teşekkür ederim, duydum\" der kabul ederim", "b": "\"Geç bile kaldı\" derim",
           "c": "Kabul ederim ama günlerce hatırlatırım", "d": "\"Boş ver, önemli değil\" der geçiştiririm"},
}

# R güvenlik soruları (puanlamaya girmez)
R_SORU = {
    "r1": ("Partnerime katılmadığımı söylemekten korkuyorum.", None),  # F ölçeği
    "r2": ("Partnerim telefonumu, paramı ya da kiminle görüştüğümü kontrol etmek istiyor.",
           {"a": "Evet, ve gösteriyorum", "b": "Evet, ama \"mahremiyetim var\" diyebiliyorum", "c": "Hayır, böyle bir durum yok"}),
    "r3": ("Kavgalarda bağırma, aşağılama, eşya kırma ya da fiziksel bir şey oldu mu?",
           {"a": "Hiç", "b": "Bağırma oldu", "c": "Aşağılama ya da tehdit oldu", "d": "Fiziksel bir şey oldu"}),
}

# Z soruları: (kod, {şık: tip})
Z = [
    ("z1", {"a": "T", "b": "C"}),
    ("z2", {"a": "B", "b": "D"}),
    ("z3", {"a": "T", "b": "C"}),
    ("z4", {"a": "D", "b": "B"}),
    ("z5", {"a": "T", "b": "B"}),
    ("z6", {"a": "T", "b": "C"}),
    ("z7", {"a": "B", "b": "D"}),
    ("z8", {"a": "D", "b": "B"}),
]

Z_SORU = {
    "z1": ("Gerginlikte daha çok…", {"a": "yaklaşırım, konuşmak isterim", "b": "uzaklaşırım, susarım"}),
    "z2": ("Hangisi daha çok sen?", {"a": "Söylemesem de anlamalı", "b": "Ben hallederim, mesele büyümesin"}),
    "z3": ("Beni daha çok yoran…", {"a": "terk edilme korkusu", "b": "boğulma hissi"}),
    "z4": ("Kavgadan sonra…", {"a": "ilk adımı ben atarım, bazen hakkım olmasa da", "b": "beklerim, o atsın"}),
    "z5": ("Partnerim beni nasıl bilir?", {"a": "\"Çok ister, çok sorar\"", "b": "\"Hiçbir şey istemez, belli etmez\""}),
    "z6": ("Kırgınlığımı…", {"a": "hemen söylerim, bazen sert", "b": "içimde tutarım, soğurum"}),
    "z7": ("İlişkide zor olan…", {"a": "istemek", "b": "bırakmak, kontrolü vermek"}),
    "z8": ("\"İyiyim\" dediğimde genelde…", {"a": "kavga uzamasın diye derim", "b": "fark etmesini beklediğim için derim"}),
}

# Soru kısa etiketleri
KISA = {
    "y1": "yakınlığı beklemek", "y2": "ilk adımı atamamak", "y3": "istemeyi muhtaçlık saymak",
    "y4": "karşılık gelmeyince ısrar", "y5": "sormadan yanına gidebilmek",
    "y6": "zor gün, o telefonda", "y7": "baş başa hafta sonu", "y8": "cevapsız mesaj",
    "u1": "kendine zaman ayırınca suçluluk", "u2": "onun alanını mesafe okumak", "u3": "yalnız kalmayı isteyememek",
    "u4": "gerginlikte uzaklaşmak", "u5": "açıklamasız alan isteyebilmek",
    "u6": "pazar sabahı kitap", "u7": "onun arkadaş hafta sonu", "u8": "tartışmada ara istemek",
    "s1": "kırılıp söylememek", "s2": "ima etmek", "s3": "söylemek anlamsız demek",
    "s4": "kavga çıkmasın diye açmamak", "s5": "aynı gün sakin söyleyebilmek",
    "s6": "unutulan doğum günü", "s7": "ev işi yükü", "s8": "cinsel yakınlıkta istek",
    "o1": "günlerce küslük", "o2": "haklı çıkmak", "o3": "geçmemişken geçti demek",
    "o4": "özrü yenilgi saymak", "o5": "24 saatte geri dönebilmek",
    "o6": "kavga sonrası sabah", "o7": "haksız olduğunu fark etmek", "o8": "özrü kabul etmek",
}

RISK_KELIMELER = [
    "bağır", "vur", "tehdit", "korku", "kork", "şiddet", "döv", "kıskanç",
    "yasak", "izin vermiyor", "intihar", "ölmek istiyorum", "ölmek isti",
    "takip ediyor", "konumumu", "şifremi", "çıkmama izin", "paramı alıyor", "tokat", "itti",
]
