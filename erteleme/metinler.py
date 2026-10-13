# -*- coding: utf-8 -*-
"""Erteleme Haritası rapor metinleri."""

NE_NE_DEGIL = [
    "Bu rapor tembellik ölçmüyor. Ertelemenin neredeyse her zaman bir sebebi vardır: bir korku, bir yorgunluk, bir itiraz ya da kusursuz olma isteği. Burada aranan şey senin motorun; hangi korunma refleksi devreye girince işin ertesi güne kayıyor.",
    "Fotoğraf bir aylık. Yoğun bir ay geçirdiysen alanların düşük, sakin bir ay geçirdiysen yüksek çıkmış olabilir. Sayıları kimlik gibi değil, hava durumu gibi oku: bugün böyle, iki hafta sonra başka olabilir.",
    "Raporu iki kerede oku. İlkinde sadece bak; kendini savunma, \"ama o ay şöyleydi\" deme. İkincisinde en çok rahatsız eden cümlenin altını çiz. O cümle, bu raporun sana asıl söylemek istediği şey.",
]

TIP = {
    "M": {
        "ad": "Mükemmeliyetçi",
        "karsi": "Hazır olmak, başlamak değildir.",
        "mekanizma": "Senin motorun kusursuzluk. Bir işe başlamak, o işin iyi olacağına dair bir söz vermek gibi geliyor; söz tutulamayacaksa hiç başlamamak daha güvenli. Bu yüzden hazırlık uzuyor: önce kaynaklar, önce sistem, önce doğru an. Hazırlık bitmiyor çünkü hazırlık, başlamaktan daha az riskli.",
        "his": "İçeriden şöyle hissediliyor: \"Daha hazır değilim.\" Başladığında da durmak zor; bir paragrafı on kere yazıyor, bir rafı üç kere diziyorsun. Bitirdiğinde rahatlama yerine \"daha iyi olabilirdi\" sesi geliyor.",
        "koken": "Bu motor genellikle sevginin ya da onayın başarıya bağlı olduğu yerde öğrenilir: iyi yaparsan görülürsün, eksik yaparsan eleştirilirsin. Çocuk, eksik görünmektense hiç görünmemeyi seçer. Şimdi kimse puan vermiyor, ama içerideki yargıç hâlâ masada.",
        "erdem": "Bu motorun erdemi titizlik. Senin yaptığın iş genellikle iyi olur; sorun kalite değil, kaliteye ulaşmak için ödenen gecikme. Aynı titizliği \"ilk taslak\" denen bir ara durağa izin vermek için kullanabilirsin.",
        "on_dakika": "Senin için ilk 10 dakika kuralı: bilerek kötü yap. İlk taslak, ilk raf, ilk cümle kötü olmak zorunda; çünkü iyi olma şartı başlamayı kilitliyor. On dakika sonra dilediğin kadar düzelt.",
    },
    "G": {
        "ad": "Kaygılı",
        "karsi": "Bakmamak, güvende olmak değildir.",
        "mekanizma": "Senin motorun kaçınma. Bir iş kötü bir duygu çağırıyor: kötü haber, utanç, belirsizlik. O duyguya yaklaşmamak için işin kendisinden uzaklaşıyorsun. Kısa vadede rahatlama geliyor; uzun vadede iş büyüyor, büyüyen iş daha çok kaygı çağırıyor.",
        "his": "İçeriden şöyle hissediliyor: iş aklına gelince midende bir sıkışma, sonra hızla başka bir şeye geçiş. Zarf kapalı kaldıkça, mesaj açılmadıkça bir rahatlama var ama arka planda sürekli bir uğultu da var.",
        "koken": "Bu motor genellikle kötü haberin sert karşılandığı ya da hataların büyütüldüğü yerde öğrenilir. Çocuk, bilmemenin bilmekten daha güvenli olduğunu öğrenir. Şimdi bilmek çoğu zaman sana güç verir, ama beden eski alarmı hatırlıyor.",
        "erdem": "Bu motorun erdemi duyarlılık. Riskleri görüyor, sonuçları düşünüyorsun; birçok insanın kaçırdığı şeyleri fark ediyorsun. Bu duyarlılık, korkuyu küçük parçalara bölmek için de kullanılabilir.",
        "on_dakika": "Senin için ilk 10 dakika kuralı: sadece bak. Açmak, okumak, fotoğrafını çekmek; karar vermek ya da çözmek yok. Korkulan şey kapalıyken büyür, açılınca çoğu zaman küçülür.",
    },
    "S": {
        "ad": "Son dakikacı",
        "karsi": "Adrenalin, motivasyon değildir.",
        "mekanizma": "Senin motorun baskı. Zaman bolken iş seni çağırmıyor; son tarih yaklaşınca beden uyanıyor, odak geliyor, iş bir gecede bitiyor. Bu yöntem çalıştığı için bırakmak zor; ama bedelini uykuyla, stresle ve \"keşke daha önce\" pişmanlığıyla ödüyorsun.",
        "his": "İçeriden şöyle hissediliyor: \"Yaparım ya, daha vakit var.\" Son gece ise bir tür heyecan, hatta keyif var. Sonrasında yorgunluk ve bir dahakine erken başlama sözü; söz yine tutulmuyor.",
        "koken": "Bu motor genellikle yapının az, uyarının çok olduğu yerde öğrenilir; ya da sıradan günlerin sıkıcı, krizlerin canlı olduğu bir ortamda. Beden, ancak acil olanın dikkat aldığını öğrenir.",
        "erdem": "Bu motorun erdemi hız. Baskı altında toparlanıyor, kısa sürede çok iş çıkarıyorsun. Sorun hız değil, hızın tek tetikleyicisinin kriz olması. Baskıyı gece değil gündüz, kendin kurabilirsin.",
        "on_dakika": "Senin için ilk 10 dakika kuralı: sahte son tarih. Bugün belli bir saatte yarım hâlini birine göstereceksin. Baskıya ihtiyacın varsa onu krize bırakma, kendin üret.",
    },
    "D": {
        "ad": "Direnen",
        "karsi": "Yapmamak, seçmek değildir.",
        "mekanizma": "Senin motorun itiraz. Bir iş dayatılmış, haksız ya da başkasının kuralı gibi gelince içinde sessiz bir \"hayır\" yükseliyor. Bu hayırı söylemek yerine işi yapmayarak gösteriyorsun. Ertelemek, kontrolün sende olduğunu hissettiren tek alan oluyor.",
        "his": "İçeriden şöyle hissediliyor: birisi hatırlatınca daha da yapasın gelmiyor. \"Neden ben\", \"bu saçma\", \"kimse karışmasın\" cümleleri tanıdık. Yapmadığında bir zafer duygusu var ama bedeli çoğu zaman yine sana dönüyor.",
        "koken": "Bu motor genellikle kontrolün dışarıda olduğu bir ortamda öğrenilir: sesini duyuramayan çocuk, tek özgürlüğünü yavaşlıkta ve yapmamakta bulur. Şimdi sesin var, ama eski strateji hâlâ çalışıyor.",
        "erdem": "Bu motorun erdemi özerklik. Kendi kararını vermek, dayatmaya teslim olmamak değerli bir şey. Sorun itirazın kendisi değil, söylenmeyip ertelemeyle gösterilmesi. Aynı itirazı bir cümleyle söyleyebilirsin.",
        "on_dakika": "Senin için ilk 10 dakika kuralı: kendi yolunu seç. İşte değiştirebileceğin tek bir şeyi değiştir (sıra, saat, araç) ve başlangıcı kendi kuralınla yap. Söylenmesi gereken bir hayır varsa önce onu söyle.",
    },
}

