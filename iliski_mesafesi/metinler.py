# -*- coding: utf-8 -*-
"""İlişki Mesafesi Haritası rapor metinleri."""

NE_NE_DEGIL = [
    "Bu rapor partnerin hakkında değil, senin adımın hakkında. İlişkide iki kişi dans eder; burada yalnız senin ayağının nereye bastığı var. Partnerine teşhis koymaz, etiket yapıştırmaz; onu tanımıyoruz, seni de sadece bir aylık fotoğraftan tanıyoruz.",
    "Fotoğraf bir aylık. Zor bir ay geçirdiysen puanlar düşük, sakin bir ay geçirdiysen yüksek çıkmış olabilir. Sayıları kimlik gibi değil, hava durumu gibi oku: bugün böyle, yarın başka olabilir ve olacak.",
    "Raporu bir kerede değil, iki kerede oku. İlkinde sadece bak; itiraz etme, savunma, \"ama o da…\" deme. İkincisinde en çok rahatsız eden cümlenin altını çiz. O cümle, raporun sana söylemek istediği şeydir.",
]

TIP = {
    "T": {
        "ad": "Takip eden",
        "karsi": "Yaklaşmak, ısrar etmek değildir.",
        "mekanizma": "Gerginlik ya da mesafe hissettiğinde refleksin yaklaşmak: sormak, yazmak, konuşmak istemek, bazen peşinden gitmek. Yakınlık senin için güvenlik; mesafe ise alarm. Alarm çalınca sesi kısmak yerine kapıya daha sert vuruyorsun.",
        "his": "Partnerin kapandığında içinde bir boşluk açılıyor; o boşluğu doldurmak için konuşmak istiyorsun, o uzaklaştıkça sen hızlanıyorsun. Sonra kendine kızıyorsun: \"Neden bu kadar ısrar ettim.\" Ama ertesi sefer yine aynı.",
        "koken": "Bu adım genellikle sevginin kesintili olduğu yerde öğrenilir: bazen var, bazen yok. Çocuk, yokluğu önlemek için varlığı garanti altına almayı öğrenir; bunun yolu da peşinden gitmektir. Şimdi çoğu zaman öyle değil, ama beden eski alarmı hatırlıyor.",
        "erdem": "Bu adımın erdemi var: cesaret. Çoğu insan isteyemez; sen istiyorsun. Mesele istemek değil, istemenin dozu ve zamanlaması. Aynı cümle sakin söylenince yakınlık, üç kere üst üste söylenince baskı.",
        "partner": "Partnerinde tetiklediği şey genellikle çekilme: sen yaklaştıkça o geri gidiyor, o geri gittikçe sen yaklaşıyorsun. Bu dansı tek başına durdurabilirsin: ilk adımı değil, ikinci adımı atmayarak.",
    },
    "C": {
        "ad": "Çekilen",
        "karsi": "Susmak, sakinleşmek değildir.",
        "mekanizma": "Gerginlik ya da yakınlık fazlası hissettiğinde refleksin uzaklaşmak: susmak, odadan çıkmak, telefona bakmak, \"sonra konuşuruz\" demek. Mesafe senin için nefes; yakınlık ise bazen boğulma. Alarm çalınca kapıyı kapatıyorsun.",
        "his": "Partnerin yaklaştığında, sorduğunda, konuşmak istediğinde içinde bir daralma oluyor; cevap vermek yerine çekilmek istiyorsun. Çekilince rahatlıyorsun ama kısa sürüyor; çünkü sorun yerinde duruyor ve o daha da yaklaşıyor.",
        "koken": "Bu adım genellikle duyguların fazla ya da tehlikeli olduğu yerde öğrenilir: ağlayınca azar, konuşunca kavga. Çocuk, hissetmemeyi ve odasına kapanmayı öğrenir; sessizlik güvenli olur. Şimdi karşındaki o kişi değil, ama beden eski kapıyı hatırlıyor.",
        "erdem": "Bu adımın erdemi var: sakinlik. Kavgayı büyütmüyorsun, bağırmıyorsun, kapıyı çarpsan bile geri geliyorsun. Mesele uzaklaşmak değil, uzaklaşırken bunu söylememek. \"Yirmi dakika\" diyerek çıkmakla hiçbir şey demeden çıkmak arasında bir ilişki var.",
        "partner": "Partnerinde tetiklediği şey genellikle takip: sen kapandıkça o sorar, o sordukça sen kapanırsın. Bu dansı tek başına durdurabilirsin: kapanmadan önce bir cümle bırakarak.",
    },
    "B": {
        "ad": "Bekleyen",
        "karsi": "Beklemek, istemek değildir.",
        "mekanizma": "İhtiyacın olduğunda refleksin söylemek değil, fark edilmeyi beklemek. İma ediyorsun, soğuyorsun, susuyorsun; \"anlamalı\" diyorsun. Anlamayınca kırılıyorsun ama kırgınlığı da söylemiyorsun. İstek içeride büyüyor, dışarıya sessizlik çıkıyor.",
        "his": "\"Söylemem gerekiyorsa zaten anlamı yok\" cümlesi çok tanıdık. İstediğin şeyi istemek, istediğin şeyi değersizleştiriyormuş gibi geliyor. Sonra partnerin bir şey fark etmeyince içinde bir dosya açılıyor: kanıt birikiyor.",
        "koken": "Bu adım genellikle istemenin bedelli olduğu yerde öğrenilir: istersen ya alay, ya yük olursun. Çocuk, istemeden almayı; alamazsa da ihtiyacı yok saymayı öğrenir. Şimdi karşındaki kişi istediğinde vermeye hazır olabilir, ama sen sormuyorsun.",
        "erdem": "Bu adımın erdemi var: incelik. Karşındakini okuyorsun, küçük şeyleri fark ediyorsun, kendin de öyle okunmayı hak ediyorsun. Mesele okunmayı istemek değil, okunmadığında söyleyebilmek. Fark edilmek bir hak; söylemek o hakkın anahtarı.",
        "partner": "Partnerinde tetiklediği şey genellikle bilmezlik: senin ihtiyacını bilmiyor, bilmeyince karşılamıyor, karşılamayınca sen \"görmüyor\" diyorsun. Bu dansı tek başına durdurabilirsin: bir ihtiyacı ima etmeden söyleyerek.",
    },
    "D": {
        "ad": "Düzenleyen",
        "karsi": "İdare etmek, onarmak değildir.",
        "mekanizma": "Gerginlikte refleksin ilişkiyi tek başına taşımak: planı sen yapıyorsun, kavgayı sen kapatıyorsun, \"tamam haklısın\" diyorsun, ortamı yumuşatıyorsun. Mesele çözülmüyor, kapanıyor. Sen yorgun, o rahat; sen rahatlayınca da o pasif.",
        "his": "Bir kavgada en çok istediğin şey kavganın bitmesi. Haklı olup olmamak ikinci planda; sessizlik gelsin, akşam kurtulsun. Sonra gece yarısı, çözülmemiş konu geri geliyor. İdare ettiğin her şey birikiyor ve sen bu birikimi de tek başına taşıyorsun.",
        "koken": "Bu adım genellikle huzurun kırılgan olduğu bir evde öğrenilir: biri patlamasın diye ortamı yumuşatan çocuk. Düzenleyen çocuk sevilir, güvenilir, \"olgun\" denir. Şimdi karşındaki kişi yetişkin, ama sen hâlâ evi ayakta tutuyorsun.",
        "erdem": "Bu adımın erdemi var: beceri. Gerginliği okuyor, zamanlamayı biliyor, kapıları kapatabiliyorsun. Mesele bu beceri değil, tek yönlü kullanılması. Aynı beceriyle \"bu konu kapanmadı\" da diyebilirsin.",
        "partner": "Partnerinde tetiklediği şey genellikle rahatlama, sonra pasiflik: sen hallettikçe o halletmez. Bu dansı tek başına durdurabilirsin: bir kavgayı kapatmadan bırakarak.",
    },
}

