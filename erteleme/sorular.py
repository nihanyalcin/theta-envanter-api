# -*- coding: utf-8 -*-
"""Erteleme Haritası soru bankası.

Kanal F: 0-4 ölçek; sızıntı puanı alana yazılır (ters sorular 4-v).
Kanal S: şık -> motor tipi (M/G/S/D) ya da "TUTAR". Şık sırası soru başına döndürülür,
         böylece "akan" cevap hep aynı harfte durmaz.
Kanal R: risk soruları, puanlamaya girmez.
Kanal Z: şık -> motor tipi, 1 puan.
"""

ALANLAR = {
    "I": "İş ve okul",
    "E": "Ev ve düzen",
    "B": "Sağlık ve beden",
    "P": "Para ve evrak",
    "K": "İlişkiler ve iletişim",
}
ALAN_SIRA = ["I", "E", "B", "P", "K"]

TIPLER = {
    "M": "Mükemmeliyetçi",
    "G": "Kaygılı",
    "S": "Son dakikacı",
    "D": "Direnen",
}

BANT_ADLARI = ["Akıyor", "Takılıyor", "Tıkanıyor", "Donmuş"]

F_SIKLAR = [
    "Hiç olmadı",
    "Oldu ama yormadı",
    "Oldu, biraz yordu",
    "Sık oldu ve yordu",
    "Neredeyse hep oldu ve çok yordu",
]

# F soruları: (kod, alan, ters_mi, metin)
F = [
    ("i1", "I", False, "Bir işe başlamadan önce \"önce şunu halledeyim\" diye başka işlere saptım."),
    ("i2", "I", False, "Teslimi yaklaşan işi açmadım; açınca ne göreceğimden çekindim."),
    ("i3", "I", False, "Son geceye kalmadan işe oturamadım."),
    ("i4", "I", False, "\"Bunu neden ben yapıyorum\" diye içimden söylenip yapmadım."),
    ("i5", "I", True, "Zor bir işin ilk 10 dakikasını planladığım saatte başlatabildim."),
    ("e1", "E", False, "Dağınık bir alanı \"hepsini bir günde yaparım\" diye bekledim, o gün gelmedi."),
    ("e2", "E", False, "Bozuk bir eşyayı ya da tamir işini haftalarca görmezden geldim."),
    ("e3", "E", False, "Ev işini ancak misafir gelecekken yapabildim."),
    ("e4", "E", False, "\"Neden hep ben\" diye kalan işi inat edip bıraktım."),
    ("e5", "E", True, "Küçük bir ev işini görünce ertelemeden beş dakikada hallettim."),
    ("b1", "B", False, "Doktor ya da diş randevusunu \"müsait olunca\" diye erteledim."),
    ("b2", "B", False, "Spora \"düzgün bir program yapınca\" başlayacaktım, başlamadım."),
    ("b3", "B", False, "Uyku saatimi \"son bir şey daha\" diye kaydırdım."),
    ("b4", "B", False, "Sağlığımla ilgili bir sonucu öğrenmekten çekinip bakmadım."),
    ("b5", "B", True, "Bedenim için küçük bir şeyi (yürüyüş, su, esneme) o gün yapabildim."),
    ("p1", "P", False, "Bir fatura, ödeme ya da başvuru son güne kadar bekledi."),
    ("p2", "P", False, "Hesabıma bakmaktan çekindim; ne kadar kaldığını görmek istemedim."),
    ("p3", "P", False, "Resmi bir evrakı \"tam anlamadan başlamam\" diye bekledim."),
    ("p4", "P", False, "\"Bu kadar bürokrasi saçma\" diye bir işi askıda bıraktım."),
    ("p5", "P", True, "Gelen bir faturayı aynı gün ödeyip kapatabildim."),
    ("k1", "K", False, "Cevaplamam gereken bir mesajı ya da maili günlerce beklettim."),
    ("k2", "K", False, "Zor bir konuşmayı \"uygun an\" diye erteledim, o an gelmedi."),
    ("k3", "K", False, "Birini arayacaktım; ne diyeceğimi tam bilmeden aramadım."),
    ("k4", "K", False, "\"Önce o adım atsın\" diye bekledim."),
    ("k5", "K", True, "Ertelenmiş bir mesajı kısa ve eksik de olsa gönderebildim."),
]