CIFT_TIP = ("İki motorun birbirine çok yakın: {t1} ve {t2}. Bu, duruma göre farklı bir reflekse geçtiğin anlamına gelir; "
            "raporda ikisi de var. Çoğu zaman biri işin kendisinde, diğeri işin sende uyandırdığı duyguda devreye girer.")

SERBEST = ("Dört motorun da düşük çıktı: ertelemen tek bir kalıba yığılmamış. Bu iyi haber; zorlandığında hangi refleksin "
           "devreye girdiğini seçebiliyorsun. Raporun geri kalanı daha çok \"nerede\" sorusuna cevap verecek, \"neden\" sorusuna değil.")

LISTE_METIN = {
    True: "Liste yükün ağır: en zayıf iki alanında işler birikmiş. Bu ay her şeyi yetiştirmeye değil, bir alanda küçük bir kazanıma odaklan.",
    False: "Liste yükün taşınabilir düzeyde: birikme var ama boğucu değil. Küçük adımlar burada hızla fark yaratır.",
}

ALAN_BANT = {
    "I": {
        "Akıyor": "İş ve okulda işler akıyor: başlamak seni korkutmuyor, son tarihleri genellikle rahat karşılıyorsun. Bu alan, diğer alanlara taşıyabileceğin bir kas.",
        "Takılıyor": "İş ve okulda bazı işler akıyor, bazıları takılıyor. Hangi işlerin takıldığına bak: genellikle belirsiz, büyük ya da sana dayatılmış olanlar.",
        "Tıkanıyor": "İş ve okulda başlamak zorlaşmış: işler son ana kalıyor ya da açılmadan bekliyor. Bu ay \"bitirmek\" değil \"başlatmak\" hedef olsun.",
        "Donmuş": "İş ve okul bu ay neredeyse durmuş. Bu bir karakter sorunu değil, bir yük ya da bir korku işareti. En küçük işten, tek bir maille başla.",
    },
    "E": {
        "Akıyor": "Ev ve düzen akıyor: küçük işler birikmeden hallediliyor. Bu ritim, diğer alanlarda da kullanılabilir.",
        "Takılıyor": "Evde günlük işler dönüyor ama büyük işler (dolap, tamir, arşiv) bekliyor. Büyük işi on dakikalık parçalara böl.",
        "Tıkanıyor": "Evde işler birikmiş; birikim de yeni ertelemeye sebep oluyor. Bütün evi değil, tek bir yüzeyi hedefle.",
        "Donmuş": "Ev bu ay ağır gelmiş. Dağınıklık çoğu zaman yorgunluğun ya da içerideki yükün dışarıdaki görüntüsüdür. Kendine yargı değil, on dakika ver.",
    },
    "B": {
        "Akıyor": "Bedenine iyi bakıyorsun: randevular, uyku, hareket ertelenmiyor. Bu, kendine verdiğin değerin somut hâli.",
        "Takılıyor": "Beden için yapılması gerekenler bazen sıranın sonuna kalıyor. Özellikle \"düzgün program\" beklenen işlere bak.",
        "Tıkanıyor": "Beden ertelenen alanların başında. Başkalarının işi önde, kendi sağlığın bekliyor. Bu ay tek bir randevu ya da tek bir yürüyüş yeter.",
        "Donmuş": "Beden bu ay neredeyse hiç sıraya girmemiş. Ertelenen kontroller varsa en önemlisi bu raporun en önemli satırı olabilir.",
    },
    "P": {
        "Akıyor": "Para ve evrak düzenli: faturalar, başvurular, hesaplar kontrol altında. Bu alan güçlüyken diğer alanlardaki kaygı da azalır.",
        "Takılıyor": "Para ve evrakta bazı işler son güne kalıyor. Otomatik ödeme ve takvim hatırlatması bu alanın en hızlı ilacı.",
        "Tıkanıyor": "Para ve evrak kaygı üretiyor; bakmamak kısa vadede rahatlatıyor. Bu ay sadece bakmak bile büyük adım.",
        "Donmuş": "Para ve evrak bu ay neredeyse hiç açılmamış. Biriken evrak cezaya ya da kayba dönüşebilir; en acil olanı bul ve bugün belge listesini çıkar.",
    },
    "K": {
        "Akıyor": "İletişimde gecikme yok: mesajlar cevaplanıyor, zor konuşmalar açılıyor. İlişkilerin bu yüzden hafif.",
        "Takılıyor": "Bazı mesajlar ve konuşmalar bekliyor. Genellikle bekleyenler, \"doğru cevap\" ya da \"doğru an\" isteyenler.",
        "Tıkanıyor": "İletişim borcu birikmiş: cevaplanmayan mesajlar, açılmayan konuşmalar. Gecikme uzadıkça utanç büyüyor, utanç büyüdükçe gecikme uzuyor.",
        "Donmuş": "İletişim bu ay neredeyse durmuş. Bu bazen bir geri çekilme işaretidir. Tek bir kişiye, iki cümleyle başla.",
    },
}

