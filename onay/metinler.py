# -*- coding: utf-8 -*-
"""Onay İhtiyacı Haritası rapor metinleri."""

NE_NE_DEGIL = [
    "Bu rapor zayıflık ölçmüyor. Onay istemek insan olmanın parçası; hepimiz görülmek, sevilmek, kabul edilmek isteriz. Burada aranan şey, bu ihtiyacın sana neye mal olduğu: hangi alanda kendi sesini bıraktığın ve bunu hangi stratejiyle yaptığın.",
    "Fotoğraf bir aylık. Zor bir ilişki dönemi, yeni bir iş ya da bir aile meselesi yaşadıysan bazı alanlar olduğundan düşük çıkmış olabilir. Sayıları kimlik gibi değil, hava durumu gibi oku: bugün böyle, birkaç hafta sonra başka olabilir.",
    "Raporu iki kerede oku. İlkinde sadece bak; kendini savunma, \"ama o kişi öyle biri\" deme. İkincisinde en çok rahatsız eden cümlenin altını çiz. O cümle, bu raporun sana asıl söylemek istediği şey.",
]

TIP = {
    "U": {
        "ad": "Uyumlu",
        "karsi": "Evet demek, sevilmek değildir.",
        "mekanizma": "Senin tipin uyum. Karşındakinin hoşnutsuzluğu sende bir alarm çalıyor ve alarmı susturmanın en hızlı yolu onun istediğini yapmak. Bu yüzden hayır cümlesi ağzına gelmeden evet çıkıyor. Kısa vadede ortam yumuşuyor; uzun vadede kendi istediğin şeyin ne olduğunu hatırlamak zorlaşıyor.",
        "his": "İçeriden şöyle hissediliyor: biri bir şey isteyince göğsünde bir sıkışma ve ağzından \"tabii\" çıkıyor. Sonra bir kırgınlık geliyor, kime olduğunu tam bilmediğin. Ortam gerildiğinde onu yumuşatmak sana düşüyormuş gibi.",
        "koken": "Bu tip genellikle bir yetişkinin öfkesinin ya da üzüntüsünün evin havasını belirlediği yerde öğrenilir. Çocuk, ortamı sakin tutmanın güvende kalmak demek olduğunu öğrenir. Şimdi kimsenin hoşnutsuzluğu seni yok edemez, ama beden hâlâ eski hesabı yapıyor.",
        "erdem": "Bu tipin erdemi incelik. İnsanların ne hissettiğini çabuk fark ediyor, ortamı yumuşatabiliyorsun. Sorun inceliğin kendisi değil, hep tek yöne akması. Aynı inceliği kendine de gösterebilirsin.",
        "kural": "Senin için küçük deney: cevabı ertele. Bir şey istendiğinde hemen evet deme; \"bakıp dönerim\" de. Arada kalan on dakika, kendi isteğini duyman için yeterli.",
    },
    "K": {
        "ad": "Kanıtlayan",
        "karsi": "Çok yapmak, yeterli olmak değildir.",
        "mekanizma": "Senin tipin kanıtlamak. Değerin bir sınav gibi geliyor ve sınav hiç bitmiyor: iyi yaptığında kısa bir rahatlama, sonra yeni bir çıta. Onay yaptığın şeye geliyor; bu yüzden durmak, değersiz kalmak gibi hissettiriyor.",
        "his": "İçeriden şöyle hissediliyor: dinlenirken bile içten içe bir suçluluk. Övgü geldiğinde birkaç dakika iyi, sonra \"bir dahakine\" sesi. Takdir gelmediğinde hızla \"yetmedi\" sonucuna varıyorsun.",
        "koken": "Bu tip genellikle sevginin ya da ilginin başarıya bağlandığı yerde öğrenilir: karne güzelse görülürsün, değilse görünmezsin. Çocuk olduğu hâliyle değil, yaptığıyla sevildiğine inanmaya başlar. Şimdi yetişkinsin, ama içerideki karne hâlâ dağıtılıyor.",
        "erdem": "Bu tipin erdemi emek ve yetkinlik. Yaptığın işler genellikle iyi, sana güveniliyor. Sorun çalışkanlık değil, değerinin buna bağlanması. Aynı emeği dinlenmeye de ayırabildiğinde gerçek güç ortaya çıkar.",
        "kural": "Senin için küçük deney: yeterince iyi teslim et. Bu hafta bir işi yüzde seksenle bırak ve kimseye açıklama yapma. Sonra ne olduğunu gözle; çoğu zaman hiçbir şey olmaz.",
    },
    "S": {
        "ad": "Silinen",
        "karsi": "Görünmez olmak, güvende olmak değildir.",
        "mekanizma": "Senin tipin silinmek. Onay kazanmak yerine onaysızlıktan kaçıyorsun: ihtiyacını küçültüyor, fikrini saklıyor, az yer kaplamaya çalışıyorsun. Kimseye yük olmazsan kimse senden uzaklaşmazmış gibi geliyor. Ama görünmediğin yerde sevilmen de zorlaşıyor.",
        "his": "İçeriden şöyle hissediliyor: \"Benim istediğim o kadar önemli değil.\" Bir şey istemek, rahatsız etmek gibi. Kalabalıkta kenarda durmak daha rahat; ama bazen kimsenin seni gerçekten tanımadığı hissi ağır geliyor.",
        "koken": "Bu tip genellikle ihtiyaçların fazla ya da yük gibi görüldüğü yerde öğrenilir; ya da evde başka birinin ihtiyacı her şeyi kapladığında. Çocuk, en az yer kaplayanın en az zarar gördüğünü öğrenir. Şimdi yer kaplamak senin hakkın, ama alışkanlık eskisi gibi.",
        "erdem": "Bu tipin erdemi tevazu ve dikkat. Gözlemliyor, dinliyor, başkalarına alan açıyorsun. Sorun alçakgönüllülük değil, kendi alanının hiç açılmaması. Aynı dikkati kendi sesine de verebilirsin.",
        "kural": "Senin için küçük deney: tek bir tercih söyle. Bu hafta bir kez \"ben şunu istiyorum\" de: yemek, film, saat, masa. Küçük bir tercih, görünür olmanın en güvenli ilk adımı.",
    },
    "T": {
        "ad": "Tetikte",
        "karsi": "Herkesi okumak, kendini duymak değildir.",
        "mekanizma": "Senin tipin tetikte olmak. Zihnin sürekli tarama yapıyor: ses tonu, mesajın gecikmesi, yüzdeki küçük bir değişiklik. Bir tehlike işaretini erken yakalarsan önlem alabileceğini düşünüyorsun. Bu tarama yorucu, çünkü hiç kapanmıyor ve çoğu zaman olmayan şeyleri de yakalıyor.",
        "his": "İçeriden şöyle hissediliyor: bir mesaj kısa gelince midende bir düğüm. Konuşmaları sonradan kafanda tekrar oynatıyorsun. Biri sessizleşince sebebini bulana kadar rahat etmiyorsun.",
        "koken": "Bu tip genellikle havanın aniden değişebildiği bir ortamda öğrenilir: bir yetişkinin ruh hâli öngörülemezse çocuk onu okumayı ustalıkla öğrenir. O zaman bu bir hayatta kalma becerisiydi. Şimdi ortam değişti ama radar hâlâ açık.",
        "erdem": "Bu tipin erdemi sezgi. İnsanları derinden okuyor, söylenmeyeni duyuyorsun. Sorun sezginin kendisi değil, hep tehlikeye ayarlı olması. Aynı radarı kendi içine çevirdiğinde ne istediğini de duyabilirsin.",
        "kural": "Senin için küçük deney: tahmin etme, sor. Bu hafta bir kez kafanda senaryo kurmak yerine doğrudan sor: \"Bana kırgın mısın?\" Cevap çoğu zaman senaryodan hafiftir.",
    },
}

