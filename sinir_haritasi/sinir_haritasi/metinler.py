# -*- coding: utf-8 -*-
"""Rapor paragraf havuzu. Her girdi deterministik seçilir; {ad} alanı kişinin adıyla doldurulur."""

NE_NE_DEGIL = [
    "Bu rapor bir ölçek değil, bir ayna. Son bir ayda beş ilişki alanında sınırının nerede tuttuğunu, nerede esnediğini ve esnediğinde hangi kapıdan esnediğini gösteriyor. Teşhis koymuyor, etiket yapıştırmıyor; sadece bir fotoğraf çekiyor.",
    "Fotoğraf bir aylık. Zor bir ay geçirdiysen puanlar daha düşük, sakin bir ay geçirdiysen daha yüksek çıkmış olabilir. Bu yüzden sayıları kimlik gibi değil, hava durumu gibi oku: bugün böyle, yarın başka olabilir ve olacak.",
    "Raporu bir kerede değil, iki kerede oku. İlkinde sadece bak; itiraz etme, savunma. İkincisinde en çok rahatsız eden cümlenin altını çiz. O cümle, bu raporun sana söylemek istediği şeydir.",
]

TIP = {
    "S": {
        "ad": "Suçluluk kapısı",
        "mekanizma": "Hayır demek üzereyken içinde bir şey kabarıyor: suçluluk. Kelime henüz ağzından çıkmadan \"kırılır mı, üzülür mü, bencil mi görünürüm\" soruları geliyor ve cevap olarak \"peki\" çıkıyor. Sınırın yok değil; sınırın var ama suçluluk ondan daha hızlı.",
        "his": "Dışarıdan bakan seni esnek, anlayışlı, iyi kalpli görür. İçeriden ise her evet küçük bir borç gibi birikir; gün sonunda yorgunluk değil, bir tür kırgınlık kalır. Kimseye değil, kendine.",
        "koken": "Bu kapı genellikle sevginin şartlı olduğu bir yerde öğrenilir: iyi olursan sevilirsin, hayır dersen sevgi geri çekilir. O zaman gerçekten böyle olmuş olabilir. Şimdi çoğu zaman öyle değil; ama beden eski kuralı hatırlıyor.",
        "erdem": "Bu kapının bir erdemi var: vicdan. Başkasının ne hissedeceğini gerçekten görüyorsun. Mesele o görüşü kaybetmek değil, o görüşe kendini de dahil etmek.",
        "karsi": "Suçluluk bir duygu, bir kanıt değil.",
    },
    "K": {
        "ad": "Çatışma kaçınması",
        "mekanizma": "Rahatsız olduğunda sesin çıkmıyor. Tartışma çıkmasın, hava bozulmasın, kavga olmasın diye konuyu açmıyorsun; konu kapanmıyor, içeri giriyor. Sınırın belli değil, çünkü hiç söylenmedi.",
        "his": "Dışarıdan uyumlu, sakin, \"sorun çıkarmayan\" görünürsün. İçeride ise konuşulmayan her şey birikir ve bazen hiç ilgisi olmayan bir yerde, hiç ilgisi olmayan bir insana patlar. Ya da patlamaz; bedene yazılır.",
        "koken": "Bu kapı genellikle tartışmanın tehlikeli ya da yararsız olduğu bir evde öğrenilir: ya bağıran biri vardı ya da konuşulsa da hiçbir şey değişmezdi. Sessizlik o gün güvenli olandı. Bugün çoğu zaman sadece pahalı olan.",
        "erdem": "Bu kapının erdemi barış. Gerilimi erken sezen, ortamı yumuşatan bir yetenek bu. Mesele barışı bırakmak değil, kendi payına da barış istemek.",
        "karsi": "Konuşulmayan şey kaybolmuyor, sadece adres değiştiriyor.",
    },
    "G": {
        "ad": "Görünmezlik",
        "mekanizma": "Sınırını söylemiyorsun; karşı tarafın anlamasını bekliyorsun. \"Görmüyor mu yorulduğumu, fark etmiyor mu her şeyi ben yaptığımı?\" Fark etmiyor. Çünkü söylenmedi. Kırgınlık buradan büyüyor: ihtiyaç içeride, bekleyiş dışarıda.",
        "his": "Dışarıdan güçlü, her şeyi halleden biri görünürsün; kimse senin de yorulduğunu düşünmez, sen öyle gösterdin. İçeride ise \"görülmek\" ihtiyacı o kadar büyümüş ki görülmek için daha çok yapıyorsun; bu da seni daha görünmez kılıyor.",
        "koken": "Bu kapı genellikle ihtiyaç söylemenin işe yaramadığı bir yerde öğrenilir: söyledin, duyulmadı; ya da söylemek zayıflık sayıldı. O gün beklemek, istemekten güvenliydi.",
        "erdem": "Bu kapının erdemi algı. Söylenmeyeni sen de fark ediyorsun, başkaları için de. Mesele bu algıyı başkalarından beklemek değil, kendi ihtiyacını sesli söylemek.",
        "karsi": "Görülmek için daha fazla yapmak zorunda değilsin; söylemek yeter.",
    },
    "T": {
        "ad": "Tek başına taşıma",
        "mekanizma": "Sınır, \"ben yaparım\"la siliniyor. Kimse istemeden üstleniyor, devretmiyor, devretsen de kontrol ediyorsun. Hayır demen gerekmiyor, çünkü zaten evet demeden işi almış oluyorsun.",
        "his": "Dışarıdan yetkin, güvenilir, vazgeçilmez görünürsün. İçeride ise \"bıraksam dağılır\" inancı var ve bu inanç seni hiçbir zaman bırakmıyor. Tatilde bile liste dönüyor.",
        "koken": "Bu kapı genellikle bir şeylerin gerçekten dağıldığı bir yerde öğrenilir: biri tutmadı, sen tuttun. O gün gerekliydi. Bugün ise taşıdığın şeylerin çoğu senin değil.",
        "erdem": "Bu kapının erdemi yetkinlik. Gerçekten iyi yapıyorsun. Mesele kötü yapılmasına izin vermek; dünya kötü yapılmış bir bulaşıkla dönmeye devam ediyor.",
        "karsi": "Her şeyi tutan el, hiçbir şeyi tutamaz hale geliyor.",
    },
}

