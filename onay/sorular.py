# -*- coding: utf-8 -*-
"""Onay İhtiyacı Haritası soru bankası.

Kanal F: 0-4 ölçek; yük puanı alana yazılır (ters sorular 4-v).
Kanal S: şık -> onay tipi (U/K/S/T) ya da "TUTAR" (kendinde kalan cevap). Şık sırası soru başına döndürülür.
Kanal R: risk soruları, puanlamaya girmez.
Kanal Z: şık -> onay tipi, 1 puan.
"""

ALANLAR = {
    "I": "İş ve otorite",
    "A": "Aile",
    "P": "Partner ve yakın ilişki",
    "C": "Arkadaşlık ve çevre",
    "G": "Görünürlük",
}
ALAN_SIRA = ["I", "A", "P", "C", "G"]

TIPLER = {
    "U": "Uyumlu",
    "K": "Kanıtlayan",
    "S": "Silinen",
    "T": "Tetikte",
}

BANT_ADLARI = ["Kendinde", "Dalgalı", "Dışarıda", "Kaybolmuş"]

F_SIKLAR = [
    "Hiç olmadı",
    "Oldu ama yormadı",
    "Oldu, biraz yordu",
    "Sık oldu ve yordu",
    "Neredeyse hep oldu ve çok yordu",
]

# F soruları: (kod, alan, ters_mi, metin)
F = [
    ("i1", "I", False, "Yöneticim ya da hocam bir şey istediğinde, işim olduğu hâlde hayır diyemedim."),
    ("i2", "I", False, "Yaptığım işe dönüt gelmeyince bütün gün içim rahat etmedi."),
    ("i3", "I", False, "Toplantıda aklımdakini söylemedim; yanlış anlaşılırım diye sustum."),
    ("i4", "I", False, "Takdir görmek için gereğinden fazla çalıştım, mesainin dışına taştım."),
    ("i5", "I", True, "Bir fikrime itiraz edildiğinde, onaylanmasam da fikrimi savunabildim."),
    ("a1", "A", False, "Ailemin onaylamayacağını bildiğim bir kararımı onlardan sakladım."),
    ("a2", "A", False, "Aile buluşmalarında herkes memnun olsun diye kendi isteğimi geri çektim."),
    ("a3", "A", False, "Annemin ya da babamın bir sözü ya da bakışı günlerce aklımdan çıkmadı."),
    ("a4", "A", False, "Ailemde \"başarılı olan\" ya da \"sorun çıkarmayan\" rolünü sürdürmekten yoruldum."),
    ("a5", "A", True, "Ailemden biri kırılacak olsa da kendi kararımı uyguladım."),
    ("p1", "P", False, "Partnerim sessizleşince ya da mesajı gecikince yanlış bir şey yaptığımı düşündüm."),
    ("p2", "P", False, "Partnerim istemez diye kendi isteğimden (bir plan, bir arkadaş, bir uğraş) vazgeçtim."),
    ("p3", "P", False, "Kırgınlığımı söylemek yerine yuttum; ortam bozulmasın istedim."),
    ("p4", "P", False, "Sevilmeye değer olduğumu göstermek için fazlasını yaptım: iyilik, hediye, sürekli ilgi."),
    ("p5", "P", True, "Partnerime bir ihtiyacımı, nasıl karşılayacağını bilmeden de açıkça söyleyebildim."),
    ("c1", "C", False, "Gitmek istemediğim bir buluşmaya, kırılırlar diye gittim."),
    ("c2", "C", False, "Grupta herkes bir fikre katılınca, katılmasam da sesimi çıkarmadım."),
    ("c3", "C", False, "Birinin bana soğuk davrandığını hissedince ne yaptığımı kafamda tekrar tekrar düşündüm."),
    ("c4", "C", False, "Sevilmek için hep yardım eden, hep dinleyen, hep organize eden ben oldum."),
    ("c5", "C", True, "Bir arkadaşımın isteğine, bahane uydurmadan hayır diyebildim."),
    ("g1", "G", False, "Bir paylaşım yaptıktan sonra beğeni ve yorumları defalarca kontrol ettim."),
    ("g2", "G", False, "Fikrimi açıkça söylemekten, ne düşünürler diye vazgeçtim."),
    ("g3", "G", False, "Dışarı çıkmadan önce görünüşümün nasıl yorumlanacağını düşünüp huzursuz oldum."),
    ("g4", "G", False, "Başkalarının hayatına bakıp kendimi geride ya da yetersiz hissettim."),
    ("g5", "G", True, "Kimse beğenmeyecek olsa da kendi hoşuma giden bir şeyi gösterebildim."),
]