CIFT_TIP = ("İki tipin birbirine çok yakın: {t1} ve {t2}. Bu, ilişkiye ve duruma göre farklı bir stratejiye geçtiğin anlamına gelir; "
            "raporda ikisi de var. Genellikle biri yakın ilişkilerde, diğeri daha uzak ilişkilerde öne çıkar.")

SERBEST = ("Dört tipin de düşük çıktı: onay ihtiyacın tek bir stratejiye yığılmamış. Bu iyi haber; zorlandığında hangi tepkiyi "
           "vereceğini seçebiliyorsun. Raporun geri kalanı daha çok \"nerede\" sorusuna cevap verecek, \"nasıl\" sorusuna değil.")

YUK_METIN = {
    True: "Onay yükün ağır: en zayıf iki alanında kendi sesin büyük ölçüde başkalarının tepkisine bağlanmış. Bu ay her yerde değişmeye çalışma; tek bir ilişkide küçük bir deney yeter.",
    False: "Onay yükün taşınabilir düzeyde: bazı alanlarda kendinden uzaklaşıyorsun ama boğucu değil. Küçük deneyler burada hızla fark yaratır.",
}

ALAN_BANT = {
    "I": {
        "Kendinde": "İş ve otorite karşısında kendinde kalabiliyorsun: itiraz edebiliyor, takdir gelmediğinde de işinin değerini biliyorsun. Bu alan, diğerlerine taşıyabileceğin bir dayanak.",
        "Dalgalı": "İşte bazen kendindesin, bazen dışarıdasın. Özellikle yetkili birinin karşısında ya da dönüt gelmediğinde onay ihtiyacı sesini yükseltiyor.",
        "Dışarıda": "İşte değerin büyük ölçüde başkalarının gözünden ölçülüyor: dönüt gelmeyince huzursuzluk, istek gelince hayır diyememe. Bu ay bir kez \"bakıp dönerim\" demek hedef olsun.",
        "Kaybolmuş": "İş bu ay neredeyse tamamen başkalarının onayına göre şekillenmiş. Bu bir zayıflık değil, uzun süre taşınmış bir yükün işareti. Tek bir küçük hayırla başla.",
    },
    "A": {
        "Kendinde": "Ailenin içinde kendi yerin var: sevgiyi kaybetmeden farklı düşünebiliyorsun. Bu, kolay kazanılmayan bir özgürlük.",
        "Dalgalı": "Ailede bazı konularda kendindesin, bazılarında eski rol devreye giriyor. Hangi konuların seni küçülttüğüne bak; genellikle kararlar ve beklentiler.",
        "Dışarıda": "Ailenin onayı hâlâ kararlarının ortağı: söylenmeyen kararlar, üstlenilen roller, akıldan çıkmayan sözler var. Bu ay tek bir kararı uzun açıklama yapmadan uygulamak hedef olsun.",
        "Kaybolmuş": "Ailede kendi sesin neredeyse duyulmuyor. Bu çoğu zaman en eski ve en derin onay bağıdır; bir günde çözülmez. Bu ay sadece fark etmek bile yeterli.",
    },
    "P": {
        "Kendinde": "Yakın ilişkinde kendinde kalabiliyorsun: ihtiyacını söyleyebiliyor, partnerin uzaklaştığında kendini kaybetmiyorsun.",
        "Dalgalı": "İlişkinde bazen kendindesin, bazen onun ruh hâline göre şekil alıyorsun. Özellikle sessizlik ve kırgınlık anlarına bak.",
        "Dışarıda": "İlişkinde kendi isteğin geride kalmış: kırgınlıklar yutuluyor, sessizlikler alarm çalıyor. Bu ay bir kırgınlığı kısa bir cümleyle söylemek hedef olsun.",
        "Kaybolmuş": "İlişkide kendini neredeyse kaybetmişsin: istekler, kırgınlıklar, kararlar hep onun etrafında dönüyor. Bu bazen senin yorgunluğunun, bazen ilişkinin kendisinin işaretidir. İkisini ayırmak için bir uzmanla konuşmak iyi gelebilir.",
    },
    "C": {
        "Kendinde": "Arkadaşlıklarında rahatsın: hayır diyebiliyor, kırılmaktan korkmadan farklı düşünebiliyorsun. Bu ilişkiler seni yormuyor, besliyor.",
        "Dalgalı": "Arkadaşlıklarda bazen kendindesin, bazen kabul görmek için fazlasını yapıyorsun. Kimlerin yanında küçüldüğüne bak.",
        "Dışarıda": "Çevrende kabul görmek için çok emek veriyorsun: istemediğin buluşmalar, sustuğun fikirler, sonradan tekrar oynatılan konuşmalar. Bu ay tek bir davete bahanesiz hayır demek hedef olsun.",
        "Kaybolmuş": "Arkadaşlıklarda kendi sesin neredeyse kaybolmuş; ilişkiler senin için dinlenme değil sınav olmuş. Bu ay seni gerçekten rahatlatan tek bir kişiyle zaman geçir.",
    },
    "G": {
        "Kendinde": "Görünür olmakta rahatsın: fikrini söylüyor, paylaşıyor, beğeni gelmese de kendi zevkine güveniyorsun.",
        "Dalgalı": "Görünür olmak bazen rahat, bazen kaygılı. Özellikle paylaşımdan sonraki saatlere ve kalabalıkta fikir söyleme anlarına bak.",
        "Dışarıda": "Görünürlük ciddi bir onay alanı olmuş: beğeni kontrolü, görünüş kaygısı, söylenmeyen fikirler. Bu ay bir paylaşımdan sonra 24 saat bakmamak hedef olsun.",
        "Kaybolmuş": "Görünmek neredeyse tamamen başkalarının yorumuna bağlanmış. Karşılaştırma ve görünüş kaygısı bu kadar yoğunsa ekran süresini sınırlamak en hızlı rahatlamadır.",
    },
}

