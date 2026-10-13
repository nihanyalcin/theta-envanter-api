# -*- coding: utf-8 -*-
"""20 Deney: no -> (durum, ilk adım, zorlanırsan).

Numara = alan harfi + tip sırası (1 U, 2 K, 3 S, 4 T). Çoğu deney hazır bir cümle içerir.
"""
TIP_NO = {"U": "1", "K": "2", "S": "3", "T": "4"}

BASLATICILAR = {
    # İş ve otorite
    "I1": ("Bir iş isteği geldi ve ağzından hemen \"tamam\" çıkmak üzere.",
           "Şu cümleyi hazır tut: \"Bakıp sana dönerim.\" Bugün bir istekte kullan. Dönmeden önce kendine sor: yapmak istediğim için mi evet diyeceğim, yoksa hayırın bedelinden korktuğum için mi?",
           "Hayır diyemiyorsan önceliği sor: \"Bunu alırsam şu gecikir; hangisi önce?\" Seçimi ona bırakmak, her şeyi sessizce üstlenmekten daha dürüsttür."),
    "I2": ("Takdir görmek için gereğinden fazla çalışıyorsun.",
           "Bugün işi mesai bitiminde bırak, bitmemiş olsa da. Akşam kendine sor: \"Kimse fark etmese, bugün yaptığım yeterli miydi?\"",
           "Bırakmak suçluluk getiriyorsa bunu yaz. Bu suçluluk yanlış bir şey yaptığının değil, değerini işe bağladığının işaretidir."),
    "I3": ("Toplantılarda fikrin var ama sesin çıkmıyor.",
           "Bir sonraki toplantıya tek cümle hazırla ve ilk yarım saatte söyle: \"Bir şey eklemek istiyorum...\" Uzun açıklama yok.",
           "Konuşmak çok zorsa toplantıdan sonra yazılı gönder. Önemli olan fikrin nerede söylendiği değil, söylenmiş olması."),
    "I4": ("Yöneticinin ses tonunu, mesajının gecikmesini sürekli okuyorsun.",
           "Aklına takılan tek bir şeyi doğrudan sor: \"Gönderdiğim işe bakma fırsatın oldu mu?\" Cevap gelene kadar senaryo yazma.",
           "Cevap gecikirse kendine bir saat ver ve o saate kadar mesaj kutusunu açma. Radar, bilgi gelmeyince boşluğu korkuyla doldurur."),
    # Aile
    "A1": ("Ailen bir şey bekliyor ve sen kendi planından vazgeçmek üzeresin.",
           "Yarım evet dene. Hazır mesaj: \"Geleceğim ama saat beşte çıkmam gerekiyor.\" Gönder ve saatinde kalk.",
           "Biri kırılırsa ikna etmeye çalışma; \"Biliyorum, üzüldün\" de ve kararında kal. Kırılmak, sevginin bittiği anlamına gelmez."),
    "A2": ("Ailede \"başarılı olan\" rolü seni yoruyor.",
           "Bu hafta aileden birine bir başarını değil, bir zorluğunu anlat. Hazır cümle: \"Bu aralar biraz yoruldum, bunu da bilmeni istedim.\"",
           "Tepki beklediğin gibi olmazsa hemen rolüne geri koşma. Bir kez farklı görünmek, eski rolü çatlatmaya yeter."),
    "A3": ("Ailende isteğini söylemiyorsun; zaten sorulmuyor.",
           "Küçük bir tercihle başla: \"Bu sefer yemeği ben seçebilir miyim?\" ya da \"Pazar yerine cumartesi gelsem?\"",
           "Söylemek boğazında düğümleniyorsa yazarak söyle. Ses ilk seferde değil, tekrarda güçlenir."),
    "A4": ("Ailenden birinin sözü ya da bakışı günlerdir aklında.",
           "O sözü bir kâğıda yaz. Altına iki soru: \"Bu onun hakkında ne söylüyor?\" ve \"Benim hakkımda gerçekten ne söylüyor?\" Dürüstçe cevapla.",
           "Hâlâ dönüyorsa sor: \"Geçen gün şöyle dedin, aklıma takıldı; ne demek istedin?\" Sormak, tahmin etmekten daha az yorar."),
    # Partner ve yakın ilişki
    "P1": ("İlişkinde ortam bozulmasın diye her şeye evet diyorsun.",
           "Bugün küçük bir şeye hayır de: film, yemek, saat. Hazır cümle: \"Bu akşam ben başka bir şey istiyorum.\"",
           "Hayal kırıklığı seni sıkıştırırsa nefes al ve kal. Sağlıklı bir ilişki küçük bir hayırı taşıyabilir."),
    "P2": ("Sevilmeye değer olduğunu göstermek için fazlasını yapıyorsun.",
           "Bu akşam fazladan hiçbir şey yapma: hediye, sürpriz, ekstra ilgi yok. Sadece yanında otur ve neler hissettiğine bak.",
           "Boşluk huzursuz ediyorsa bunu söyle: \"Bir şey yapmadan durunca huzursuz oluyorum.\" Kanıtlamadan sevilmek, söylenince başlar."),
    "P3": ("Kırgınlığını yutuyorsun, ortam bozulmasın diye.",
           "Bugün tek cümle: \"Dün akşam biraz kırıldım, konuşabilir miyiz?\" Saati sen öner.",
           "Konuşmada geri çekilmek istersen bir cümle daha söyle: \"Bu benim için önemliydi.\" Görünür olmak tek seferde değil, cümle cümle olur."),
    "P4": ("Partnerin sessizleşince yanlış bir şey yaptığını düşünüyorsun.",
           "Tahmin yerine bir kez sor: \"Bir şey mi var, yoksa sadece yorgun musun?\" Cevabı olduğu gibi kabul et.",
           "\"Yok bir şey\" dediğinde iç ses devam ederse kendine şunu söyle: \"Onun hâli her zaman benimle ilgili değil.\" Sonra kendi işine dön."),
    # Arkadaşlık ve çevre
    "C1": ("Bir arkadaşın bir şey istiyor, senin de işin var.",
           "Bahanesiz hayır dene: \"Bu sefer olmuyor ama şu kadarını yapabilirim.\" Uzun açıklama yok.",
           "Açıklama yapma isteği gelirse tut. Uzun gerekçe, hayırı özür gibi gösterir."),
    "C2": ("Arkadaşlıklarında hep yardım eden, hep organize eden sensin.",
           "Bu hafta bir buluşmayı başkasının planlamasına bırak: \"Bu sefer siz seçin, ben gelirim.\"",
           "Plan aksarsa toparlamaya koşma. Sevilmek için hep işe yarar olman gerekmiyor."),
    "C3": ("Grupta sesini çıkarmıyor, kenarda kalıyorsun.",
           "Bir sonraki buluşmada tek bir tercih söyle: \"Ben şurayı tercih ederim.\"",
           "Kimse duymazsa bir kez daha söyle. İlk cümle çoğu zaman duyulmaz, ikincisi duyulur."),
    "C4": ("Buluşmalardan sonra her cümleyi kafanda tekrar oynatıyorsun.",
           "Eve dönünce iyi geçen tek bir anı yaz. Sonra defteri kapat; tekrar oynatma saati bitti.",
           "İçin rahat etmiyorsa ertesi gün yaz: \"Dün çok keyif aldım, sen de iyi miydin?\" Cevap çoğu zaman radarın tahmininden sıcaktır."),
    # Görünürlük
    "G1": ("Ortama uymak için fikrini değiştiriyorsun.",
           "Bu hafta küçük bir konuda farklı düşündüğünü söyle: \"Ben biraz farklı düşünüyorum.\" Tartışmaya girmek zorunda değilsin.",
           "Tepki gelirse savunmaya geçme. \"Olabilir, ben böyle görüyorum\" yeter."),
    "G2": ("Görünür olmak için daha iyi, daha çarpıcı olmaya çalışıyorsun.",
           "Bu hafta bir şeyi \"yeterince iyi\" hâliyle paylaş: düzeltmeden, filtre eklemeden, ikinci kez yazmadan.",
           "Az ilgi görürse bunu bir veri olarak not et, hüküm olarak değil. Beğeni senin değerini değil, o günkü akışı ölçer."),
    "G3": ("Paylaşmıyor, fikir söylemiyor, görünmemeye çalışıyorsun.",
           "Kimseye sormadan hoşuna giden bir şeyi göster: bir fotoğraf, bir cümle, bir kıyafet. Küçük olsun; tek bir kişiye de olabilir.",
           "Gösterdikten sonra silmek istersen 24 saat bekle. Görünür olmanın ilk dakikaları en zor olanlarıdır."),
    "G4": ("Beğenileri, yorumları, tepkileri sürekli kontrol ediyorsun.",
           "Bir sonraki paylaşımdan sonra uygulamayı kapat ve 24 saat bildirimlere bakma. Telefonu başka odada şarja tak.",
           "Dayanamazsan tek bir kontrol saati belirle: akşam dokuzda, bir kez. Radarın da bir mesai saati olabilir."),
}


def baslatici(no):
    """(durum, ilk adım, zorlanırsan) döndürür; yoksa None."""
    return BASLATICILAR.get(str(no).upper())


def no_bul(alan, tip):
    return alan + TIP_NO.get(tip or "U", "1")