# S soruları tasarım sırasıyla: (kod, alan, durum, [(şık metni, tip), ...])  ilk şık hep TUTAR
_S_HAM = [
    ("i6", "I", "Cuma 17.30'da yöneticin acil bir iş verdi; hafta sonu planın var.", [
        ("\"Pazartesi sabah ilk iş bakarım\" derim", "TUTAR"),
        ("Tamam derim, planımı iptal ederim", "U"),
        ("Hafta sonu çalışır, kusursuz teslim ederim; fark edilsin", "K"),
        ("Hayır desem ne düşünür diye bütün akşam kafamda kurarım", "T")]),
    ("i7", "I", "Toplantıda bir fikrin var ama kimse senin gibi düşünmüyor gibi.", [
        ("Fikrimi kısaca söylerim, kabul görmese de", "TUTAR"),
        ("Susarım; nasılsa önemli değil", "S"),
        ("Çoğunluğa katılıyormuş gibi başımı sallarım", "U"),
        ("Yüzlere bakar, havayı okuyunca vazgeçerim", "T")]),
    ("i8", "I", "Bir projeyi bitirdin; kimse bir şey demedi.", [
        ("İşimin iyi olduğunu bilirim, devam ederim", "TUTAR"),
        ("Bir dahakine daha fazlasını yaparım ki görülsün", "K"),
        ("Neden bir şey demediklerini çözmeye çalışırım", "T"),
        ("Zaten beklemiyordum; arka planda kalırım", "S")]),
    ("a6", "A", "Bayramda ailen bütün günü onlarla geçirmeni bekliyor; senin başka bir planın var.", [
        ("Yarım gün gelirim, diğer yarısını kendime ayırırım", "TUTAR"),
        ("Planımı iptal ederim, kimse üzülmesin", "U"),
        ("İstediğimi söylemem bile; zaten sorulmaz", "S"),
        ("Gider, sofrayı, mutfağı, her şeyi ben üstlenirim", "K")]),
    ("a7", "A", "Annen ya da baban verdiğin bir kararı eleştirdi.", [
        ("\"Düşünceni anladım, karar benim\" derim", "TUTAR"),
        ("Kararımın doğru olduğunu kanıtlamak için daha çok çabalarım", "K"),
        ("Sesindeki tonu günlerce düşünürüm", "T"),
        ("Kararımı değiştiririm ya da değiştirmiş gibi yaparım", "U")]),
    ("a8", "A", "Aile grubunda bir konu tartışılıyor; senin fikrin farklı.", [
        ("Fikrimi bir kez, sakince yazarım", "TUTAR"),
        ("Hiç yazmam; ortalıkta görünmem", "S"),
        ("Kim ne yazdı, kim kime kızdı, sürekli takip ederim", "T"),
        ("Ortam yumuşasın diye herkese hak veririm", "U")]),
    ("p6", "P", "Partnerin bir akşam soğuk ve kısa cevaplar veriyor.", [
        ("\"Bir şey mi oldu?\" diye bir kez sorar, gerisini ona bırakırım", "TUTAR"),
        ("Ne yaptım diye geçmişi tararım, uyuyamam", "T"),
        ("Ortam yumuşasın diye her dediğine evet derim", "U"),
        ("Fazladan ilgi gösteririm, sevdiği bir şeyi yaparım", "K")]),
    ("p7", "P", "Partnerin seninle geçireceğin akşama başka bir plan yaptı; kırıldın.", [
        ("\"Kırıldım, konuşabilir miyiz?\" derim", "TUTAR"),
        ("Bir şey demem; ne de olsa önemli değil", "S"),
        ("\"Sorun değil, git tabii\" derim, içim burkulur", "U"),
        ("Bunun ne anlama geldiğini günlerce düşünür, işaret ararım", "T")]),
    ("p8", "P", "Senin için önemli bir karar var (iş, taşınma, harcama); partnerin pek sıcak bakmıyor.", [
        ("Gerekçemi anlatır, ortak bir yol ararım", "TUTAR"),
        ("Vazgeçerim; benim isteğim o kadar önemli değil", "S"),
        ("Onu ikna edecek kadar çok çalışır, haklı olduğumu ispatlarım", "K"),
        ("O nasıl isterse; yeter ki aramız bozulmasın", "U")]),
    ("c6", "C", "Bir arkadaşın son dakika senden büyük bir iyilik istedi; senin de işin var.", [
        ("\"Bu sefer olmuyor, şu kadarını yapabilirim\" derim", "TUTAR"),
        ("İşimi bırakıp koşarım", "U"),
        ("Yaparım; iyi bir arkadaş olduğumu göstermiş olurum", "K"),
        ("Hayır derim, sonra günlerce bana kızgın mı diye mesajlarına bakarım", "T")]),
    ("c7", "C", "Arkadaş grubu bir yere gitmek istiyor; sen istemiyorsun.", [
        ("\"Ben bu sefer yokum, sonrakine gelirim\" derim", "TUTAR"),
        ("Sesimi çıkarmam, giderim", "S"),
        ("\"Harika fikir!\" der, coşkuyla katılırım", "U"),
        ("Gitmezsem arkamdan ne konuşurlar diye kafamda kurarım", "T")]),
    ("c8", "C", "Bir buluşmadan sonra eve döndün.", [
        ("Güzel bir akşamdı; düşünmeden uyurum", "TUTAR"),
        ("Söylediğim her şeyi kafamda tekrar oynatırım", "T"),
        ("Bir dahakine daha eğlenceli, daha ilgili olmalıyım derim", "K"),
        ("Çok mu konuştum diye utanır, bir süre geri çekilirim", "S")]),
    ("g6", "G", "Emek verdiğin bir paylaşım beklediğin ilgiyi görmedi.", [
        ("Paylaşmak istediğim içindi; akışına bırakırım", "TUTAR"),
        ("Sık sık açıp kimin baktığını, kimin beğenmediğini kontrol ederim", "T"),
        ("Silerim; bir daha paylaşmam", "S"),
        ("Daha iyisini, daha çarpıcısını hazırlarım", "K")]),
    ("g7", "G", "Bir ortamda çoğunluğun aksine bir görüşün var.", [
        ("Görüşümü sakin bir şekilde söylerim", "TUTAR"),
        ("Ortama uyar, onlar gibi konuşurum", "U"),
        ("Hiçbir şey demem, görünmez olurum", "S"),
        ("Önce kim nasıl tepki verir diye yoklarım; çoğu zaman vazgeçerim", "T")]),
    ("g8", "G", "Biri görünüşün hakkında olumsuz bir yorum yaptı.", [
        ("Bir an canım sıkılır, sonra geçer", "TUTAR"),
        ("Kimse bir şey diyemesin diye kendimi daha çok düzeltirim", "K"),
        ("O yorumu aylarca hatırlar, aynaya her baktığımda duyarım", "T"),
        ("Gülüp geçer, \"haklısın\" derim", "U")]),
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
S_DURUM = {kod: durum for kod, _, durum, _ in _S_HAM}

# R risk soruları (puanlamaya girmez)
R_SORU = {
    "r1": ("Son iki haftada kendimi değersiz hissettim ve bu duygu günlük hayatımı zorlaştırdı.", None),  # F ölçeği
    "r2": ("Yakınlarımdan birinin tepkisi söz konusu olduğunda...",
           {"a": "Çekinirim ama kendimi güvende hissederim",
            "b": "O kadar çekinirim ki kendi kararlarımı veremez hâle gelirim",
            "c": "Kendimi duygusal ya da fiziksel olarak güvende hissetmem"}),
}

# Z soruları: (kod, {şık: tip})  her tip dört kez
Z = [
    ("z1", {"a": "U", "b": "S"}),
    ("z2", {"a": "K", "b": "T"}),
    ("z3", {"a": "U", "b": "K"}),
    ("z4", {"a": "S", "b": "T"}),
    ("z5", {"a": "U", "b": "T"}),
    ("z6", {"a": "K", "b": "S"}),
    ("z7", {"a": "U", "b": "S"}),
    ("z8", {"a": "K", "b": "T"}),
]

Z_SORU = {
    "z1": ("Bir anlaşmazlıkta daha çok...", {"a": "karşımdakine hak veririm", "b": "geri çekilir, sessizleşirim"}),
    "z2": ("Değerli hissetmem için daha çok...", {"a": "bir şey başarmam gerekir", "b": "kimsenin bana kızgın olmadığından emin olmam gerekir"}),
    "z3": ("İnsanlar beni nasıl bilir?", {"a": "\"Hayır demeyi bilmez\"", "b": "\"Her şeyi kusursuz yapar\""}),
    "z4": ("Kalabalık bir ortamda...", {"a": "fark edilmemeye çalışırım", "b": "herkesin hâlini okurum"}),
    "z5": ("Biri bana kızgın görünürse...", {"a": "hemen gönlünü alırım", "b": "nedenini bulana kadar rahat edemem"}),
    "z6": ("Bir övgü aldığımda...", {"a": "bir sonrakini nasıl hak edeceğimi düşünürüm", "b": "utanır, konuyu değiştiririm"}),
    "z7": ("Bir ihtiyacım olduğunda...", {"a": "önce başkalarının ihtiyacını hallederim", "b": "söylemem, kendim idare ederim"}),
    "z8": ("Beni en çok yoran...", {"a": "yeterince iyi olamamak", "b": "ne düşündüklerini bilmemek"}),
}

KISA = {
    "i1": "yetkiliye hayır diyememek", "i2": "dönüt gelmeyince huzursuzluk", "i3": "toplantıda susmak",
    "i4": "takdir için fazla çalışmak", "i5": "itiraza rağmen fikrini savunabilmek",
    "i6": "cuma akşamı acil iş", "i7": "toplantıda farklı fikir", "i8": "takdir görmeyen proje",
    "a1": "kararları aileden saklamak", "a2": "aile buluşmasında isteğini geri çekmek",
    "a3": "anne-babanın sözünün yankılanması", "a4": "ailedeki rolün yükü", "a5": "aile kırılsa da kararını uygulayabilmek",
    "a6": "bayram beklentisi", "a7": "anne-babanın eleştirisi", "a8": "aile grubunda farklı fikir",
    "p1": "sessizliği suçluluk gibi okumak", "p2": "partner için isteğinden vazgeçmek", "p3": "kırgınlığı yutmak",
    "p4": "sevilmek için fazlasını yapmak", "p5": "ihtiyacını açıkça söyleyebilmek",
    "p6": "partnerin soğuk akşamı", "p7": "partnerin başka planı", "p8": "partnerin sıcak bakmadığı karar",
    "c1": "kırılmasınlar diye buluşmaya gitmek", "c2": "grupta susmak", "c3": "soğukluğu kafada tekrar oynatmak",
    "c4": "hep veren taraf olmak", "c5": "bahanesiz hayır diyebilmek",
    "c6": "son dakika iyilik isteği", "c7": "istemediğin grup planı", "c8": "buluşma sonrası",
    "g1": "beğenileri kontrol etmek", "g2": "fikrini söylemekten vazgeçmek", "g3": "görünüş kaygısı",
    "g4": "karşılaştırma", "g5": "beğenilmese de gösterebilmek",
    "g6": "ilgi görmeyen paylaşım", "g7": "çoğunluğa aykırı görüş", "g8": "görünüşe olumsuz yorum",
}

RISK_KELIMELER = [
    "intihar", "ölmek istiyorum", "ölmek isti", "ölsem", "yaşamak istemiyorum", "yaşamak istemi",
    "kendime zarar", "kendimi öldür", "hiçbir anlamı kalmadı", "yok olmak istiyorum", "her şeye son",
    "beni döv", "bana vur", "beni öldür", "şiddet gör", "şiddete uğr", "bana şiddet",
]