ALAN_TIP = {
    "I": {"U": "İşte tipin uyum: hayır diyememek, fazladan yükü sessizce almak.",
          "K": "İşte tipin kanıtlamak: takdir görmek için gereğinden fazla çalışmak.",
          "S": "İşte tipin silinmek: fikrini saklamak, toplantılarda görünmez kalmak.",
          "T": "İşte tipin tetikte olmak: yöneticinin ses tonunu ve dönüt gecikmesini sürekli okumak."},
    "A": {"U": "Ailede tipin uyum: herkes memnun olsun diye kendi planından vazgeçmek.",
          "K": "Ailede tipin kanıtlamak: \"başarılı çocuk\" rolünü bırakamamak.",
          "S": "Ailede tipin silinmek: isteğini söylememek, kararlarını saklamak.",
          "T": "Ailede tipin tetikte olmak: bir sözün ya da bakışın günlerce yankılanması."},
    "P": {"U": "İlişkide tipin uyum: ortam bozulmasın diye her şeye evet demek.",
          "K": "İlişkide tipin kanıtlamak: sevilmeye değer olduğunu fazlasıyla göstermeye çalışmak.",
          "S": "İlişkide tipin silinmek: kırgınlığı yutmak, isteğinden vazgeçmek.",
          "T": "İlişkide tipin tetikte olmak: sessizlikleri ve gecikmeleri tehlike işareti gibi okumak."},
    "C": {"U": "Çevrede tipin uyum: istemediğin davetlere kırılmasınlar diye gitmek.",
          "K": "Çevrede tipin kanıtlamak: hep yardım eden, hep organize eden olmak.",
          "S": "Çevrede tipin silinmek: grupta sesini çıkarmamak, kenarda kalmak.",
          "T": "Çevrede tipin tetikte olmak: buluşmalardan sonra her cümleyi tekrar oynatmak."},
    "G": {"U": "Görünürlükte tipin uyum: çoğunluğa uymak, onlar gibi konuşmak.",
          "K": "Görünürlükte tipin kanıtlamak: daha iyi, daha çarpıcı olmak için sürekli çabalamak.",
          "S": "Görünürlükte tipin silinmek: paylaşmamak, fikir söylememek, görünmemek.",
          "T": "Görünürlükte tipin tetikte olmak: beğenileri ve yorumları sürekli kontrol etmek."},
}