CIFT_ADIM = ("İki adımın birbirine çok yakın: {t1} ve {t2}. Bu, duruma göre adım değiştirdiğin anlamına gelir; "
             "iki adımı da tanı, raporda ikisi de var. Çoğu zaman biri \"yakınlık fazlasında\", diğeri \"yakınlık azlığında\" devreye girer.")

SERBEST = ("Dört adım tipi de düşük çıktı: refleksin tek bir kalıba yığılmamış. Bu, zorlandığında adımı seçebildiğin anlamına gelir; "
           "raporun geri kalanı daha çok \"nerede takılıyorsun\" sorusuna cevap verecek, \"neden\" sorusuna değil.")

BOYUT_BANT = {
    "Y": {
        "Akıyor": "Yakınlığı isteyebiliyorsun: \"gel\", \"sarıl\", \"yanımda otur\" demek sana muhtaçlık gibi gelmiyor. Bu, ilişkide en pahalı becerilerden biri; sende var.",
        "Takılıyor": "Yakınlığı istiyorsun ama istemek bazen takılıyor: ya bekliyorsun ya da ısrar ediyorsun. Arası, yani sakin istemek, henüz alışkanlık değil.",
        "Tıkanıyor": "Yakınlık isteğin var ama çıkış yolu tıkalı: ya söylemiyorsun ya da söylediğinde baskı gibi geliyor. Çoğu zaman beklemek ve patlamak arasında gidip geliyorsun.",
        "Kapalı": "Yakınlığı istemek bu ay neredeyse hiç mümkün olmamış. Bu bir eksiklik değil, bir korunma; istemenin güvenli olmadığı bir yerden geliyor. En yavaş değişen boyut burası olacak ve bu normal.",
    },
    "U": {
        "Akıyor": "Kendi alanını alabiliyorsun: yalnız kalmak suç değil, partnerinin alanı da tehdit değil. Mesafe seni korkutmuyor; bu, yakınlığı mümkün kılan şey.",
        "Takılıyor": "Alan almak bazen takılıyor: ya suçlulukla alıyorsun ya da onun aldığı alanı mesafe diye okuyorsun. Mesafe hâlâ biraz alarm.",
        "Tıkanıyor": "Alan ihtiyacı var ama ya söyleyemiyorsun ya da tek sığınağın oluyor. Mesafe ya terk edilme ya kaçış; ikisi de dinlenmek değil.",
        "Kapalı": "Alan almak bu ay neredeyse hiç mümkün olmamış ya da tam tersi, alan tek yaşadığın yer olmuş. İki uç da aynı kapıyı gösteriyor: mesafe güvenli değil.",
    },
    "S": {
        "Akıyor": "Söyleyebiliyorsun: kırgınlığı, ihtiyacı, rahatsızlığı aynı gün, sakin bir cümleyle. İlişkideki çoğu sorunun ilacı bu; sende hazır.",
        "Takılıyor": "Söylemek bazen takılıyor: bazı konuları açıyorsun, bazılarını ima ediyorsun ya da erteliyorsun. Hangi konuların ima'da kaldığına bak; genellikle en önemlileri.",
        "Tıkanıyor": "Söylemek tıkanmış: ihtiyaç ima oluyor, kırgınlık soğukluk oluyor, konu kavga çıkmasın diye kapalı kalıyor. Partnerin seni bilmiyor, çünkü sen söylemiyorsun.",
        "Kapalı": "Söylemek bu ay neredeyse hiç mümkün olmamış. \"Söylemem gerekiyorsa anlamı yok\" cümlesi burada en çok işliyor. Bu boyut düşükken diğerleri de düşer; ilk çalışılacak yer burası.",
    },
    "O": {
        "Akıyor": "Onarabiliyorsun: kavgadan sonra ilk adımı atmak, özür dilemek, özrü kabul etmek sana yenilgi gibi gelmiyor. Kavga edebilen ve barışabilen çiftler uzun yaşar; sende bu var.",
        "Takılıyor": "Onarım bazen takılıyor: ya geç dönüyorsun ya da erken kapatıyorsun. \"Tamam geçti\" dediğin ama geçmediği anlara bak.",
        "Tıkanıyor": "Onarım tıkanmış: kavga bitiyor ama konu çözülmüyor; ya küslük uzuyor ya da haklı çıkmak barışmaktan önemli geliyor. İlişki bitmiyor ama her kavga iz bırakıyor.",
        "Kapalı": "Onarım bu ay neredeyse hiç olmamış: kavgalar kapanmamış, günlerce küslük ya da her şey olmamış gibi davranmak. Bu en acil boyut; çünkü diğer üçü burada tamir edilir.",
    },
}

