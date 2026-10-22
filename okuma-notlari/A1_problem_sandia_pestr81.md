# A1 — Problem tanımı: Sandia/Siemens/EPRI boşluk analizi (2024) ve IEEE PES TR-81 (2020)

Bu notlar, yardımcı sinyal (auxiliary signal) tabanlı arıza tespiti projesi için hazırlandı. Projede evirici, optimize edilmiş küçük bir negatif-dizi akımı enjekte ediyor; böylece mesafe rölesi arızayı normal işletmeden küme-tabanlı (set-based) bir garantiyle ayırt edebiliyor. Notlar yalnızca iki raporun metnine ve şekillerine dayanıyor.

> **Sayfa numaraları:** Sandia raporunda basılı sayfa numarası PDF sayfa numarasıyla aynı. TR-81'de "s. N" raporun basılı (Arap rakamlı) sayfa numarasını gösteriyor. Baştaki i–vi sayfaları yüzünden **PDF sayfası = N + 6**.
> **"Şekilden okunmuştur"** ibaresi geçen sayılar metinde yazmıyor. Bunları grafikten göz kararı okudum, bu yüzden yaklaşık değerler.

---

## Mini sözlük (ilk kez okuyan için)

| Terim | Kısa açıklama |
|---|---|
| **IBR** (inverter-based resource) | Şebekeye güç elektroniğiyle bağlanan kaynak: PV, Tip III (çift beslemeli) ve Tip IV (tam dönüştürücülü) rüzgâr, batarya (BESS), STATCOM. |
| **GFL / GFM** | *Grid-following*: şebeke gerilimini PLL (faz kilitlemeli döngü) ile takip eder ve akım kaynağı gibi davranır. *Grid-forming*: kendi gerilim genliğini ve açısını üretir, gerilim kaynağı gibi davranır. Arızada ise akım sınırlayıcısı yüzünden "kısmen akım kaynağı" olur. |
| **FRT / LVRT / VRT** | Fault/low-voltage/voltage ride-through: arıza ve gerilim çökmesi sırasında şebekeye bağlı kalma zorunluluğu. |
| **Simetrik bileşenler** | Üç faz büyüklükleri pozitif (1), negatif (2) ve sıfır (0) dizi bileşenlerine ayrılır. Dengesiz arızalar negatif dizi (I2, V2) üretir. Toprak arızaları ayrıca sıfır dizi (I0, V0) üretir. Senkron makinede negatif dizi yaklaşık sabit bir endüktif reaktanstır, bu yüzden I2 ile V2 arasında yaklaşık 90°'lik "endüktif" bir açı ilişkisi oluşur. Klasik röleler bu ilişkiye güvenir. |
| **Mesafe rölesi (21, 21G)** | Gerilim/akım oranından görünür empedansı hesaplar ve R-X düzleminde mho (daire) ya da quad (dörtgen) bölgeyle karşılaştırır. Zone 1 anlıktır ve hattın bir kısmını kapsar. Zone 2 gecikmelidir ve hattın ötesine uzanır. 21G toprak mesafe elemanıdır. |
| **Overreach / underreach** | Röle ayarından uzaktaki (dış) arızada açarsa fazla erişim (overreach) olur ve güvenlik (*security*) kaybedilir. İç arızada açmazsa eksik erişim (underreach) ya da açmama olur ve güvenilirlik (*dependability*) kaybedilir. |
| **Yön elemanı (32/67), 67Q, 32GF/GR** | Arızanın ileri (hat tarafı) mı geri mi olduğuna karar verir. "Q" negatif dizi demektir: 67Q, I2'nin V2'ye göre açısına bakar. 32GF ve 32GR toprak arızası için ileri ve geri yön çıkışlarıdır. |
| **51Q** | Negatif-dizi ters-zamanlı aşırı akım elemanı. |
| **Polarizasyon** | Rölenin açı referansı olarak kullandığı büyüklük (ör. V2, I2, I0, pozitif-dizi bellek gerilimi). |
| **POTT, DCB, DTT, echo** | Haberleşmeli hat koruma şemaları. POTT izin sinyaliyle, DCB bloklama sinyaliyle çalışır. DTT karşı uca doğrudan açma komutu gönderir. Echo, zayıf uçtaki rölenin izin sinyalini geri yansıtmasıdır. |
| **LCD** | Line current differential: iki uçtaki akımları haberleşmeyle karşılaştıran hat diferansiyel koruması. |
| **PSB / OST** | Power swing blocking: güç salınımında mesafe rölesini bloke eder. Out-of-step tripping: senkron dışı salınımda açtırır. |
| **pu** | Per-unit, yani anma değerine oranlanmış büyüklük. |
| **EMT** | Electromagnetic transient: anlık dalga şekli düzeyinde simülasyon (PSCAD, EMTP, Simulink/Simscape). |

---

## Rapor 1: Sandia/Siemens/EPRI (2024), %100 evirici baskın sistemlerin korunması: boşluk analizi ve uzman görüşmeleri

- **Künye:** Ulrich Muenz, Siddharth Bhela, Nan Xue, Abhishek Banerjee (Siemens Technology); Matthew J. Reno, Daniel Kelly (Sandia National Laboratories); Evangelos Farantatos, Aboutaleb Haddadi, Deepak Ramasubramanian, Amin Banaie (EPRI).
  - Başlık: *"Protection of 100% Inverter-dominated Power Systems with Grid-Forming Inverters and Protection Relays – Gap Analysis and Expert Interviews"*.
  - Yayın: Sandia Report **SAND2024-04848**, Nisan 2024.
  - Uzunluk: **48 PDF sayfası**. Ana metin s. 9–35, kaynakça s. 37–43, 95 kaynak.
  - Destek: ARPA-E (DE-AR0001570). Rapor, ARPA-E'nin *PICo-Design: Protection-Inverter Co-Design for 100% Renewable Power Systems* projesinin parçası (s. 4, 9).
- **Tek cümlede:** GFM eviricilerin arıza davranışı ve klasik koruma rölelerinin bu davranışa tepkisi hakkında literatür neredeyse boş. Uzmanlar en çok etkilenecek fonksiyonların mesafe, yön ve güç salınımı koruması olduğunda hemfikir. Öncelikli ihtiyaç, eviricilerin öngörülebilir negatif-dizi akımı vermesi ve evirici kontrolüyle korumanın birlikte tasarlanması (co-design).

### Problem ve bağlam
- Koruma şemaları 50 yılı aşkın sürede, arıza akımının senkron generatörlerce belirlendiği varsayımıyla geliştirildi. Hawaii ve Teksas gibi sistemler evirici baskın hale geliyor (s. 3, 9).
- Bugün IBR'lerin çoğu GFL. Ancak IBR baskın bir sistemde belirgin bir GFM payı bulunması gerekiyor ve GFM'in arıza davranışı GFL'den çok farklı (s. 9).
- IEEE 2800-2022 GFL ile GFM'i ayırmıyor; aynı FRT kuralları ikisine de uygulanıyor (s. 11).
- Raporun iki ana sorusu var: (1) GFM'lerin FRT davranışı, (2) modern rölelerin GFM arıza akım ve gerilimlerine tepkisi. Giriş bölümünde ikisi için de yanlışlıkla "Section 1" yazıyor (s. 9). Doğrusu Bölüm 2 ve Bölüm 3.

### Yöntem / yaklaşım
- **Literatür taraması:** IEEE 2800 FRT kuralları, GFM akım sınırlama yöntemleri ve GFL/GFM'in korumaya etkisi.
- **Uzman görüşmeleri:** Bahar 2023'te inverter ve koruma üreticileri, danışmanlar, ulusal laboratuvarlar ve elektrik şirketleriyle yapıldı. Kurumlar arasında Electranix, EPC Power, Siemens PTI, Siemens Gamesa, Southern Company, Quanta, ETAP, GE, HickoryLedge, RTE, Dominion ve Hawaiian Electric var. Teşekkür listesinde 22 isim veya kurum geçiyor (s. 4).
- **Ölçüm özeti:** Sandia'nın daha önce yaptığı GFM donanım testlerinin özeti (Bölüm 2.3).
- Rapor yeni simülasyon ya da yeni analiz içermiyor; tamamen sentez niteliğinde.

### Ana bulgular

**A. IEEE 2800-2022 FRT kuralları (s. 11–13)**
- Gerilim-zaman ride-through eğrisi dört bölge tanımlıyor: Mandatory Operation, 30 dakika sürekli çalışma, süresiz sürekli çalışma ve Permissive Operation (Şekil 1, s. 12).
- Kuralların varsayılan uygulama noktası (RPA, reference point of applicability), ana IBR trafosunun yüksek gerilim tarafındaki ölçüm noktası (POM, point of measurement) (s. 11).
- **Dengesiz arızada:** IBR, pozitif-dizi reaktif akıma ek olarak terminal V2'ye bağlı bir **artımsal negatif-dizi akımı** basmalı. Bu akım V2 fazörünün **90°–100° önünde** olmalı. Tip III rüzgârda bu aralık 90°–150° (s. 12).
- **Akım sınırına ulaşılırsa:** Pozitif-dizi reaktif akım, negatif-dizi reaktif akım ya da ikisi birden azaltılabilir. Eşit azaltma tercih ediliyor. Ancak artımsal pozitif-dizi reaktif akım, artımsal negatif-dizi reaktif akımın **altına düşürülemez** (s. 12).
- **Standart I2'nin büyüklüğünü belirtmiyor** (s. 13).
- **Zamanlama:** Basamak cevabı (step response) Tip III dışındaki IBR'lerde **≤ 2,5 çevrim**. Yerleşme (settling) süresi Tip III dışında **≤ 4 çevrim**, Tip III'te ≤ 6 çevrim. Yerleşme bandı, istenen değişimin ±%10'u ya da maksimum akımın ±%2,5'i (s. 13).
- **Arıza sonrası:** Aktif güç toparlanma süresi varsayılan olarak 1 s ve 1–10 s arasında ayarlanabiliyor (s. 13).