ALAN_ADIM = {
    "I": {"U": "Bu hafta bir isteğe hemen evet deme; \"bakıp dönerim\" de ve on dakika sonra karar ver.",
          "K": "Bu hafta bir işi mesai saatinde bitir ve fazladan bir şey eklemeden teslim et.",
          "S": "Bu hafta bir toplantıda tek bir cümleyle fikrini söyle.",
          "T": "Bu hafta dönüt gelmeyen bir iş için senaryo kurmak yerine doğrudan sor: \"Nasıl buldun?\""},
    "A": {"U": "Bu hafta bir aile isteğine yarım evet de: \"Gelirim ama erken çıkarım.\"",
          "K": "Bu hafta ailene bir başarını değil, bir yorgunluğunu anlat.",
          "S": "Bu hafta ailene küçük bir tercihini söyle: ne yemek istediğin, ne zaman geleceğin.",
          "T": "Bu hafta aileden gelen bir söz takılınca yaz ve sor: \"Bu onun mu, benim mi?\""},
    "P": {"U": "Bu hafta partnerine bir kez \"ben bunu istemiyorum\" de; gerekçeyi uzatmadan.",
          "K": "Bu hafta partnerin için fazladan bir şey yapmadan, sadece birlikte otur.",
          "S": "Bu hafta küçük bir kırgınlığı aynı gün, tek cümleyle söyle.",
          "T": "Bu hafta partnerin sessizleşince tahmin etme; bir kez \"bir şey mi var?\" diye sor ve cevaba güven."},
    "C": {"U": "Bu hafta bir davete bahanesiz hayır de: \"Bu sefer gelemiyorum, sonrakine.\"",
          "K": "Bu hafta bir buluşmada organize eden sen olma; sadece katıl.",
          "S": "Bu hafta grupta bir kez \"ben şunu tercih ederim\" de.",
          "T": "Bu hafta bir buluşmadan sonra konuşmayı tekrar oynatmak yerine iyi geçen tek bir anı yaz."},
    "G": {"U": "Bu hafta çoğunluğa uymayan küçük bir görüşünü bir kez söyle.",
          "K": "Bu hafta \"yeterince iyi\" bir şeyi düzeltmeden paylaş.",
          "S": "Bu hafta hoşuna giden bir şeyi kimseye sormadan göster: bir fotoğraf, bir kıyafet, bir cümle.",
          "T": "Bu hafta bir paylaşımdan sonra 24 saat bildirimlere bakma."},
}