# boyut × tip kesişimi (boyut düşükken o boyutta baskın adım)
BOYUT_TIP = {
    "Y": {
        "T": "Yaklaşma boyutunda adımın takip: istiyorsun ama istemenin dozu kaçıyor; cevap gelmeyince sormak baskıya dönüşüyor.",
        "C": "Yaklaşma boyutunda adımın çekilme: yakınlık istediğinde bile geri çekiliyorsun; \"zaten ilgilenmiyor\" cümlesi istemenin yerini alıyor.",
        "B": "Yaklaşma boyutunda adımın bekleme: sarılmak istiyorsun ama o fark etsin diye bekliyorsun; beklerken soğuyorsun.",
        "D": "Yaklaşma boyutunda adımın düzenleme: yakınlık istemek yerine ortamı hazırlıyorsun; sofra, plan, ilgi. İstemek yerine veriyorsun.",
    },
    "U": {
        "T": "Alan boyutunda adımın takip: onun alanı sana mesafe gibi geliyor, kendi alanını da istemiyorsun; alan = uzaklık.",
        "C": "Alan boyutunda adımın çekilme: alanı söyleyerek değil, kaybolarak alıyorsun; o da alanı terk gibi okuyor.",
        "B": "Alan boyutunda adımın bekleme: alana ihtiyacın var ama \"ne der\" diye isteyemiyorsun; suçlulukla alıyorsun.",
        "D": "Alan boyutunda adımın düzenleme: kendi alanını başkasının alanını düzenleyerek dolduruyorsun; kitabı unutup kahvaltı hazırlıyorsun.",
    },
    "S": {
        "T": "Söyleme boyutunda adımın takip: söylüyorsun ama suçlayarak; \"sen zaten\" ile başlayan cümleler ihtiyacı değil kızgınlığı taşıyor.",
        "C": "Söyleme boyutunda adımın çekilme: söylemek yerine uzaklaşıyorsun; kırgınlık soğukluk, ihtiyaç sessizlik oluyor.",
        "B": "Söyleme boyutunda adımın bekleme: ima ediyorsun, anlamasını bekliyorsun, anlamayınca küsüyorsun; dosya biriktiriyorsun.",
        "D": "Söyleme boyutunda adımın düzenleme: söylemek yerine idare ediyorsun; \"onun istediği gibi olsun\" senin isteğini siliyor.",
    },
    "O": {
        "T": "Onarım boyutunda adımın takip: özür dilemek yerine \"ama sen de\" ile devam ediyorsun; haklı çıkmak barışmanın önüne geçiyor.",
        "C": "Onarım boyutunda adımın çekilme: kavgadan sonra kapanıyorsun, günlerce; ilk adımı o atıyor ya da kimse atmıyor.",
        "B": "Onarım boyutunda adımın bekleme: o özür dilesin diye bekliyorsun; dilerse de günlerce hatırlatıyorsun.",
        "D": "Onarım boyutunda adımın düzenleme: kavgayı hemen kapatıyorsun, \"boş ver\" diyorsun; konu kapanıyor, çözülmüyor.",
    },
}