# S soruları tasarım sırasıyla: (kod, alan, durum, [(şık metni, tip), ...])  ilk şık hep TUTAR
_S_HAM = [
    ("i6", "I", "Pazartesi sabahı, önünde büyük bir rapor var.", [
        ("İlk başlığı yazarım, kötü de olsa", "TUTAR"),
        ("Önce kaynakları kusursuz toplarım", "M"),
        ("Dosyayı açmam, öğleden sonraya bırakırım", "G"),
        ("Perşembe gece başlarım, ancak öyle açılırım", "S")]),
    ("i7", "I", "Yöneticin \"bunu da sen yap\" dedi; haksız buldun.", [
        ("\"Bu hafta sığmaz, hangisi öncelik?\" derim", "TUTAR"),
        ("Tamam derim, yapmam, sorulunca bahane bulurum", "D"),
        ("Yaparım ama kusursuz olsun diye geç veririm", "M"),
        ("Düşündükçe bunalır, başka şeylere kaçarım", "G")]),
    ("i8", "I", "Sıkıcı ama zorunlu bir eğitim modülü var.", [
        ("20 dakikalık dilimlere böler, ilkini bugün yaparım", "TUTAR"),
        ("Son gün tek seferde geçerim", "S"),
        ("\"Anlamsız, yapmayacağım\" der, ertelerim", "D"),
        ("Başlarım, notları düzenlerken bitiremem", "M")]),
    ("e6", "E", "Dolap taşıyor, hafta sonu boş.", [
        ("Tek rafla başlarım", "TUTAR"),
        ("Önce kutuları, etiketleri alırım; sonra başlarım", "M"),
        ("Açmam, bakmak bile yoruyor", "G"),
        ("Birisi \"ne zaman?\" diye sorunca hiç yapasım gelmez", "D")]),
    ("e7", "E", "Mutfakta birikmiş bulaşık var, saat 23.", [
        ("On dakika yıkar, kalanı sabaha bırakırım", "TUTAR"),
        ("\"Sabah erken kalkıp hepsini yaparım\" derim, kalkamam", "S"),
        ("\"Ben kirletmedim ki\" der, bırakırım", "D"),
        ("Görmemek için mutfağa girmem", "G")]),
    ("e8", "E", "Yıllardır \"düzenlenecek\" duran fotoğraf ya da dosya arşivi.", [
        ("Bu hafta tek klasör", "TUTAR"),
        ("Önce kusursuz bir sistem kurmam lazım", "M"),
        ("Bakmak eski şeyleri açıyor, girmem", "G"),
        ("Canım isteyince; zorlamayla olmaz", "D")]),
    ("b6", "B", "Altı aydır ertelediğin bir sağlık kontrolü.", [
        ("Bugün arayıp randevu alırım", "TUTAR"),
        ("Önce en iyi doktoru araştırırım; araştırmam bitmez", "M"),
        ("\"Ya bir şey çıkarsa\" diye düşünüp aramam", "G"),
        ("Canımı yakmadıkça gitmem", "S")]),
    ("b7", "B", "Birisi \"artık spora başla\" dedi.", [
        ("\"Haftada iki yürüyüş, başlıyorum\" derim", "TUTAR"),
        ("İnadına başlamam; kimse karışmasın", "D"),
        ("Salon, program, ayakkabı araştırırım; başlamam", "M"),
        ("Utanırım, konuyu kapatırım", "G")]),
    ("b8", "B", "Gece bir, yarın erken kalkman gerekiyor.", [
        ("Telefonu bırakıp yatarım", "TUTAR"),
        ("\"Bir bölüm daha\" derim, sabah çekerim", "S"),
        ("Günün kendime ait tek saati; bırakmam", "D"),
        ("Yarını düşünüp sıkışırım, uyuyamam", "G")]),
    ("p6", "P", "Resmi bir başvurunun son tarihi iki hafta sonra.", [
        ("Bugün ilk adımı, belge listesini çıkarırım", "TUTAR"),
        ("Son gün tek oturuşta yaparım", "S"),
        ("Her şeyi öğrenmeden başlamam; zaman kalmaz", "M"),
        ("Zarfı açmam; görmezsem yokmuş gibi", "G")]),
    ("p7", "P", "Birine borcun ya da alacağın var; konuşulması gerekiyor.", [
        ("Bu hafta kısa bir mesaj yazarım", "TUTAR"),
        ("Nasıl söyleyeceğimi kurgularım; kurgu bitmez", "M"),
        ("Konu açılınca içim sıkışır, ertelerim", "G"),
        ("O açsın, ben neden açayım", "D")]),
    ("p8", "P", "Ay sonu bütçe yapman gerekiyor.", [
        ("On beş dakikada kaba bir tablo çıkarırım", "TUTAR"),
        ("Uygulama, kategori, renk... sistemi kurarken bırakırım", "M"),
        ("Rakamlara bakmak kaygı veriyor, bakmam", "G"),
        ("Bütçe bana göre değil; zorla olmaz", "D")]),
    ("k6", "K", "Haftalardır cevapsız duran bir arkadaş mesajı.", [
        ("İki cümle yazarım, geç kaldığımı söylerim", "TUTAR"),
        ("Uzun ve güzel bir cevap yazmak istiyorum, o yüzden yazamıyorum", "M"),
        ("Bu kadar geç kalınca utanıyorum, açmıyorum", "G"),
        ("O da bana geç cevap vermişti", "D")]),
    ("k7", "K", "Partnerinle konuşulması gereken bir konu var.", [
        ("\"Bu akşam on dakika konuşalım mı?\" derim", "TUTAR"),
        ("Kavga çıkmasın diye uygun anı beklerim", "G"),
        ("Taşınca patlarım; ancak öyle çıkar", "S"),
        ("O fark etsin, ben açmayacağım", "D")]),
    ("k8", "K", "Bir teşekkür, tebrik ya da taziye mesajı yazman gerekiyor.", [
        ("Kısa yazarım, bugün", "TUTAR"),
        ("Doğru kelimeleri bulamayınca yazamam", "M"),
        ("Ne hissettireceğini düşününce kaçınırım", "G"),
        ("Herkes yazıyor diye yazmak zorunda değilim", "D")]),
]