ORUNTU = {
    "kendini_silen_uyum": "Uyumlu ve silinen tiplerin birlikte çalışıyor: hem karşındakinin istediğini yapıyor hem de kendi isteğini hiç söylemiyorsun. Dışarıdan çok kolay biri gibi görünüyorsun; içeride ise kimsenin seni tanımadığı bir yalnızlık birikiyor. İlk adım küçük bir tercih söylemek.",
    "deger_ise_bagli": "Değer işe bağlı: kanıtlayan tipin en çok iş ve otorite alanında çalışıyor. Takdir geldiğinde yükseliyor, gelmediğinde çöküyorsun. İşin iyi olabilir; ama değerinin tek kaynağı iş olduğunda her dönüt bir hüküm gibi geliyor.",
    "secici": "Onay ihtiyacın genel değil, seçici: bir alanda kendindeyken diğerinde kayboluyorsun. Bu, sorunun senin karakterin değil, o alandaki ilişkilerin sende uyandırdığı bir şey olduğunu gösteriyor. En zayıf alanına bu gözle bak.",
    "aile_koku": "Ailenin kökü: en zayıf alanın aile. Onay ihtiyacı çoğu zaman burada başlar ve diğer ilişkilere buradan taşınır. Diğer alanlardaki küçük deneyler, ailede de zamanla yer açar; aileyle başlamak zorunda değilsin.",
    "iliskide_kaybolma": "İlişkide kaybolma: partner alanın düşük ve uyum ya da silinme tipin güçlü. İlişkiyi korumak için kendinden vazgeçiyorsun; ama kendinden vazgeçtiğin ilişkide sen de yoksun. Sınır Haritası bu alanı daha ayrıntılı gösterebilir.",
    "begeni_alarmi": "Beğeni alarmı: görünürlük alanın düşük ve tetikte tipin güçlü. Her paylaşım bir sınav, her bildirim bir sonuç gibi. Radarı kapatmanın en hızlı yolu, ona bakmayacağın saatleri belirlemek.",
    "surekli_tarama": "Sürekli tarama: tetikte tipin baskın ve neredeyse her alanda kendinden uzaklaşıyorsun. Zihin hiç dinlenmeyen bir nöbetçi gibi. Bu yorgunluk tek başına bile bir mesaj; nöbeti azaltmak için önce bir ilişkide tahmin yerine soru sormayı dene.",
    "yaygin": "Üç ya da daha çok alanda aynı anda kendinden uzaklaşmışsın. Bu ay ağır geçmiş olabilir. Hepsini birden değiştirmeye çalışma; en güçlü alanından başla, kas önce kolay yerde çalışır.",
}

PLAN_GIRIS = ("Üç hafta, her hafta tek alan. En güçlü alanından başlıyor, en zayıf alanına son hafta geliyorsun; "
              "ilk haftanın kolay deneyi, üçüncü haftanın zor deneyine güç verir.")