# boyut × tip -> (bu hafta tek adım, mesaj no)
BOYUT_ADIM = {
    "Y": {"T": ("Bu hafta bir kere iste ve bir kere sus: cevap gelmezse ikinci mesajı atma.", "Y4"),
          "C": ("Bu hafta bir kere \"yanıma otur\" de; sebep söyleme.", "Y1"),
          "B": ("Bu hafta bir kere sarılmak istediğini söyle; fark etmesini bekleme.", "Y2"),
          "D": ("Bu hafta bir akşamı iste, hazırlama: \"cumartesi bize ayrılsın\".", "Y3")},
    "U": {"T": ("Bu hafta onun bir planına \"iyi eğlen\" de ve o gün kendine bir şey yap.", "U2"),
          "C": ("Bu hafta uzaklaşmadan önce tek cümle bırak: \"yirmi dakika\".", "U3"),
          "B": ("Bu hafta bir saat kendine ayır ve bunu açıklamadan söyle.", "U1"),
          "D": ("Bu hafta pazar sabahı bir saat sadece sana; kahvaltı sonra.", "U4")},
    "S": {"T": ("Bu hafta bir kırgınlığı \"sen\" ile değil \"üzüldüm\" ile başlayarak söyle.", "S1"),
          "C": ("Bu hafta açmadığın bir konuyu aç: \"açmazsam içimde büyüyor\".", "S3"),
          "B": ("Bu hafta bir ihtiyacı ima etmeden iste; cümle hazır.", "S2"),
          "D": ("Bu hafta bir ev işini devret ve yapılmazsa yapılmasın.", "S4")},
    "O": {"T": ("Bu hafta bir kavgada \"ama sen de\" demeden dur; sadece \"haklıydın\" de.", "O2"),
          "C": ("Bu hafta kavgadan sonraki sabah ilk adımı sen at, kısa.", "O1"),
          "B": ("Bu hafta bir özrü \"duydum\" diyerek kabul et, hatırlatma.", "O3"),
          "D": ("Bu hafta \"geçti\" demek yerine \"geçmedi, biraz daha\" de.", "O4")},
}