def _dondur():
    """Şık sırasını soru başına döndür: TUTAR sırayla a, b, c, d'ye kayar."""
    S, S_SIK = [], {}
    for n, (kod, alan, durum, siklar) in enumerate(_S_HAM):
        k = n % 4
        sirali = siklar[-k:] + siklar[:-k] if k else list(siklar)
        harita, metin = {}, {}
        for harf, (m, t) in zip("abcd", sirali):
            harita[harf] = t
            metin[harf] = m
        S.append((kod, alan, durum, harita))
        S_SIK[kod] = metin
    return S, S_SIK


S, S_SIK = _dondur()

# R risk soruları (puanlamaya girmez)
R_SORU = {
    "r1": ("Son iki haftada eskiden keyif aldığım şeyler de bana ağır geldi.", None),  # F ölçeği
    "r2": ("Erteleme son zamanlarda...",
           {"a": "Her zamanki gibi", "b": "Belirgin arttı; gündelik işler bile zorlaştı",
            "c": "İşimi, okulumu ya da ilişkimi tehlikeye sokacak kadar arttı"}),
}

# Z soruları: (kod, {şık: tip})
Z = [
    ("z1", {"a": "M", "b": "G"}),
    ("z2", {"a": "S", "b": "D"}),
    ("z3", {"a": "M", "b": "G"}),
    ("z4", {"a": "M", "b": "S"}),
    ("z5", {"a": "S", "b": "D"}),
    ("z6", {"a": "G", "b": "S"}),
    ("z7", {"a": "D", "b": "G"}),
    ("z8", {"a": "M", "b": "S"}),
]