PLAN_KAPANIS = "Üç hafta sonra envanteri yeniden doldur; fark genellikle ilk ayda en zayıf alanında görünür."

DURUSTCE = [
    "Bu rapor bir koçluk aracı; psikolojik değerlendirme ya da tanı aracı değil. Onay ihtiyacı bir kişilik kusuru değil, öğrenilmiş bir korunma stratejisidir ve yeniden öğrenilebilir.",
    "Her uyum, onay ihtiyacı değildir. Bazen ortamı yumuşatmak, susmak ya da kabul etmek bilinçli ve doğru bir seçimdir. Buradaki soru, bunu seçerek mi yoksa kaçınamadığın için mi yaptığın.",
    "Bazı ilişkilerde kendi sesini kullanmak gerçekten risklidir. Bir ilişkide kendini fiziksel ya da duygusal olarak güvende hissetmiyorsan, bu raporun deneyleri o ilişki için değil; önce güvenliğin gelir.",
]
DURUSTCE_GENIS = ("Cevaplarında onay ihtiyacının ötesine işaret eden bir şey var: değersizlik duygusunun günlük hayatı zorlaştırması "
                  "ya da bir yakınının tepkisi karşısında kendi kararlarını veremez hâle gelmen. Bu bir onay meselesi olmayabilir, "
                  "bir güvenlik ya da yük meselesi olabilir. Böyle dönemlerde bir uzmanla konuşmak iyi gelebilir; bunu söylemek bu raporun görevi.")

SONRAKI = [
    ("Raporu birlikte okuyalım", "30 dakikalık görüşme. Raporda en çok rahatsız eden cümleyi konuşur, ilk hafta için tek bir deney seçeriz. WhatsApp'tan yaz, uygun saati bulalım."),
    ("Bireysel Koçluk", "Onay ihtiyacı çoğu zaman eski bir güvenlik stratejisidir; haftalık koçlukta bu stratejiyi birlikte tanır ve yerine yenisini kurarız. thetakapisi.com.tr/danismanlik"),
    ("Diğer envanterler", "Hayır demekte zorlanıyorsan Sınır Haritası, yakın ilişkide kayboluyorsan İlişki Mesafesi Haritası iyi bir sonraki adım. thetakapisi.com.tr/envanterler"),
]

# --- kişinin kendi cevapları ---
S_TIP_YORUM = {
    "U": ["Burada tipin uyum: karşındakinin isteği seninkinin önüne geçti.",
          "Burada ortamı yumuşatmak, kendi isteğini söylemekten daha güvenli geldi.",
          "Burada evet, hayırın bedelinden kaçmanın yolu oldu."],
    "K": ["Burada tipin kanıtlamak: görülmek için fazlasını yaptın.",
          "Burada değerin yaptığın şeye bağlandı; yetmemekten korktun.",
          "Burada onayı emekle satın almaya çalıştın."],
    "S": ["Burada tipin silinmek: sesini geri çektin.",
          "Burada görünmemek, onaylanmamaktan daha güvenli geldi.",
          "Burada kendi isteğini \"önemli değil\" diye küçülttün."],
    "T": ["Burada tipin tetikte olmak: karşı tarafı okumak, kendini duymanın önüne geçti.",
          "Burada radar çalıştı; bilgi gelmeyince boşluğu tahminle doldurdun.",
          "Burada tepkiyi çözmeye çalışmak seni yordu."],
    "TUTAR": ["Burada kendindesin: hem ilişkiyi hem kendini korudun. Bu cevabı hatırla; diğer alanlara taşınabilir.",
              "Burada sesini kullandın ve yerinde kaldın; tam olması gereken bu.",
              "Burada onay beklemeden kendi değerini bildin; bu kas sende var."],
}
S_TUTAN_GIRIS = "Aynı anın kendinde kalan hâli:"

Z_GIRIS = ("Sekiz ikilemde iki zor seçenek arasında seçim yaptın; doğru cevap yoktu. "
           "Onaya ihtiyaç duyduğunda hangi stratejiye kaydığın burada görünüyor: puan değil, refleks.")