**B. GFM akım sınırlama yöntemleri (s. 13–20, büyük ölçüde Fan ve ark. 2022 derlemesine [15] dayanıyor)**
- **İki ana FRT stratejisi var:**
  - (i) Arızada GFL'ye geçmek. Bu yol yedek PLL gerektirir ve arıza boyunca GFM özelliği kaybolur.
  - (ii) GFM'de kalıp akımı sınırlamak. Literatür daha çok bu yolu tercih ediyor (s. 13).
- **Gereksinimler:** Faz akımı sınırı tipik olarak 1,2–2 pu. Bunun yanında arıza akımı katkısı ve arızadan toparlanma yeteneği isteniyor (s. 14).
- **Akım sınırlayıcı (current limiter):** Üç türü var: anlık (instantaneous), genlik (magnitude) ve öncelikli (priority-based) (Şekil 3, s. 15).
  - Anlık sınırlayıcı abc ya da αβ çerçevesinde **sinüs olmayan** akım üretir ve muhafazakâr sınır gerektirebilir; [22]'de bu sınır 2 pu (s. 16).
  - Öncelikli sınırlayıcı, akım açısını kullanıcı tanımlı bir φ_I değerine sabitleyebilir. Böylece IEEE 2800'ün aktif/reaktif öncelik kuralı uygulanabilir (s. 15).
  - Sorunlar: açı kayması, gerilim kontrolcülerinde wind-up, toparlanamama ve LC filtre rezonansını uyarma (s. 16).
- **Sanal empedans (virtual impedance, VI):** Wind-up yapmaz ve kendiliğinden toparlanır. Ancak gerilim döngüsünün bant genişliği düşük olduğundan **ilk çevrimlerde akımı sınırlayamaz** (s. 16–17).
  - Sabit VI simetrik arızada işe yarar, **asimetrik arızada başarısız olur**. Uyarlamalı (adaptive) VI tüm arıza tiplerinde çalışır (s. 18).
  - Düşük X/R ile daha az salınım olur, ama akım çoğunlukla aktif kalır ve gerilim desteği zayıflar. Büyük VI kararsızlık riskini artırır (s. 18).
  - **Önemli nokta:** VI kullanıldığında dizi akımlarının açısı VI'nın genliği ve açısıyla, arıza direnci ve hat empedansıyla belirlenir (s. 18). Yani rölenin göreceği I2 açısı kontrol tasarımına bağlı.
- **Gerilim sınırlayıcı:** Kalıcı rejimde iyidir. Ama sinüs olmayan akım üretir, wind-up yapar ve ilk çevrimlerde geçici aşırı akım görülür (s. 18–19).
- **Hibrit yöntemler:** Örneğin [13] geçici rejimde akım doyumunu, kalıcı rejimde VI'yı kullanıyor (s. 19).
- Karşılaştırma Tablo 1'de (s. 20).

**C. Şebeke kodlarına uyan GFM FRT çalışmaları (s. 20–21)**
- **Nasr & Hooshyar [13]:** IEEE 2800'ün negatif-dizi kuralını karşılıyor. Negatif dizide salt reaktif bir akım kaynağı gibi davranırken pozitif dizide GFM gerilim-kaynağı davranışını koruyor. Evirici kapasitesini I1 ve I2 arasında uyarlamalı olarak paylaştırıyor.
- **Rosso ve ark. [4]:** NGESO (Büyük Britanya şebeke işletmecisi) kodunu karşılıyor. Dizi-akımı sınırlamalı varyantı "daha dengeli akım" üretiyor ve rapor bunu **koruma açısından istenmeyen** buluyor. Ayrıca I2 doğrudan regüle edilmediği için **endüktif olması garanti değil**; bu da negatif-dizi elemanlarını tehlikeye atıyor.
- **Piya ve ark. [36]:** Danimarka ve Almanya kodlarına uyuyor, ancak gerilim-kaynağı davranışı muhtemelen kayboluyor.
- **Dadjo ve ark. [51]:** Mevcut kodları karşılamıyor ve koruma güvenilirliğini garanti etmiyor.

**D. Uzman görüşmesi, evirici tarafı (s. 21–23)**
- **Negatif dizi:** Tüm uzmanlar, IBR'lerin (sadece GFM değil) arızada negatif-dizi akımı vermesi gerektiğinde hemfikir. Bugünkü GFL'lerin çoğu yalnızca pozitif dizi veriyor.
- **Sıfır dizi:** İletimde sorun değil, çünkü Δ-Y trafolar bu akımı sağlıyor (s. 22).
- **Aşırı akım koruması:** IBR'ler aşırı-akım rölelerini çalıştıracak kadar akım veremiyor. Bazı uzmanlara göre limitte çalışmayan birden çok GFM toplamda yüksek akım verebilir (s. 22).
- **Açma sırası:** IBR'ler hızlı oldukları için genelde korumadan **önce** açıyor (s. 22).
- **Doyumdaki GFM davranışı:** İlk birkaç çevrimde donanım limiti ve anahtarların hızlı açılması **bozuk dalga şekli** üretiyor. Ardından yazılım kontrolü akımı sinüse döndürüyor. Doyumda çoğu GFM **en fazla 1,1–1,2 pu** veriyor (s. 22).
- **Beklentiler:** Klasik rölelerin çalışması için akım ve gerilim sinüs olmalı. İlk birkaç çevrimde donanımsal bloklama kabul edilebilir. GFM, arıza akımının faz açısını kontrol etmeli (s. 22).
- **Mod değiştirme:** Çoğu uzmana göre GFM'den GFL'ye geçişten kaçınılmalı. Bu geçiş salınım ve "chattering" (modlar arası gidip gelme) riski taşıyor (s. 22–23).
- **I1/I2 oranı:** **I1/I2 oranı işletme koşuluna göre ayarlanabilir olmalı.** Bir üretici bu özelliğin ürününde bulunduğunu teyit etmiş (s. 23).
- **Sıfır dizi kaynağı:** GFM'in I0 vermesi mümkün, ama ek donanım ve maliyet gerektiriyor. Trafodan sağlanması tercih ediliyor (s. 23).

**E. Ölçümler (s. 23–25)**
- **Test yöntemi:** PHIL (power hardware-in-the-loop) karmaşık bulunduğu için testler büyük yük bankalarıyla yapılmış. Örneğin 100 kVA GFM'in A fazına 500 kW yük bağlamak tek faz-toprak arızasına benziyor (s. 23–24).
- **[52], iki tek-fazlı 120/240 V off-grid GFM:** Arızada **kare dalga** akım veriyorlar. RMS akım birinde **2,25 pu**, diğerinde **1,3 pu**. Yük dirençsel olduğundan akım gerilimle aynı fazda (Şekil 6, s. 24).
- **[53], üç-fazlı GFM'ler:**
  - Birincisi üç tek-fazlı eviriciden (master/slave) oluşuyor ve A fazına 6 pu yük bağlanarak test edilmiş. **Trafo olmadan doğrudan I0 basabiliyor** ve I1 = I2 = I0 (kare dalga).
  - İkincisi yüksek empedanslı faz-faz arızada sinüs I1 ve I2 veriyor (I1 = I2). I0 veremiyor ama Δ-Y trafo üzerinden bağlı (Şekil 7, s. 24–25).
- **[54]:** Modeller donanım testleriyle çok iyi örtüşüyor (Şekil 8, s. 25).
- **[55]:** Faz açısı sıçramasında GFM büyük akım çekiyor ve **10 çevrim içinde** kararlı hale geliyor (s. 25).

**F. Korumaya etki, literatür (s. 27–30)**
- GFM'in korumaya etkisi mikroşebekeler dışında büyük ölçüde incelenmemiş (s. 27).
- **En ilgili çalışma: Baeckeland ve ark. [58]**
  - **Kurulum:** GFM'e bağlı hattı koruyan mesafe rölesi, B-C (faz-faz) arızası ve üç kontrolcü:
    - M1: dq çerçevesi, yalnız pozitif-dizi akım kontrolü ve akım sınırlayıcı.
    - M2: αβ çerçevesi ve akım sınırlayıcı.
    - M3: αβ çerçevesi ve sanal empedans.
  - M2 ve M3 kontrolsüz bir I2 akışına izin veriyor (s. 27).
  - **M1 ve M2 ile röle hatalı çalışıyor:** İç arızada empedans **4. bölgede** görünüyor, dış arızada ise Zone 1'de görünüyor, yani **overreach** oluyor.
  - **M3 ile empedans küçük hatayla ölçülüyor.** Gerekçe olarak VI'nın X/R oranının hat X/R'siyle eşleşmesi gösteriliyor (s. 27).
  - **Rapordaki eleştiriler:** Sadece simülasyon var, analiz yok. Tek arıza tipi kullanılmış ve arıza direnci bilinmiyor. IEEE 2800 uyumlu I2 kontrolü denenmemiş. Röle basit görünür-empedans modeli. Duyarlılık analizi yok (s. 27).
- **[59]:** 46 kV alt-iletimde ters-zamanlı aşırı akım, mesafe ve yön elemanlarında "büyük zorluk yok". Ancak GFM akımı çok bozuk, sinüs dışı (s. 27).
- **Tablo 2 (s. 28–29), GFL beklentileri:**
  - PSB/OST hatası.
  - Negatif-dizi aşırı akım (I2 küçük olduğundan) ve yön elemanı (I2 açısı alışılmadık olduğundan) hataları.
  - Faz seçimi (phase selection) hatası.
  - POTT, PUTT, DCB ve DCUB'de yön elemanının başarısız olması.
  - Mesafe: denetim akımının (supervising current) yetersiz kalması ve mho dairesinin öngörülemez dinamik genişlemesi.
  - Bellek-polarizeli sıfır-dizi yön elemanı hatası.
  - Alpha-plane LCD'nin hata yapma eğilimi (eğimli LCD bağışık görünüyor).
  - Yürüyen dalga (traveling wave) korumasında evirici kontrolü yeterince hızlı olmadığından etki yok.