ALAN_TIP = {
    "I": {"M": "İşte motorun kusursuzluk: hazırlık bitmiyor, ilk taslak hiç gelmiyor.",
          "G": "İşte motorun kaçınma: dosyayı açmamak, ne göreceğinden çekinmek.",
          "S": "İşte motorun baskı: iş ancak son gece başlıyor.",
          "D": "İşte motorun itiraz: dayatılan iş, sessiz bir hayırla bekletiliyor."},
    "E": {"M": "Evde motorun kusursuzluk: \"hepsini bir günde, düzgünce\" beklentisi küçük adımı engelliyor.",
          "G": "Evde motorun kaçınma: bazı köşeler, açtığı duygu yüzünden kapalı kalıyor.",
          "S": "Evde motorun baskı: ev ancak misafir gelince toplanıyor.",
          "D": "Evde motorun itiraz: \"neden hep ben\" duygusu işi askıda bırakıyor."},
    "B": {"M": "Bedende motorun kusursuzluk: doğru program, doğru doktor, doğru zaman bekleniyor.",
          "G": "Bedende motorun kaçınma: sonuçtan korkmak randevuyu erteliyor.",
          "S": "Bedende motorun baskı: ancak bir şey acıyınca harekete geçiliyor.",
          "D": "Bedende motorun itiraz: başkası söyledikçe yapmamak."},
    "P": {"M": "Parada motorun kusursuzluk: kusursuz sistem kurulmadan bütçeye başlanmıyor.",
          "G": "Parada motorun kaçınma: rakamlara bakmamak.",
          "S": "Parada motorun baskı: ödemeler ancak son gün yapılıyor.",
          "D": "Parada motorun itiraz: bürokrasiye öfke, işi askıda bırakıyor."},
    "K": {"M": "İletişimde motorun kusursuzluk: uzun ve güzel cevap yazılamayınca hiç yazılmıyor.",
          "G": "İletişimde motorun kaçınma: geç kalmanın utancı, daha da geç kalmaya sebep oluyor.",
          "S": "İletişimde motorun baskı: konuşma ancak taşınca, patlayınca açılıyor.",
          "D": "İletişimde motorun itiraz: \"önce o adım atsın\" diye beklemek."},
}