CIFT_KAPI = "Sende iki kapı neredeyse eşit açılıyor: {t1} ve {t2}. Bu, iki mekanizmanın birbirini beslediği anlamına geliyor; birini kapatınca diğeri devreye giriyor. Rapor ikisini de anlatacak, ama bu hafta yalnız birine bak."

TUTUYOR = "Dört kapı da düşük açılıyor: sınırın büyük ölçüde tutuyor. Bu raporda \"sorun\" aramak yerine neyin işe yaradığına bak; aşağıdaki alan sayfaları, hangi ilişkide sınırı nasıl koruduğunu gösteriyor. Zayıf görünen tek alan varsa, oradaki adım yeter."

ALAN_BANT = {
    "A": {
        "Tutuyor": "Ailede sınırın tutuyor. Yemek davetine hayır diyebiliyor, son dakika isteklere planını koruyabiliyorsun. Bu, çoğu kadının en zor alanı; sende en güçlülerden biri.",
        "Esniyor": "Ailede sınırın var ama baskı altında açılıyor. Normal günlerde tutuyor; bayram, hastalık, \"bir kerelik\" gibi anlarda kapı aralanıyor ve sonra kapanması zor oluyor.",
        "Sızıyor": "Ailede çoğu kez evet diyor, sonra bedelini ödüyorsun. Sınır kavramı var, ama aile içinde geçerli değilmiş gibi davranıyorsun; sanki orada başka kurallar varmış gibi. Belki gerçekten var; o zaman kuralı sen koydun değil, sana kondu.",
        "Kapı yok": "Ailede sınır henüz kurulmamış. İstek geliyor, evet çıkıyor; arada \"ister miyim\" sorusu hiç sorulmuyor. Bu bir eksiklik değil, bir alışkanlık; en eski alışkanlık. En yavaş değişen alan burası olacak ve bu normal.",
    },
    "I": {
        "Tutuyor": "İşte sınırın tutuyor. Mesai dışına, kapsam dışına, yıkılan işe hayır diyebiliyorsun. Profesyonellik bu; çoğu insan bunu sertlik sanır, sen değil.",
        "Esniyor": "İşte sınırın var ama \"acil\" kelimesi onu açıyor. Normal akışta koruyorsun; baskı, patron, müşteri devreye girince evet çıkıyor ve akşam saatleri kayıyor.",
        "Sızıyor": "İşte çoğu kez evet diyorsun. Mesai dışı mesajlara hemen cevap, başkasının işini üstlenme, kapsam dışı isteğe bedava evet. Sonuç: yorgunluk ve fark edilmeme hissi birlikte büyüyor.",
        "Kapı yok": "İşte sınır yok; iş saatleri, görev tanımı, ücret gibi çizgiler sende silinmiş. Bu seni kısa vadede vazgeçilmez, uzun vadede tükenmiş yapar. Burada en küçük adım bile büyük fark eder.",
    },
    "R": {
        "Tutuyor": "Arkadaş ve çevrede sınırın tutuyor. Gece mesajına sabah cevap verebiliyor, borç isteğini reddedebiliyor, grup işini başkasına bırakabiliyorsun.",
        "Esniyor": "Arkadaşlıkta sınırın var ama \"ayıp olur\" onu açıyor. Yakın ilişkilerde tutuyor, çevre genişledikçe (veli grubu, komşu, uzak arkadaş) kapı aralanıyor.",
        "Sızıyor": "Arkadaş ve çevrede çoğu kez evet diyorsun. Dinleyen hep sen, arayan hep sen, organize eden hep sen. Dengesizliği görüyorsun ama dile getirmiyorsun; getirsen arkadaşlık bozulur diye.",
        "Kapı yok": "Çevrede sınır yok; herkesin ihtiyacı senin programından önce geliyor. \"İyi arkadaş\" olmak için ödediğin bedel bu. İyi arkadaş hayır da diyebilen arkadaştır.",
    },
    "E": {
        "Tutuyor": "İlişkide sınırın tutuyor. İhtiyacını söyleyebiliyor, rahatsızlığını açabiliyor, yükü paylaşabiliyorsun. İlişkilerde en zor olan şey bu; sende çalışıyor.",
        "Esniyor": "İlişkide sınırın var ama \"kavga çıkmasın\" onu açıyor. Küçük konularda tutuyor, büyük konularda (para, aile, zaman) susuyorsun.",
        "Sızıyor": "İlişkide çoğu kez kendi ihtiyacını erteliyorsun. Konuyu açmıyor, anlaşılmayı bekliyor, yükü tek taşıyorsun. Bu bir sevgi biçimi gibi görünüyor; aslında yavaş bir uzaklaşma.",
        "Kapı yok": "İlişkide sınır yok; ne istediğin, ne istemediğin ortada değil. Bu alanda sınır koymak diğerlerinden farklı: tek başına değil, konuşarak kurulur. Raporun \"Dürüstçe\" sayfasını bu alan için oku.",
    },
    "N": {
        "Tutuyor": "Kendine sınırın tutuyor: zamanını, dinlenmeni, ihtiyacını koruyabiliyorsun. Bu alan tutuyorsa diğer alanlar daha kolay toparlanır; en iyi haber burada.",
        "Esniyor": "Kendine ayırdığın alan var ama ilk sıkışmada ilk feda edilen o oluyor. Dinlenme planı, kendine ayrılan cumartesi, uyku: hepsi \"sonra\"ya atılabilir sayılıyor.",
        "Sızıyor": "Kendine sınır koyamıyorsun: zaman başkası istedi diye iptal, yorgunluk \"iyiyim\"le kapatılıyor, bir şey alırken suçluluk. Herkese bakıyorsun; listede olmayan tek kişi sensin.",
        "Kapı yok": "Kendine dair sınır yok; dinlenmek, istemek, almak gibi fiiller sende izinle çalışıyor ve izni veren yok. Bu alan, diğer dört alanın temeli. Burası kurulmadan diğerleri tutmaz.",
    },
}

