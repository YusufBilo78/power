# D — Makine Öğrenmesi ve Veri Seti Makaleleri: Okuma Notları

**Bağlam:** Bu notlar, eviricinin (inverter) optimal tasarlanmış küçük bir negatif dizi "yardımcı sinyal" (auxiliary signal) enjekte ettiği ve mesafe rölesinin arızayı normal işletmeden küme tabanlı (set-based) bir garantiyle ayırdığı proje için yazıldı. Projedeki iş paketleri (İP):

- **İP1:** CVXPY ile tasarım aracı
- **İP2:** EMT simülasyonu
- **İP3:** Röle tarafında tespit (konvansiyonel elemanlar, Kalman filtresi, öğrenilmiş dedektörler)
- **İP4:** Edge kartta, bir çevrimlik (~16.7 ms, 60 Hz) gecikme bütçesi

**Okuma kuralları:**

- "s. N", **PDF sayfa numarasıdır**. Ouali vd. makalesinde basılı sayfa numarası PDF sayfasından 2 eksiktir. Diğerlerinde ikisi aynıdır.
- **(hesap)** ve **(çıkarım)** etiketli değerleri ben hesapladım ya da yorumladım; makalede doğrudan yazmazlar. Bunların dışındaki bütün sayılar makalelerden alındı.
- Notlar yalnızca makalelerin kendisine dayanıyor; depo notları ve README kullanılmadı.
- Terimler: **dependability** = arıza varken doğru açma (çalışma güvenilirliği); **security** = arıza yokken açmama (yanlış açma yapmama).

**İncelenen makaleler:**

1. Beikbabaei vd. 2024: %100 IBR mikroşebekede karar ağacı
2. Ouali vd. 2024: GFL/GFM kontrol modunun ML ile sınıflandırılması
3. Martinez-Velasco vd. 2025: YZ ile arıza tanılama taraması
4. Oelhaf, Kordowich vd. 2026: PROTECT-90 veri seti
5. Kordowich vd. 2026: EvEMTBench veri seti
6. Oelhaf vd. 2025/2026: FC/FL için kontrollü ML karşılaştırması
7. Abukhousa vd. 2026: Gecikme farkındalıklı DL kıyaslaması

---

## 1. Beikbabaei vd. (2024): %100 eviricili mikroşebekede karar ağacı ile koruma

- **Künye:**
  - Yazarlar: M. Beikbabaei, M. Lindemann, M. Heidari Kapourchali, A. Mehrizi-Sani (Virginia Tech, Univ. of Alaska Anchorage)
  - "Machine Learning–Based Protection and Fault Identification of 100% Inverter-Based Microgrids"
  - arXiv:2405.07310v1 (eess.SY), 12 Mayıs 2024. IEEE konferans formatında; yayın yeri metinde yok ("© 20XX IEEE" notu var).
  - 4 sayfa
- **Tek cümlede:** PSCAD'de 4 eviricili, 4 baralı bir mikroşebekede bara-1 rölesi, yerel RMS akım/gerilim ve P/Q değerlerini (1 ms aralıkla) kullanıyor. Tek bir karar ağacı (decision tree) hem arıza tespiti hem arıza tipi tanıma yapıyor; raporlanan doğruluk yaklaşık %96.
- **Problem ve bağlam:**
  - %100 IBR mikroşebekede arıza akımı düşük ve güç akışı çift yönlü; bu yüzden klasik aşırı akım koruması yetersiz kalıyor.
  - Hedef, haberleşme gerektirmeyen ve mikrodenetleyicide çalışabilecek basit bir çözüm (s. 1–2).
  - Derin öğrenme gerçek zamanlı uygulama zorluğu gerekçesiyle eleniyor. SVM, eğitim maliyeti veri karmaşıklığıyla karesel/kübik büyüdüğü için eleniyor (s. 3).
- **Veri:**
  - *Şebeke (s. 2):*
    - 4 baralı radyal mikroşebeke. Baz güç 1.5 MVA; AG tarafı 480 V, OG tarafı 12.47 kV.
    - IBR1 ve IBR3 grid-forming (GFM): P–f ve Q–V droop, PI kontrol. IBR2 ve IBR4 grid-following (GFL): PLL ve dq akım kontrolü.
    - Her evirici en fazla 1.5 MVA. DC kaynak 1.2 kV. RL filtre 1.5 mΩ / 20 µH.
    - PI kazançları ve hat empedansları (R ve reaktans, Ω cinsinden) verilmiş.
    - Bara 3'te kesiciyle bağlı bir yük var: P 0.1–0.6 pu, Q 0.01–0.06 pu. Röle R1, bara 1'de.
  - *Simülatör:* PSCAD/EMTDC ve onun Python otomasyon API'si.
  - *Senaryolar (s. 3):*
    - Arıza tipleri: AG, BG, CG, ABG, ACG, BCG, ABCG (7 tip). **Toprak temassız faz-faz (LL) arızası yok.**
    - Rf ∈ {100, 10, 1, 0.1, 0.001} Ω.
    - Arıza konumu: yalnızca baralar (1–4); hat ortasında arıza yok.
    - Arıza süresi ∈ {0.05, 0.1, 0.2} s.
    - Toplam **420 simülasyon**, her biri 1 s.
    - **Bütün arızalar t = 0.05 s'de başlıyor.**
  - *Örnekleme:* 3 faz akım ve gerilimin RMS değerleri ile P ve Q, 1 ms aralıkla kaydediliyor. Bu, nokta-dalga (point-on-wave) verisi değil. RMS'in hangi pencere ya da filtreyle hesaplandığı yazılmamış.
  - *Etiket:* Arıza var/yok bayrağı ve 0–7 arasında tip numarası (Tablo I, s. 3).
  - *Arıza dışı olay* (anahtarlama, inrush, motor yolverme): yok. Yük aralığı veriliyor; ancak yük anahtarlamasının ayrı bir olay olarak simüle edilip edilmediği belirtilmiyor.
  - *Erişim:* Veri ve kod yayımlanmamış.
- **Yöntem (s. 3):**
  - Model: scikit-learn karar ağacı (Gini). En büyük derinlik 43, toplam **4044 yaprak**.
  - Girdi: R1'deki I, V, P, Q. Anlık örnek kullanılıyor; zaman penceresi yok.
  - Veri boyutu: **715,959** adet 1 ms'lik örnek.
  - Bölme: `train_test_split` ile **%80/%20, karıştırarak (shuffle), random_state=20**.
  - Metrik: yalnızca doğruluk (accuracy).
- **Ana bulgular:**
  - Özellik kümelerine göre doğruluk (tespit / tip, Tablo II, s. 3):

    | Girdi | Tespit | Tip |
    |---|---|---|
    | I | %95.58 | %95.50 |
    | I, V | %95.92 | %95.82 |
    | I, P, Q | %96.26 | %96.05 |
    | I, V, P, Q (seçilen) | %96.33 | %96.04 |

  - Yazarların iddiaları (s. 2): eğitim 9 s'den kısa sürüyor; arıza "5 ms'den kısa sürede" tespit ediliyor.
  - Örnek vakalar:

    | Vaka | Arıza | Rf | Bara | Süre | Sonuç |
    |---|---|---|---|---|---|
    | 1 (s. 3) | AG | 0.01 Ω | 1 | 50–150 ms | Başlangıç 50 ms'de, temizlenme 155 ms'de (5 ms gecikme) bulunuyor. t = 0.104 s'de tek örnekte hata var. |
    | 2 (s. 4) | ACG | 1 Ω | 2 | 50–100 ms | Hem tespit hem tip doğru. |
    | 3 (s. 4) | ABCG | 40 Ω (eğitimde yok) | 3 | 50–200 ms | Başlangıçtan sonra birkaç adım yanlış. İlk 40 ms boyunca tip yanlış. Temizlenme 10 ms gecikmeyle bulunuyor. Yazarlar yine de modelin "eğitilmemiş yüksek empedanslı arızada iyi çalıştığı" sonucuna varıyor. |
- **Metodoloji eleştirisi:**
  1. **Örnek düzeyinde karıştırılmış bölme (sample-level split):** Aynı simülasyonun birbirine çok benzeyen ardışık 1 ms örnekleri hem eğitim hem test kümesine düşüyor. Bu ciddi bir veri sızıntısıdır (leakage). Raporlanan %96 bir ezber üst sınırıdır; simülasyon düzeyinde (episode-level) çapraz doğrulama yapılmamış.
  2. **Kardeş simülasyonlar (sibling simulations):** Aynı (tip, Rf, konum) üçlüsü üç farklı süreyle simüle edilmiş. Bu üç simülasyonun ilk 50 ms'lik arıza dalga biçimi aynıdır. Bölme simülasyon düzeyinde yapılsa bile gruplama anahtarı (tip, Rf, konum) olmalı.
  3. **Gösterilen vakalar büyük olasılıkla eğitim verisinden.** Vaka 2 (ACG, 1 Ω, bara 2, 0.05 s) eğitim ızgarasındaki bir konfigürasyonun ta kendisi; örneklerinin yaklaşık %80'i muhtemelen eğitimdeydi (çıkarım). Vaka 1'deki 0.01 Ω ve Vaka 3'teki 150 ms süre ise listelenen değerler arasında yok. Bunlar ya yazım hatası ya da tanımsız bir test; makale açıklamıyor.
  4. **Sayılar tutmuyor:** 420 simülasyon × 1 s / 1 ms ≈ 420,000 örnek eder (hesap). Makale 715,959 diyor ve farkı açıklamıyor.
  5. **Başlangıç anı tek:** Bütün arızalar t = 0.05 s'de başlıyor. Arıza başlangıç açısı (inception angle) ve DC ofset çeşitliliği yok.
  6. **Kapsam dar:** Rf için yalnızca 5 ayrık değer var (en fazla 100 Ω). LL arızası yok. Arızalar yalnızca baralarda.
  7. **Güvenlik ölçülmemiş:** Arıza dışı olay yok. Yanlış açma oranı, precision/recall ve karışıklık matrisi yok; yalnızca accuracy var. Üstelik sınıflar dengesiz: 1 s'lik kaydın yalnızca 50–200 ms'si arıza.
  8. **Gecikme iddiası belirsiz:** Ağaç anlık örnekle çalıştığı için kendi başına nedensel (causal). Ancak RMS büyüklüğü bir pencere gerektirir ve PSCAD RMS bloğunun gecikmesi tanımlanmamış. "<5 ms" değeri simülasyon zaman ekseninde ölçülmüş. "Mikrodenetleyiciye uygun" iddiası donanımda denenmemiş. 43 derinlik ve 4044 yaprak, aşırı uyumun (overfitting) işareti.
  9. **Seçicilik ve gerçekçilik yok:** R1, bara 1–4'teki tüm arızalara "arıza" demeye eğitiliyor; koruma bölgesi (zone) kavramı yok. Arızalar kendiliğinden kalkıyor; kesici açması ya da topoloji değişimi simüle edilmiyor. CT/VT modeli, gürültü ve ADC yok.