- **Tablo 2'nin GFM sütunu:** Mesafe dışında hemen hepsi **"No literature found"**. Mesafe için: akım sınırlayıcılı GFM under/overreach yaratabiliyor, sanal empedanslı GFM ise doğru çalışmayı sağlayabiliyor [58, 85].
- **Tablo 3 (s. 29–30):** FRT gereksinimlerinin korumaya etkisi. Negatif-dizi enjeksiyonu empedans, aşırı akım, yön, faz seçimi ve haberleşmeli korumayı etkiliyor. **I2'nin artması I1'i azaltabilir** ve yüksek IBR payında bunun tam etkisi bilinmiyor (s. 30).

**G. Uzman görüşmesi, koruma tarafı (s. 31–34)**
- **Etkiler:** GFM üreticilerinin kontrolleri tescilli (proprietary) olduğu için arıza davranışları farklı.
  - **Mesafe korumasının faz seçimi ciddi biçimde etkilenebilir.**
  - **Sinüs dışı akımlar RMS-tabanlı korumayı etkiler.**
  - Bir şirket çözüm olarak DCB, tam fiber diferansiyel ya da POTT kullanıyor (s. 31).
- **Sahadan hatalar:** Raporlananların çoğu GFL kaynaklı.
  - **Faz-faz arızaları, özellikle yön elemanlarında hatalı çalışmaya yol açabiliyor.**
  - Arızaların çoğu tek faz-toprak olduğundan, trafonun sağladığı I0 hataların çoğunu önlüyor.
  - Fırtınalı gecelerde IBR'ler korumadan önce açıyor.
  - Odessa (TX, 2021) olayı örnek gösteriliyor (s. 31–32).
- **Arıza sonrası:** Fabrika kabul testinde (FAT) gerilim toparlanma sorunları görülüyor. Akım sınırlama modundan çıkışta salınımlar oluşuyor (s. 32).
- **"Evirici mi uyum sağlasın, koruma mı?":** Her iki taraf da değişmeli; donanım aşırı tasarımından kaçınmak için evirici kontrolü ve koruma **birlikte tasarlanmalı**. Uzmanlar örnek olarak **15–30 çevrim boyunca 1,5 pu** akım ve **öngörülebilir negatif-dizi akımı** istiyor (s. 32).
- **Uyarlamalı koruma:** Haberleşme yükü nedeniyle tercih edilmiyor. **Bir şirketin tercihi, tüm işletme koşullarını kapsayan tek bir ayar** (s. 32).
- **Yük tecavüzü (load encroachment):** Ağır yük empedansının mesafe bölgesine girmesi. Görüşler karışık ve sonuçsuz.
  - Bazı uzmanlar "mesafe koruması akımdan bağımsızdır" diyor.
  - Bazıları ise büyük asenkron motor ve trafo ani akımlarının (inrush) yüksek "normal" akımlar yaratacağını ve arıza akımı düşük olduğu için yanlış açmaların artacağını düşünüyor (s. 33).
- **Güç salınımı:** Görüşülen 4 şirketin hiçbiri generatör koruması dışında OOS/PSB kullanmıyor. Bir sahada **frekansa agresif tepki veren bir BESS'in hızlı rampası güç salınımı rölesinin hattı yanlışlıkla açmasına** yol açmış (s. 33).
- **Modeller:** EMT (PSCAD) şart ama yavaş. Uzmanlar fazör araçlarında (Aspen, PSS/CAPE) doğru GFM modelleri ve PSCAD'de ticari röle kütüphaneleri istiyor. Ko-simülasyon konusunda görüşler karışık (s. 33–34).

**H. Sonuç (s. 35), neredeyse hiç bilgi olmayan alanlar:**
- (a) GFM arıza akımı ölçümleri.
- (b) Röle odaklı GFM FRT stratejileri.
- (c) IBR baskın sistemde doğru çalışan röle fonksiyonları.
- (d) GFM-GFL etkileşimi.
- (e) Doğru GFM ve röle modelleri.
- (f) Araçlar.
- (g) Standartlara girdi.

### Varsayımlar ve sınırlamalar
- **Nicel kanıt yok:** Yeni simülasyon, analiz ya da veri içermiyor. Uzman görüşleri anonim ve nitel. Kaç uzmanın neye katıldığı sayılmamış. 5 görüşme Siemens içinde gizlilik sözleşmesi (NDA) altında yapılmış ve paylaşılamayan bilgiler çıkarılmış (s. 21, 31).
- **Tutarsız sayılar:** Bölüm 2.2'de "toplam 18 uzman… 22 görüşmenin 5'i" yazıyor (s. 21). Bölüm 3.2'de "toplam 22 uzman… 18 görüşmenin 5'i" yazıyor (s. 31). Teşekkür listesinde 22 giriş var. Kesin sayı belirsiz.
- **Kaynakça şişkin:** Aynı EPRI raporları birden çok numarayla geçiyor: [61]=[65]=[82], [63]=[76], [66]=[83], [67]=[84]. "Kaynak [73]–[84]" gibi aralıklar olduğundan geniş görünüyor.
- **Ölçümler iletim ölçeğini temsil etmiyor:** Cihazlar küçük (100 kVA, 120/240 V off-grid). Arıza yerine **dirençsel yük bankası** kullanılmış; bu yüzden endüktif arıza yolu ve iletimdeki akım-gerilim açı ilişkisi yok. Ölçülen dalga şekilleri bir röleye uygulanmamış.
- **Asimetrik arızalar zayıf kalmış:** Akım sınırlama taraması büyük ölçüde **simetrik bozuculara** odaklanan tek bir derlemeye [15] dayanıyor. Oysa projemizin odağı negatif dizi, yani asimetrik arızalar.
- **Ölçüt yok:** "Koruma dostu" bir GFM davranışı için nicel bir ölçüt önerilmiyor. 1,5 pu / 15–30 çevrim yalnızca bir uzman görüşü.
- **Kapsam:** Başlıkta "%100 IBR" geçiyor, ama mikroşebeke ve HVDC'ye bağlı açık deniz rüzgâr sistemleri ayrıca ele alınmıyor. GFM'in farklı türleri (droop, VSM vb.) birbirinden ayrılmıyor.
- **Tarih:** Literatür taraması Bahar 2023 itibarıyla. Tablo 2'deki "No literature found" girişleri 2026'da güncelliğini yitirmiş olabilir.

### Projeyle bağlantı
- **WP1 (CVXPY tasarım aracı):**
  - **Kısıtlar:** IEEE 2800 kuralları doğrudan kısıt adayıdır.
    - I2 açısı V2'nin 90°–100° önünde olmalı. Bu, açı aralığı kısıtı ya da sabit açıda doğrusal parametreleme olarak yazılabilir.
    - "Artımsal I1 reaktif ≥ artımsal I2 reaktif" doğrusal bir eşitsizliktir.
    - Faz akımı ≤ I_max bir SOC (ikinci-derece koni) kısıtıdır.
  - **I_max için gerçekçi aralık:** Muhafazakâr değer 1,1–1,2 pu (uzmanlar, s. 22). Literatür 1,2–2 pu (s. 14) veriyor.
  - Nasr & Hooshyar'ın I1/I2 kapasite paylaşımı [13], optimizasyonun yapacağı işin sezgisel bir versiyonu.
  - Öncelikli sınırlayıcının açı parametresi φ_I, komutlanan bir I2 açısının fiziksel olarak uygulanabileceğini gösteriyor.
- **WP2 (EMT):**
  - Evirici modelinde akım sınırlayıcı türü (anlık, genlik, öncelikli, VI, gerilim sınırlayıcı, hibrit) **seçilebilir parametre** olmalı, çünkü I2'nin açısını ve dalga bozulmasını bu belirliyor (s. 16–18, 27).
  - Baeckeland'ın M1/M2/M3 senaryoları hazır bir test matrisi sunuyor.
  - Kare dalga akımlar (2,25 pu RMS, s. 24) ve 10 çevrimlik faz sıçraması cevabı (s. 25), "normal ama zorlayıcı" olay olarak modellenmeli.
  - Uzmanlar PSCAD'de iyi röle modeli bulunmadığını söylüyor (s. 33). Projenin kendi röle modelleri (21, 67Q vb.) başlı başına bir katkı olabilir.
- **WP3 (röle tarafı tespit):**
  - Klasik mesafe rölesinin GFM ile 4. bölgede empedans ve overreach üretmesi [58], WP3'ün "klasik eleman" referans çizgisi (baseline) için motivasyon.
  - **Yük tecavüzü tartışması, yardımcı sinyalin çözmeyi hedeflediği "arıza mı normal mi" sorusunun ta kendisi** (s. 33).
  - RMS-tabanlı şemaların sinüs dışı akımdan etkilenmesi (s. 31), Kalman filtresi ve öğrenen dedektörlerin bozuk dalga şekilleriyle test edilmesi gerektiğini gösteriyor.
- **WP4 (gömülü gecikme):**
  - İlk birkaç çevrimdeki donanım kaynaklı bozulma (s. 22) ve VI'nın ilk çevrimlerde akımı sınırlayamaması (s. 17), **bir çevrimlik (~16 ms) bütçenin tam da en bozuk zaman penceresine düştüğü** anlamına geliyor.
  - IEEE 2800'ün ≤ 2,5 çevrimlik basamak cevabı (s. 13), eviricinin arızaya "komutlu" tepkisinin röle bütçesinden yavaş olabileceğini gösteriyor.

### Buradan çıkan açık sorular / araştırma fikirleri
1. **[EN UMUT VERİCİ] Normal olay ve arıza ayrım test seti.** Uzmanların ayrıştığı yük tecavüzü sorusunu (s. 33) doğrudan test et.
   - Normal olaylar: ağır yük, asenkron motor ani akımı, trafo enerjilendirme, kondansatör anahtarlama (s. 33), BESS hızlı rampası (s. 33), faz sıçraması (s. 25).
   - Bunlara karşı düşük akımlı ve yüksek dirençli arızalar kullan.
   - Klasik 21 elemanı ile yardımcı sinyal dedektörünün yanlış alarm ve kaçırma oranlarını karşılaştır.
   - Hipotez: Küme-tabanlı tasarım, klasik mho'nun karıştırdığı olayları ayırır.