ALAN_TIP = {
    "A": {"S": "Ailede en çok suçluluk kapısından sızıyorsun: hayır deyince \"kötü evlat\" olacağın korkusu.",
          "K": "Ailede en çok çatışma kaçınmasından sızıyorsun: tartışma çıkmasın diye konu hiç açılmıyor.",
          "G": "Ailede en çok görünmezlikten sızıyorsun: söylemiyor, anlamalarını bekliyor, anlamayınca kırılıyorsun.",
          "T": "Ailede en çok tek başına taşımadan sızıyorsun: organizasyon, bakım, iş; hepsi sende, kimse istemeden."},
    "I": {"S": "İşte en çok suçluluk kapısından sızıyorsun: hayır demek ekibi yarı yolda bırakmak gibi geliyor.",
          "K": "İşte en çok çatışma kaçınmasından sızıyorsun: haksızlığa ses çıkarmıyor, \"tamam\" diyorsun.",
          "G": "İşte en çok görünmezlikten sızıyorsun: emeğin fark edilmiyor, sen de fark ettirmiyorsun.",
          "T": "İşte en çok tek başına taşımadan sızıyorsun: \"daha hızlı olur\" diye başkasının işi sana kalıyor."},
    "R": {"S": "Çevrede en çok suçluluk kapısından sızıyorsun: reddetmek ayıp, borç vermemek kabalık geliyor.",
          "K": "Çevrede en çok çatışma kaçınmasından sızıyorsun: üzen arkadaşa bir şey söylemiyorsun.",
          "G": "Çevrede en çok görünmezlikten sızıyorsun: hep sen arıyor, hep sen dinliyorsun; kimse fark etmiyor.",
          "T": "Çevrede en çok tek başına taşımadan sızıyorsun: grup işi, organizasyon, veli grubu; hepsi sende."},
    "E": {"S": "İlişkide en çok suçluluk kapısından sızıyorsun: kendi ihtiyacını istemek bencillik gibi geliyor.",
          "K": "İlişkide en çok çatışma kaçınmasından sızıyorsun: kavga çıkmasın diye konu açılmıyor.",
          "G": "İlişkide en çok görünmezlikten sızıyorsun: anlamasını bekliyor, anlamayınca kırılıyorsun.",
          "T": "İlişkide en çok tek başına taşımadan sızıyorsun: ev de, ilişki de \"ben hallederim\"le yürüyor."},
    "N": {"S": "Kendine karşı en çok suçluluk kapısından sızıyorsun: kendine zaman ya da bir şey ayırmak suç gibi.",
          "K": "Kendine karşı en çok çatışma kaçınmasından sızıyorsun: yorgunum demek yerine iyiyim diyorsun.",
          "G": "Kendine karşı en çok görünmezlikten sızıyorsun: ihtiyacını söylemiyor, fark edilmesini bekliyorsun.",
          "T": "Kendine karşı en çok tek başına taşımadan sızıyorsun: bitirmeden dinlenemiyorsun ve hiç bitmiyor."},
}