ALAN_ADIM = {
    "I": {"M": "Bu hafta bir iş için bilerek kötü bir ilk taslak yaz; 10 dakika, silmek yasak.",
          "G": "Bu hafta açmaktan çekindiğin dosyayı aç ve sadece ilk paragrafı oku.",
          "S": "Bu hafta bir işe sahte teslim saati koy ve yarım hâlini birine göster.",
          "D": "Bu hafta dayatılan bir iş için \"bu sığmaz, hangisi öncelik?\" diye sor."},
    "E": {"M": "Bu hafta tek raf, tek çekmece; 10 dakika sonra yarıda da olsa bırak.",
          "G": "Bu hafta kapalı tuttuğun köşenin sadece fotoğrafını çek.",
          "S": "Bu hafta iki gün aynı saatte 10 dakikalık \"misafir geliyor\" turu yap.",
          "D": "Bu hafta bir ev işinin paylaşımını tek cümleyle söyle."},
    "B": {"M": "Bu hafta programsız 10 dakika yürü.",
          "G": "Bu hafta ertelediğin randevuyu sadece al; gitmek ayrı adım.",
          "S": "Bu hafta telefonu yatak odası dışında şarja tak.",
          "D": "Bu hafta bedenin için kendi seçtiğin tek küçük şeyi yap, kimseye söyleme."},
    "P": {"M": "Bu hafta 15 dakikalık kaba bir bütçe tablosu çıkar.",
          "G": "Bu hafta hesabına bak ve bakiyeyi bir kâğıda yaz; yorum yok.",
          "S": "Bu hafta bir faturayı otomatik ödemeye bağla.",
          "D": "Bu hafta askıdaki evrakın sadece belge listesini çıkar."},
    "K": {"M": "Bu hafta uzun cevap beklettiğin kişiye iki cümle gönder.",
          "G": "Bu hafta geç kaldığın bir mesajı utancını söyleyerek gönder.",
          "S": "Bu hafta açman gereken konuşma için \"bu akşam on dakika\" mesajını gönder.",
          "D": "Bu hafta \"önce o atsın\" dediğin kişiye ilk adımı sen at."},
}