2. **[UMUT VERİCİ] Akım sınırlayıcı türüne dayanıklılık.**
   - M1/M2/M3 ve farklı VI X/R değerleri altında aynı yardımcı sinyal tasarımı garantisini koruyor mu?
   - Tasarımda belirsizlik kümesine "sınırlayıcı modu" boyutunu ekle ve garantinin hangi modda bozulduğunu ölç.
   - Yan hipotez: Hatla eşleşen X/R'li VI (M3) yardımcı sinyal tespitini de kolaylaştırır.
3. **[UMUT VERİCİ] Kare dalga ve bozuk akımda fazör kestirimi.**
   - Tam çevrim DFT, yarım çevrim DFT ve harmonikli durum vektörlü Kalman filtresi, %X THD ile bozulmuş I2 kestiriminde nasıl davranıyor?
   - Kestirim hatası ile gecikme arasındaki ödünleşimi WP4 kartında ölç.
4. **Çok-evirici ortak tasarım.** Limitte çalışmayan GFM'ler toplamda daha fazla akım verebiliyor (s. 22, 32).
   - Birden çok eviricinin I2 sinyalini CVXPY'de ortak karar değişkeni olarak tasarla.
   - Evirici başına genliğin ne kadar düştüğünü ölç.
5. **Tek ayar ile tüm koşullar.** Şirketlerin tercihi tüm koşulları kapsayan tek ayar (s. 32). Yardımcı sinyal tasarımının belirsizlik kümesi ne kadar büyütülebilir, ne zaman olurlu (feasible) olmaktan çıkar?
   - Ödünleşim eğrisini çiz: sinyal genliği ile kapsanan işletme kümesinin boyu.
6. **Arıza sonrası etki.** Sürekli enjekte edilen bir I2 sinyali, GFM'in arıza sonrası yeniden senkronizasyonunu ya da akım sınırlamadan çıkış salınımlarını (s. 32) kötüleştiriyor mu? EMT'de A/B testi yap.
7. **IEEE 2800 uyumu.** "I1 reaktif ≥ I2 reaktif" ve "eşit azaltma tercihi" kuralları yardımcı sinyalle çelişiyor mu? Sinyal bu kuralların içinde kalarak hâlâ ayırt edici olabiliyor mu? Bu bir CVXPY olurluluk deneyi.

### Kilit şekil / tablo / denklemler
- **Şekil 1 (s. 12):** IEEE 2800 VRT eğrisi ve işletme bölgeleri.
- **IEEE 2800 madde listesi (s. 12–13):** I2 açısı 90°–100°, sınırda azaltma kuralları, 2,5 / 4 / 6 çevrim zamanlama değerleri.
- **Şekil 2 (s. 14):** GFM kontrol mimarisi ve sınırlayıcıların yerleşimi. İç döngü, dış döngü, VI ve gerilim sınırlayıcı blokları gösteriliyor.
- **Şekil 3 (s. 15):** Anlık, genlik ve öncelikli akım sınırlayıcı geometrisi (dq düzleminde kare ya da daire).
- **Şekil 4–5 (s. 17–18):** VI ve gerilim sınırlayıcının eşdeğer devreleri.
- **Tablo 1 (s. 20):** Sınırlama yöntemlerinin karşılaştırması.
- **Şekil 6–8 (s. 24–25):** GFM donanım arıza testleri (kare dalga, sequence akımları) ve model doğrulaması.
- **Tablo 2 (s. 28–29) ve Tablo 3 (s. 29–30):** Korumaya etki haritası. Proje literatür taramasının iskeleti olarak kullanılabilir.
- **Bölüm 4 madde listesi (s. 35):** Boşluk listesi.

---

## Rapor 2: IEEE PES PSRC WG C32 (TR-81, 2020), IBR'lerin iletim sistemine bağlanmasında koruma sorunları ve uygulamaları

- **Künye:** IEEE Power System Relaying and Control Committee (PSRC), System Protection Subcommittee, **Working Group C32** raporu.
  - Başlık: *"Protection Challenges and Practices for Interconnecting Inverter Based Resources to Utility Transmission Systems"*. Sayfa üst bilgisinde: *"Impact of Inverter Based Resources on Utility Transmission System Protection"*.
  - Yönetim: Başkan Mukesh Nagpal, Başkan Yardımcısı Mike Jensen, Sekreter Michael Higginson.
  - Üyeler: ~30 kişi; AEP, SEL, EPRI, Hydro-Québec, Duke, TVA, Southern, U. Toronto, Clemson ve başka kurumlardan.
  - Uzunluk: **70 PDF sayfası** (i–vi ve 1–64).
  - Rapor numarası ve tarih belgenin içinde yazmıyor. Dosya adı "2020_PES_TR81". Sandia raporu da bu belgeye "PES-TR-81, IEEE, July 2020" diye atıf yapıyor (Sandia ref. [75], s. 42).
- **Tek cümlede:** Gerçek saha kayıtları ve birkaç simülasyon gösteriyor ki IBR'lerin düşük, kontrollü ve üreticiye özgü arıza akımı (özellikle eksik ya da endüktif olmayan negatif-dizi akımı ve arızadan ~2 çevrim sonra akımı kesen kontrol modları) klasik mesafe, yön ve negatif-dizi elemanlarını ve güç salınımı korumasını yanıltıyor. Rapor çözüm olarak sıfır-dizi tabanlı toprak koruması, LCD, DTT ve gerilim düşüklüğü yedeği öneriyor; ayrıca I2'nin V2 ile orantılı enjekte edilmesini (eğim k = 2–6) zorunlu kılan bir şebeke kodu öneriyor.

### Problem ve bağlam
- **Senkron kaynak:** Arıza akımı yüksek ve kontrolsüz; kaynağın elektriksel parametreleri ve arıza yolunun empedansıyla belirleniyor.
- **IBR:** Arıza akımı **düşük, yüksek derecede kontrollü ve üreticiye özgü** (s. 2). Ana kontrol hedefi, güç elektroniğinin termal sınırı içinde kalırken şebeke kodunu karşılamak. Sonuç: IBR'nin kısa devre karakteristiği "düşük genlikli ve evrensel olmayan" bir karakteristik (s. 2).
- **Neden bozuluyor:** Klasik şemalar arıza akımının yüksek ve endüktif olmasına dayanıyor. Bu yüzden bazı dış arızalarda yanlış açabilir, bazı iç arızalarda açmayabilir. Hava koşulları da IBR çıkışını değiştirerek güvenilirliği etkiliyor (s. 2).
- **Kapsam:** İletim ve alt-iletimde bağlantı noktası (POI) sorunları. Dağıtım ve mikroşebeke kapsam dışı (s. 2). IEEE C37.246-2017'de anlatılanların üzerine gelen IBR'ye özgü sorunlara odaklanıyor (s. 3).
- **Referans topoloji:** Şekil 4'teki (s. 3) genel bağlantı topolojisi (CB1–CB10, güneş ve rüzgâr santralleri, iki klasik santral CG1/CG2) tüm rapor boyunca kullanılıyor.
- **Kontenjans riski:** Güçlü bara tarafındaki röleler bile risk altında. Örneğin CG2 devre dışıyken CB5, CG1 devre dışıyken CB7 neredeyse yalnızca IBR akımıyla çalışmak zorunda kalıyor (s. 5).

### Yöntem / yaklaşım
- Bu bir çalışma grubu raporu. Her vakada "sistem tanımı → kayıt/analiz → çıkarılan ders" sırası izleniyor.
- **Saha kayıtları:** Röle osilografları, 60 Hz bant geçiren filtreden geçirilmiş ve **çevrim başına 4 örnekle** saklanmış fazörler (s. 4, 39).
- **Simülasyonlar:** EMTP-RV ile bir Kuzey Amerika sistemi (detaylar EPRI raporunda, ref. [20]) ve IEEE PSRC D6 test sistemi.
- Yeni bir algoritma önerilmiyor. Öneriler mevcut çok-fonksiyonlu röle özellikleriyle sınırlı (s. 2).

### Ana bulgular

**A. Giriş vakası, Şekil 5 (s. 4–5)**
- **Sistem:** 138 kV kısa hat, 100 MW Tip IV rüzgâr santrali, iç A-C (faz-faz) arızası. Santral arızadan önce anma gücünde ve birim güç faktöründe ihraç ediyormuş.
- **Şebeke tarafı (CB4):** Faz akımı 420 A'den **6000 A'in üzerine** çıkmış. Zone 1 **3 çevrim içinde** doğru açmış.
- **IBR tarafı (CB2):** Akım arızada **hiç artmamış**. ~2 çevrim sonra hızla düşmeye başlamış ve 3. çevrimin sonunda **neredeyse sıfıra** inmiş. Röle hiç tepki vermemiş.
- **Neden:** Koruma mühendisi santralin kontrol modunu bilmiyormuş (s. 5).

**B. Şebeke kodu (s. 5–10)**
- **LVRT:** Örnek olarak Alman kodu kullanılıyor (Şekil 6). LVRT nedeniyle dış arızada istenmeyen bir açma generatörü kopararak kodu ihlal ediyor (s. 5–6).
- **Pozitif-dizi reaktif akım (Şekil 7, s. 6):** Arıza tipinden bağımsız olarak gerilim düşüşüne bağlı enjeksiyon.
- **Negatif-dizi (s. 7):**
  - Negatif-dizi elemanları sıfır-dizi karşılıklı kuplajdan (mutual coupling) etkilenmez ve yüksek dirençli toprak arızasında duyarlıdır; bu yüzden yaygınlar.
  - Yazıldığı tarihte I2 enjeksiyonu isteyen tek kod **VDE-AR-N 4130 (Almanya)**. Üreticiler I2'yi **bastırıyor**.
  - **Öneri (Şekil 8):** I2 reaktif akımı V2 dengesizliğiyle orantılı olsun, eğim k. **k = 2–6** seçildiğinde IBR yaklaşık **j1/k pu** negatif-dizi reaktansı taklit eder. Karşılaştırma için senkron generatörün negatif-dizi reaktansı tipik olarak **j0,12–j0,4 pu**.
  - Uyarı: Nihai I2 akım sınırlayıcısına bağlı. Eviricinin V2'yi ölçüp tepki vermesi **1–2 çevrim** (ya da kodun izin verdiği maksimum süre) sürüyor ve bu geçici rejim yüksek hızlı korumayı bozabilir (s. 7).