# (adım cümlesi, Hayır Deme Cümleleri mesaj numarası)
ALAN_ADIM = {
    "A": {"S": ("Bu hafta aileden gelen bir isteğe \"bu hafta olmuyor\" de; sebep açıklama.", "01"),
          "K": ("Bu hafta ailede seni rahatsız eden tek bir şeyi tek cümleyle söyle.", "02"),
          "G": ("Bu hafta aileden bir ihtiyacını açıkça iste; anlamalarını bekleme.", "06"),
          "T": ("Bu hafta bir aile işini birine devret ve nasıl yapıldığına karışma.", "03")},
    "I": {"S": ("Bu hafta mesai dışı bir mesaja sabah cevap ver.", "32"),
          "K": ("Bu hafta işte katılmadığın bir şeye \"katılmıyorum\" de, yazılı olsun.", "37"),
          "G": ("Bu hafta yaptığın bir işi sorulmadan söyle: \"bunu ben yaptım.\"", "36"),
          "T": ("Bu hafta sana yıkılan bir işi geri ver: \"bu senin işin.\"", "29")},
    "R": {"S": ("Bu hafta bir isteğe \"şu an cevap veremem, döneceğim\" de.", "19"),
          "K": ("Bu hafta bir arkadaşına seni üzen şeyi tek cümleyle söyle.", "20"),
          "G": ("Bu hafta aramayı bekle; arayan sen olma.", "21"),
          "T": ("Bu hafta bir grup görevini almayı reddet.", "39")},
    "E": {"S": ("Bu hafta partnerine bir ihtiyacını açıklama yapmadan söyle.", "14"),
          "K": ("Bu hafta ertelediğin bir konuyu sakin bir saatte aç; çözmek zorunda değilsin, açman yeter.", "17"),
          "G": ("Bu hafta \"anlamalıydı\" dediğin bir şeyi ona söyle.", "18"),
          "T": ("Bu hafta bir ev işini devret ve yapılmazsa yapılmasın.", "12")},
    "N": {"S": ("Bu hafta kendine bir şey al ve kimseye açıklama.", "60"),
          "K": ("Bu hafta bir kişiye \"yorgunum\" de; iyiyim deme.", "58"),
          "G": ("Bu hafta bir ihtiyacını yüksek sesle iste; fark edilmesini bekleme.", "58"),
          "T": ("Bu hafta bir işi yarım bırak ve dinlen.", "55")},
}