ORUNTU = {
    "mukemmel_kacis": "Mükemmeliyetçi ve kaygılı motorların birlikte çalışıyor: \"kusursuz olmalı, olmazsa hiç bakmayayım.\" Biri çıtayı yükseltiyor, diğeri yüksek çıtanın korkusundan kaçıyor. İkisini birden gevşetmenin yolu, çıtayı bilerek \"yeterince iyi\"ye indirmek.",
    "son_dakika": "Son dakika döngüsü: işler bitiyor ama hep son gece, hep adrenalinle. Bu yöntem çalıştığı için bırakmak zor; bedeli uyku, yorgunluk ve hiç bitmeyen \"bir dahakine erken\" sözü.",
    "secici": "Ertelemen genel değil, seçici: bir alanda işler akarken diğerinde duruyor. Bu, sorunun senin karakterin değil, o alanın sende uyandırdığı bir şey olduğunu gösteriyor. En zayıf alanına bu gözle bak.",
    "beden_sonda": "Beden sıranın en sonunda: başkalarının işi, iş yerinin işi önde; kendi sağlığın bekliyor. Bu ay listenin başına tek bir beden işi koy.",
    "para_kacinma": "Para kaçınması: rakamlar kaygı üretiyor, bakmamak geçici bir rahatlama veriyor. Ama kapalı zarf açılmadıkça büyür. Bu ay sadece bakmak bile büyük bir adım.",
    "iletisim_borcu": "İletişim borcu birikmiş: cevaplanmayan mesajlar faiz gibi büyüyor. Gecikmenin utancı yeni gecikme doğuruyor. Döngüyü kırmanın yolu uzun bir özür değil, iki cümlelik bir mesaj.",
    "otorite_direnc": "Otoriteye direnç: ertelemen bir \"hayır\" taşıyor ve en çok iş alanında görünüyor. Bu hayır söylenmediği için işi bekleterek gösteriliyor. Sınır Haritası bu itirazın nereden geldiğini daha net gösterebilir.",
    "yaygin": "Üç ya da daha çok alan aynı anda takılmış. Bu ay ağır geçmiş olabilir. Hepsini birden düzeltmeye çalışma; en güçlü alandan başla, kas önce kolay yerde çalışır.",
}

PLAN_GIRIS = ("Üç hafta, her hafta tek alan. En güçlü alanından başlıyor, en zayıf alanına son hafta geliyorsun; "
              "ilk haftanın kolay kazanımı, üçüncü haftanın zor işine güç verir.")
PLAN_KAPANIS = "Üç hafta sonra envanteri yeniden doldur; fark genellikle ilk ayda en zayıf alanda görünür."