- **Akım bütçesi örneği (s. 8, Şekil 9):**
  - **Senkron generatör:** 100 MVA, X'' = %15, trafo %10. Trafoya yakın faz-faz arızada **~%50 V2** ve **~%200 I2** veriyor (yük akımından bağımsız).
  - **IBR:** 100 MVA, akım sınırı **%120**. %100 yük akımını korurken yalnızca **~%20 I2** verebiliyor. Yük akımı taşımak zorunda değilse **~%60** verebiliyor.
  - **Sebep:** Yük, I1 reaktif ve I2 reaktif akımlarının vektör toplamı akım sınırını aşamaz.
  - Şekil 9'dan okunan (benim çıkarımım): Yüksüz durumda B fazı %120'de, A ve C fazları %60'ta. Bu, I1 reaktif ve I2'nin eşit büyüklükte (~%60) varsayıldığını düşündürüyor. **Rapor bu varsayımları açıkça yazmıyor.**
- **Sıfır dizi (s. 9):** IBR'ler topraklı değil; bu yüzden I0 kuralı yok.
- **Frekans ride-through (s. 9):** Kuzey Amerika bölgelerinin gereksinimleri Şekil 10'da. Québec, IBR'lerin 66 Hz yerine 61,7 Hz üzerinde anında açmasına izin veriyor. Güney Kaliforniya'da ~1200 MW PV yanlış frekans algılaması nedeniyle çıkışını kesmiş ya da açmış (s. 9).

**C. IBR arıza akımının genel karakteristiği (s. 10–15)**
- **Basit model yetmez:** IBR'yi "Thévenin empedansı arkasında sabit gerilim" ya da "sabit akım kaynağı" olarak modellemek uygun değil (s. 10). Şekil 11'deki basit dizi eşdeğeri yalnızca kalıcı rejim arıza seviyesi hesabı için uygun (s. 10).
- **CSC ve DSC (s. 11):**
  - Coupled sequence control (CSC): Mevcut tam dönüştürücülü tasarımların çoğu her koşulda **yalnızca I1** basıyor.
  - Decoupled sequence control (DSC): I1 ve I2'yi bağımsız kontrol ediyor. Bu modda I2, V2'nin **90° önünde** olur.
- **Kalıntı gerilime bağımlılık:** Arıza akımı kalıntı gerilimin doğrusal olmayan bir fonksiyonu (s. 11).
  - Gerilim > %90 ise arıza sayılmıyor.
  - Gerilim < %20 ise çoğu IBR akım basmayı kesebiliyor (s. 11).
  - Tip IV ve Tip III için maksimum ve minimum akım zarfları Şekil 12–13'te (s. 12), "hemen sonra" ve "~3 çevrim sonra" olarak veriliyor. Şekil 12'den okunan: Tip IV'te hemen sonra üst zarf ~2,3 pu, 3 çevrim sonra ~1,2–1,5 pu.
- **Ön koşul bağımlılığı:** Arıza akımı ön-arıza koşullarına göre **0 ile anma akımı arasında** değişebiliyor (s. 13).
- **Zaman pencereleri (s. 13):**
  - IBR arızayı algılamadan önce (1–2 çevrim): Akım 1,1–2,0 pu aralığına çıkıyor, öncesinde kısa bir sıçrama olabiliyor.
  - IBR arızayı algıladıktan sonra: Akımı kontrol mantığı belirliyor.
  - Adalanabilen sistemlerde (BESS) bazı şartnameler 5–10 s boyunca 2–3× anma akımı istiyor (s. 13).
- **Tip III özel durumu (s. 13–14):** Crowbar devresi nedeniyle üç ayrı arıza şiddeti rejimi var. Akımda temel frekans dışı bileşenler oluşabiliyor.
- **Dengeli akım eğilimi (s. 14):** IBR'ler dengesiz arızada bile **dengeli akım tutmaya** çalışıyor. Bu, simetrik bileşen analizinin dizilerin ayrık olduğu varsayımını bozuyor.
- **Mho genişlemesi (s. 15–16):**
  - Pozitif-dizi bellek polarizeli mho, kaynak empedansıyla orantılı genişler (Şekil 14).
  - Düşük akımlı IBR, rölenin arkasında yüksek empedanslı bir kaynak gibi görünür ve daireyi çok genişletir.
  - Kaynak empedansı kontrole bağlı olduğundan genişleme **R-X düzleminin herhangi bir yerine** gidebilir. Sonuç over- ya da underreach olabilir.
  - Ayrıca mesafe rölesi bir **minimum faz akımı denetimi** (supervision) altında çalışır. IBR akımı röle çalışmadan önce bu eşiğin altına düşerse röle açmaz.
- **Yön elemanı (s. 16–18):**
  - Klasik sistemde ileri arızada I2 (ya da I0) polarize gerilimin önünde, geri arızada arkasındadır (Şekil 15–16).
  - Yön elemanları yalnızca dizi akımı bir **minimum eşiğin** üzerindeyse devreye giriyor.

**D. Negatif-dizi yönlü toprak koruması, 4 vaka (s. 19–33)**
- **Örnek 1, Tip III rüzgâr, saha kaydı, 5 Ağustos 2014 (s. 19–23):**
  - **Sistem:** 230 kV. WF1 142 MW, WF2 170 MW, ISTN tarafında 3200 MW hidroelektrik santral. Santraller YNd trafoyla bağlı.
  - **Olay:** ISTN'den 13,5 km uzakta B-toprak arızası, ~3 çevrim sonra B-C-toprak arızasına dönüşmüş.
  - **Güçlü kaynak tarafı:** I2 ve I0 dizi gerilimlerinin ~90° önünde.
  - **Rüzgâr tarafı, GDKT (ileri arıza):** I0 > 600 A ve V0'ın ~90° önünde, yani doğru. Ama **I2 < 90 A ve V2 ile neredeyse ters fazda**. 32GF yalnızca anlık olarak çalışmış.
  - **RTLR (geri arıza):** I0 90 A'den ~140 A'e çıkmış ve V0'ın 90° gerisinde, yani doğru. **I2 < 40 A ve V2 ile neredeyse aynı fazda.** 32GR yalnızca anlık çalışmış.
  - **Ders:** Tip III'ün I2-V2 açı ilişkisi bilinmiyor ve klasik değil. Sıfır-dizi kaynağı trafo varsa toprak koruması I0 ile yapılmalı, çünkü I0 türbin kontrolünden bağımsız.
- **Örnek 2, 100 MW PV, 230 kV, saha kaydı, B-toprak arızası (s. 23–25):**
  - Trafo üç sargılı YNyn ve Δ tersiyerli.
  - **I2, I1'in yalnızca ~%21'i ve I0'ın ~%24'ü** çıkmış. Eviriciler I2'yi sınırlıyor.
  - **Ders:** Şebeke kodu yoksa bu tür bir hatta negatif-dizi rölesi güvenilir biçimde kullanılamaz.
- **Örnek 3, STATCOM, saha kaydı, 30 Haziran 2015 (s. 25–30):**
  - **Sistem:** 138 kV. STATCOM sürekli ±12 MVAr, geçici ±24 MVAr. 1L10 hattı 195 km.
  - **Kaynak gücü:** ISKL arkasındaki pozitif-dizi kaynak TAVL'ye göre ~10 kat güçlü. Thévenin empedansları (100 MVA bazında) ISKL Z1 = 0,136 / Z0 = 0,260 pu, TAVL Z1 = 1,55 / Z0 = 0,271 pu (Şekil 23).
  - **Olay:** ISKL'ye yakın C-toprak arızası. ISKL'de Zone 1 21G doğru açmış (~2000 A). **TAVL 1L10 ise dış arızada yanlış açmış ve tüm bölge beslemesini kaybetmiş.**
  - **TAVL ölçümleri:**
    - Beklenen maksimum ~200 A, ölçülen ~240 A.
    - I1 ~130 A (modelde 50 A); fark STATCOM'un reaktif akımından geliyor.
    - I2 değişken, maksimum ~55 A.
    - I0 sabit 100 A.
    - 1,5. çevrimde **I2, V2 ile 180° ters fazda**, I0 ise V0'ın ~90° önünde.
  - **Analiz:** Quad 21G'nin reaktans sınırı I2 ile polarize edilmişti. Hat empedansı 5,18 sekonder Ω (104 primer Ω), reaktif erişim ayarı 3,8 sekonder Ω.
  - **Denklem (1)** (s. 29) ile yeniden hesaplanan reaktans, I2 polarizasyonunda **~1 çevrim sonra eşiğin altına düşmüş** ve hatalı açmaya yol açmış. I0 polarizasyonunda kararlı kalmış (Şekil 26).
  - **Ders:** Tam dönüştürücülü kaynaklar varsa toprak koruması I2 yerine I0 kullanmalı. Faz aşırı akım ayarı kalıcı rejim kısa devre analiziyle belirlenemiyor.
- **Örnek 4, Tip IV 300 MW, EMTP-RV simülasyonu, faz-faz arızası (s. 30–33):**
  - **Sistem:** 200 × 1,5 MW türbin, 315 kV şebeke, dört rüzgâr santrali daha var.
  - **Röle:** Arıza 67Q'ya göre geri yönde. 67Q'nun I2 devreye girme eşiği **0,02 pu**, burada 1 pu = 550 A.
  - **Senaryo 1, senkron generatör:** V2, I2'nin ~88° önünde. 67QR doğru çalışıyor.
  - **Senaryo 2, CSC:** I2 çok küçük. 67Q **kararsız**; 67QF yanlışlıkla ve düzensiz çalışıyor, yani ileri arıza sanıyor.
  - **Senaryo 3, DSC, K = 2:** Yön kararı doğru.
  - Şekil 30'dan okunan: 67QR, senaryo 1'e göre birkaç on ms (~2 çevrim) **geç** çalışıyor. Metinde bu gecikme sayısal olarak verilmiyor.
  - **Ders:** I2 eşiğin altındaysa röle ya yön elemanını bloke eder ya da yönsüz moda geçer. Hangisinin olacağı röleye göre değişir (s. 33).