ORUNTU = {
    "herkese_var_kendine_yok": "Herkese var, kendine yok. Sınırı başkasına koyabiliyorsun; ailede, işte, çevrede kapı tutuyor. Koyamadığın tek kişi sensin: zaman, dinlenme, ihtiyaç. Bu durumda dışarıdaki sınırlar da uzun süre dayanmaz, çünkü içeride dolduracak yer yok. Plan bu yüzden kendinden başlıyor.",
    "evde_siziyor_iste_tutuyor": "Evde sızıyor, işte tutuyor. Sınır koyma becerin var; aile içinde kapanıyor. Bu bir beceri eksikliği değil, eski bir anlaşma: ailede hayır demek bir zamanlar bir şeye mal olmuş. Anlaşma hâlâ geçerli mi, şimdi sen karar veriyorsun.",
    "iste_siziyor_evde_tutuyor": "İşte sızıyor, evde tutuyor. Evde koruduğun şeyi işte veriyorsun; muhtemelen onay için. İşte hayır demek kariyer intiharı değil, kapasite yönetimi. Rapordaki iş sayfası sana uygun cümleyi veriyor.",
    "sessiz_tasiyici_ikilisi": "Sessiz taşıyıcı ikilisi: çatışma kaçınması ve görünmezlik birlikte açılıyor. Söylemiyorsun ve anlaşılmayı bekliyorsun; iki mekanizma birbirini besliyor. Çıkış tek yerden: söylemek. Söylediğinde beklemek de biter.",
    "sucluluk_ustlenme_sarmali": "Suçluluk ve üstlenme sarmalı: hayır diyemiyorsun, sonra aldığın işi devredemiyorsun. Yük iki kere biniyor; bir kere evet derken, bir kere tek başına yaparken. Sarmalı ilk halkadan kırmak daha kolay: hayır.",
    "tek_alan_cokusu": "Tek alan çöküşü: genel bir sınır sorunun yok. Dört alanda kapı tutuyor; tek bir ilişki var ve orada kapı yok. Mesele \"sınır koyamıyorum\" değil, \"bu kişiye sınır koyamıyorum\". Bu daha dar ve daha çözülebilir bir mesele.",
    "yaygin_sizinti": "Yaygın sızıntı: dört ya da beş alanda birden sızıyorsun. Mesele tek kişi değil, sınır kurma becerisinin kendisi. Bu durumda büyük kararlar değil, çok küçük adımlar işe yarar. Plan bu yüzden haftada tek davranış istiyor; fazlası geri teper.",
    "partner_golgesi": "İlişki alanında puanın düşük ve hayır dediğinde partnerinin tepkisinden çekindiğini söyledin. Bunu özellikle not ediyoruz: sınır koymak tehlikeli hissettiriyorsa mesele sınır değildir. Dürüstçe sayfası bu alan için yazıldı.",
}