DURUSTCE = [
    "Bu rapor bir koçluk aracı; psikolojik değerlendirme ya da tanı aracı değil. Erteleme bir karakter kusuru değil, öğrenilmiş bir korunma refleksidir ve yeniden öğrenilebilir.",
    "Dikkat ve odaklanma zorluğu çocukluktan beri her alanda sürüyorsa, bu raporun anlatabileceğinden fazlası olabilir. Bunu bir uzmanla konuşmak faydalı olabilir.",
    "Bazı ertelemeler aslında haklı bir hayırdır: yapılmaması gereken bir iş, sana ait olmayan bir yük. Her ertelenen işi yapmak zorunda değilsin; bazılarını bırakmak da bir karardır.",
]
DURUSTCE_GENIS = ("Cevaplarında, ertelemenin ötesine işaret eden bir şey var: eskiden keyif aldığın şeylerin de ağır gelmesi "
                  "ya da ertelemenin hayatını tehlikeye sokacak kadar artması. Bu bir erteleme meselesi olmayabilir, bir enerji "
                  "meselesi olabilir. Böyle dönemlerde bir uzmanla konuşmak iyi gelebilir; bunu söylemek bu raporun görevi.")

SONRAKI = [
    ("Raporu birlikte okuyalım", "30 dakikalık görüşme. Raporda en çok rahatsız eden cümleyi konuşur, ilk hafta için tek bir adım seçeriz. WhatsApp'tan yaz, uygun saati bulalım."),
    ("Bireysel Koçluk", "Erteleme çoğu zaman başka bir şeyin görünen yüzüdür: kusursuzluk, korku ya da söylenmemiş bir hayır. Haftalık koçlukta bu motoru birlikte çalışırız. thetakapisi.com.tr/danismanlik"),
    ("Diğer envanterler", "Direnen motorun güçlüyse Sınır Haritası, iletişim borcun yüksekse İlişki Mesafesi Haritası iyi bir sonraki adım. Üçlü Paket ile üçü birlikte. thetakapisi.com.tr/envanterler"),
]

# --- kişinin kendi cevapları ---
S_TIP_YORUM = {
    "M": ["Burada motor kusursuzluk: hazırlık başlamanın yerini aldı.",
          "Burada iyi olma şartı işi kilitledi; ilk taslak gelmedi.",
          "Burada sistem kurmak, işin kendisinden daha güvenli geldi."],
    "G": ["Burada motor kaçınma: bakmamak geçici bir rahatlama verdi.",
          "Burada işin uyandırdığı duygudan uzaklaştın; iş yerinde kaldı.",
          "Burada kapalı tutmak güvenli geldi; ama kapalı olan büyür."],
    "S": ["Burada motor baskı: iş ancak son ana kalınca kıpırdadı.",
          "Burada zaman bolken iş seni çağırmadı; adrenalin bekledin.",
          "Burada baskıyı krize bıraktın; kendin kurabilirdin."],
    "D": ["Burada motor itiraz: söylenmeyen bir hayır, yapmamakla gösterildi.",
          "Burada dayatılma hissi işi bekletti; kontrol sende kaldı ama bedel de.",
          "Burada inat, kendi ihtiyacının önüne geçti."],
    "TUTAR": ["Burada akıyor: küçük bir adımla başladın. Bu cevabı hatırla; diğer alanlara taşınabilir.",
              "Burada işi böldün ve ilk parçayı yaptın; tam olması gereken bu.",
              "Burada ne istediğini söyledin ya da hemen başladın; bu kas sende var."],
}
S_TUTAN_GIRIS = "Aynı anın akan hâli:"

Z_GIRIS = ("Sekiz ikilemde iki zor seçenek arasında seçim yaptın; doğru cevap yoktu. "
           "Ertelerken hangi motorun devreye girdiği burada görünüyor: puan değil, refleks.")