**E. Negatif-dizi aşırı akım, 51Q (s. 33–38)**
- **Saha olayı, 27 Temmuz 2017 (s. 34–37):**
  - **Sistem:** 25 kV dağıtım fideri. 1 MW batarya (485–780 V DC), 1,25 MVA evirici, 480 V/25 kV Δ-Y trafo. Evirici akımı **~3008 A = 2,0 pu** ile sınırlıyor.
  - **Olay:** A-C-toprak arızasına yeniden enerjileme.
  - **Ölçüm:** Arızalı fazlarda ~100 A var; bu değer √3·3008·480/25000 ile tutarlı. **I2 hiç yok.** I0 V0'ın ~95° önünde, yani yön doğru.
  - **Ders:** Eviricinin negatif-dizi kaynak empedansı çok yüksek.
- **Simülasyon (s. 37–38, Şekil 33):**
  - **Kurulum:** Aynı 300 MW sistem, faz-faz arızası t = 1,0 s'de. 51Q primer pickup değeri **330 A ≈ 0,6 pu**. k = 0, 2 ve 6 değerleri sırasıyla sonsuz, j0,5 ve j0,17 pu negatif-dizi reaktansı taklit ediyor.
  - **Ölçülen I2 / I1 (Şekil 33 lejandı):**

    | Kaynak | I2 (pu) | I1 (pu) |
    |---|---|---|
    | Senkron generatör | **1,30** | 2,04 |
    | Tip III | 0,88 | 1,12 |
    | Tip IV, k = 6 | 0,67 | 0,72 |
    | Tip IV, k = 2 | **0,54** | 0,54 |
    | Tip IV, k = 0 | **0,11** | 1,09 |

  - **Sonuç:** 51Q, k = 0 ve k = 2'de çalışmıyor; k = 6'da açıyor.
  - **Dikkat:** I2 enjeksiyonu açıldığında I1 düşüyor (k = 0'da 1,09, k = 2'de 0,54 pu). Bu, akım bütçesi paylaşımıyla tutarlı. Ancak k = 6'daki I1 (0,72) monoton değil ve rapor bunu açıklamıyor.

**F. Faz mesafe koruması ve ZPM (s. 38–43)**
- **Saha olayı, 29 Temmuz 2018, yıldırım (s. 39–41):**
  - **Sistem:** 34 × 3 MW Tip IV ve STATCOM. 7,5 km, 138 kV hat. 34,5/138 kV Δ/YN trafo.
  - **Ayar:** Kısa hat ve zayıf kaynak nedeniyle Zone 1 kullanılmamış, yalnızca gecikmeli Zone 2 var.
  - **Olay:** İç üç-faz arızasında röle pickup bile yapmamış.
  - **Neden 1:** Faz akım denetimi **> 420 A = 1,0 pu** olarak ayarlanmış; bu santralin beklenen maksimum akımı.
  - **Neden 2:** Eşik doğru ayarlansa bile santral arızanın **ilk 2 çevriminde** akımı ön-arıza seviyesinde tutup sonra kesiyor. Bu davranışın adı **Zero Power Mode (ZPM)**: santral bağlı kalıyor ama geçici olarak akım basmayı bırakıyor.
  - **Yarış:** "Hızlı Zone 1'in bile **1 çevrime kadar** doğal gecikmesi var; röle ile IBR kontrolü arasında bir yarış oluşur." Gecikmeli Zone 2'nin hiç şansı yok (s. 40).
  - **Sonuç:** Arızayı yavaş faz-faz gerilim düşüklüğü yedeği temizlemiş.
- **Dış 500 kV A-B-toprak arızası (s. 40–41):** I1 yine 2 çevrim sonra kesilmiş, I2 ihmal edilebilir düzeyde, I0 V0'ın 90° önünde. Toprak arızası için I0 koruması güvenilir.
- **Blue Cut Fire, 16 Ağustos 2016 (s. 41):** 500 kV arızası 3 çevrimden kısa sürede temizlenmiş, ama ~1200 MW PV geçici olarak durmuş ya da kaybolmuş. Çoğunun nedeni momentary cessation, yani anlık akım kesme modu.
- **Karşı önlemler (s. 41–43):**
  - Faz akım denetimini minimuma çek. Modern rölelerdeki gerilim trafosu kaybı (LOP) mantığı bu ayarı güvenli kılıyor.
  - **I2 denetimli yeni mesafe röleleri**, IBR I2'yi bastırıyorsa kullanılamaz.
  - Yavaş faz-faz gerilim düşüklüğü yedeği LVRT ve PRC-024 ile koordine edilmeli (Şekil 36).
  - Tap yükün kötü güç kalitesine maruz kalmaması için DTT kullanılmalı.

**G. Haberleşmeli şemalar ve diğerleri (s. 43–46)**
- **POTT:** Echo mantığı ve DTT işe yarıyor. Echo'lu açma "birkaç çevrim" daha yavaş.
  - Bir şirkette, I2 yön polarizasyonlu echo mantığı **geri arızayı tanıyamadığı için izin sinyalini yanlışlıkla yansıtmış**. Bunun üzerine echo devre dışı bırakılmış (s. 44).
- **DCB:** Çok hassas aşırı akım denetimi ya da DTT gerekiyor (s. 44).
- **LCD:** 64 kbps dijital kanalla en güvenilir çözüm. Ancak pahalı ve tap yük sayısı sınırlı (s. 44–45).
- **Tek-faz açma ve tekrar kapama:** IBR negatif-dizi akımı veremiyorsa uygulanamayabilir (s. 45–46).

**H. Sistem koruma şemaları (s. 46–60)**
- **Güç salınımı (IEEE PSRC D6 test sistemi, s. 46–51):**
  - **Kurulum:** Mho ve üç blinder, PSB gecikmesi **3 çevrim (rapor 48 ms yazıyor)**.
  - **PSB hatası:** 270 ms'lik üç-faz arıza ve ardından L2/L4 hatlarının çıkması incelenmiş.
    - %0 IBR'de PSB doğru çalışıyor.
    - **%25 IBR'de** empedans gidişi dış ve orta karakteristiği 3 çevrimden **kısa** sürede geçiyor. PSB çıkmıyor ve salınım Zone 2 arızası sanılıyor (s. 47).
  - **OST hatası:** En ağır kararlı salınım %0'da 88 ms'lik arızadan, %50 IBR'de 120 ms'lik arızadan kaynaklanıyor. %50'de gidiş iç blinder içinde dönüyor ve **yanlış OST** çıkıyor (s. 49–50).
  - Bu sonuçlar Tip III modeliyle gösterilmiş. Tip IV ve PV için "benzer" deniyor (s. 47, 49).
- **Senkron kompansatör (s. 51):** Anma akımının 3–6 katı alt-geçici akım ve doğru açılı I2 sağlıyor. Ancak pahalı.
- **SSCI (alt-senkron kontrol etkileşimi, s. 51–55):** IBR kontrolünün seri kompanzasyonlu hatla etkileşerek alt-senkron salınım üretmesi.
  - AEP 2009 olayı ve AEP/ERCOT 2017'de üç olay var.
  - **Olay 1:** ~25,6 Hz. Alt-senkron bileşen temel bileşenin ~2 katı.
  - **Olay 2:** ~22,5 Hz. Salınım 400 ms içinde büyümüş ve trafo diferansiyel koruması yanlış açmış.
  - **SSO rölesi önerisi:** 10–50 Hz bant geçiren filtre, durdurma bandında ≥ 40 dB zayıflatma. Maksimum tespit süresi T_delay = 2,5/f_osc s; 25 Hz için 100 ms (s. 55).
  - Not: Metin f_osc'u (f_low + f_upper)/2 olarak tanımlıyor, ama örnekte 25 Hz kullanıyor.
- **Adalanma (s. 57–60):**
  - IEEE 1547-2018'e göre ada 2 s içinde ayrılmalı.
  - NERC, iletime bağlı IBR'lerde pasif anti-adalanma korumasının kapatılmasını öneriyor.
  - Örnek şirket metodolojisinde: POI'de 3'ten az hat varsa analiz yapılıyor. Üretim, omuz mevsimlerinde 10:00–16:00 arası minimum yükün %66'sından büyükse şema gerekiyor (s. 59–60).
  - **Projeye ilginç not:** "Aktif" anti-adalanma yöntemlerinde evirici şebekeye bir şey uygulayıp şebekenin tepkisini ölçüyor (s. 58). Bu, yardımcı sinyal fikrinin endüstrideki mevcut bir öncülü.

**I. Sonuç maddeleri (s. 60–61), en önemlileri**
- **İlk iki çevrim:** IBR'nin arızaya ilk iki çevrimlik cevabı, sonraki akım limitleriyle aynı değil. Yüksek hızlı röleler (Zone 1, anlık aşırı akım) bu pencerede **overreach** yapabilir. Önerilen çözümler: röleyi geciktirmek ya da başlangıç akımını anlayıp hızlı açmada **kullanmak** (s. 60).
- **Negatif-dizi eşiği:** **"Bazı röleler güvenilir çalışmak için I2'nin I1'e göre ~%10 mertebesinde olmasını ister"** (s. 60). Çözüm önerisi: k = 2–6 eğimli ve j0,5 pu'dan küçük reaktans taklit eden I2 enjeksiyonu; mümkünse IBR geçici rejiminde röleyi yavaşlatmak (s. 60–61).
- **51Q sınırı:** k = 2 (~j0,5 pu) ile bile 51Q pickup değerine göre sorun sürebilir (s. 61).
- **ZPM:** Gelecekteki tesislerde önerilmiyor (s. 60).
- **LCD:** En güvenilir çözüm, ama haberleşmeden bağımsız yavaş bir yerel yedek gerektiriyor (s. 61).