Z_YORUM = {
    "U": "İkilemlerde en çok uyumu seçtin: ilişkiyi korumanın yolu, karşındakinin istediğini yapmak gibi geliyor.",
    "K": "İkilemlerde en çok kanıtlamayı seçtin: değerin, başardığın şeyle ölçülüyor.",
    "S": "İkilemlerde en çok silinmeyi seçtin: güvende kalmanın yolu, az yer kaplamak gibi geliyor.",
    "T": "İkilemlerde en çok tetikte olmayı seçtin: güvende kalmanın yolu, herkesi önceden okumak gibi geliyor.",
}
Z_DENGELI = "İkilemlerde tek bir stratejiye yığılmadın; tepkin ilişkiye ve duruma göre değişiyor."
Z_OZEL = {
    ("z2", "a"): "Değerli hissetmek için bir şey başarman gerekiyor. Bu, dinlenmeyi ve sıradan günleri zorlaştırır; değerin yaptığın şeyden önce de vardı.",
    ("z2", "b"): "Değerli hissetmek için kimsenin sana kızgın olmadığından emin olman gerekiyor. Bu, değerini başkalarının ruh hâline emanet etmek demek.",
    ("z3", "a"): "İnsanlar seni \"hayır demeyi bilmez\" diye biliyor. Bu bir sevilme biçimi, ama bedelini yalnız sen ödüyorsun.",
    ("z3", "b"): "İnsanlar seni \"her şeyi kusursuz yapar\" diye biliyor. Bu bir güç; yeter ki kusursuz olmadığın günlerde de kendini sevebil.",
    ("z5", "a"): "Biri kızgın görününce hemen gönlünü alıyorsun. Böylece onun duygusu senin görevin oluyor; oysa bazı kızgınlıklar sana ait değil.",
    ("z5", "b"): "Biri kızgın görününce nedenini bulana kadar rahat edemiyorsun. Bazen neden hiç senin bilebileceğin bir şey değildir.",
}

CUMLE_ALAN = {
    "I": "Beklediğin onay İş ve otorite alanına düşüyor.",
    "A": "Beklediğin onay Aile alanına düşüyor.",
    "P": "Beklediğin onay Partner ve yakın ilişki alanına düşüyor.",
    "C": "Beklediğin onay Arkadaşlık ve çevre alanına düşüyor.",
    "G": "Beklediğin onay Görünürlük alanına düşüyor.",
}
CUMLE_ALAN_UYUM = {
    True: "Bu alan haritanda zaten düşük; cümlen haritanı doğruluyor.",
    False: "İlginç olan şu: bu alan haritanda görece iyi. Demek ki genel bir eğilim değil, bu kişiye ya da bu duruma özel bir bağ var.",
}
CUMLE_TIP = {
    "U": "Cümlende \"{ipucu}\" geçiyor: bu bağın içinde birini kırmama, uyumu koruma isteği var.",
    "K": "Cümlende \"{ipucu}\" geçiyor: bu bağın içinde kendini kanıtlama isteği var.",
    "S": "Cümlende \"{ipucu}\" geçiyor: bu bağın içinde kendi sesini geri çekme eğilimi var.",
    "T": "Cümlende \"{ipucu}\" geçiyor: bu bağın içinde karşı tarafın tepkisini okuma yorgunluğu var.",
}
CUMLE_TIP_UYUM = {
    True: "Bu, haritandaki baskın tipinle aynı; cümlen tipini tarif ediyor.",
    False: "Bu, haritandaki baskın tipinden farklı; bu ilişkide başka bir strateji devreye giriyor. İkisini de tanı.",
}
CUMLE_BELIRSIZ = ("Cümlende kimin onayını beklediğin ya da neden tam okunmuyor; bu da bir bilgi. "
                  "Bazen en güçlü onay bağı, adı konmamış olandır. Önce ona bir ad ver: kim, ne istiyorsun?")
CUMLE_KARSI_GIRIS = "Bu bağ için deney ({no}):"
CUMLE_YARIN = "Bu hafta ilk adım: {eylem}"
CUMLE_KAPANIS = ("Bu bağı bir haftada çözmek zorunda değilsin. Ama bu hafta tek bir küçük cümleyi kendi adına söyle. "
                 "Onay beklemeden atılan ilk adım, en zor olanıdır.")

BASLATICI_UST = "DENEY · {no}"
BASLATICI_ILK = "İlk adım:"
BASLATICI_GERI = "Zorlanırsan:"
