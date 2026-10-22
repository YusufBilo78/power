# Yüklenen paywall'lı makaleler (1. grup): Saleh, Banaiemoqadam, Haddadi, Yang/Popov

Dört makaleyi de baştan sona kendim okudum (NJIT kopyaları; repoya konmadı). Sayfa numaraları derginin sayfa numaraları. "Bizim gözlemimiz" diye işaretli yerler benim çıkarımım.

| Kısaltma | Makale |
|---|---|
| **SA** | Saleh, Allam & Mehrizi-Sani, *Protection of Inverter-Based Islanded Microgrids via Synthetic Harmonic Current Pattern Injection*, IEEE TPWRD 36(4):2434–2445, 2021 |
| **BA** | Banaiemoqadam, Hooshyar & Azzouz, *A Control-Based Solution for Distance Protection of Lines Connected to Converter-Interfaced Sources During Asymmetrical Faults*, IEEE TPWRD 35(3):1455–1466, 2020 |
| **HA** | Haddadi, Zhao, Kocar, Karaagac, Chan & Farantatos, *Impact of Inverter-Based Resources on Negative Sequence Quantities-Based Protection Elements*, IEEE TPWRD 36(1):289–298, 2021 (hakem sonrası kabul edilmiş sürüm; sayfa numaraları bu sürümün 1–10'u) |
| **YA** | Yang, Liu, Zhang, Chen, Chavez & Popov, *A Control Method for Converter-Interfaced Sources to Improve Operation of Directional Protection Elements*, IEEE TPWRD 38(1):642–654, 2023 |

---

## SA: Saleh ve ark. (2021), sentetik harmonik desen enjeksiyonu

**Tek cümlede:** Adalanmış (islanded), yalnızca invertörlü bir mikroşebekede her invertör, arıza sırasında 3., 5. ve 7. harmoniklerden oluşan ikili (var/yok) bir "desen" basıyor. Röleler ölçtükleri deseni önceden ayarlanmış karakteristik desenle kosinüs benzerliğiyle karşılaştırıp arızanın ileri mi geri mi olduğunu buluyor. Hangi invertörün hangi harmoniği basacağı bir optimizasyonla seçiliyor.

**Yöntem**
- **Enjeksiyon (Bölüm II):** Her faz ve her harmonik için ayrı bir oransal-rezonant (PR) kontrolcü kullanılıyor. Harmonikler, faz kayması hθ yerine θ olacak şekilde üretiliyor; böylece sentetik 3. ve 5. harmonik **pozitif bileşen** oluyor (s. 2436). Doğal 3. harmonik sıfır bileşen, doğal 5. harmonik negatif bileşen olduğu için bu ayrım önemli.
- **Tetikleme:** Fazın gerilimi 0.88 pu'nun altına düşerse (IEEE 1547 LVRT eşiği) ve sadece o fazda enjeksiyon başlıyor.
- **Akım bütçesi (denklem 1–2):** Toplam etkin akım sınırı α = 1.2 pu, temel bileşen sınırı β = 1.0 pu. Buradan α² = β² + 3·I_inj² ve harmonik başına **I_inj = 0.38 pu**. Yani enjeksiyona yer açmak için temel bileşen arıza akımı **1.0 pu'ya düşürülüyor**.
- **Yön elemanı (Bölüm III):** Pozitif bileşen akımının FFT'sinden 3/5/7 genlikleri ölçülüyor (MP). Karakteristik desenle (CP) kosinüs benzerliği λ = 0.85'i geçerse ileri yön. Bu eşik, farklı ikili desenler arasındaki en büyük benzerlik olan 0.8165'in üstünde, %5 pay bırakılarak seçilmiş.
- **Koruma şeması:** Birincil koruma POTT (iki uç da ileri derse açma), yedek koruma DZI. İletişim olarak IEC 61850 GOOSE kullanılıyor; şema **haberleşme gerektiriyor**.
- **Optimizasyon (Bölüm IV):** Toplam enjeksiyon sayısı minimize ediliyor (denklem 5). Kısıtlar şunlar: her arızada en az bir harmonik görülsün (denklem 6); her rölenin ileri ve geri arızadaki desenleri arasındaki kosinüs benzerliği ≤ λ olsun (denklem 7). Değişkenler ikili, problem doğrusal olmayan bir tamsayı programı. **Genetik algoritmayla** çözülüyor. Desenler düğüm analiziyle hesaplanıyor.
- **Olağanüstü durum yönetimi (Bölüm V):** Bir invertör ya da hat devre dışı kalırsa desenler yeniden optimize ediliyor; röle ayarları değişmiyor.

**Sonuçlar (CIGRE 12.47 kV, 14 invertör, 30 röle, adalanmış)**
- Gözlü (meshed) yapıda 14 invertörden 6'sının birer harmonik basması yetiyor (Tablo I).
- 3, 5 ve 7 harmonik tahmini, enjeksiyon geçici rejiminin sönmesi için **3 periyot** bekliyor (s. 2441).
- **Açma süreleri:** POTT 58.33 ms, DZI 166.66 ms; ikisi de başarısız olursa LVRT ile bütün mikroşebeke 250 ms'de kapanıyor (s. 2443).
- Tek faz-toprak, faz-faz, faz-faz-toprak ve üç faz arızaları denenmiş; desenin genliği değişiyor ama yönü değişmiyor.
- 10 Ω ve 40 Ω dirençli arızalarda da doğru yön buluyor.

**Varsayımlar ve sınırlamalar**
- **Sadece adalanmış mod.** Şebekeye bağlıyken düşük empedanslı şebeke harmonik akımı emer; bu durum incelenmemiş.
- **Garanti nominal modelde.** Tasarım, belirli arıza noktalarında düğüm analizine dayanıyor; arıza direnci, yük ve invertör çıkışı için bir belirsizlik kümesi yok. Arıza direncine dayanıklılık 2 vakayla gösterilmiş.
- **Hız:** 3 periyot FFT artı POTT. Bir periyotluk bütçenin çok üstünde.
- **Arıza akımı bedeli:** Temel bileşen arıza akımı 1.2'den 1.0 pu'ya düşüyor.
- **Ayırdığı şey sadece yön** (ileri/geri), bölge değil. Bölge seçiciliği iki uçtan haberleşmeyle sağlanıyor.

**Projeyle bağlantı ve bizim gözlemlerimiz**
- Taylor'ın yaklaşımına en yakın öncül: o da sinyali **çevrimdışı, optimizasyonla** tasarlıyor ve hipotezleri (ileri/geri) ayırmaya çalışıyor. Farklar şunlar: ayırma ölçütü kosinüs benzerliği; garanti küme tabanlı değil, nominal modelde; sinyal alanı ayrık (ikili); temel frekans yerine harmonikler kullanılıyor.
- **Bizim gözlemimiz: frekans ayrımı belirsizliğin büyük kısmını yok ediyor.** Enjeksiyon frekansında şebeke (doğrusal kaldığı sürece) **sadece bilinen enjeksiyonla** sürülüyor. Senkron generatörlerin ve diğer invertörlerin bilinmeyen temel frekanslı çalışma noktası o frekansta ölçüme hiç girmiyor.
  - Taylor'ın modellerindeki asıl belirsizlik tam da bu kaynak belirsizliği: Geometry'deki i_C°, v_S° ve Λ.
  - Temel frekanslı negatif bileşen sinyalinde ise arızanın ve kaynakların ürettiği negatif bileşen, sinyalin etkisiyle iç içe geçiyor.
  - Bu, Taylor 2026'nın artımsal makalesinin "durağanlık" varsayımıyla elde etmeye çalıştığı şeyin **varsayımsız** bir yolu olabilir. Bölüm sonundaki F7'ye bakın.

---

## BA: Banaiemoqadam ve ark. (2020), mesafe koruması için kontrol tabanlı çözüm

**Tek cümlede:** İnvertörün bulunduğu baradaki mesafe rölesinin ölçtüğü empedansı bozan "uzak uç besleme" (remote infeed) terimini neredeyse reel yapacak şekilde, invertörün pozitif bileşen arıza akımının **açısı** kontrol ediliyor.

**Problem (Bölüm III)**
- Röle şunu ölçer:
  - BC arızasında Z = Z_f + R_f(1 + M_r) (denklem 1)
  - AG arızasında Z = Z_f + R_f·M_r (denklem 2)
  - Burada M_r, uzak uç akımının yerel akıma oranı.
- **Senkron generatörlü şebekede:** İki ucun gerilim açıları birbirine yakın olduğu için M_r neredeyse reel. Hata dirençsel yönde kalır ve dörtgen karakteristiğin hafifçe eğilmesiyle telafi edilir.
- **İnvertörlü şebekede:** Yerel akımın açısını kontrol yazılımı belirler, bu yüzden M_r'nin büyük bir sanal kısmı olur. Örnek: bölge 1 içinde, hattın %40'ında, 20 Ω'luk bir BCG arızası (s. 1457):
  - Alman kodunun istediği reaktif akım modunda pay paydadan 57° önde; ölçülen empedans bölge 1'in üstünde kalıyor.
  - Birim güç faktörü modunda pay 76° geride; ölçülen reaktans −62.2 Ω. Röle iki durumda da açmıyor.
- **Ara besleme (intermediate infeed):** Komşu hattın %40'ındaki bolted bir BCG arızasında birim güç faktörü modunda **bölge 1 aşırı erişiyor** (X = 45.1 Ω) ve yanlış açıyor (s. 1458).
- **Kilit gözlem (s. 1458):** Şebeke gerilimini ileri beslemeyle telafi eden tipik invertör, negatif ve sıfır bileşen devrelerinde **açık devre**. Kontrol edilebilen tek şey pozitif bileşen akımının genliği ve açısı.

**Yöntem (Bölüm IV)**
1. **Senkron generatör taklidi:** Senkron generatörlerde pozitif ve negatif bileşen akımları arasındaki açı ilişkisi arıza tipine göre belirli bir desen izler (Şekil 9). İnvertörde negatif bileşen olmadığı için, "burada senkron generatör olsaydı I₋ hangi açıda olurdu" hesaplanıyor: ∠Z₋eq ≈ 84° (denklem 6). Arıza tipi, V₂ ile V₀ arasındaki açıdan bulunuyor (Hooshyar 2016). Sonra I₊'nın açısı desene göre seçiliyor.
2. **En kötü duruma göre ayar:** 84° yerine bir α sabiti kullanılıyor (denklem 7). α, **bölge 1'in sınırındaki, en yüksek dirençli** arızada M_r'nin açısını sıfırlayacak şekilde çevrimdışı ve iteratif olarak bulunuyor. Sonuç: LL ve LLG arızaları için 73°, SLG için 63°. Algoritma en fazla 5 iterasyonda yakınsıyor.
- Genlik her durumda en fazla 1.2 pu. Yöntem gerilim 0.9 pu'nun altına düştüğünde devreye giriyor; arıza tipi 2–3 ms'de belirleniyor.

**Sonuçlar (IEEE 9-bara; bara 9'daki generatör yerine 100 MVA invertör; bölge 1 = %90 = 48 Ω, R erişimi 100 Ω, ABB REL670 modeli)**
- Bölge 1 içinde 10, 50 ve 90 Ω'luk arızaların hepsi anlık açılıyor. Reaktanstaki en büyük hata 4.4 Ω (Tablo I). Empedans **9 ms** içinde bölge 1'e giriyor (Şekil 17).
- Bölge sınırında 100 Ω'luk AG ve BCG arızalarında ölçülen empedans tam sınırda.
- Bölge 2 (uzak uçta 10 Ω'luk BCG): yöntemle 54.7 Ω ölçülüyor, gerçek değer 53 Ω. Birim güç faktörü modunda hata 73 Ω.
- Ara beslemede M_i'nin açısı 5.2°'ye iniyor.
- Diğer modlarda **0.5 Ω** gibi küçük bir arıza direnci bile yanlış çalışmaya yol açabiliyor (s. 1463).
- Gerilim polarizeli mho elemanında, negatif bileşen basan çift akım kontrolünde (DCC: Mr açısı 3°, aşırı erişim 0.6 Ω), chopper'sız FRT'de ve 5 kat zayıflatılmış şebekede de çalışıyor.

**Varsayımlar ve sınırlamalar**
- Özetteki "arıza koşullarından bağımsız olarak doğru çalışma" iddiası **abartılı**. α tek bir en kötü durum noktasında ayarlanıyor, sonra vakalarla doğrulanıyor; garanti yok.
- α şebekeye ve şebekenin gücüne bağlı. Ağ değişirse yeniden ayar gerekiyor.
- Sadece asimetrik arızalar ve sadece invertör ucundaki röle (R98) incelenmiş. Karşı uç (R89) ve 32Q yön elemanları sistematik olarak incelenmemiş.
- Seçilen akım açısı, şebeke kodunun istediği reaktif akımla çelişebilir.

**Projeyle bağlantı ve bizim gözlemlerimiz**
- M_r, Taylor'ın Geometry makalesindeki z_F = m_r(ξ + Ξ·i_R) teriminin ta kendisi. Banaiemoqadam, invertör akımının açısını seçerek bu terimin **sanal kısmını küçültüyor**; yani belirsizlik bulutunu daraltıyor.
- Taylor'ın modeli ise IBR akımının açısını 120°'lik bir belirsizlik olarak alıyordu. Bu makale ve Baeckeland gösteriyor ki o açı aslında **bir kontrol tercihi**.
- **Fikir F6'nın somut bir hali:** α'yı tek bir en kötü durum noktasında değil, Taylor'ın küme tabanlı ayırma kriteriyle **bütün bir küme** (yer, direnç, şebeke gücü) üzerinde seçmek. Arıza tipi başına tek boyutlu bir arama; küçük, öğrenci ölçeğinde bir problem.

---

## HA: Haddadi ve ark. (2021), negatif bileşen elemanlarına IBR etkisi

**Tek cümlede:** Rüzgâr türbinlerinin negatif bileşen davranışını eşdeğer bir negatif bileşen empedansıyla modelleyip senkron generatörle karşılaştırıyor. Küçük genliğin 50Q'yu, yanlış açının 67Q'yu bozduğunu simülasyonla ve gerçek röleyle gösteriyor.

**Eşdeğer negatif bileşen empedansı (Bölüm II)**

| Kaynak | Z₂ (genlik ∠ açı) | Kaynak |
|---|---|---|
| Senkron generatör | 0.12–0.4 pu ∠ −90° (akım şebekeye doğru) | s. 3 |
| DFIG (Tip III) | 0.19–0.58 pu ∠ −102° … −113° | Tablo 2 |
| FSC (Tip IV), birlikte kontrol (CSC) | 5–1142 pu ∠ 144° … 163°; pratikte **açık devre** | Tablo 1 |
| FSC, ayrık kontrol (DSC, VDE-AR-N 4120, K = 2–6) | 0.167–0.5 pu | s. 2 |

Test sistemindeki iki rüzgâr parkı için simülasyon 4.36∠19° ve 4.80∠28° pu, analitik değer 4.47∠20.4° pu veriyor (Tablo 3).

**Yanlış çalışma örnekleri (Bölüm III–V; 15 baralı 315/230/120 kV sistem, 5 rüzgâr parkı)**
- **50Q (AG1 arızası, I₂ eşiği 0.2 pu):** Ölçülen I₂: senkron generatör 0.78, DFIG 0.52, **FSC-CSC 0.14 (açmıyor)**, FSC-DSC 0.65 pu (Tablo 4). DSC için en büyük K = 6 gerekmiş; daha küçük K bazı arızalarda yetmemiş.
- **67Q (AB2 arızası, röle geri yön görmeli):** Ölçülen açılar: senkron generatör 87.4°, DFIG 78.0°, **FSC-CSC −20.0°**, FSC-DSC 91.5° (Tablo 5). CSC'de I₂ eşiğin altında kalıyor. Eşik 0.02 pu'ya indirilince röle **yanlışlıkla ileri** diyor.
- **POTT:** CSC'de R1'in 67Q'su sadece anlık tetikleniyor (açı ≈ −180°, hiçbir bölgede değil). İzin gönderilemiyor ve **iç arıza açılmıyor**. DSC ile düzeliyor.
- **Arızalı faz seçimi (FID):** Senkron generatörde IA2, IA0'dan 6° geride; AG doğru seçiliyor. CSC'de IA2, IA0'dan 80° önde ve hiçbir sektöre düşmüyor; FID başarısız (Şekil 6).
- **Gerçek röleyle HIL:** FSC-CSC durumunda hattın ortasındaki **ileri** bir AG arızasını röle **geri** olarak sınıflandırıyor.

**Varsayımlar ve sınırlamalar**
- Empedans modeli durağan durum fazörlerine dayanıyor. Açılar **arızadan 100 ms sonra** ölçülmüş; ilk periyot incelenmemiş.
- Tek bir yüklenme durumu (minimum yük). Devredeki türbin sayısı ve rüzgâr hızı yer darlığından çalışılmamış.
- Yazarlar bir uyarı da yapıyor: hat açısı 90°'ye yakın değilse ve enjekte edilen I₂ akım sınırı yüzünden küçük kalırsa, VDE kodu bile 67Q'yu kurtarmayabilir (s. 5).

**Projeyle bağlantı ve bizim gözlemlerimiz**
- Bu tablo, IBR'nin negatif bileşen dalı için **hazır bir belirsizlik kümesi** veriyor. Kontrol türüne göre açık devreden 0.17 pu'ya, açı olarak da −113°'den +163°'ye kadar.
- Taylor 2023 ve TAC 2025 "i₋ ≈ 0" (yani CSC) varsayıyor ve θ'yı onun yerine koyuyor. Ama IEEE 2800 ve VDE'den sonra temel durum artık i₋ = 0 değil, **I₂ = K·V₂** (DSC). Yardımcı sinyal bu şönt admitansın üstüne tasarlanmak zorunda. Bu şönt, sinyalin röleye ulaşan izini de küçültür.
- 67Q için doğru davranış, tanımı gereği **endüktif bir Z₂**. Bu, genel sentezdeki "tasarlanmış empedans" paradigmasının bir kez daha teyidi.

---

## YA: Yang ve ark. (2023), yön elemanları için kontrol yöntemi

**Tek cümlede:** İnvertörün pozitif ve negatif bileşen akım referansları ölçülen gerilimlerden **gerçek zamanlı** hesaplanıyor. Amaç, arıza bileşeni tabanlı yön elemanlarının gördüğü empedans açısının ileri arızalarda tam −90° olması. Akım genlikleri de sınır içinde en büyük değere çekiliyor.

**Problem (Bölüm II)**
- Yön elemanları ∠Z₁ = ∠(ΔU₁/ΔI₁) ve ∠Z₂ = ∠(U₂/I₂) değerlerine bakıyor; ileri arızada açı −180° ile 0° arasında olmalı, ideali −90° (denklem 3–5).
- Danimarka FRT kuralıyla (reaktif akım gerilim düşümüne göre, I₂ referansı 0) bir AG arızasında ∠Z₁ = −139.52° çıkıyor; elemanın duyarlılığı düşük. ∠Z₂ ise geniş bir aralıkta oynuyor.
- Şebeke tarafındaki röle (R21), bir geri arızayı ileri görebiliyor.
- Sıfır bileşen yön elemanı YNd transformatör sayesinde etkilenmiyor, ama sadece toprak arızalarında işe yarıyor.

**Yöntem (Bölüm III)**
- Pozitif bileşen akımının açısı α₁, ölçülen U₁, U_b ve I_b'den ∠Z₁ = −90° olacak şekilde hesaplanıyor (denklem 13–15).
- Negatif bileşen akımının açısı **α₂ = φ₂ + 90°** (denklem 20). Yani I₂, V₂'nin 90° önünde; IEEE 2800'ün açı şartıyla aynı.
- Genlikler: |I₁| + |I₂| = γ·I_N ile başlanıyor, |I₂| = β·|I₁|, β ∈ [0.2, 1). Kosinüs teoremiyle faz akımları hesaplanıp en büyük faz akımı γ·I_N'ye eşitlenene kadar iterasyon yapılıyor (denklem 23–26). 2–3 iterasyonda yakınsıyor.
- **Arıza tipine bağlı parametre yok** ve sadece yerel ölçüm kullanılıyor.

**Sonuçlar (100 MW invertör, 220 kV ve 40 km hat; invertör, şebeke kısa devre gücünün 1/30'u; γ = 1.5, β = 0.3)**
- ∠Z₁ = −90.61° oluyor (önceki −139.52° yerine). Akım referansları i₁d = 1.0024, i₁q = −0.68 pu. PCC gerilimi %70.5, P = 0.70 pu, Q = 0.62 pu (s. 648).
- **İlk 20 ms'de açı büyük dalgalanıyor.** Yazarlar korumaya **40 ms gecikme** eklenmesini öneriyor (s. 648). Tablo değerleri arızadan 100 ms sonra okunmuş.
- 50 Ω'luk arızada −91.33°, 100 Ω'da −91.38° (Şekil 9).
- Şebeke gücü 1/10 ve 1/3'e indirildiğinde de, invertör gücü 200 ve 300 MW'a çıkarıldığında da çalışıyor.
- Banaiemoqadam 2021'in yöntemi arıza öncesi güç faktörüne bağlı (0.9 ve 0.95'te yanlış yön veriyor); bu yöntem değil (Şekil 12).
- RTDS: 100 Ω AG için −90.65°, 20 Ω BC için −91.36°. Küçük ölçekli donanım deneyinde akım 40 ms'de oturuyor.

**Varsayımlar ve sınırlamalar (kısmen yazarların kendi kabulü, Bölüm VII)**
- Kararlılık kanıtı yok.
- Sadece ayrık (decoupled) bileşen kontrolünde geçerli.
- Tip III rüzgâr kümelerinin yakınında geçerli değil.
- Reaktif akım artık gerilim düşümüne göre ayarlanmadığı için gerilim desteğine etkisi incelenmemiş.
- **Bizim gözlemimiz:**
  - Yöntem oturma süresi yüzünden **40 ms gecikme** gerektiriyor; bu, projenin bir periyotluk hedefinin tam tersi.
  - Sadece yön elemanlarını hedefliyor, mesafe erişimini değil. Banaiemoqadam'ın tersi.

**Projeyle bağlantı:** Bu, genel sentezdeki ikinci paradigmanın ("tasarlanmış empedans", toplamsal sinyalin karşısındaki yaklaşım) en saf hali. İnvertör, röle açısından kaynak empedansı tam −90° görünecek biçimde davranıyor. Hem açı hem genlik çalışma anında hesaplanıyor. Ama ortada bir garanti ya da belirsizlik kümesi yok; doğrulama vakalarla yapılmış.

---

## Dört makalenin birlikte söyledikleri

1. **Temel sorun (HA):** Bugünkü invertör, negatif bileşende ya açık devre ya da yanlış açılı bir empedans. 50Q, 67Q, POTT ve FID bu yüzden bozuluyor; gerçek röleyle de doğrulanmış.
2. **Endüstrinin cevabı (BA, YA, ayrıca HA'daki VDE):** İnvertörün arıza akımının **açısını** röleye uygun seçmek. BA bunu mesafe elemanı için, YA yön elemanları için yapıyor. Kimse **garanti** vermiyor:
   - BA tek bir en kötü durum noktasına ayar yapıyor.
   - YA ölçülen açıları gerçek zamanlı takip ediyor ama oturması 40 ms sürüyor.
3. **Enjeksiyon seçeneği (SA):** Optimizasyonla tasarlanmış bir sinyal, ama nominal modelde ve haberleşmeli. Arızanın ileri mi geri mi olduğunu söylüyor, bölgeyi söylemiyor. Yavaş: 3 periyot artı POTT.
4. **Zamanlama:**
   - BA: 9 ms'de bölge 1'e giriş (bir AG vakası).
   - YA: 20 ms dalgalanma, 40 ms önerilen gecikme.
   - SA: 58 ms.
   - Yani yalnızca kontrol tabanlı açı seçimi bir periyoda yaklaşabiliyor.

## Yeni fikirler

**F6, güncellenmiş hali:** "Sinyal yerine açı tasarımı" fikri artık iki somut öncüle dayanıyor: Banaiemoqadam'ın α'sı ve Baeckeland'ın φ_lim'i. Önerilen araştırma sorusu şu: **α (veya φ_lim) Taylor'ın küme tabanlı kriteriyle tüm bir belirsizlik kümesi üzerinde seçilirse, hem mesafe hem yön elemanı için garanti verilebilir mi, ve bu garanti toplamsal bir δ'nın sağlayacağı paydan büyük mü?**

**F7 (yeni): frekans ayrımıyla kaynak belirsizliğini ortadan kaldırmak.** Saleh ve Taylor 2026 artımsal makalesinden çıkan bir fikir.
- **Gerekçe:** Doğrusal bir şebekede, temel frekanstan farklı bir f_h frekansında, rölenin ölçtüğü gerilim ve akım **sadece bilinen enjeksiyonla** belirleniyor (süperpozisyon). Senkron generatörlerin ve diğer invertörlerin çalışma noktası o frekansta ölçüme girmiyor. Uzak uç beslemenin açısı da artık kaynaklara değil, **pasif şebeke empedanslarına** bağlı; bunlar modelden hesaplanabilir. Taylor'ın modellerindeki en büyük belirsizlik kaynağı böylece kayboluyor.
- **Artı:** Saleh'in "pozitif bileşen sentetik harmonik" hilesi, enjeksiyonu doğal harmoniklerden **bileşen uzayında** ayırıyor. Doğal 3. harmonik sıfır bileşen, doğal 5. harmonik negatif bileşen.
- **Riskler:**
  - Ark arızaları 3. harmonik başta olmak üzere kendileri harmonik üretiyor.
  - Sınırlamadaki invertörler de harmonik üretiyor.
  - Yük ve diğer invertörlerin f_h'deki empedansları belirsiz.
  - Bir periyotluk pencere ancak tam katlı (harmonik) frekansları birbirinden ayırabiliyor. Ara harmonik kullanmak için daha uzun pencere ve dolayısıyla daha yavaş karar gerekiyor.
  - Sürekli enjeksiyon güç kalitesi sınırlarına (THD) takılıyor.
- **Not:** Harmonik enjeksiyonla empedans ölçümü literatürde (özellikle adalanma tespitinde) var. Bu fikrin ne kadar yeni olduğu bir literatür taramasıyla kontrol edilmeli. Yeni olabilecek kısım, onu Taylor'ın küme tabanlı tasarım çerçevesine bağlamak.