- **Projeyle bağlantı:**
  - **İP3:** Hem "nasıl yapılmamalı" örneği hem de basit bir öğrenilmiş taban çizgisi (baseline) adayı.
  - **İP2:** Küçük bir %100 IBR test sistemi parametre seti olarak yeniden kullanılabilir (GFM droop + GFL, PI kazançları, hat değerleri, s. 2).
  - Yeniden kullanılabilir veri yok.
- **Açık sorular / araştırma fikirleri:**
  - **[EN UMUT VERİCİ] Sızıntı denetimi (leakage audit):** Bu düzeneği yeniden kur. Aynı karar ağacını üç yolla değerlendir: (a) örnek karıştırmalı bölme, (b) simülasyona göre gruplanmış CV, (c) (tip, Rf, konum) üçlüsüne göre gruplanmış CV. Aradaki skor farkını raporla. İP3 için kısa ve öğretici bir öğrenci çıktısı olur.
  - Ağaç girdisine yardımcı sinyalin oluşturduğu negatif dizi tepkisi eklenirse yüksek Rf'li arızalar (≥40 Ω) daha iyi ayrılır mı?
  - GFM/GFL oranı ya da kontrol yapısı değişince model genelleşir mi? (Makale 2 ile birlikte düşünülmeli.)

---

## 2. Ouali vd. (2024): Evirici kontrol modunun (GFL/GFM) ML ile sınıflandırılması

- **Künye:**
  - Yazarlar: R. Ouali, J.-Y. Dieulot, P. Yim, X. Guillaud, F. Colas, Y. Wu, H. Wu
  - "Machine learning classification of power converter control mode", 19 Ocak 2024
  - Yayın yeri metinde yok. PDF meta verisindeki dosya adı arXiv gönderimini düşündürüyor.
  - 13 sayfa: kapak, özet ve basılı numaralı 11 sayfa. ANR DELTWINCO projesi.