ORUNTU = {
    "takip_cekilme": "İki adımı da sen atıyorsun: önce yaklaşıp sonra kapanıyorsun ya da önce kapanıp sonra peşinden gidiyorsun. Bu, partnerinin değil senin içindeki dans; iki adım da \"güvende miyim\" sorusuna cevap. Hangi adımın önce geldiğine bak, genellikle o daha eski.",
    "soylemeden_bekleyen": "Söyleme boyutun düşük ve adımın bekleme: ihtiyaç söylenmiyor, kırgınlık birikiyor, biriken kırgınlık sessizlik olarak çıkıyor. Partnerin \"ne oldu\" diye sorduğunda \"hiç\" diyorsan, örüntü tam olarak bu.",
    "idare_eden": "Onarım puanın yüksek ama adımın düzenleme: kavgalar hızlı kapanıyor çünkü sen kapatıyorsun. Bu onarım değil, idare. Bir sonraki kavgada konuyu kapatmadan bırak ve ne olduğuna bak; genellikle dünya yıkılmıyor.",
    "yapisik": "Yakınlık isteğin kendi alanını eziyor: alan almak suçluluk, onun alanı mesafe. Yakınlık, nefes alacak yer olmadan sürmez; bu ay bir saat alan al ve suçluluğun sönmesini bekle.",
    "uzak": "Alan ihtiyacın yakınlığı eziyor: mesafe güvenli, yakınlık riskli. Bu, sevmemek değil; yakınlığın pahalı olduğu bir yerden gelen tasarruf. Bu ay bir kere kendin iste; cevap ne olursa olsun.",
    "onarim_yok": "Onarım kapalı: kavgalar bitiyor ama tamir edilmiyor. Her kavga bir çentik bırakıyor ve çentikler toplanıyor. Bu rapordaki en acil satır bu; diğer her şey onarımın üstüne kurulur.",
    "yaygin": "Üç ya da dört boyut birden takılmış. Bu, ilişkinin kötü olduğu anlamına gelmiyor; bu ayın yorucu olduğu anlamına geliyor. Hepsini birden değil, en güçlü boyuttan başla; kas önce kolay yerde çalışır.",
    "korku_golgesi": "Söylememenin altında korku olabilir: katılmadığını söylemekten korktuğunu söylüyorsun ve söyleme boyutun düşük. Bunu rapor değil, bir insan okumalı. Dürüstçe sayfasındaki satırlara bak.",
}

PLAN_HAFTA = {
    "Y": "Yaklaşma haftası: bir kere iste, bir kere sus. İstediğin şey küçük olsun: yanına oturmak, bir sarılma.",
    "U": "Alan haftası: bir saat kendine, açıklamasız. Onun alanına da \"iyi eğlen\" de ve o saatte kendine bir şey yap.",
    "S": "Söyleme haftası: bir kırgınlığı ya da bir ihtiyacı aynı gün, tek cümleyle söyle. İma yok, dosya yok.",
    "O": "Onarım haftası: kavga olursa 24 saat içinde ilk adımı sen at; olmazsa eski bir kavgayı \"geçmedi\" diyerek aç.",
}

DURUSTCE = [
    "Bu rapor bir koçluk aracı; çift terapisi ya da psikolojik değerlendirme değil. İlişkide takılan adım öğrenilmiş bir beceridir ve yeniden öğrenilir. Burada yazanlar sana kim olduğunu değil, son bir ayda ne yaptığını söylüyor.",
    "Partnerin burada yok. Onun adımını bilmiyoruz; bu yüzden raporda onun hakkında hiçbir yargı yok. Senin adımın değişince dans değişir; ama dansın tamamı senin sorumluluğun değil.",
    "Bazı ilişkiler tek adımla düzelmez. Yakınlık korkusu, terk edilme teması, eski kayıplar; bunlar bir rapor okuyarak değil, bir insanla konuşarak çözülür. O zaman araç bu rapor değil, görüşme.",
]
DURUSTCE_GENIS = ("Cevaplarında güvenlikle ilgili bir işaret var: korku, kontrol ya da kavgalarda sınırı aşan bir şey. Bunu burada yargılamıyoruz; "
                  "ama bir ilişkide söylemek korkutuyorsa, yakınlık cümlesi değil destek gerekir. 183 Sosyal Destek Hattı ve 155 Polis İmdat 7/24 açık; "
                  "KADES uygulaması tek dokunuşla ulaşır. Bunu söylemek bu raporun görevi; gerisi senin kararın ve bu kararda yalnız değilsin.")