Z_SORU = {
    "z1": ("Ertelerken daha çok...", {"a": "başka işlerle meşgul olurum", "b": "hiçbir şey yapmam, donarım"}),
    "z2": ("Hangisi daha çok sen?", {"a": "\"Son dakikada daha iyiyim\"", "b": "\"Kimse bana ne yapacağımı söylemesin\""}),
    "z3": ("Beni daha çok durduran...", {"a": "yetersiz olma korkusu", "b": "kötü haber alma korkusu"}),
    "z4": ("Bitirdiğimde...", {"a": "\"daha iyi olabilirdi\" derim", "b": "\"neden bu kadar beklemişim\" derim"}),
    "z5": ("İnsanlar beni nasıl bilir?", {"a": "\"Her şeyi son dakikaya bırakır\"", "b": "\"İnatçı, zorlanmayı sevmez\""}),
    "z6": ("Ertelediğim iş aklıma gelince...", {"a": "midem sıkışır, konuyu değiştiririm", "b": "\"yaparım ya\" der, geçerim"}),
    "z7": ("Birisi hatırlatınca...", {"a": "daha da yapasım gelmez", "b": "utanırım, yine de başlayamam"}),
    "z8": ("Başlamadan önce...", {"a": "planın kusursuz olması lazım", "b": "baskı olmalı, yoksa olmaz"}),
}

KISA = {
    "i1": "başlamadan önce başka işlere sapmak", "i2": "açınca ne göreceğinden çekinmek",
    "i3": "son geceye kalmak", "i4": "\"neden ben\" deyip yapmamak", "i5": "ilk 10 dakikayı başlatabilmek",
    "i6": "büyük rapor", "i7": "haksız bulunan ek iş", "i8": "sıkıcı zorunlu eğitim",
    "e1": "\"hepsini bir günde\" beklemek", "e2": "tamir işini görmezden gelmek", "e3": "ancak misafir gelince",
    "e4": "\"neden hep ben\" inadı", "e5": "beş dakikalık işi hemen yapabilmek",
    "e6": "taşan dolap", "e7": "gece birikmiş bulaşık", "e8": "düzenlenecek arşiv",
    "b1": "randevuyu ertelemek", "b2": "\"düzgün program\" beklemek", "b3": "uyku saatini kaydırmak",
    "b4": "sonuca bakmamak", "b5": "beden için küçük bir şey yapabilmek",
    "b6": "ertelenen sağlık kontrolü", "b7": "\"spora başla\" baskısı", "b8": "gece telefon",
    "p1": "son güne kalan ödeme", "p2": "hesaba bakmamak", "p3": "evrakı \"tam anlamadan\" beklemek",
    "p4": "bürokrasiye inat", "p5": "faturayı aynı gün kapatabilmek",
    "p6": "resmi başvuru", "p7": "borç-alacak konuşması", "p8": "ay sonu bütçe",
    "k1": "bekletilen mesaj", "k2": "\"uygun an\" beklenen konuşma", "k3": "ne diyeceğini bilmeden aramamak",
    "k4": "\"önce o atsın\"", "k5": "kısa da olsa gönderebilmek",
    "k6": "cevapsız arkadaş mesajı", "k7": "partnerle konuşma", "k8": "teşekkür/taziye mesajı",
}

RISK_KELIMELER = [
    "intihar", "ölmek istiyorum", "ölmek isti", "ölsem", "yaşamak istemiyorum", "yaşamak istemi",
    "kendime zarar", "kendimi öldür", "hiçbir anlamı kalmadı", "yok olmak istiyorum", "her şeye son",
]