### Varsayımlar ve sınırlamalar
- **Kapsam (2020):** Neredeyse tamamen **GFL ya da akım kaynağı** davranışlı cihazlar inceleniyor: Tip III/IV, PV, STATCOM, BESS. GFM hiç ele alınmıyor. IEEE 2800-2022'den önce yazılmış.
- **Saha verisi kısıtlı:** Kayıtlar tek olaylardan oluşuyor ve **4 örnek/çevrim filtrelenmiş fazörler**. Bunlarla çevrim-altı (sub-cycle) davranış incelenemez. Üreticilerin kontrol detayları bilinmiyor; ZPM vakasındaki iç arızanın kaydı ise üzerine yazılmış ve kaybolmuş (s. 39).
- **Tekrarlanabilirlik zayıf:** Simülasyon sistemi EPRI raporunda [20] ve TR-81'den yeniden kurulamıyor. Evirici modellerinin akım sınırlayıcı ve k uygulaması detayları ile arıza direnci verilmiyor.
- **k = 2–6 önerisi dar bir kanıta dayanıyor:** Tek sistem, tek arıza tipi (faz-faz), tek röle ayarı ve yalnızca k = 0, 2, 6 denenmiş. "j0,5 pu'dan küçük reaktans güvenilirdir" genellemesi az vakaya dayanıyor. Üstelik k = 2 bile 51Q için yetmemiş.
- **Şekil 9'un varsayımları yok:** I1 reaktif oranı ve I2 açısı belirtilmemiş.
- **Güç salınımı kanıtı dolaylı:** Yalnızca **Tip III** modeliyle gösterilmiş. Tip III tam dönüştürücülü değil, stator doğrudan şebekeye bağlı. "Diğerleri benzer" iddiası verisiz.
- **Nitel kalan konular:** Mho genişlemesi ve ilk iki çevrimde overreach yalnızca nitel anlatılıyor; sayısal bir örnek yok.
- **Maliyet ve hız sayısallaştırılmamış:** Önerilen karşı önlemlerin (I0 koruması, LCD, DTT, UV yedeği, senkron kompansatör) maliyeti ve hız kaybı ölçülmemiş. Örneğin echo için yalnızca "birkaç çevrim daha yavaş" deniyor.
- **Faz-faz arızaları için çözüm zayıf:** I0 çözümü yalnızca toprak arızalarına uygulanabiliyor. Faz-faz ve üç-faz arızaları için önerilen yollar gerilim düşüklüğü yedeği (yavaş) ve haberleşme (pahalı ya da kanal kesintisine açık).

### Projeyle bağlantı
- **WP1 (CVXPY):**
  - **Akım bütçesi kısıtı:** Şekil 9'un fiziği (s. 8), faz akımlarının üçünün de I_max altında kalması demek. I0 = 0 ve a = e^{j120°} ile:
    - I_a = I1 + I2
    - I_b = a²I1 + aI2
    - I_c = aI1 + a²I2
    - Her biri için |I_φ| ≤ I_max yazılır. CVXPY'de bunlar `cp.abs(...) <= Imax` biçiminde **SOC kısıtları**.
  - **Eşikler iki taraflı kısıt olarak:** Röle eşikleri tasarım hedefi olarak kullanılabilir.
    - **Normal işletmede güvenlik:** Sürekli enjekte edilen yardımcı sinyal mevcut 67Q'yu devreye sokmamalı. Bu bir **üst sınır**: I2 < 0,02 pu (s. 31) ve I2/I1 < ~%10 (s. 60).
    - **Arızada güvenilirlik:** Tepkinin dedektör eşiğini aşması gerekiyor. Bu bir **alt sınır**.
  - **Doğal referans politika (baseline):** k-eğimli I2 = k·V2 kuralı. Yardımcı sinyal bunun yerine ya da üzerine tasarlanan bir terim olarak karşılaştırılmalı.
  - **Belirsizlik kümesi:** Ön-arıza yükü (0–%100, s. 13), devredeki ünite sayısı ve hava durumu (s. 16), kontenjanslar (CG1 ya da CG2 devre dışı, s. 5) ve yakındaki STATCOM etkisi (s. 28).
- **WP2 (EMT):**
  - **Hazır senaryo matrisi:**
    - CSC ile DSC (k = 0/2/6), ZPM ya da momentary cessation, Tip III crowbar, STATCOM.
    - Trafo bağlantısı (YNd var ya da yok).
    - Arıza tipi: özellikle faz-faz ve üç-faz.
    - İç/dış arıza ve IBR'nin tek kaynak olduğu kontenjans.
  - Şekil 4 topolojisi ve IEEE PSRC D6 salınım test sistemi iyi başlangıç noktaları.
  - **Model uyarısı:** Basit dizi modeli (Şekil 11) yalnızca kalıcı rejim için geçerli. Çevrim-altı davranış için detaylı kontrol modeli şart (s. 10–11).
- **WP3 (röle tarafı):**
  - **Klasik referans elemanlar raporda tanımlı:**
    - Pozitif-dizi bellek polarizeli mho (Şekil 14).
    - I2 ya da I0 polarizeli quad reaktans, **Denklem (1)**, s. 29.
    - 67Q (0,02 pu devreye girme eşiği), 51Q (0,6 pu pickup), 32GF/GR, PSB/OST.
  - Bunları Simulink'te kodlamak, yardımcı sinyal dedektörünün kıyaslanacağı zemini oluşturur.
  - Kalman filtresi için Örnek 3 iyi bir test: I2'nin genliği ve açısı arıza boyunca dalgalanıyor (s. 28). İzlemeyi zorlaştıran, tam da bu dalgalanma.
  - Öğrenen dedektörler için saha verisi 4 örnek/çevrim; bu yetersiz. Eğitim verisi WP2'den gelmeli.
- **WP4 (gecikme):**
  - **Projenin 1 çevrim hedefi saha pratiğinden agresif:** Zone 1'in doğal gecikmesi 1 çevrime kadar (s. 40). Giriş vakasında Zone 1 3 çevrimde açmış (s. 5). PSB zamanlayıcısı 3 çevrim (s. 47). SSO tespit hedefi 100 ms (s. 55).
  - **Asıl kısıt evirici tarafında:** I2 tepkisi 1–2 çevrim sürüyor (s. 7) ve ZPM akımı ~2 çevrimde kesiyor (s. 40). Evirici arızayı algıladıktan sonra sinyal basarsa, röle bir çevrim içinde karar veremeyebilir.

### Buradan çıkan açık sorular / araştırma fikirleri
1. **[EN UMUT VERİCİ, ilk iş] Şekil 9'u CVXPY'de yeniden üret.**
   - %120 sınırda, birim güç faktörlü %0–100 yük için ulaşılabilir maksimum |I2|'yi hesapla.
   - %0 yükte ~%60, %100 yükte ~%20 çıkmalı (s. 8).
   - Bu, WP1 akım bütçesi modelinin doğrulama testi olur. Raporun yazmadığı varsayımları (I1 reaktif oranı, I2 açısı) parametre olarak tara.
2. **[EN UMUT VERİCİ] Yardımcı sinyal ile k-eğimli enjeksiyonu karşılaştır.**
   - Örnek 4/51Q benzeri bir sistemde (Tip IV, 67Q 0,02 pu, 51Q 0,6 pu, faz-faz arızası) üç politikayı kıyasla: k = 0/2/6 ve optimize yardımcı sinyal.
   - Ölçütler: doğru yön kararı, karar süresi, kullanılan akım payı (headroom).
   - Hipotez: Tasarlanan sinyal, k = 6'nın verdiği ayırt ediciliği daha az akımla sağlar.
3. **[UMUT VERİCİ] Ön-arıza sürekli enjeksiyon ile tetiklemeli enjeksiyon.**
   - Sinyal arızadan önce zaten varsa, röle eviricinin 1–2 çevrimlik arıza algılama ve tepki gecikmesini (s. 7) beklemek zorunda kalmaz.
   - EMT'de iki stratejinin tespit süresi dağılımını karşılaştır.
   - Bedel: Normal işletmede gerilim dengesizliği ve mevcut I2 elemanlarının güvenliği (fikir 4).
4. **Mevcut negatif-dizi elemanlarıyla bir arada çalışma.** Yardımcı sinyal normal işletmede 67Q, 51Q ya da I2 denetimli mesafe elemanlarını yanlışlıkla devreye sokuyor mu?
   - Eşik değerlerini kısıt olarak koy (s. 31, 60) ve EMT'de güvenlik testi yap.
5. **Denklem (1)'in I2 ile I0 polarizasyonu.** STATCOM benzeri bir reaktif kontrol altında Şekil 26 davranışını yeniden üret. Ardından yardımcı sinyalin I2 polarizasyonunu kararlı hale getirip getirmediğini test et.
6. **ZPM ve momentary cessation sınır durumu.** Evirici akım basmayı keserse yardımcı sinyal de kaybolur.
   - Bu mod belirsizlik kümesine ya alınmalı ya da açıkça kapsam dışı ilan edilmeli.
   - Akım kesilmesinin kendisi bir arıza imzası olarak kullanılabilir mi?
7. **Güç salınımı ile arızayı ayırma.** %25 IBR'de PSB'nin 3 çevrimlik zamanlayıcısı yetmiyor (s. 47). Simetrik bir salınımda negatif-dizi yardımcı sinyalin tepkisi arızadakinden farklı olmalı; bu, PSB'ye alternatif bir ayırıcı olarak denenebilir. Daha ileri bir konu.
8. **Etkin negatif-dizi empedansını tasarım değişkeni yapmak.** k, eviricinin "görünen" Z2'sini belirliyor (j1/k). Yardımcı sinyal tasarımı aslında Z2'nin genliğini ve açısını optimize etmek olarak da yazılabilir.
   - Kısıtlar: IEEE 2800 açı penceresi (Sandia s. 12) ve akım limiti.
   - Hedef: Mho ve yön elemanlarının polarizasyonunu kararlı tutmak.