SONRAKI = [
    ("Raporu birlikte okuyalım", "30 dakikalık görüşme. Raporda en çok rahatsız eden cümleyi konuşuruz, bir sonraki adımı birlikte seçeriz. WhatsApp'tan yaz, uygun saati bulalım."),
    ("ThetaHealing odak programı", "Adımın takip ya da bekleme ise terk edilme teması, çekilme ise boğulma teması için 3-4 seanslık odak çalışması. thetakapisi.com.tr/danismanlik"),
    ("Sınır Haritası", "Bu rapor yakınlığı ölçtü; Sınır Haritası hayır diyebilmeyi ölçer. İkisi birlikte okununca ilişkideki adımın nereden geldiği görünür. thetakapisi.com.tr/envanterler"),
]

# --- kişinin kendi cevapları ---
S_TIP_YORUM = {
    "T": ["Burada adım takip: cevap gelmeyince yaklaşmayı artırdın; istemek baskıya dönüştü.",
          "Burada istediğin şey yakınlıktı ama çıkan şey suçlama; \"sen zaten\" ile başlayan cümle isteği gizledi.",
          "Burada ısrar ettin; ısrar, isteğin değil korkunun sesi."],
    "C": ["Burada adım çekilme: söylemek yerine uzaklaştın; sorun yerinde kaldı.",
          "Burada kapandın; kapanmak rahatlattı ama kısa sürdü.",
          "Burada mesafe aldın ama söylemeden; o da mesafeyi terk diye okudu."],
    "B": ["Burada adım bekleme: istemedin, fark edilmeyi bekledin; beklerken soğudun.",
          "Burada ima ettin; ima, isteğin şifreli hâli ve karşı taraf şifreyi çözemedi.",
          "Burada sustun ve dosya açtın; dosya büyüyor, o bilmiyor."],
    "D": ["Burada adım düzenleme: istemek yerine hallettin; yük sende kaldı.",
          "Burada kavgayı kapattın; kapandı ama çözülmedi.",
          "Burada \"onun istediği gibi olsun\" dedin; kendi isteğin silindi."],
    "TUTAR": ["Burada adımın aktı: söyledin, istedin ya da bıraktın. Bu cevabı hatırla; diğer boyutlara taşınabilir.",
              "Burada kısa ve sakin söyledin; tam olması gereken bu.",
              "Burada yakınlık ve alan birlikte durabildi; bu kas sende var."],
}
S_TUTAN_GIRIS = "Aynı anın akan hâli:"

Z_GIRIS = ("Sekiz ikilemde iki kötü arasından seçim yaptın; doğru cevap yoktu. Zorlandığında hangi adımı attığın burada görünüyor: puan değil, refleks.")
Z_YORUM = {
    "T": "İkilemlerde en çok takip adımını seçtin: zor anda ilk korumaya çalıştığın şey bağ, ilk feda ettiğin şey kendi sakinliğin.",
    "C": "İkilemlerde en çok çekilme adımını seçtin: zor anda ilk korumaya çalıştığın şey kendi alanın, ilk feda ettiğin şey bağ.",
    "B": "İkilemlerde en çok bekleme adımını seçtin: zor anda söylemek yerine anlaşılmayı bekliyorsun; beklemek istemekten daha güvenli geliyor.",
    "D": "İkilemlerde en çok düzenleme adımını seçtin: zor anda ilişkiyi tek başına ayakta tutuyorsun; kontrol sende kalınca güvende hissediyorsun.",
}
Z_DENGELI = "İkilemlerde tek bir adıma yığılmadın; refleksin duruma göre değişiyor. Bu, adımı seçebildiğin anlamına gelir."
Z_OZEL = {
    ("z3", "a"): "Seni daha çok yoran terk edilme korkusu. Bu korku yaklaşma adımını hızlandırır; yavaşlatmanın yolu korkuyu söylemek, yakınlığı istemek değil.",
    ("z3", "b"): "Seni daha çok yoran boğulma hissi. Bu his çekilme adımını hızlandırır; yavaşlatmanın yolu alanı söyleyerek almak, kaybolarak değil.",
    ("z5", "a"): "Partnerin seni \"çok ister, çok sorar\" diye biliyor. Bu bir kusur değil, bir doz meselesi; aynı istek sakin söylenince yakınlık.",
    ("z5", "b"): "Partnerin seni \"hiçbir şey istemez, belli etmez\" diye biliyor. Bu bir erdem değil, bir perde; perdenin arkasında istekler birikiyor.",
    ("z8", "a"): "\"İyiyim\"i kavga uzamasın diye diyorsun. Yani iyiyim bir cevap değil, bir kapı kapatma.",
    ("z8", "b"): "\"İyiyim\"i fark etmesini beklediğin için diyorsun. Yani iyiyim bir cevap değil, bir sınav.",
}

