# -*- coding: utf-8 -*-
"""20 Başlatıcı: no -> (durum, ilk 10 dakika, takılırsan).

Numara = alan harfi + motor sırası (1 M, 2 G, 3 S, 4 D). İletişim başlatıcıları hazır mesaj içerir.
"""
TIP_NO = {"M": "1", "G": "2", "S": "3", "D": "4"}

BASLATICILAR = {
    # İş ve okul
    "I1": ("Büyük bir iş var ve \"henüz hazır değilim\" diyorsun.",
           "Zamanlayıcıyı 10 dakikaya kur ve bilerek kötü bir ilk taslak yaz. Başlık, üç madde, yarım cümleler. Silmek yasak; düzeltmek yarının işi.",
           "Kötü yazmak bile zor geliyorsa sadece başlıkları yaz. Boş sayfa ile dolu sayfa arasındaki fark, mükemmel sayfa ile dolu sayfa arasındaki farktan büyüktür."),
    "I2": ("Açmaktan çekindiğin bir dosya ya da mail var.",
           "Sadece aç ve ilk paragrafı oku. Cevap vermek, düzeltmek, karar vermek yok. Okuduğun şeyi tek cümleyle bir kâğıda yaz: \"İçinde şu var.\"",
           "Açmak bile ağır geliyorsa birinden yanında oturmasını iste. Korkulan şey çoğu zaman kapalıyken büyür, açılınca küçülür."),
    "I3": ("İş hep son geceye kalıyor.",
           "Kendine sahte bir teslim saati koy: bugün 18:00'de yarım hâlini birine göndereceksin. Kime göndereceğini şimdi seç ve ona haber ver.",
           "Haber verecek kimse yoksa yarım hâli kendine mail at, konu satırına saati yaz. Baskıyı gece değil gündüz üret."),
    "I4": ("Sana dayatılmış, haksız bulduğun bir iş var.",
           "\"Bunu kendi yolumla yapacağım\" de ve işte değiştirebileceğin tek bir şeyi değiştir: sıra, araç, saat, yer. Sonra ilk 10 dakikayı kendi kuralınla başlat.",
           "Asıl mesele işin kendisi değil de yükse, bunu söyle: \"Bu hafta bunu alırsam şu kayar; hangisi öncelik?\" Yapmamak bir cümle kadar net değildir."),
    # Ev ve düzen
    "E1": ("Dağınık bir alan \"hepsini bir günde\" yapılmayı bekliyor.",
           "Tek raf ya da tek çekmece seç. Zamanlayıcı 10 dakika. Süre dolunca yarıda da olsa bırak; bitmemiş raf, hiç başlanmamış dolaptan iyidir.",
           "Hangi raftan başlayacağını seçemiyorsan göz hizasındakinden başla. Seçim de bir erteleme biçimidir."),
    "E2": ("Bakmaya kıyamadığın, içine girmediğin bir köşe var.",
           "Bugün sadece fotoğrafını çek. Dokunmak, ayırmak, atmak yok. Fotoğrafa bakıp içinde ne olduğunu üç kelimeyle yaz.",
           "Eşyalar bir hatırayı açıyorsa bunu yazmaya izin ver. Ertelenen bazen dolap değil, dolabın açtığı duygudur."),
    "E3": ("Ev işleri ancak misafir gelecekken yapılıyor.",
           "Misafir geliyormuş gibi 10 dakika: en görünen yüzeyi topla. Süre bitince dur. Bunu haftada iki kez aynı saate bağla.",
           "Gerçekten birini çağırmak da işe yarar. Baskıya ihtiyacın varsa onu kendin kur, krize bırakma."),
    "E4": ("\"Neden hep ben\" diye inat ettiğin bir ev işi var.",
           "Paylaşımı söyle. Hazır mesaj: \"Bu hafta çamaşır sende, ben bulaşıktayım. Böyle bölelim mi?\" Gönder ve kendi payını yap.",
           "Karşı taraf yapmazsa onun payını yapma. İnat değil, sınır: senin payın bitti."),
    # Sağlık ve beden
    "B1": ("Spora \"düzgün bir program\" yapınca başlayacaksın.",
           "Bugün 10 dakika yürü. Program, salon, ayakkabı yok. Dönünce takvime bir sonraki 10 dakikayı yaz.",
           "Yürümek bile çok geliyorsa merdiven, esneme, pencere önünde beş derin nefes. Beden düzenle değil, tekrarla değişir."),
    "B2": ("Aylardır ertelediğin bir sağlık kontrolü var.",
           "Sadece randevu al. Gitmek ayrı bir adım; bugünün işi yalnızca telefon ya da internetten tarih seçmek.",
           "Sonuçtan korkuyorsan bunu birine söyle ve randevuya birlikte gitmeyi iste. Bilmemek, bilmekten daha uzun sürer."),
    "B3": ("Uyku saatin \"bir şey daha\" diye kayıyor.",
           "Bu akşam telefonu yatak odasının dışında şarja tak. Yerine bir kitap ya da defter koy.",
           "Gece saatleri günün tek \"sana ait\" zamanıysa onu gündüze taşı: akşam yemeğinden sonra yarım saat sadece senin."),
    "B4": ("\"Kimse karışmasın\" diye bedenin için hiçbir şey yapmıyorsun.",
           "Kendi seçtiğin, kimseye söylemediğin tek küçük şey: bir bardak su, beş dakika esneme, kısa bir yürüyüş. Seçim senin.",
           "Biri karıştıkça yapasın gelmiyorsa onlara değil kendine söz ver. Kendi kuralın, başkasının kuralına inattan daha sağlamdır."),
    # Para ve evrak
    "P1": ("Bütçe için kusursuz bir sistem kurmayı bekliyorsun.",
           "On beş dakikalık kaba tablo: gelen, giden, kalan. Kategori, renk, uygulama yok. Rakamlar yuvarlak olabilir.",
           "Tablo bile ağır geliyorsa sadece bu ayın üç büyük gideri. Kaba harita, mükemmel haritadan daha çok yol gösterir."),
    "P2": ("Hesabına bakmaktan çekiniyorsun.",
           "Sadece bakiyeyi gör ve bir kâğıda yaz. Yorum yapmak, plan kurmak, kendini suçlamak yok. Bugünün işi yalnızca bakmak.",
           "Bakmak içini sıkıştırıyorsa bakarken nefesini say. Rakam ne olursa olsun, bilmek kontrolün ilk adımıdır."),
    "P3": ("Ödemeler ve başvurular hep son güne kalıyor.",
           "Bugün bir faturayı otomatik ödemeye bağla ya da takvime son tarihten üç gün önceye hatırlatma koy.",
           "Hangisinden başlayacağını bilmiyorsan en küçük tutarlıdan başla. Kazanılan ilk küçük zafer bir sonrakini kolaylaştırır."),
    "P4": ("Bürokrasi seni öyle sinirlendiriyor ki işi askıda bırakıyorsun.",
           "Bugün sadece belge listesini çıkar. Doldurmak, göndermek yarının işi. Listeyi göz önünde bir yere as.",
           "Öfke haklı olabilir; ama bedelini sistem değil sen ödüyorsun. Öfkeyi bir cümleyle yaz, sonra listeye dön."),
    # İlişkiler ve iletişim
    "K1": ("Uzun ve güzel bir cevap yazmak istediğin için hiç yazamadığın bir mesaj var.",
           "İki cümle gönder: \"Geç kaldım ama seni düşündüm. Hafta sonu uzun uzun yazacağım.\" Sonra takvime hafta sonunu yaz.",
           "Hafta sonu gelince yine uzun yazamazsan beş cümle yeter. İlişkiyi uzun mesaj değil, düzenli temas taşır."),
    "K2": ("Bu kadar geç kaldığın için utandığın bir mesaj var.",
           "Utancı söyleyerek başla: \"Bu kadar geç yazdığım için mahcubum, ama yazmak istedim. Nasılsın?\" Gönder.",
           "Cevap gelmezse ikinci mesaj atma; senin işin kapıyı açmaktı. Gecikme utancı, yeni gecikmenin en büyük sebebidir."),
    "K3": ("Bir konuşmayı ancak taşınca, patlayınca yapabiliyorsun.",
           "Bugün gönder: \"Bu akşam on dakika konuşabilir miyiz? Bir şeyi sakin sakin anlatmak istiyorum.\" Saati sen öner.",
           "Konuşmada sesin yükselirse dur ve \"yirmi dakika ara\" de. Baskı olmadan konuşmak, ilk seferde tuhaf gelir."),
    "K4": ("\"Önce o adım atsın\" diye beklediğin biri var.",
           "İlk adımı sen at; kısa ve sitemsiz: \"Seni özledim, bir kahve içelim mi?\" Geçmişi bu mesaja taşıma.",
           "Karşılık gelmezse bu senin değerini değil, onun o günkü hâlini gösterir. Sen adımını attın."),
}


def baslatici(no):
    """(durum, eylem, takılırsan) döndürür; yoksa None."""
    return BASLATICILAR.get(str(no).upper())


def no_bul(alan, tip):
    return alan + TIP_NO.get(tip or "M", "1")