### Kilit şekil / tablo / denklemler
- **Şekil 4 (s. 3):** Genel bağlantı topolojisi (CB1–CB10). EMT test sistemi için şablon.
- **Şekil 5 (s. 4):** Senkron kaynak ile Tip IV'ün faz-faz arıza akımları (6000+ A'e karşı ~2 çevrimde sıfıra inen akım).
- **Şekil 8 (s. 7):** Önerilen I2-V2 karakteristiği, eğim k.
- **Şekil 9 (s. 8):** Akım bütçesi; yük oranına göre ulaşılabilir I2.
- **Şekil 11 (s. 10):** Basit dizi eşdeğeri (yalnızca kalıcı rejim için).
- **Şekil 12–13 (s. 12):** Kalıntı gerilime göre arıza akımı zarfları.
- **Şekil 14 (s. 15):** Dinamik mho genişlemesi.
- **Şekil 15–16 (s. 17–18):** İleri ve geri arızada dizi polarizasyon fazörleri.
- **Şekil 19–20, 22, 25 (s. 21–28):** Saha olaylarında I2-V2 açı anomalileri.
- **Denklem (1) ve Şekil 26 (s. 29):** I2 ya da I0 polarizeli toprak reaktans elemanı:
  X_CG = Im(V_C · I_P*) / Im(Z1ang · (I_C + k0·I0) · I_P*)
  Burada I_P = I2 ya da I0, k0 sıfır-dizi kompanzasyon katsayısı, Z1ang hat açısı.
- **Şekil 28–30 (s. 32–33):** 67Q'nun üç senaryodaki tepkisi.
- **Şekil 33 (s. 38):** 51Q ve k; sayısal I1/I2 değerleri.
- **Şekil 34–35 (s. 40–41):** ZPM kayıtları.
- **Şekil 36 (s. 43):** Gerilim düşüklüğü yedeğinin açma bölgeleri.
- **Şekil 38–41 (s. 48–50):** PSB ve OST hataları.
- **Şekil 43–44 (s. 53–54):** SSCI spektrumları.
- **Bölüm 6 (s. 60–61):** Sonuç ve önerilerin listesi.

---

## Grup sentezi

### İki rapor birlikte ne söylüyor?
- **Aynı kök neden:** İki rapor dört yıl arayla ve farklı yöntemlerle yazılmış: TR-81 saha kayıtlarına ve GFL'ye, Sandia literatüre, uzmanlara ve GFM'e dayanıyor. Ama aynı kök nedene varıyorlar. Klasik koruma, arıza akımının **büyük, endüktif ve kaynak fiziğiyle belirlenmiş** olduğunu varsayıyor. IBR akımı ise **küçük, kontrollü ve üreticiye özgü**.
- **Kritik kanal negatif dizi:** En kırılgan kanal **negatif dizi**, hem genlik hem açı olarak.
  - TR-81 bunu saha olaylarında gösteriyor: I2'nin bastırılması, ters faz, aynı faz, dalgalanma (s. 21–28, 36).
  - Sandia, uzmanların oybirliğiyle "IBR öngörülebilir I2 vermeli" dediğini aktarıyor (s. 22–23, 31–32).
- **Toprak arızaları büyük ölçüde çözülmüş:** Trafo üzerinden gelen I0 sayesinde (TR-81 s. 23, 30, 36; Sandia s. 22, 31–32). **Açık kalan zor sınıf faz-faz (ve üç-faz) arızaları.** TR-81'deki giriş vakası, Örnek 4 ve 51Q simülasyonu faz-faz arızası; Baeckeland çalışması B-C arızası; Sandia uzmanları da faz-faz arızasında hata bildiriyor (s. 31).
- **Standartların evrimi:** TR-81, I2'nin V2'nin 90° önünde ve k ile orantılı olmasını öneriyor. IEEE 2800-2022 (Sandia'nın aktarımıyla) **açıyı** 90°–100° olarak sabitliyor, ama **genliği belirtmiyor**. Sandia'ya göre GFM'de I2 açısı ve dalga şekli akım sınırlayıcı türüne de bağlı (s. 18, 21, 27). Bu, belirsizliğe yeni bir katman ekliyor.
- **İlk 1–2 çevrim belirsiz:** İki rapor da arızanın ilk 1–2 çevrimini en belirsiz pencere olarak görüyor.
  - TR-81: geçici overreach, 1–2 çevrimlik I2 tepki gecikmesi, ~2 çevrimde ZPM kesmesi.
  - Sandia: donanım limiti kaynaklı bozuk dalga şekli, VI'nın ilk çevrimlerde akımı sınırlayamaması.

### Çelişkiler ve gerilimler
1. **Arıza akımı büyüklüğü:**
   - TR-81: tipik 1,1–2,0 pu (s. 13–14); BESS'te 5–10 s boyunca 2–3× (s. 13); örnek eviricide 2,0 pu sınır (s. 34); Şekil 9'da %120 sınır.
   - Sandia uzmanları: GFM doyumda "en fazla 1,1–1,2 pu" (s. 22).
   - Sandia ölçümleri: 2,25 pu RMS kare dalga (s. 24).
   - Uzman dileği: 1,5 pu, 15–30 çevrim (s. 32).
   - **Sonuç:** I_max tek bir sayı değil. Tasarım aracında bir parametre ya da belirsizlik boyutu olmalı.
2. **Mesafe rölesi akımdan bağımsız mı?** Bazı Sandia uzmanlarına göre mesafe koruması "akımdan bağımsız" (s. 33). TR-81 bunun aksini saha kanıtıyla gösteriyor: minimum akım denetimi, mho genişlemesi ve ZPM yüzünden mesafe rölesi açmamış (s. 15–16, 39–40).
3. **Röle hızı:** TR-81 geçici rejimden korunmak için **röleyi yavaşlatmayı** öneriyor (s. 60–61). Sandia uzmanlarına göre ise IBR'ler zaten korumadan **önce** açıyor (s. 22, 32). Projenin **1 çevrim** hedefi bu ikilemin hız tarafında duruyor. Değeri de burada: hem hızlı hem güvenli olabilmek.
4. **Sıfır dizi:** TR-81 "IBR'ler topraklı değil, I0 vermez" diyor (s. 9). Sandia ise trafosuz doğrudan I0 basan bir GFM ölçmüş (s. 24). İki taraf da I0'ın trafodan sağlanmasını tercih ediyor.
5. **Haberleşme:** TR-81'in çözümleri büyük ölçüde haberleşmeye dayanıyor: POTT/echo, DCB, DTT, LCD. Sandia'daki şirket ise **uyarlamalı** korumayı haberleşme yükü nedeniyle istemiyor ve "tek ayar" tercih ediyor (s. 32). Yani haberleşmeli hat şemaları kabul görüyor, ama ayarların koşula göre değişmesi görmüyor. Yardımcı sinyal yaklaşımının yerel, haberleşmesiz ve tek tasarımlı olması bu tercihle örtüşüyor.
6. **Sandia'nın kendi içindeki tutarsızlık:** Uzman sayısı 18 ile 22 arasında değişiyor (s. 21 ve s. 31).

### Proje için en önemli 3 çıkarım
1. **Negatif-dizi kanalı hem gerekli hem kıt; tasarım açık bir akım bütçesiyle yapılmalı.**
   - %120 sınırlı bir IBR, tam yükte faz-faz arızasında ~%20 I2 verebiliyor. Aynı arızada senkron generatör ~%200 veriyor (TR-81 s. 8).
   - IEEE 2800 açıyı belirliyor ama genliği serbest bırakıyor (Sandia s. 12–13). **Optimize edilmiş yardımcı sinyal tam da bu serbestliği dolduruyor.**
   - Ancak ancak faz akım limiti (SOC), "I1 reaktif ≥ I2 reaktif" kuralı ve mevcut I2 elemanlarının eşikleri (0,02 pu, ~%10 I2/I1) altında tasarlanırsa anlamlı.
   - **İlk somut adım:** Şekil 9'u CVXPY'de yeniden üretmek. Sonra TR-81 Örnek 4'ü (67Q, CSC/DSC) Simulink'te yeniden üretip bir referans çizgisi (baseline) kurmak.
   - Öncelik **faz-faz arızaları** olmalı, çünkü toprak arızalarında I0 zaten iyi bir alternatif.
2. **Zamanlama: 1 çevrimlik bütçe, en kirli ve en belirsiz pencerenin içinde.**
   - İlk 1–2 çevrimde evirici henüz arızayı algılamamış ya da tepkisi oturmamış olabilir. Bu pencerede dalga şekli bozuk ve akım limitleri farklı; bazı modlarda ~2 çevrimde akım tamamen kesiliyor.
   - Bu yüzden WP4'ün gecikme bütçesi **yalnızca rölenin hesaplama süresi değil, eviricinin tepki süresi** de olmalı. IEEE 2800 basamak cevabı için 2,5 çevrime izin veriyor.
   - **Ön-arıza sürekli enjeksiyon** stratejisi bu sorunu aşmanın en olası yolu. Ancak normal işletmede güvenlik ve güç kalitesi bedeli ölçülmeli.
   - WP2, çevrim-altı EMT verisini gerçekçi sınırlayıcı modelleriyle üretmeli. İki raporda da bu çözünürlükte veri yok.
3. **Garanti, belirsizlik kümesi kadar iyidir; kümeye kontrol modları ve "normal ama tuhaf" olaylar girmeli.**
   - Hataların kökü üreticiye özgü kontrol davranışı:
     - CSC ya da DSC, k değeri, ZPM / momentary cessation, STATCOM dinamiği.
     - GFM'de akım sınırlayıcı türü ve VI X/R oranı.
     - GFM'den GFL'ye geçiş ve chattering.
   - İşletme belirsizlikleri de kümeye girmeli: yük %0–100, devredeki ünite sayısı, kontenjanslar.
   - Normal olaylar da kümeye girmeli: yük tecavüzü, motor ve trafo ani akımı, BESS rampası, faz sıçraması, güç salınımı.
   - Bunlar kümede yoksa küme-tabanlı garanti sahada anlamsız kalır.
   - Proje ayrıca neden I0 koruması, LCD veya DTT ve UV yedeği ya da senkron kompansatör yerine yardımcı sinyal kullanılması gerektiğini savunmalı. Güçlü argümanlar şunlar: haberleşme gerektirmemesi, faz-faz arızalarında işe yaraması, hız ve "tek tasarım, tüm koşullar".