- **Tek cümlede:** Eviricinin bağlantı noktasından (PCC) dışarıdan ölçülen dq admitans spektrumu (Ydd ve Yqq'nun genlik ve fazı) kullanılarak eviricinin GFL mi GFM mi olduğu yedi klasik ML algoritmasıyla sınıflandırılıyor. Eğitimde görülen kontrol yapılarında doğruluk %92–98; görülmemiş bir yapıda (viGFL) %40–92.
- **Problem ve bağlam:** İletim sistemi operatörleri (TSO), özel şirketlere ait eviricilerin kontrol yapısını ve parametrelerini bilemiyor. Şebeke koduna uyumun (GFM mi GFL mi?) kara kutu (black-box) ölçümüyle doğrulanması gerekiyor (s. 3).
- **Veri:**
  - *Kapsam:* Bu arıza verisi değil. Tek bir evirici ve şebeke empedansı MATLAB/Simulink'te modellenmiş.
  - *Sistem (Tablo 1, s. 6; s. 8):*
    - VSC: 1.044 GVA, 400 kV, 1 GW, Qmax 300 MVar.
    - Filtre: Lc 0.15 pu, Rc 0.005 pu. Şebeke: 0.5 pu / 0.05 pu.
    - **SCR = 15, sabit.**
  - *Ölçüm yöntemi (s. 5–7):*
    - PCC'ye hibrit uyarım (hybrid excitation) ile PRBS bozucu sinyal enjekte ediliyor. d ekseni: derece 8, Fmax 1000 Hz. q ekseni: derece 7, Fmax 1020 Hz.
    - FFT ile Ydd, Ydq, Yqd ve Yqq hesaplanıyor; sonuç analitik küçük-sinyal modeliyle doğrulanıyor (Şekil 5).
    - Kontrolün admitansı belirlediği bant 1 Hz–1 kHz (s. 6).
  - *Kontrol yapıları (s. 4–5):*
    - GFL: pqGFL, pvGFL, viGFL.
    - GFM: vcGFM, ccGFM.
  - *Parametre aralıkları:*
    - GFL (Tablo 2, s. 8): ωp ve ωq [6, 38] rad/s; ωv [3, 15] rad/s; PLL ωn [50, 1500] rad/s (ξ = 1); ωcc [1200, 3000] rad/s; gecikme 50–200 µs.
    - GFM (Tablo 3, s. 9): H [0.5, 5] s; ξ [0.7, 4]; TVR ωf 60 rad/s, R 0.09; QSEM ωLPF 83 rad/s; ωcc [1200, 3000] rad/s; gecikme 50–200 µs.
    - Çalışma noktası (s. 8): P −1…1 pu; Q −0.4…0.4 pu; gerilim ±%10.
  - *Boyut (s. 9–11):*
    - Her mod için 5000 örnek. GFM için vcGFM + ccGFM, GFL için pvGFL + pqGFL.
    - Genelleme testi için ayrıca 2500 viGFL örneği.
    - Aalborg Üniversitesi verisinden her mod için 100 test örneği.
    - Her örnek yaklaşık 300 sütunluk bir spektrum vektörü (Şekil 8). Çapraz eksenler (Ydq, Yqd) kullanılmamış.
  - *Erişim:* Veri ve kod yayımlanmamış.
- **Yöntem (s. 9–10):**
  - Modeller: DT (max_depth = 6), RF (100 ağaç), LR, SVM (lineer), KNN (k = 20), XGB, Naive Bayes.
  - Normalizasyon ve %80/%20 bölme. "100 koşu üzerinden ortalama çapraz doğrulama skoru" raporlanıyor.
  - Metrik: accuracy. Ayrıca özellik önemleri inceleniyor (Şekil 9, s. 11).
- **Ana bulgular (doğruluk, %):**

  | Test | LR | RF | DT | NBC | XGB | SVM | KNN |
  |---|---|---|---|---|---|---|---|
  | Eğitimdeki yapılar (Tablo 4, s. 10) | 96 | 98 | 92 | 92 | 95 | 96 | 96 |
  | Görülmemiş viGFL, 2500 örnek (Tablo 5, s. 11) | 85 | 92 | 40 | 82 | 79 | 84 | 84 |
  | Aalborg verisi (s. 11) | 92 | 95 | 83 | 93 | 87 | 94 | 94 |

  - viGFL, pqGFL'den yalnızca aktif güç döngüsünde ayrılıyor; bu fark dd ekseninde 1–50 Hz arasındaki admitansı değiştiriyor (s. 10).
  - DT kararını tek bir frekans sütununa dayandırıyor. RF önemi birçok sütuna yayıyor ve bu yüzden daha iyi genelleşiyor (s. 11).
- **Metodoloji eleştirisi:**
  1. **Olumlu:** Bir kontrol yapısını dışarıda bırakan (leave-one-structure-out) genelleme testi ve harici bir veri seti var. Bu, gruptaki en yararlı protokol fikri.
  2. **viGFL testi tek sınıflı:** Test örneklerinin hepsi GFL, yani "accuracy" aslında GFL'yi yakalama oranı. GFL'ye yanlı bir model bu testte yüksek skor alır. Dengeli metrik ya da karışıklık matrisi yok. Ayrıca yalnızca bir GFL yapısı dışarıda bırakılmış; hiçbir GFM yapısı dışarıda bırakılmamış.
  3. **Protokol belirsiz:** Hem 80/20 bölmeden hem "100 koşu ortalama CV"den söz ediliyor. Hiperparametrelerin nasıl seçildiği yazmıyor.
  4. **Raporlama hataları:**
     - Tablo 4'te XGB için "kernel=linear" yazıyor; XGBoost'ta böyle bir parametre yok, muhtemelen kopyalama hatası.
     - Ölçüm aralığı "1 Hz–800 KHz" olarak verilmiş (s. 5); muhtemelen yazım hatası.
     - Yapının adı bir yerde "cvGFM", başka yerde "vcGFM".
  5. **Gerçekçilik sınırlı:** SCR ve filtre sabit, ölçüm gürültüsü yok.
  6. **Sızıntı riski düşük-orta:** Her örnek bağımsız bir parametre çekiminden geliyor. Ancak aynı yapıya ait birbirine yakın parametreli örnekler hem eğitim hem testte bulunuyor.
- **Projeyle bağlantı:**
  - **İP1:** Tablo 2 ve 3'teki aralıklar (bant genişlikleri, PLL, 50–200 µs gecikme, H), küme tabanlı tasarımda evirici belirsizlik kümelerine (uncertainty sets) gerçekçi bir başlangıç verir. Makale, 1 Hz–1 kHz arasındaki admitansın kontrol yapısına bağlı olduğunu gösteriyor. Dolayısıyla yardımcı sinyalin evirici tarafında nasıl "görüneceği" de kontrol moduna bağlı; tasarım modeli bu belirsizliği kapsamalı.
  - **İP2:** EMT modelinde çeşitlendirme için hazır yapı listesi: GFL (pq/pv/vi) ve GFM (vc/cc).
  - **İP3:** Kontrol yapısını dışarıda bırakarak değerlendirme. Öğrenilmiş dedektör bir evirici kontrol yapısıyla eğitilip başka bir yapıda test edilmeli.
  - **Kavramsal bağ:** PRBS enjeksiyonu bir aktif yoklama (active probing) tekniğidir; bizim yardımcı sinyalimizin kuzeni sayılır.
- **Açık sorular / araştırma fikirleri:**
  - **[EN UMUT VERİCİ]** Yardımcı negatif dizi enjeksiyonuna verilen tepkiden çevrimiçi (online) olarak negatif dizi admitansı ya da kontrol modu tahmin edilebilir mi? Aynı sinyal hem arıza tespiti hem evirici kimliklendirmesi için kullanılabilir mi?
  - Küme tabanlı garanti, Tablo 2–3 aralıklarındaki bütün GFL/GFM yapıları için geçerli kalıyor mu? Yoksa yapı değiştiğinde (ör. vi ile pq arasında) arıza ve normal kümeleri örtüşüyor mu?
  - Bu makale yalnızca dq çerçevesindeki admitansa bakıyor. Aynı analiz negatif dizi admitansı için yapılmalı.

---

## 3. Martinez-Velasco vd. (2025): YZ ile arıza tespiti, sınıflandırma ve konum belirleme taraması

- **Künye:**
  - Yazarlar: J. A. Martinez-Velasco, A. Serrano-Fontova, R. Bosch-Tous, P. Casals-Torrens (UPC ve UPC emeklileri, Reactive Technologies Ltd)
  - "Survey on Methods for Detection, Classification and Location of Faults in Power Systems Using Artificial Intelligence"
  - 2025. PDF Temmuz 2025 tarihli; kaynak erişim tarihleri Mayıs 2025. Yayın yeri PDF'te belirtilmemiş.
  - 44 sayfa, 549 kaynak.
- **Tek cümlede:** İletim ve dağıtım hatları ile kablolarında (AC ve DC) YZ tabanlı arıza tanılama (tespit + sınıflandırma + konum) literatürünü haritalayan, kaynakça ağırlıklı bir tarama; nicel karşılaştırma yapmıyor.
- **Problem ve bağlam:**
  - Akıllı şebeke, dağıtık üretim (DER) ve güç elektroniği korumaya yeni zorluklar getiriyor: dönüştürücü kaynakların sınırlı kısa devre akımı, istenmeyen ada modu, koordinasyon kaybı (s. 10).
  - Makalenin yapısı: Bölüm II YZ ve arıza tanılama kavramlarını tanımlıyor. Bölüm III YZ'nin güç sistemlerindeki uygulamalarını özetliyor. Bölüm IV arıza tanılama çalışmalarını tablolarla listeliyor. Bölüm V tartışma.
- **Veri:**
  - Taramanın kendine ait verisi yok.
  - Kaynak aralıkları: iletim [243–342], dağıtım [343–451], DC [459–490].
  - 2021 sonrasından seçilmiş çalışmalar: Tablo 4 (iletim, s. 17), Tablo 5 (dağıtım, s. 18–19), Tablo 6 (DC, s. 19).
  - Veri seti depoları [507–511] olarak listelenmiş (s. 21). Örnekler: INL "Power System Waveform Datasets for Machine Learning" (2024), Gillioz vd. 2025 (Sci. Data).
- **Yöntem:**
  - Anlatısal (narrative) bir tarama; seçim ölçütleri açık değil. Yazarlar da "seçimin nasıl yapıldığı tartışmaya açıktır" diyor (s. 20).
  - Tablolar yalnızca yazar, yıl, görev ve tekniği veriyor. Doğruluk, veri boyutu, bölme yöntemi ya da gecikme bilgisi yok.
- **Ana bulgular (nitel):**
  - İletim hattında açma kararı bir çevrimden (one cycle) kısa sürede verilmeli. Arıza yer bulucular (fault locator) ise çevrimdışı çalışıyor (s. 14).
  - Arıza direnci (Rf) çok büyükse mesafe rölesi hiç çalışmayabilir. Havai hatlarda en sık görülen arıza toprak arızası (s. 15).
  - Sınıflandırmadan bağımsız arıza tespit yöntemleri negatif dizi bileşenlerini ya da dalgacık (wavelet) parametrelerini kullanıyor (s. 14).
  - Çalışmaların büyük kısmı iki uçlu bir hat modeli ya da küçük bir IEEE test sistemi üzerinde yapılmış. Açık veri (ör. Kaggle) kullanan çalışma az. Tespit, sınıflandırma ve konumun üçünü birden yapan çalışma az. En yaygın yöntem grubu denetimli ML (NN, SVM, DT) (s. 15–16).
  - Simülasyonlar çoğunlukla MATLAB/Simulink ya da EMTP türü araçlarla (ATP, PSCAD) yapılmış. Bunların hepsi frekansa bağlı hat modeli gibi doğru modelleri kullanmıyor (s. 16).
  - Pek çok çalışmada ölçü transformatörleri (CT/VT) modellenmemiş; sonuçlara dikkatle yaklaşılmalı (s. 20, madde 8).
  - Basit bir sistem modelinde iyi çalışan yöntem "kazanan" ilan edilmemeli (s. 21, madde 13).
  - Pratik ve verimli bir tam arıza tanılama sistemi kısa vadede mümkün görünmüyor (s. 22).
- **Metodoloji eleştirisi:**
  - Tarama değerlendirme protokolünü hiç ele almıyor. Veri sızıntısı, bölme türü, güvenlik (security) metrikleri, arıza dışı olaylar, nedensellik ve gecikmenin nasıl ölçüldüğü tartışılmıyor.
  - IBR'ye özgü koruma sorunları (akım sınırlama, negatif dizi kontrolü) yalnızca genel bir paragrafta geçiyor.
  - Bazı genel YZ ifadeleri tartışmalı. Örneğin "DL modelleri tipik olarak yüzlerce ya da binlerce katman kullanır" (s. 5).
  - Sistematik tarama protokolü (PRISMA vb.) kullanılmamış.
- **Projeyle bağlantı:**
  - İlgili çalışmalar (related work) bölümü için bağlam kaynağı.
  - CT/VT'nin modellenmemesi ve küçük test sistemleri üzerine yapılan eleştiri, İP2–İP3'teki "gerçekçi ölçüm zinciri" kuralımızı destekliyor.
  - Bir çevrim gereksinimi İP4'ün gecikme bütçesini destekliyor.
  - Yeniden kullanılabilir veri ya da protokol yok.
- **Açık sorular / araştırma fikirleri:**
  - Tablo 4–5'teki 2021+ çalışmalardan küçük bir alt küme seç (ör. 10 makale). Her biri için "simülasyon düzeyinde bölme, security metriği, CT modeli ve gecikme ölçümü raporlanmış mı?" kontrol listesini doldur. Bu, literatür bölümünde nicel bir boşluk iddiasını destekleyecek iyi bir öğrenci görevi olur.
  - Taramanın işaret ettiği açık veri depolarında (INL raporu, Gillioz vd.) IBR içeren nokta-dalga verisi var mı? Kontrol edilmeli.

---

## 4. Oelhaf, Kordowich vd. (2026): PROTECT-90 arıza veri seti

- **Künye:**
  - Yazarlar: J. Oelhaf, G. Kordowich (eşit katkı), C. Bergler, A. Maier, J. Jäger, S. Bayer (FAU Erlangen-Nürnberg, OTH Amberg-Weiden)
  - "PROTECT-90: A Fault Dataset for Power System Protection"
  - arXiv:2606.24298v1 (eess.SP), Haziran 2026, © 2026 IEEE. EvEMTBench makalesinin kaynakçasında "ISGT Europe [Accepted]" olarak geçiyor.
  - 6 sayfa
- **Tek cümlede:** 90 kV'luk, çift hatlı, 3 baralı standart bir topolojide alan rastgeleleştirmesiyle (domain randomization) üretilmiş 9,022 EMT kısa devre bölümünü (episode) yayımlıyor. Her bölüm 8 röle konumunda 6.4 kHz ham dalga biçimi ve makinece okunur metaveri içeriyor; lisans CC BY 4.0.
- **Problem ve bağlam:**
  - Koruma alanındaki ML çalışmaları çoğunlukla kapalı modellerle yapılıyor. Atıf yapılan bir kapsam taramasına (scoping review) göre çalışmaların yalnızca %3.4'ü verisini yayımlamış ya da açık veri kullanmış (s. 1).
  - Mevcut açık kaynaklar ya ölçülmüş kayıtlar (SoCal, RTE, GESL) ya da parametre sınırları belgelenmemiş simülasyonlar (IRTSD) (Tablo I, s. 3).
- **Veri:**
  - *Şebeke (Şekil 1, s. 2):*
    - 90 kV, Bara 1–3, iki paralel koridor (Hat 1–2 A/B ve Hat 2–3 A/B).
    - Bara 1 ve Bara 3'te harici şebeke eşdeğeri; Bara 2 ve Bara 3'te yük.
    - Topoloji değişimi: B hatları ve Bara 3'teki harici şebeke, senaryoların yaklaşık yarısında devre dışı (s. 4).
  - *Simülasyon (s. 3):*
    - DIgSILENT PowerFactory EMT, sabit adım 10 µs.
    - 0.1 s ısınmadan sonra 1 s kaydediliyor.
    - Örnekleme 6,400 Hz; 50 Hz'de çevrim başına 128 örnek. Bölüm başına 6,400 örnek.
  - *Ölçüm:*
    - Her hat ucunda 3 faz gerilim ve akım: 8 röle × 6 = 48 kanal.
    - **CT/VT modeli yok.** Makaleye göre sinyaller "ideal birincil (primary)" büyüklükler (s. 3).
    - Ancak aynı sayfada sinyallerin "secondary voltage (V) and current (A)" olduğu da yazıyor ve Şekil 2 kV/kA gösteriyor. **Metin kendi içinde çelişkili.**
  - *Rastgeleleştirme aralıkları (Tablo II, s. 3):*
    - Arıza: **Rf 0.1–10 Ω**, başlangıç anı tf 0.2–0.5 s.
    - Hat: uzunluk 10–60 km, R′ 0.01–0.20 Ω/km, X′ 0.35–0.45 Ω/km, C′ 8.5–10 nF/km.
    - Yük: P 20–50 MW, Q −20…20 Mvar.
    - Harici şebeke: Sk″ 90–1000 MVA, V 0.95–1.05 pu, gerilim açısı −180…180°.
    - Ek kısıtlar: hat R/X oranı [0.05, 0.5] içinde olmalı; yük akışı yakınsamayan kombinasyonlar atılıyor.
  - *Arıza tipleri ve dağılım (s. 4):*
    - SLG, LL, LLG, LLL; tipler yaklaşık dengeli.
    - Arıza konumu hat boyunca yaklaşık düzgün dağılmış.
    - A koridorlarının her biri verinin yaklaşık %35'i, B koridorlarının her biri yaklaşık %15'i.
  - *Arıza dışı veri:* **"9,022 fault scenarios without a non-fault class"** (s. 4). Arızasız bölüm, anahtarlama, inrush ya da motor yolverme yok.
  - *IBR:* Modellenmemiş. Sk″ aralığının bilerek düşük tutulmasıyla "gelecekte IBR'ler nedeniyle düşecek arıza seviyesi" temsil ediliyor (s. 3).
  - *Arıza süresi:* Tablo II'de yok. Ama Şekil 2'deki örnekte arıza 0.458 s'de başlıyor ve 0.688 s'de kaldırılıyor (s. 4). Yani sürenin nasıl belirlendiği belgelenmemiş.
  - *Erişim (s. 4–5):*
    - Zenodo DOI 10.5281/zenodo.18418330, **CC BY 4.0**.
    - 12.5 GB sıkıştırılmış, açılınca yaklaşık 31 GB.
    - Her bölüm bir .pkl dosyası (pandas, float32, 49 sütun). Ayrıca 7.3 MB'lık metaveri CSV'si: `sample_id`, `sc_type`, `phase_select`, `fault_target`, `sc_location`, Rf, tf, şebeke parametreleri, topoloji bayrakları.
- **Yöntem:** Bu bir veri makalesi; model eğitilmiyor. Önerilen görevler: arıza sınıflandırma, arızalı hattın tanımlanması, konum regresyonu, alan kayması (domain shift) analizi (s. 5).
- **Ana bulgular:**
  - Hazır bir train/test bölmesi yok; bölüm düzeyinde (episode-wise) bölme öneriliyor. Makaleye göre aynı bölümden alınan kayan pencereler eğitim ve teste dağıtılmamalı, aksi halde zamansal sızıntı (temporal leakage) olur (s. 4–5).
  - Veri yalnızca arıza içerdiği için tespit görevlerinde pencereleme ve etiketleme varsayımları açıkça tanımlanmalı (s. 5).
- **Metodoloji eleştirisi:**
  1. **Güvenlik test edilemez.** Arıza dışı olay da arızasız bölüm de yok. "Arıza yok" örnekleri ancak aynı bölümün arıza öncesi kısmından çıkarılabilir. Bu setle yanlış açma (false trip) oranı ölçmek anlamsız.
  2. **Yüksek Rf yok.** Rf yalnızca 0.1–10 Ω. IBR'li sistemlerde ve mesafe korumasında kritik olan onlarca ohm'luk arızalar kapsanmıyor.
  3. **IBR yok.** Sk″'si düşük bir Thevenin kaynağı IBR'nin akım sınırlamasını, negatif dizi kontrolünü ve FRT davranışını temsil etmez. Bu set "IBR'ye hazır" sayılmamalı.
  4. **Ölçüm zinciri ideal.** CT/VT/CCVT, anti-aliasing filtre ve gürültü yok; birincil/ikincil ifadesi de çelişkili.
  5. **Frekans uyumsuz.** Şebeke 50 Hz; bizim proje 60 Hz.
  6. **Tek topoloji.** Topoloji bilerek sabit tutulmuş; topolojiler arası genelleme test edilemez.
  7. **Olumlu yönler:** Bölüm düzeyinde bölme önerisi, açıkça belgelenmiş parametre sınırları, metaveri şeması ve açık lisans.
     - Dikkat: her bölümde 8 röle var. Röle başına örnekler bağımsız sayılırsa aynı bölüm hem eğitime hem teste düşer. Gruplama `sample_id` ile yapılmalı.
- **Projeyle bağlantı:**
  - **İP3:** Değerlendirme hattımızı (bölüme göre gruplanmış CV, pencereleme, metrikler) gerçek bir açık veri setinde "kuru çalıştırma" (dry run) ile test etmek için kullanılabilir. Konvansiyonel mesafe elemanını öğrenilmiş dedektörlerle karşılaştıracak iskelet burada kurulabilir.
  - **İP2:** Metaveri şeması (CSV, `sample_id`, tüm rastgele parametreler, topoloji bayrakları) ve parametre sınırları tablosu, kendi veri setimiz için şablon.
  - Yardımcı sinyal içeren veri değil; doğrudan kullanılamaz.
- **Açık sorular / araştırma fikirleri:**
  - **[EN UMUT VERİCİ]** Aynı belgeleme standardında bir "kardeş" veri seti üret: 60 Hz, IBR'ler optimal negatif dizi yardımcı sinyalini enjekte ediyor, CT/CCVT modelleri var, arıza dışı olaylar ve yüksek Rf'li arızalar var. İP2 çıktısı olarak açık lisansla yayımlanabilir.
  - PROTECT-90 üzerinde konvansiyonel mesafe elemanının (quadrilateral/mho) Rf ve Sk″'ye bağlı doğruluğu. Makalelerde öğrenilmiş modellerle karşılaştırılmamış; kolay bir taban çizgisi çalışması.

---

## 5. Kordowich vd. (2026): EvEMTBench, arıza ve olay simülasyon veri seti

- **Künye:**
  - Yazarlar: G. Kordowich, J. Loebel, J. Oelhaf, A. Maier, S. Bayer, C. Bergler, J. Jaeger (FAU, OTH Amberg-Weiden)
  - "A simulation based dataset of faults and events for machine learning in power systems"
  - arXiv:2608.19777v1 (eess.SY), Ağustos 2026. Scientific Data tarzı bir "data descriptor" yapısında; yayın yeri belirtilmemiş.
  - 33 sayfa
- **Tek cümlede:** PowerFactory EMT ile hem 4 literatür şebekesinde hem de rastgele üretilmiş sentetik şebekelerde (20/110/345 kV, 50 ve 60 Hz) 22 olay tipi simüle ediliyor. Olaylar arızaları, yüksek empedanslı arızayı (HIF), ark arızasını, başlangıç halindeki (incipient) arızayı ve anahtarlama, inrush, motor yolverme gibi arıza dışı olayları kapsıyor. Ölçümler 9.6 kHz nokta-dalga. Veri üç türde (benchmark / adaptgrid / multigrid) alt setler halinde açık.
- **Problem ve bağlam:**
  - Açık veri eksikliği. Atıf yapılan taramaya göre 119 makaleden yalnızca %1.7'si verisini yayımlamış (s. 1).
    - Not: PROTECT-90 aynı taramadan %3.4 alıntılıyor. Muhtemelen tanım farkı var: "verisini yayımlayan" ile "verisini yayımlayan ya da açık veri kullanan".
  - Tek bir şebekede eğitip aynı şebekede test etmek gerçeğe genellenmiyor. Hedef, alan rastgeleleştirmesiyle topolojiler arası (cross-topology) genelleme (s. 3–5).
- **Veri:**
  - *Simülasyon (s. 3):*
    - PowerFactory EMT, adım 10 µs. Her simülasyon 1.5 s; ilk 1.0 s atılıyor, son 0.5 s dışa aktarılıyor.
    - Örnekleme 9600 Hz; pencere uçları dahil T = 4801 örnek. 60 Hz'de bu çevrim başına 160 örnek demek (hesap).
    - Her ölçüm noktasında ("cubicle") 3 faz-toprak gerilimi ve 3 faz akımı.
    - Modelleme "Group I" frekansları (0.1 Hz–3 kHz) için doğru olacak şekilde yapılmış (s. 3).
  - *Olay zamanı:* Olay başlangıcı U[1.1, 1.3] s (Tablo 2, s. 15). Bu, kaydedilen pencerede 100–300 ms arıza öncesi veri bulunduğu anlamına geliyor (hesap). Nedensel değerlendirme için uygun.
  - *Üç alt set türü (s. 4–5, s. 24):*
    - **benchmark:** 4 sabit şebeke; olay parametreleri ayrık değerler alıyor (ör. konum {1, 20, 50, 80, 99}%).
    - **adaptgrid:** Aynı 4 şebeke; yükler %50–150 arasında ölçekleniyor, olaylar rastgele. Her şebekede 10,000 olay.
    - **multigrid:** Her gerilim seviyesi için 105 rastgele topoloji ve 10,000 olay.
    - Başarısız simülasyonlar atıldığı için her set "10,000'den biraz az" simülasyon içeriyor (s. 3). Toplam 11 adet .tar.gz arşiv var (s. 24).
    - Toplam simülasyon sayısı açıkça verilmemiş; en fazla yaklaşık 110,000 olmalı (çıkarım).
  - *Şebekeler (s. 5):*
    - CIGRE MV Avrupa (20 kV, 14 bara)
    - Protection Reference Grid (110 kV)
    - IEEE 39-bara (345 kV; **setteki tek 60 Hz şebeke**)
    - Simple Double Line (110 kV)
  - *Olaylar (Tablo 1, s. 7):* 22 tip. Bunların 13'ü arıza dışı, 9'u arıza.
    - Arıza dışı olaylar: yük açma/kapama; kondansatör açma/kapama; havai hat enerjilendirme/kesme; kablo enerjilendirme/kesme (yalnızca OG); AG ve YG taraflı transformatör inrush; motor yolverme (yalnızca OG); senkron makine açması; IBR açması.
    - Arızalar: 1PHG, arklı 1PHG, 2PH, 2PHG, 3PH; HIF ve arklı HIF (yalnızca OG); incipient arıza ve arklı incipient arıza.
  - *Arıza parametreleri (Tablo 2, s. 15):*
    - Kısa devre Rf 0.001–50 Ω.
    - HIF direnci 50 Ω–150 kΩ. Dört aralıkta örnekleniyor (50–500, 500–5000, 5000–50,000, 50,000–150,000 Ω); aralıklar eşit olasılıklı (s. 7).
    - Incipient arıza süresi 0.002–0.08 s.
    - Ark için Kizilcay modeli kullanılıyor (s. 14, Tablo 18).
  - *IBR modeli (s. 12–13; Tablo 15, s. 22):*
    - **Yalnızca GFL.** Anahtarlamasız ortalama model: ideal AC gerilim kaynağı.
    - DDSRF-PLL ile pozitif ve negatif dizi ayrıştırması yapılıyor.
    - Kontrol: aktif güç kontrolü + frekans desteği, reaktif güç kontrolü + gerilim desteği, pozitif ve negatif dizi FRT. Negatif dizi FRT, dengesiz arızada endüktif reaktif akım enjekte ediyor.
    - Faz akım sınırı 1.2 pu. Sınıra ulaşıldığında öncelik sırası: (i) pozitif ve negatif dizi reaktif akım (eşit ve en yüksek), (ii) pozitif dizi aktif akım (en düşük). Pozitif ve negatif dizi reaktif akım referanslarının oranı korunuyor.
    - Güçler: OG'de 1–15 MVA, YG'de 20–50 MVA. P ayarı 0.1–0.9 pu.
  - *IBR'lerin yeri (Tablo 3, s. 15):* OG'de baraların yaklaşık %20'sinde IBR. 110 kV'ta kaynaklar {senkron, IBR}. 345 kV'ta yalnızca senkron makine.
  - *Diğer modeller (s. 8–14):* Frekansa bağlı ULM hat ve kablo modeli, doygunluklu transformatör, AC1A uyarma sistemi, ZIP yük, topraklama (direkt, dirençli, rezonanslı).
  - *Ölçüm zinciri:* Makalede CT/VT modeli ya da ölçüm gürültüsünden söz edilmiyor. CSV'deki alan adı "c:Isec:A" olsa da bir ölçü trafosu modeli tarif edilmemiş.
  - *Etiketler (s. 24–25):*
    - `settings_clean.csv`: olay tipi, başlangıç anı, hedef eleman, konum, Rf, HIF direnci, faz seçimi, incipient süresi, rastgele eleman parametreleri.
    - Ayrıca NetworkX graf dosyası ve PowerFactory .pfd topolojisi.
  - *Erişim:* FAUDataCloud bağlantısı (s. 27). **Lisans makalede belirtilmemiş.**
- **Yöntem:** Model eğitilmiyor. "Teknik doğrulama" görsel (Şekil 8–10, s. 25–27): RMS gerilim dağılımları, parametre dağılımları ve örnek dalga biçimleri.
- **Ana bulgular (s. 27):**
  - HIF'ler faz büyüklüklerinde zor fark ediliyor, ama sıfır dizide belirgin.
  - LL ve LLL arızalarında sıfır dizi bileşeni yok.
  - Anahtarlama olayları faz akımlarında belirgin.
  - Kullanım önerisi: adaptgrid için simülasyon düzeyinde, multigrid için topoloji düzeyinde bölme.
- **Metodoloji eleştirisi:**
  1. **En büyük artı:** Arıza dışı olaylar sayesinde güvenlik (security) testi yapılabiliyor. Ancak koruma bölgesi (zone) etiketi yok, yalnızca olayın hedef elemanı var. "Bu röle açmalı mı?" etiketini kullanıcı kendisi türetmeli.
  2. **Rf sınırı:** Kısa devrelerde Rf en fazla 50 Ω (HIF hariç). İletim seviyesinde mesafe koruması için daha yüksek dirençli toprak arızaları yok (bu benim yorumum).
  3. **IBR çeşitliliği sınırlı:** Yalnızca GFL var, GFM yok. 345 kV'ta hiç IBR yok.
  4. **Arıza temizleme belirsiz:** Kalıcı arızaların koruma tarafından temizlenip temizlenmediği anlatılmıyor; yalnızca incipient süresi tanımlı. Arızalar 0.5 s'lik pencere boyunca sürüyor gibi görünüyor.
  5. **Ölçüm zinciri idealleştirilmiş görünüyor:** CT/VT ya da gürültü tarif edilmemiş.
  6. **Kardeş simülasyon riski:** benchmark seti ayrık bir ızgaradan üretildiği için yalnızca tek parametresi farklı kardeş simülasyonlar içeriyor. Rastgele bölünürse sızıntı olur. Makale bu seti yalnızca test için önerdiğinden doğru kullanımda sorun yok, ama dikkat gerekiyor.
  7. **Doğrulama zayıf:** Lisans belirsiz. Teknik doğrulama yalnızca görsel ve literatürle tutarlılığa dayanıyor; ölçülmüş verilerle nicel karşılaştırma yok.
  8. **Zorluk bilinmiyor:** Hiç model sonucu verilmediği için veri setinin ne kadar zor olduğu bilinmiyor.
- **Projeyle bağlantı:**
  - **İP3:** Güvenlik test seti için en iyi açık kaynak. Özellikle IEEE 39-bara (60 Hz) ve IBR'li 110 kV şebekeleri değerli. Konvansiyonel elemanların ve öğrenilmiş dedektörlerin inrush, kondansatör anahtarlama, motor yolverme ve IBR açması altındaki yanlış açma oranı ölçülebilir. Bu, yardımcı sinyal olmadan bir taban çizgisi verir.
  - **İP2:** Tablo 1'deki olay listesi ve Tablo 2–18'deki parametre aralıkları kendi EMT senaryo üretecimiz için doğrudan şablon. GFL IBR kontrolünün tarifi (negatif dizi FRT + akım sınırlama öncelikleri), yardımcı sinyalin FRT'nin negatif dizi enjeksiyonuyla nasıl bir arada var olacağını düşünmek için kritik.
  - **Değerlendirme protokolü:** Simülasyon ve topoloji düzeyinde bölme önerisi kurallarımıza giriyor.
- **Açık sorular / araştırma fikirleri:**
  - **[EN UMUT VERİCİ] Yardımcı sinyal ile şebeke kodu negatif dizi FRT'si nasıl etkileşir?** Dengesiz arıza sırasında evirici zaten negatif dizi akımı basıyor. Optimal yardımcı sinyal bu enjeksiyonla çakışır mı? 1.2 pu akım sınırı içinde ikisi nasıl paylaştırılmalı?
  - **Topolojiyi dışarıda bırakarak değerlendirme (leave-topology-out):** Küme tabanlı garanti modele bağlı. Öğrenilmiş dedektörler topoloji değişimine ne kadar dayanıyor? multigrid fikriyle kendi küçük topoloji ailemizi üretebiliriz.
  - EvEMTBench olaylarını bir CT/CCVT modelinden geçirerek ölçüm zincirinin etkisini ölçmek.

---

## 6. Oelhaf vd. (2025/2026): Arıza sınıflandırma ve konum için ML modellerinin kontrollü karşılaştırması

- **Künye:**
  - Yazarlar: J. Oelhaf, G. Kordowich, C. Kim, P. A. Pérez-Toro, C. Bergler, A. Maier, J. Jäger, S. Bayer
  - "Controlled Comparison of Machine Learning Models for Fault Classification and Localization in Power System Protection". Dosya adı "Benchmarking…" olsa da makalenin başlığı bu.
  - arXiv:2510.00831v2 (cs.AI), 18 Haziran 2026 (v1 2025). EvEMTBench kaynakçasında "ISGT Europe 2026 [Accepted]".
  - 5 sayfa
- **Tek cümlede:** PROTECT-90 üzerinde, aynı algılama, zamanlama ve doğrulama koşullarında, 10–50 ms karar pencereleriyle birçok scikit-learn modeli arıza sınıflandırma (FC) ve arıza konumu (FL) için karşılaştırılıyor. FC'de MLP 10 ms'de bile F1 ≈ 0.99'a ulaşıyor. FL'de en iyi modeller bile hat uzunluğunun yaklaşık %10'u kadar bir MAE'de takılı kalıyor.
- **Problem ve bağlam:** Literatürdeki skorlar farklı veri, algılama ve karar ufku varsayımlarıyla elde edildiği için karşılaştırılamıyor. Makalenin örneğiyle: basit radyal fiderde %99 F1 ile gözlü (meshed) bir topolojide %90 F1 aynı zorluğu ifade etmiyor (s. 1).
- **Veri (s. 2):**
  - PROTECT-90: 9,022 bölüm, her biri 1 s, 6400 Hz, 90 kV çift hat.
  - Her bölümde arıza başlangıcının **±80 ms'si kesilip alınıyor**. Bu kesitte 5 ms adımla (stride) kayan pencereler çıkarılıyor.
  - Pencere boyutları ve sayıları (Tablo II):

    | Pencere | Örnek sayısı | Toplam pencere | Arıza içeren pencere |
    |---|---|---|---|
    | 10 ms | 64 | 279,682 | 9,022 |
    | 20 ms | 128 | 261,638 | 27,066 |
    | 30 ms | 192 | 243,594 | 45,110 |
    | 40 ms | 256 | 225,550 | 63,154 |
    | 50 ms | 320 | 207,506 | 81,198 |

  - Pencere uzadıkça arıza içeren pencerelerin payı %3.2'den %39.1'e çıkıyor.
- **Yöntem (s. 3–5):**
  - *Girdi:* 8 rölenin tüm 3 faz V ve I sinyalleri art arda ekleniyor. Bu, tüm röle ölçümlerine merkezi erişim varsayıyor; yazarlar bunu IEC 61850 mimarisinde bir "performans üst sınırı" olarak sunuyor. Girdi standardize ediliyor; özellik mühendisliği yok.
  - *FC görevi:* 11 sınıf. c0 "No Fault" ve 10 arıza tipi (AG, BG, CG, AB, BC, CA, ABG, BCG, CAG, ABC). Ana metrik makro F1.
  - *FL görevi:* Konumun hat uzunluğuna oranı (%0–100). Metrik MAE. Yalnızca arıza başlangıcını içeren pencereler kullanılıyor (ε = 5 µs).
  - *Modeller:* LG, Ridge, KNN, DT, ET, GB (histogram), RF, Stacking, Voting, MLP. Hepsi scikit-learn varsayılan hiperparametreleriyle. Eğitimi 24 saati aşan modeller çıkarılmış (SVC, Bagging, SGD, SVR, RF regresör vb.).
  - *Doğrulama:* **5 katlı çapraz doğrulama, simülasyon bölümüne göre gruplanmış (episode-grouped).**
  - *Gecikme ölçümü:* i7-13700HX tek çekirdek; 5000 iterasyon boyunca tek örnekli ileri geçiş. Yalnızca çıkarım (inference) süresi ölçülüyor.
- **Ana bulgular:**
  - FC, makro F1 (Tablo III, s. 4):

    | Model | 50 ms | 20 ms | 10 ms |
    |---|---|---|---|
    | MLP | 0.990 | 0.993 | 0.989 |
    | GB | 0.982 | 0.738 | 0.418 |
    | KNN | 0.863 | 0.799 | 0.738 |
    | RF | 0.838 | 0.771 | 0.292 |
    | ET | 0.431 | 0.162 | 0.098 |
    | Ridge | 0.089 | 0.095 | 0.097 |
    | LG | 0.071 | 0.090 | 0.104 |

  - FL, MAE (hat uzunluğunun %'si; Tablo IV, s. 4):

    | Model | 50 ms | 10 ms |
    |---|---|---|
    | Stacking | 9.676 | 10.304 |
    | MLP | 9.915 | 10.662 |
    | Voting | 10.623 | 10.943 |
    | GB | 14.658 | 14.646 |
    | KNN | 19.121 | 20.376 |
    | DT | 19.714 | 22.102 |
    | ET | 21.761 | 21.730 |

  - Hat bazında MAE (MLP, 50 ms; Şekil 2, s. 4): 1–2A 9.08, 1–2B 9.18, 2–3A 10.58, 2–3B 11.05.
  - Örnek başına çıkarım süresi (Şekil 3, s. 4; metin s. 5):
    - DT 0.04 ms, MLP 0.56 ms, GB 1.23 ms, ET 1.64 ms, Voting 2.88 ms, Stacking 2.95 ms, KNN 1287.53 ms.
    - Ön işleme 0.1 ms'den kısa. KNN hariç bütün işlem hattı 3.1 ms'nin altında.
- **Metodoloji eleştirisi:**
  1. **Olumlu:** Bölüme göre gruplanmış CV, sistematik pencere uzunluğu taraması, ortalama ± std ve bütün modeller için aynı koşullar. Bu gruptaki en temiz protokol bu.
  2. **Değerlendirmede gizli ileriye bakış (oracle hizalama).**
     - Her bölüm, gerçek arıza başlangıcına göre ±80 ms kesiliyor ve pencere ızgarası bu ana hizalanıyor.
     - Tablo II'den çıkarım: bölüm başına (160 − L)/5 + 1 pencere var. 10 ms için bu 31 eder ve 31 × 9,022 = 279,682.
     - 10 ms pencerelerde bölüm başına tam 1 arıza penceresi var. Bu, arıza başlangıcının her zaman pencerenin tam ortasına (5. ms) düştüğü anlamına geliyor.
     - Gerçek bir akışta (stream) başlangıç anı pencereye göre rastgele konumdadır. Bu hizalama sınıflandırıcıya bir "kısayol" verebilir; 10 ms sonuçları iyimser olabilir.
     - Bu benim çıkarımım; makale açıkça söylemiyor.
  3. **Etiket tanımı belirsiz.**
     - Sayılara bakılırsa "arıza içeren pencere", arıza başlangıcını içeren pencere demek.
     - Başlangıçtan sonra tamamen arıza süresi içinde kalan pencerelerin etiketi açık değil. Sayılara göre bunlar ya "No Fault" sınıfında ya da arıza sayısına dahil edilmemiş.
     - Sonuç: ölçülen şey, rölenin ihtiyaç duyduğu "arıza durumu" (fault state) sınıflandırması değil, "başlangıç geçici rejimi" (inception transient) sınıflandırması.
  4. **Güvenlik ölçülmüyor.** "No Fault" pencereleri yalnızca aynı arıza bölümlerinin arıza öncesi kısmından geliyor; anahtarlama ya da inrush yok. Yanlış açma oranı yok. Yalnızca makro F1 var; karışıklık matrisi yok, sadece "kalan hatalar nadir" deniyor.
  5. **Merkezi girdi.** 8 rölenin hepsinin ölçümü kullanıldığı için bu, tek uçlu yerel bir röle senaryosu değil. Sonuçlar mesafe rölesine doğrudan aktarılamaz.
  6. **Varsayılan hiperparametreler.** ET'nin 0.43 F1'i gibi sonuçlar modelin değil ayarların eseri olabilir. Model sıralaması ayara duyarlı.
  7. **Zayıf bir yorum.** "Paralel hat etkileşimi daha yüksek MAE'ye yol açıyor" yorumu zayıf. Hatlar arasındaki fark küçük (9.1–11.1). Üstelik B hatlarının veri payı daha düşük (~%15'e karşı ~%35); bu, sonucu karıştıran bir değişken.
  8. **Gecikme ölçümü eksik.** Masaüstü CPU'da yalnızca çıkarım süresinin ortalaması ölçülmüş. Gömülü kartta ölçüm, en kötü durum (WCET) ve sabit karar hızında verim (throughput) yok. Pencere uzunluğunun (10–50 ms) da toplam gecikmeye eklenmesi gerekir.
  9. **Veri setinden gelen sınırlar.** PROTECT-90'da olduğu gibi ölçüm zinciri ve IBR yok.
- **Projeyle bağlantı:**
  - **İP3:** Protokolümüz için en yakın şablon: bölüme göre gruplanmış K-katlı CV, pencere uzunluğu taraması, makro metrikler, model başına çıkarım süresi. Bizim protokole eklenmesi gerekenler: nedensel akış değerlendirmesi, rastgele başlangıç fazı, arıza dışı olaylar, yerel tek röle girdisi.
  - **İP4:** 0.04–3 ms'lik masaüstü değerleri, gömülü kartta yeniden ölçülmesi gereken bir başlangıç tahmini.
- **Açık sorular / araştırma fikirleri:**
  - **[EN UMUT VERİCİ] Pencere uzunluğuna karşı dependability/security eğrisi:** Aynı taramayı yardımcı sinyalli arızalar için 60 Hz'de 4–16.7 ms pencerelerle yap. Küme tabanlı testin garanti verdiği en kısa pencere, öğrenilmiş modelin ihtiyaç duyduğu pencereyle karşılaştırılabilir.
  - Aynı deneyi rastgele başlangıç ofsetiyle (oracle hizalamayı kaldırarak) tekrarla. 10 ms'deki F1 ne kadar düşüyor?
  - Yalnızca tek bir rölenin yerel V/I ölçümleriyle FC ve FL performansı ne olur?

---

## 7. Abukhousa, Zonouz, Meliopoulos (2026): Gecikme farkındalıklı DL kıyaslaması (evirici ağırlıklı şebeke, siber-fiziksel)

- **Künye:**
  - Yazarlar: E. Abukhousa, S. Zonouz, A. P. S. Meliopoulos (Georgia Tech)
  - "Latency-Aware Deep Learning Benchmark for Real-Time Cyber-Physical Attack and Fault Classification in Inverter-Dominated Power Grids"
  - arXiv:2605.17256v1 (eess.SY), Mayıs 2026. Yayın yeri belirtilmemiş.
  - 5 sayfa
- **Tek cümlede:** WinIGS'te üretilmiş, iki merging unit'ten (MU) 4.8 kHz'de örneklenmiş bir veri akışında 8 derin öğrenme mimarisi (MLP'den Transformer'a) arıza ve siber saldırı sınıflandırması için karşılaştırılıyor. Saldırılar CT/PT oran manipülasyonu ve GPS sahteciliği. Raporlanan "sınıflandırma zamanı" 3–15 ms, ama tek ileri geçişin gecikmesi 57–89 ms.
- **Problem ve bağlam:** Derin öğrenme çalışmaları statik veri setlerinde doğruluğa odaklanıyor; "gerçek zamanlı" iddiaları zamanlama analiziyle desteklenmiyor. Koruma ise 1–2 çevrimde (16–34 ms) karar gerektiriyor (s. 1).
- **Veri:**
  - *Simülatör (s. 2):* WinIGS (tescilli yazılım; kaynak 11). IEC 61850 Sampled Value (SV) akışı emüle ediliyor; CT ve PT'lerin sayısallaştırılmış çıkışları COMTRADE dosyalarından alınıyor. Bu, gruptaki ölçü trafosu çıkışı içeren tek veri; ancak CT/PT modelinin ayrıntısı verilmiyor.
  - *Şebeke (Şekil 1, s. 2):* "Evirici ağırlıklı mikroşebeke": 50 kVA PV eviricisi, 30 kVA batarya depolama (BESS), transformatörler, dağıtım hatları ve yükler. Koruma Bölgesi 2 (PZ-2), MU23 ve MU32 ile izleniyor. **Evirici kontrol tipi (GFL/GFM) belirtilmemiş.**
  - *Boyut (s. 2):* 22 s'lik simülasyonda 4.8 kHz'de 105,768 örnek (208 µs çözünürlük). 2 MU × 7 sinyal (Ia, Ib, Ic, In, Van, Vbn, Vcn) = 14 özellik.
  - *Sınıflar (Tablo I, s. 2):* Toplam 18 sınıf (özet "17 farklı arıza ve saldırı" diyor; normal işletme ayrı sınıf).
    - 0: normal işletme
    - 1–3: SLG; 5–7: LL; 9–11: DLG; 14–15: üç faz (ABC, ABC-N)
    - 4 ve 8: CT oran saldırısı; 12–13: PT oran saldırısı; 16–17: GPS sahteciliği
  - *Çeşitlilik:* Rf, arıza konumu, yük/çalışma noktası ve başlangıç açısının nasıl değiştirildiği anlatılmıyor. Şekil 1'de tek bir "temsili arıza konumu" var.
  - *Arıza dışı olay:* Anahtarlama, inrush ya da motor yolverme yok. Test akışında tek bir bölge dışı arıza var (Event 2'de Zone 1'de A-G arızası).
  - *Erişim:* Veri ve kod yayımlanmamış.
- **Yöntem:**
  - *Eğitim (s. 2):*
    - 50 örneklik diziler, adım 1 (stride 1).
    - Ölçekleyici yalnızca eğitim bölümüne uydurulmuş (fit).
    - "Katmanlı blok tabanlı" (stratified block-based) bölme: %70 eğitim / %10 doğrulama / %20 test.
    - Sınıf ağırlıkları, Adam, 40 epok, erken durdurma.
  - *Akış işleme (Denklem 1–2, Algoritma 1; s. 2–3):*
    - Her örnek için bir olasılık vektörü üretiliyor.
    - Bu vektörler bir çevrimlik **merkezli** hareketli ortalamayla düzleştiriliyor (N_cyc = 80, N_half = 40). Yazarların kendi ifadesiyle bu "≈8.3 ms ileriye bakma (look-ahead)" demek.
    - Güven 0.6'nın (τ) altındaysa model çekimser kalıyor (abstain) ve −1 çıktısı veriyor.
  - *Metrikler (s. 3):*
    - Accuracy.
    - Kapsama (coverage): çekimser kalınmayan örneklerin oranı.
    - Sınıflandırma zamanı T_cls: olay başlangıcından ilk doğru etikete kadar geçen süre.
    - Çıkarım gecikmesi T_inf: bir ileri geçişin ortalama süresi.
  - *Test akışları (Tablo III, s. 3):*
    - Event 1: SLG A-N, LL B-C, DLG AC-N, CT saldırısı (MU32), PT saldırısı (MU23). Her olay 0.2 s; 1.0–5.2 s arası.
    - Event 2: ABC, ABC-G, GPS saldırısı (MU32) ve Zone 1'de A-G arızası.
    - Event 1 100 kez koşturulmuş (s. 4).
  - *Donanım (s. 4):* Google Colab. 1 fiziksel çekirdek / 2 iş parçacığı, 2.2 GHz; 12.67 GB RAM; Tesla T4 GPU; TensorFlow 2.19.0.
- **Ana bulgular:**
  - Eğitim performansı (Tablo II, s. 3):

    | Model | Accuracy (%) | Balanced acc. (%) | Macro F1 (%) | Parametre |
    |---|---|---|---|---|
    | MLP | 99.66 | 99.88 | 99.53 | 157,394 |
    | 1D-CNN | 98.89 | 99.77 | 98.71 | 285,842 |
    | CNN-LSTM | 97.13 | 99.65 | 96.84 | 542,290 |
    | LSTM | 97.09 | 99.64 | 96.79 | 279,826 |
    | ResNet1D | 96.21 | 99.52 | 95.87 | 977,106 |
    | ST-GCN | 95.89 | 99.49 | 95.52 | 67,730 |
    | Transformer | 95.37 | 99.88 | 95.00 | 36,434 |
    | TCN | 94.32 | 99.35 | 93.93 | 195,136 |

  - Ham çıktı titrek (jitter). Bir çevrimlik ortalama ve güven eşiği çıktıyı kararlı hale getiriyor (Şekil 2, s. 4).
  - CT oran saldırısında MLP ve Transformer 10 ms'nin altında tepki veriyor; LSTM ve CNN-LSTM 50 ms'den fazla gecikiyor (s. 3).
  - Event 1, 100 koşu (Tablo IV, s. 4):

    | Model | Accuracy (%) | Coverage (%) | Ort. sınıflandırma zamanı (ms) | Ort. gecikme (ms) |
    |---|---|---|---|---|
    | 1D-CNN | 95.73 | 96.67 | 8.54 | 70.22 |
    | CNN-LSTM | 92.59 | 97.34 | 14.83 | 69.64 |
    | LSTM | 93.40 | 89.41 | 12.63 | 58.25 |
    | MLP | 97.57 | 97.57 | 3.38 | 57.20 |
    | ResNet1D | 95.03 | 96.11 | 5.29 | 72.42 |
    | ST-GCN | 96.44 | 96.59 | 4.25 | 88.89 |
    | TCN | 90.88 | 92.50 | 4.17 | 61.68 |
    | Transformer | 96.86 | 97.15 | 6.29 | 67.77 |

  - Bölge dışı SLG arızası bilinen bir sınıf olarak etiketlenmiyor; güven düşüyor ve model −1 veriyor (s. 4).
- **Metodoloji eleştirisi:**
  1. **Nedensel değil.** Merkezli ortalama 40 örnek (8.3 ms) ileriye bakıyor. T_cls (3–15 ms) sinyal zaman ekseninde ölçülüyor. Gerçek karar zamanı en az T_cls + 8.3 ms + hesaplama süresi olmalı (çıkarım).
  2. **Gecikme ölçümü karar hızıyla uyumsuz.**
     - Algoritma her örnekte bir ileri geçiş istiyor; 4.8 kHz'de bu her 208 µs'de bir demek.
     - Ölçülen ileri geçiş süresi 57–89 ms. Bu, gerçek zamanlı akıştan yaklaşık 275–430 kat yavaş (hesap).
     - Yani "çevrim altı sınıflandırma" gerçek zamanlı bir sistemin değil, çevrimdışı tekrar oynatmanın (offline replay) sonucu.
     - Ölçüm paylaşımlı bir VM olan Colab'da yapılmış. CPU/GPU kullanımı ve framework'ün çağrı yükü birbirinden ayrılmamış. Yalnızca ortalama raporlanmış; kuyruk değerleri (p99, WCET) yok.
  3. **Sızıntı riski yüksek.**
     - Bütün veri tek bir 22 s simülasyondan geliyor.
     - Adım 1 ile çıkarılan 50 örneklik pencereler %98 örtüşüyor.
     - "Blok tabanlı" bölmede blok sınırları ve bloklar arası boşluk (gap) tarif edilmemiş.
     - Muhtemelen her arıza tipinin tek bir örneği var. Bu durumda test kümesi, eğitimdeki aynı olayların başka parçalarından oluşuyor (çıkarım).
     - Test akışlarının (Event 1/2) eğitimden bağımsız simülasyonlar olup olmadığı belirtilmemiş.
  4. **Çeşitlilik yok.** Rf, konum, yük ve başlangıç açısı değişimi tanımlanmamış. Yazarlar da farklı yük senaryolarında yeniden eğitim gerektiğini ve arıza koşullarının çeşitlendirilmesi gerektiğini sınırlılık olarak kabul ediyor (s. 4).
  5. **Güvenlik ölçülmüyor.** Arıza dışı olay yok. Tablo II'de accuracy, balanced accuracy'den düşük; bu da hataların büyük sınıflarda yoğunlaştığını gösterir. En büyük sınıf muhtemelen "normal"; bu, yanlış alarm (false trip) eğilimine işaret eder (çıkarım). Yanlış açma oranı ayrıca raporlanmıyor.
  6. **Tutarsızlıklar.**
     - Metinde MLP için "49k parametre" deniyor; Tablo II'de 157,394 yazıyor (s. 3).
     - Transformer satırı (accuracy 95.37, balanced accuracy 99.88), 18 sınıfla aynı tahminler üzerinden hesaplandıysa matematiksel olarak mümkün değil. Balanced accuracy %99.88 ise accuracy en az yaklaşık %97.8 olmalı (hesap: 1 − 18 × 0.0012).
     - Tablo I ile Tablo III'teki sınıf numaraları uyuşmuyor gibi görünüyor. Örneğin Tablo I'de CT saldırısı "4, 8 (MU23, MU32)" iken Tablo III'te "CT Attack MU32 (4)".
  7. **Bölge dışı arıza sonucu koruma açısından muğlak.** Bölge dışı arızada doğru çıktı "açma" değil, "açmama" (no-trip) olmalı. Çekimser çıktının (−1) açma mantığında neye karşılık geldiği tanımlanmamış.
  8. **Tekrarlanabilirlik iddiası desteksiz.** "Tekrarlanabilir kıyaslama" deniyor; ama veri ve kod yayımlanmamış, simülatör de tescilli.
- **Projeyle bağlantı:**
  - **İP4:** Bir "anti-örnek". Gecikmenin hedef kartta, gerçek karar hızında, ön işleme dahil ve en kötü durum olarak ölçülmesi gerektiğini gösteriyor.
  - **İP3:** Kapsama ve çekimserlik, sınıflandırma zamanı ve akış tabanlı değerlendirme yararlı kavramlar. Ancak filtre nedensel (geçmişe bakan) olmalı.
  - Çekimserlik fikri, küme tabanlı yöntemdeki "karar verilemez bölge" ile karşılaştırılabilir.
- **Açık sorular / araştırma fikirleri:**
  - **[EN UMUT VERİCİ] Gecikme bütçesini ayrıştır.** 16.7 ms = pencere uzunluğu + nedensel filtrenin grup gecikmesi + hesaplama süresi (WCET) + çıkış. Edge kartta MLP, Kalman filtresi dedektörü ve küme testi için bu bileşenleri ölç; karar hızını seç (ör. çeyrek çevrimde bir).
  - Merkezli ortalama yerine geriye bakan (trailing) ortalama ile histerezis ya da ardışık onay (k-of-n) mantığı aynı kararlılığı sağlar mı? Bunun maliyeti kaç ms?
  - **Çekimserlik ve yardımcı sinyal:** Güven düşükse yardımcı sinyalin genliği artırılabilir (uyarlamalı ya da kapalı çevrim yardımcı sinyal). Bu, Taylor çizgisiyle ilginç bir köprü olur.

---

## Grup sentezi

### Veri setleri yan yana

| Veri seti (makale) | Boyut | Şebeke / simülatör | Örnekleme | Evirici? | Arıza dışı olay? | Rf aralığı | Ölçüm zinciri | Lisans / erişim |
|---|---|---|---|---|---|---|---|---|
| Beikbabaei vd. 2024 | 420 simülasyon × 1 s; makaleye göre 715,959 örnek (tutarsız) | 4 baralı %100 IBR mikroşebeke, 480 V / 12.47 kV; PSCAD | 1 ms'de RMS I, V ve P, Q (nokta-dalga değil) | Evet: 2 GFM (droop) + 2 GFL | Hayır | {0.001, 0.1, 1, 10, 100} Ω | İdeal | Yayımlanmamış |
| Ouali vd. 2024 | Her mod için 5000 + 2500 viGFL + 2 × 100 Aalborg | Tek VSC + şebeke (400 kV, 1 GW, SCR 15); Simulink | Frekans bölgesi admitans, 1 Hz–1 kHz, ~300 sütun | Evet: pq/pv/vi-GFL, vc/cc-GFM | Uygulanamaz (arıza verisi değil) | — | İdeal | Yayımlanmamış |
| PROTECT-90 (Oelhaf/Kordowich 2026) | 9,022 bölüm × 1 s; 12.5 GB sıkıştırılmış | 90 kV çift hat, 3 bara, 50 Hz; PowerFactory EMT | 6.4 kHz nokta-dalga, 48 kanal (8 röle) | Hayır (yalnızca düşük Sk″) | Hayır; arızasız sınıf bile yok | 0.1–10 Ω | İdeal birincil; CT/VT yok (metin çelişkili) | CC BY 4.0, Zenodo |
| EvEMTBench (Kordowich 2026) | 11 alt set, her biri <10,000 simülasyon × 0.5 s | CIGRE MV 20 kV, 110 kV ref., 110 kV çift hat, IEEE 39 (345 kV, 60 Hz) + 105 sentetik topoloji/seviye; PowerFactory EMT | 9.6 kHz nokta-dalga | Evet: yalnızca GFL ortalama model (negatif dizi FRT, 1.2 pu sınır); 345 kV'ta yok | **Evet, 13 tip** (yük, kondansatör, hat/kablo, inrush, motor yolverme, generatör ve IBR açması) | Kısa devre 0.001–50 Ω; HIF 50 Ω–150 kΩ | CT/VT/gürültü tarif edilmemiş | Açık indirme (FAUDataCloud); lisans belirtilmemiş |
| Abukhousa vd. 2026 | 105,768 örnek (22 s), tek simülasyon | Evirici ağırlıklı mikroşebeke (50 kVA PV, 30 kVA BESS); WinIGS | 4.8 kHz SV, 14 kanal (2 MU) | Evet (kontrol tipi belirtilmemiş) | Hayır (yalnızca siber saldırılar ve tek bölge dışı arıza) | Belirtilmemiş | CT/PT çıkışı (COMTRADE), model ayrıntısı yok | Yayımlanmamış; tescilli simülatör |
| Kontrollü karşılaştırma (Oelhaf 2026) | PROTECT-90'ı kullanıyor (yukarıda) | — | — | — | — | — | — | — |
| Tarama (Martinez-Velasco 2025) | Veri yok; [507–511] numaralı veri seti depolarına işaret ediyor | — | — | — | — | — | — | — |

**Önemli gözlem:** Hiçbir açık veri seti, yardımcı sinyal enjekte eden IBR'ler içermiyor. 60 Hz nokta-dalga verisi yalnızca EvEMTBench'in IEEE 39-bara kısmında var ve orada hiç IBR yok. Bu iki eksik İP2'nin kendi verisini üretmesini zorunlu kılıyor.

### Projenin benimsemesi önerilen değerlendirme protokolü kuralları

1. **Bölme birimi = simülasyon bölümü (episode); sınıflandırılan birim pencere ya da örnek olsa bile.**
   - Kardeş simülasyonlar aynı gruba konmalı. Örnek: aynı tip, konum ve Rf'ye sahip olup yalnızca süresi farklı varyantlar (Beikbabaei). Aynı bölümdeki 8 rölenin kayıtları da tek grup (PROTECT-90).
   - `GroupKFold` kullanılmalı.
   - Ölçekleyici, özellik seçimi ve hiperparametre seçimi yalnızca eğitim katlarında yapılmalı; bunun için iç içe (nested) CV kullanılmalı.
2. **Dağılım dışı testler raporlanmalı:**
   - Topoloji dışarıda bırakılarak (EvEMTBench'teki multigrid mantığı)
   - Evirici kontrol yapısı dışarıda bırakılarak (Ouali: GFL↔GFM, pq↔vi)
   - Rf aralığı dışarıda bırakılarak (ör. eğitim ≤20 Ω, test 20–100 Ω)
   - Yük seviyesi değiştirilerek
3. **Güvenlik test seti zorunlu.**
   - İçeriği: arızasız bölümler; anahtarlama, inrush, kondansatör, motor yolverme, IBR açması ve hat enerjilendirme olayları; bölge dışı arızalar ("no-trip" etiketiyle).
   - Başlangıç listesi olarak EvEMTBench Tablo 1 kullanılabilir.
4. **Dependability ve security ayrı raporlanmalı.**
   - Dependability: arıza tipine ve Rf, konum, başlangıç açısı kovalarına göre kaçırma oranı.
   - Security: olay tipine göre yanlış açma oranı ve normal işletme saati başına yanlış açma sayısı.
   - Tek bir accuracy ya da F1 değeri kabul edilmemeli; karışıklık matrisi yayımlanmalı.
5. **Yalnızca nedensel işleme.**
   - Sadece geçmiş örnekler kullanılabilir. Merkezli filtre (Abukhousa) ve arıza başlangıcına hizalanmış kesit (Oelhaf) olmamalı.
   - Değerlendirme sürekli bir akış üzerinde yapılmalı; başlangıç anı pencere ızgarasına göre rastgele olmalı.
   - Açma kararı ardışık onay mantığıyla verilmeli ve bu mantığın gecikmesi raporlanmalı.
6. **Etiket tanımları açık olmalı:**
   - "Arıza durumu" (başlangıçtan temizlenmeye kadar) ile "başlangıcı içeren pencere" ayrımı
   - Bölge içi / bölge dışı ayrımı
   - Çekimser çıktının açma mantığında nasıl yorumlanacağı
7. **Gerçekçi ölçüm zinciri:**
   - CT (doyma dahil), CCVT geçici rejimi, anti-aliasing filtre, ADC nicemlemesi, gürültü.
   - SV örnekleme (60 Hz'de 80 örnek/çevrim = 4.8 kHz).
   - Fazör ve dizi bileşeni çıkarımında filtre gecikmesinin hesaba katılması.
   - Tarama makalesi (s. 20) de CT/VT'nin çoğu çalışmada eksik olduğunu vurguluyor.
8. **Tek bir gecikme tanımı.**
   - Tespit süresi: arıza başlangıcından açma bayrağına kadar geçen süre. Pencere, filtre, onay ve hesaplama sürelerinin toplamı.
   - Hesaplama süresi hedef edge kartta, gerçek karar hızında, ön işleme dahil ve ısınmadan sonra ölçülmeli. p50, p99 ve maksimum (WCET'e yakın) değerler raporlanmalı.
   - Verim (throughput) karar hızına yetmeli.
   - Toplam bütçe yaklaşık 16.7 ms veya daha az.
9. **Taban çizgileri aynı bölümler üzerinde koşturulmalı:** konvansiyonel mesafe ve negatif dizi elemanları, Kalman filtresi dedektörü, küme tabanlı yardımcı sinyal testi ve öğrenilmiş modeller.
10. **Tekrarlanabilirlik:**
    - Veri ve metaveri birlikte yayımlanmalı. PROTECT-90 tarzı bir CSV şeması kullanılabilir: bölüm kimliği, tüm rastgele parametreler, topoloji bayrakları.
    - Kod ve rastgele tohumlar (seed) yayımlanmalı.
    - Katlar arası ortalama ± std raporlanmalı.

### En önemli 3 çıkarım

1. **Güvenlik (security) bu literatürde neredeyse hiç ölçülmüyor.**
   - Arıza tespiti yapan üç model makalesinin hiçbiri arıza dışı olaylara karşı sistematik bir yanlış açma oranı raporlamıyor. Abukhousa yalnızca tek bir bölge dışı arıza örneği gösteriyor.
   - Arıza dışı olay içeren tek veri seti (EvEMTBench) model sonucu içermiyor.
   - Hiçbir açık veri seti yardımcı sinyal enjekte eden IBR içermiyor.
   - Bu nedenle İP2 kendi verisini üretmek, İP3 de güvenlik test setini kurmak zorunda. Bu, aynı zamanda projenin literatüre en net katkı yapabileceği alan.
2. **Başlıktaki yüksek skorlar (%96–99) protokol kusurlarıyla şişirilmiş olabilir.**
   - Beikbabaei: örnek düzeyinde karıştırma
   - Abukhousa: tek simülasyon içinde blok bölme ve merkezli (ileriye bakan) filtre
   - Oelhaf: gruplu CV'ye rağmen oracle'a hizalanmış pencereler
   - Simülasyon düzeyinde gruplanmış ve nedensel bir değerlendirme olmadan, öğrenilmiş dedektörlerin küme tabanlı yöntemle karşılaştırılması adil olmaz.
3. **"Gecikme" kelimesi bu makalelerde dört farklı şeyi ifade ediyor.**
   - Simülasyon zaman ekseninde tespit gecikmesi: Beikbabaei'nin "<5 ms"si
   - İleriye bakışlı sinyal zamanı: Abukhousa'nın 3–15 ms'si
   - Masaüstü CPU'da tek örnek çıkarım süresi: Oelhaf'ın 0.04–2.95 ms'si
   - Colab'da tek ileri geçiş süresi: Abukhousa'nın 57–89 ms'si
   - İP4 tek bir uçtan uca tanım benimsemeli (pencere + filtre + onay + hedef kartta WCET) ve bütün yöntemleri aynı tanımla ölçmeli.

**Ek not:** Bu gruptaki yedi makaleden üçü (PROTECT-90, kontrollü karşılaştırma, EvEMTBench) aynı FAU grubundan; birbirine bağlı bir ekosistem oluşturuyorlar. Bulguların bağımsız bir grup tarafından tekrarı henüz yok.