CUMLE_KISI = {
    "E": "Cümlen partnerine; söylemek isteyip söyleyemediğin şey ona yönelik.",
    "N": "Cümlen aslında kendine; partnerine değil, kendi ihtiyacına söylenmemiş bir şey var.",
}
CUMLE_TIP = {
    "T": "Cümlende \"{ipucu}\" geçiyor: söylenemeyen şeyin içinde yaklaşma isteği var; söylenseydi muhtemelen soru ya da sitem olarak çıkardı.",
    "C": "Cümlende \"{ipucu}\" geçiyor: söylenemeyen şeyin içinde alan isteği var; söylemek yerine uzaklaştın.",
    "B": "Cümlende \"{ipucu}\" geçiyor: söylenemeyen şey bir ihtiyaç; söylemek anlamsız geldi, fark edilmesini bekledin.",
    "D": "Cümlende \"{ipucu}\" geçiyor: söylenemeyen şey bir yük; söylemek yerine idare ettin.",
}
CUMLE_BOYUT = {
    "Y": "Cümlen Yaklaşma boyutuna düşüyor: yakınlık istemek.",
    "U": "Cümlen Alan boyutuna düşüyor: kendine yer istemek.",
    "S": "Cümlen Söyleme boyutuna düşüyor: bir kırgınlığı ya da ihtiyacı dile getirmek.",
    "O": "Cümlen Onarım boyutuna düşüyor: bir kavgadan sonra geri dönmek.",
}
CUMLE_BOYUT_UYUM = {
    True: "Bu boyut haritanda zaten düşük; cümlen haritanı doğruluyor.",
    False: "İlginç olan şu: bu boyut haritanda görece iyi. Demek ki genel bir tıkanma değil, bu konuya özel bir sessizlik var.",
}
CUMLE_TIP_UYUM = {
    True: "Bu, haritandaki baskın adımınla aynı; cümlen adımını tarif ediyor.",
    False: "Bu, haritandaki baskın adımından farklı; demek ki bu konuda başka bir adım atıyorsun. İki adımın var, ikisini de tanı.",
}
CUMLE_BELIRSIZ = ("Cümlende ne söylemek istediğin açıkça yazmıyor; bu da bir bilgi. Çoğu zaman en zor söylenen cümle, ne olduğu bile söylenemeyen cümledir.")
CUMLE_KARSI_GIRIS = "Aynı şeyi söyleyebileceğin cümle (yakınlık cümlesi {no}):"
CUMLE_KAPANIS = ("Bu cümleyi bugün söylemek zorunda değilsin. Ama bir kere yüksek sesle oku. Ağzından çıkınca ne kadar sert, ne kadar yumuşak olduğunu duy; genellikle düşündüğünden daha nazik çıkar.")

MESAJ_KUTU_UST = "YAKINLIK CÜMLESİ · {no}"
MESAJ_GERI_UST = "Karşılık gelmezse:"

MESAFE_METIN = {
    "yapışık": "Mesafe ibren yapışık tarafta: yakınlık isteğin alan ihtiyacını eziyor.",
    "uzak": "Mesafe ibren uzak tarafta: alan ihtiyacın yakınlığı eziyor.",
    "dengeli": "Mesafe ibren dengede: yakınlık ve alan birbirini ezmiyor.",
}