Z_YORUM = {
    "M": "İkilemlerde en çok kusursuzluk motorunu seçtin: başlamanın önündeki engel, yetersiz görünme korkusu.",
    "G": "İkilemlerde en çok kaçınma motorunu seçtin: başlamanın önündeki engel, işin uyandırdığı kaygı.",
    "S": "İkilemlerde en çok baskı motorunu seçtin: iş ancak acil olunca anlam kazanıyor.",
    "D": "İkilemlerde en çok itiraz motorunu seçtin: başlamanın önündeki engel, dayatılma hissi.",
}
Z_DENGELI = "İkilemlerde tek bir motora yığılmadın; refleksin duruma göre değişiyor."
Z_OZEL = {
    ("z3", "a"): "Seni en çok durduran şey yetersiz olma korkusu. Bu korku başlamayı zorlaştırır; ilacı, yeterince iyi olanı bilerek kabul etmek.",
    ("z3", "b"): "Seni en çok durduran şey kötü haber alma korkusu. Bu korku bakmayı zorlaştırır; ilacı, sadece bakmak ve henüz bir şey yapmamak.",
    ("z5", "a"): "İnsanlar seni \"her şeyi son dakikaya bırakır\" diye biliyor. Bu bir tanınırlık, ama bedelini yalnız sen ödüyorsun.",
    ("z5", "b"): "İnsanlar seni \"inatçı, zorlanmayı sevmez\" diye biliyor. Bu inat bir güç; yeter ki kendi aleyhine çalışmasın.",
    ("z7", "a"): "Birisi hatırlatınca daha da yapasın gelmiyor: itiraz motorun hatırlatmayı kontrol girişimi gibi okuyor.",
    ("z7", "b"): "Birisi hatırlatınca utanıyorsun ama yine başlayamıyorsun: utanç, başlamayı kolaylaştırmıyor, zorlaştırıyor.",
}

CUMLE_ALAN = {
    "I": "Ertelediğin şey İş ve okul alanına düşüyor.",
    "E": "Ertelediğin şey Ev ve düzen alanına düşüyor.",
    "B": "Ertelediğin şey Sağlık ve beden alanına düşüyor.",
    "P": "Ertelediğin şey Para ve evrak alanına düşüyor.",
    "K": "Ertelediğin şey İlişkiler ve iletişim alanına düşüyor.",
}
CUMLE_ALAN_UYUM = {
    True: "Bu alan haritanda zaten düşük; cümlen haritanı doğruluyor.",
    False: "İlginç olan şu: bu alan haritanda görece iyi. Demek ki genel bir tıkanma değil, bu işe özel bir şey var.",
}
CUMLE_TIP = {
    "M": "Cümlende \"{ipucu}\" geçiyor: ertelemenin içinde kusursuzluk isteği var.",
    "G": "Cümlende \"{ipucu}\" geçiyor: ertelemenin içinde bir kaygı ya da korku var.",
    "S": "Cümlende \"{ipucu}\" geçiyor: iş baskı bekliyor.",
    "D": "Cümlende \"{ipucu}\" geçiyor: ertelemenin içinde bir itiraz var.",
}
CUMLE_TIP_UYUM = {
    True: "Bu, haritandaki baskın motorunla aynı; cümlen motorunu tarif ediyor.",
    False: "Bu, haritandaki baskın motorundan farklı; bu işte başka bir refleks devreye giriyor. İkisini de tanı.",
}
CUMLE_BELIRSIZ = ("Cümlende neyi neden ertelediğin tam okunmuyor; bu da bir bilgi. "
                  "Bazen en çok ertelenen şey, adı bile konulmamış olandır. Önce ona bir ad ver.")
CUMLE_KARSI_GIRIS = "Bu iş için başlatıcı ({no}):"
CUMLE_YARIN = "Yarın sabah ilk 10 dakika: {eylem}"
CUMLE_KAPANIS = ("Bu işi bugün bitirmek zorunda değilsin. Ama yarın sabah ilk 10 dakikayı ona ver. "
                 "Başlamak, bitirmenin en büyük parçasıdır.")

BASLATICI_UST = "BAŞLATICI · {no}"
BASLATICI_ILK = "İlk 10 dakika:"
BASLATICI_GERI = "Takılırsan:"