BAGLAM = {
    ("S", "aile"): "Suçluluk kapısı ailede açılıyor, işte kapalı. Aynı davranışı patronuna yapmıyorsun; demek ki beceri var, kişiye göre değişiyor.",
    ("S", "is"): "Suçluluk kapısı işte açılıyor, ailede kapalı. Ailene hayır diyebiliyorsun; işte aynı cümleyi kuramıyorsun. Sınırın var, adresi yanlış.",
    ("K", "aile"): "Ailede susuyor, işte konuşuyorsun. Çatışmadan kaçınman genel değil; aileye özel.",
    ("K", "is"): "İşte susuyor, ailede konuşuyorsun. Evde söyleyebildiğini işte söyleyemiyorsun; muhtemelen bedeli daha büyük görünüyor.",
    ("G", "aile"): "Ailede anlaşılmayı bekliyor, işte söylüyorsun. Görünmezlik ailede devreye giriyor; en eski ilişkilerde en eski alışkanlık.",
    ("G", "is"): "İşte anlaşılmayı bekliyor, ailede söylüyorsun. Emeğin fark edilsin istiyorsun ama fark ettirmiyorsun.",
}

PLAN_HAFTA = {
    "A": "Aile: haftada bir isteğe hayır. Sebep yok, özür yok.",
    "I": "İş: mesai dışı bir mesaj sabaha kalsın; bir kapsam dışı isteğe ücret söyle.",
    "R": "Çevre: bir görev alma; bir gece mesajına sabah cevap ver.",
    "E": "İlişki: bir ihtiyacını açıklamasız söyle; bir ev işini devret.",
    "N": "Kendine: haftada bir öğleden sonra sana ait; iptal yok.",
}

DURUSTCE = [
    "Bu rapor bir koçluk aracı; psikoterapi ya da psikolojik değerlendirme değil. Sınır koymak zorlandığın bir beceri olabilir ve beceriler öğrenilir. Burada yazanlar sana kim olduğunu değil, son bir ayda ne yaptığını söylüyor.",
    "Bazı sınırlar tek başına kurulmaz. Partnerle, aileyle, iş yeriyle konuşarak kurulur ve karşı taraf değişmezse sınır da bir yere kadar tutar. Bu senin başarısızlığın değildir.",
    "Sınır koymak sana tehlikeli hissettiriyorsa, yani hayır dediğinde korku, baskı, aşağılama ya da şiddet geliyorsa, mesele sınır değildir; güvenliktir. O zaman mesaj şablonu değil destek gerekir: 183 Sosyal Destek Hattı, 155 Polis İmdat. Bunu söylemek bu raporun görevi; gerisi senin kararın.",
]
DURUSTCE_GENIS = "Cevaplarında hayır demenin sana korku ya da baskı hissettirdiğine dair işaretler var. Bunu etiketlemiyoruz; sadece şunu söylüyoruz: korkuyla verilen evet, sınır meselesi değildir ve tek başına çözülmesi beklenmez. 183 Sosyal Destek Hattı günün her saati açık, ücretsiz ve gizlidir. İstersen bu raporu birlikte okuyalım; görüşme linki son sayfada."

SONRAKI = [
    ("Raporu birlikte okuyalım", "30 dakikalık görüşme. Rapordaki üç cümleyi konuşuruz, bir sonraki adımı birlikte seçeriz. WhatsApp'tan yaz, uygun saati bulalım."),
    ("Hayır Deme Cümleleri", "Raporda numarası geçen 60 hazır mesaj. Kopyala, gönder, telefonu bırak. thetakapisi.com.tr/hayir-deme-cumleleri"),
    ("İnanç Kazısı", "\"Hayır dersem sevilmem\" cümlesinin kökü için. thetakapisi.com.tr/dijital-urunler"),
]
