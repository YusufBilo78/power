# A2: IBR'lerin Korumaya Etkisi ve Negatif Bileşen Akımı (Okuma Notları)

> **Bu notlar hakkında.** Dört kaynak baştan sona okundu. Metin `pdftotext` çıktısından okundu. Denklemler, tablolar ve şekil etiketleri de PDF'ten kontrol edildi.
>
> **Sayfa numaraları:**
> - **Li vd. (2025):** PDF'te sayfa numarası basılı değil. "s." PDF sayfasıdır (1–9).
> - **Slane & Mate (2026):** Basılı sayfa ile PDF sayfası aynı (1–11).
> - **PNNL-36069:** "s." raporda basılı numaradır (Özet s. v, metin s. 1–7, kaynaklar s. 8–9). PDF'te kapak ve künye sayfaları da olduğu için toplam 15 sayfa var.
> - **SEL (2026):** "s." basılı sayfadır. Kapak sayfası yüzünden PDF sayfası = basılı sayfa + 1.
>
> **"Benim hesabım" ya da "benim çıkarımım"** diye işaretlenen her şey makalelerde yok. Kontrol edilebilsin diye ayrı tutuldu.

---

## Kısa sözlük (alana yeni olanlar için)

- **IBR (inverter-based resource, inverter tabanlı kaynak):** Şebekeye güç elektroniğiyle bağlanan PV, Tip-IV rüzgâr ve batarya gibi kaynaklar. Arıza akımını fizik değil kontrol yazılımı belirler.
- **SG (synchronous generator, senkron generatör):** Klasik dönen makine. Arızada nominalin birkaç katı akım verir ve davranışı fizik kurallarıyla öngörülebilir.
- **GFL (grid-following, şebeke izleyen):** PLL ile şebeke gerilim açısını izler ve akım kaynağı gibi davranır.
- **GFM (grid-forming, şebeke kuran):** Kendi iç gerilimini oluşturur ve "empedans arkasında gerilim kaynağı" gibi davranır.
- **PLL (phase-locked loop):** Şebeke geriliminin açısını ve frekansını izleyen kontrol döngüsü.
- **CLC (current limiting control, akım sınırlama kontrolü):** Arızada yarı iletkenleri korumak için akımı sınırlayan kontrol katmanı. İki ana ailesi var:
  - *Akım referansı doyurma (current reference saturation):* anlık (instantaneous), öncelikli (priority-based) ve dairesel (circular) limiter.
  - *Sanal empedans/admitans (virtual impedance/admittance).*
- **Simetrik bileşenler:** Dengesiz üç fazlı büyüklükler pozitif (1), negatif (2) ve sıfır (0) bileşenlere ayrılır. Dengeli normal işletmede negatif ve sıfır bileşen ≈ 0'dır. Dengesiz bir arızada ortaya çıktıkları için arızanın "parmak izi" olarak kullanılırlar.
- **Artımsal (incremental, Δ) büyüklük:** Anlık değer eksi birkaç çevrim önceki (arıza öncesi) değer. Yük akımının etkisini çıkarır.
- **Mesafe rölesi (21):** Gerilim/akım oranından (görünür empedans) arızanın uzaklığını kestirir. Arıza koruma bölgesi (zone) içindeyse kesiciyi açtırır.
- **Denetleyici elemanlar (supervising elements):** Mesafe rölesinin seçici çalışmasını sağlayan yardımcı elemanlar:
  - *Yön elemanı:* 32 genel ad. 32Q negatif bileşenli, 32G sıfır bileşenli. 67Q negatif bileşenli yönlü aşırı akım.
  - *Faz seçimi:* FID/PSE/FTC. Hangi fazların arızalı olduğunu bulur.
- **50Q ve TD32:** 50Q ani negatif bileşen aşırı akım elemanıdır. TD32, SEL'in artımsal büyüklüklere dayalı zaman-domeni yön elemanıdır.
- **FRT/LVRT (fault/low-voltage ride-through):** Gerilim düştüğünde inverterin bağlı kalıp destek verme yükümlülüğü.
- **Momentary cessation:** İnverterin bağlı kalıp akım vermeyi geçici olarak durdurması.
- **CSC / DSC (coupled / decoupled sequence control):**
  - *CSC:* Negatif bileşeni ayrıca kontrol etmez.
  - *DSC ("dual current control"):* Pozitif ve negatif bileşen akımını bağımsız düzenler.
- **EMT (electromagnetic transient) benzetimi:** Anlık değerli (dalga şekli düzeyinde) benzetim, ör. PSCAD/EMTDC veya Simulink.
- **CHIL (controller hardware-in-the-loop):** Kontrolcü gerçek donanımda, şebeke ise gerçek zamanlı simülatörde çalışır.
- **Şebeke homojenliği (network homogeneity):** Kaynak ve hat empedans açılarının birbirine yakın olması. Bu sayede rölenin ölçtüğü akım açısı, arıza noktasındaki akımın açısıyla uyumlu kalır.
- **Bellek polarizasyonu (memory polarization):** Gerilim çok düştüğünde mho mesafe elemanının arıza öncesi gerilim açısını referans alması.

---

## 1. Li, Wu, Wang (2025): GFM inverterlerin koruma rölelerine etkisi, akım sınırlama kontrolü açısından

- **Künye:**
  - **Yazarlar ve başlık:** Yifei Li, Heng Wu, Xiongfei Wang, *"Impact of Grid-Forming Inverters on Protective Relays: A Perspective for Current Limiting Control Design"*, 2025.
  - **Yayın durumu:** IEEE dergi formatında makale. Dergi, cilt ve DOI PDF'te yok. Yazar kurumları da yazmıyor. PDF Mayıs 2025 tarihli; büyük olasılıkla hakem sürecindeki ya da kabul edilmiş bir taslak (kesin değil).
  - **Boyut:** 9 sayfa, 33 kaynak.

- **Tek cümlede:** Negatif bileşene dayalı denetleyici elemanlar, GFM inverterin akım sınırlama yöntemine bağlı olarak çalışır ya da bozulur.
  - Yüksek endüktif sanal empedans bu elemanların doğru çalışmasını sağlar.
  - Akım referansı doyurma yöntemleri (dairesel, öncelikli, anlık limiter) onları bozar.
  - Artımsal büyüklüklere dayalı elemanlar ise her iki CLC türünde de bozulabilir.

- **Problem ve bağlam:**
  - SG'li sistemlerde yön ve faz seçimi elemanları iki önkoşula dayanır (s. 3):
    - (a) Etkin empedanslar yüksek endüktiftir.
    - (b) Kaynağın eşdeğer dinamiği arızanın ilk birkaç çevriminde neredeyse değişmez.
  - GFL inverterlerle bu elemanların etkileşimi çok çalışılmış. GFM'nin arıza davranışı ise büyük ölçüde CLC'ye bağlı.
  - CLC tasarımı şimdiye kadar kararlılık, geçici performans ve GFM yeteneği açısından yapılmış, koruma açısından yapılmamış (s. 1).
  - Önceki çalışmalar [20] ve [21], CLC'nin *mesafe elemanlarını* önemli ölçüde etkilemediğini yalnızca sayısal benzetimle bulmuş. Bileşen ve artımsal büyüklüklere dayalı denetleyici elemanlar incelenmemiş (s. 1).
  - Dairesel limiter, anlık ve öncelikli limiterin zaaflarını giderdiği için "en pratik" akım referansı doyurma yöntemi sayılıyor (s. 1). Anlık limiter inverterin aşırı akım kapasitesini tam kullanamıyor. Öncelikli limiter ise arıza temizlendikten sonra bile GFM'yi akım sınırlama modunda tutabiliyor.

- **Yöntem / yaklaşım:**
  1. **SG'li sistemde önkoşulların türetilmesi** (Şekil 1–2, s. 2). Simetrik bileşen ağları ve Kirchhoff yasaları kullanılıyor:
     - φ2 = ∠(v2/i2) = ∠(−Ze2) ve φ0 = ∠(−Ze0) (Denk. 1). İleri arızada ≈ −90°, geri arızada ≈ +90°.
     - Artımsal yön açısı: Δφ1 = ∠(Δv1/Δi1) (Denk. 2).
     - Faz seçimi açıları: Δδ21 = ∠i2 − ∠Δi1 ve δ20 = ∠i2 − ∠i0 (Denk. 3–4, Şekil 4, s. 3).
  2. **GFM sistemi** (Şekil 5, s. 3):
     - Devre: inverter → Lf filtresi → 33/220 kV trafo → 100 km hat → şebeke.
     - Kontrol: Bileşen ayrımlı (sequence) kontrol; pozitif ve negatif bileşen APF (all-pass filter) ile ayrıştırılıyor.
     - Güç kontrolü: APC (sanal atalet H, sönüm KpP, P-ω droop D) ve RPC.
     - Bunların üzerinde CLC var.
     - **Negatif bileşen iç gerilim referansı Eref2 = 0** (dengeli iç gerilim için).
     - Pozitif ve negatif bileşende "basitlik için" **aynı CLC** kullanılıyor (s. 4).
  3. **Etkin empedanslar** (Denk. 7, s. 4):
     - Ze1 = n²Zv1 + jn²Xf1 + jXT1
     - Ze2 = n²Zv2 + jn²Xf2 + jXT2
     - Ze0 = jXT0. Δ-Y0 trafo sıfır bileşeni inverterden ayırdığı için bu ifadede yalnızca trafo kaçak reaktansı kalıyor.
  4. **CLC'nin negatif bileşen çıkış empedansı:**
     - Akım referansı doyurmada: Zv2 = (1−σ)/(Kpv·σ) (Denk. 8, s. 5). σ, limiterin girdi ve çıktı referansı arasındaki karmaşık oran; Kpv gerilim kontrolcüsünün oransal kazancı.
     - Sanal admitans/empedansta: Denk. 9–10 (s. 5). Parametreler: nX/R2 (X/R oranı), Ilim2 (akım sınırı), Ith2 (devreye girme eşiği), KX2 (kazanç).
  5. **Artımsal elemanlar için saf-arıza (pure-fault) bileşen ağı** (Denk. 11–15, Şekil 11, s. 6).
  6. **Doğrulama** (Şekil 15, s. 7):
     - PSCAD/EMTDC benzetimi.
     - Üç RT BOX3 ile CHIL: biri GFM kontrolcü, biri tesis modeli, biri röle algoritmaları.

- **Ana bulgular:**
  - **Güç kontrolü önkoşulları bozmuyor** (s. 4, Denk. 5–6). APC bant genişliği tipik olarak < 5 Hz, RPC çıkışı ≈ 1 pu civarında sınırlı. Bu yavaş güç kontrolü, iç gerilimi SG'ninkine benzer kılıyor.
  - **CLC, Zv2'nin açısını belirliyor** (s. 5):
    - Akım sınırına ulaşıldığında çıkış empedansı, filtre ve trafo empedansından çok büyük olur. Bu yüzden etkin empedansın X/R oranını Zv2 belirler.
    - Dairesel limiterde ∠σ = 0'dır, dolayısıyla Zv2 ağırlıkla **dirençsel** olur.
    - Öncelikli ve anlık limiterde ∠σ önceden tanımlanamaz.
    - |σ| arıza koşuluna bağlıdır.
  - **Benzetim, ag arızası** (Şekil 12, s. 7). Negatif bileşen çıkış empedansının açısı:
    - Dairesel limiter: −0,5°
    - Öncelikli limiter (yalnız aktif akım basılırken): −51,6°
    - Anlık limiter: 36,2°
  - **Sanal empedansın X/R oranının etkisi** (Şekil 13, s. 7; bcg arızası, m = 0,5, dirençsiz):
    - nX/R2 = 0,1 → φ2 = −152,1°, δ20 = −51,7°. İkisi de bandın dışında.
    - nX/R2 = 20 → φ2 = −92,3°, δ20 = −5,5°. İkisi de bandın içinde.
  - **Artımsal elemanlar** (Denk. 14–15, s. 6):
    - Zad = −n²·i1·Zv1/(i1 − ipre1).
    - Akım sınırı nedeniyle I1 ≈ Ipre1 olur. Payda küçülür ve açısı belirsizleşir.
    - Bu yüzden Zv1 yüksek endüktif olsa bile ∠(Δv1/Δi1), −90°'den sapabilir.
    - Benzetim (Şekil 14, s. 7; ag, m = 0,01, Rg = 30 Ω, endüktif sanal empedans): ∠(Δv1/Δi1) = −31,7°.
    - **Makale içi tutarsızlık:** Metin ∠Zad = 4,4° diyor, Şekil 14'ün etiketi ise ∠Zad = 8,1° gösteriyor.
  - **CHIL, negatif ve sıfır bileşenli elemanlar** (Şekil 16, s. 8; bcg, dirençsiz, m = 0,5):
    - Dairesel limiter: φ2 = −171°, δ20 = 81°. Bantların dışında.
    - Yüksek endüktif sanal admitans: φ2 = −90°, δ20 = 0°. Doğru.
    - Yüksek endüktif sanal empedans: φ2 = −90°, δ20 = 0°. Doğru.
  - **CHIL, artımsal elemanlar** (Şekil 17, s. 8; ag, m = 0,01, Rg = 20 Ω):
    - Dairesel limiter: Δφ1 = 0°, Δδ21 = 72°.
    - Endüktif sanal admitans: Δφ1 = 0°, Δδ21 = 72°.
    - Endüktif sanal empedans: Δφ1 = −27° (bant sınırına yakın), Δδ21 = 126°.
    - Artımsal elemanlar üç durumda da güvenilmez.
  - **Tablo I (s. 6), yöntemlerin özeti:**
    - Yüksek endüktif çıkış empedansı: φ2 ✓, φ0 ✓, δ20 ✓; Δφ1 ve Δδ21 "?" (belirsiz).
    - Yüksek endüktif olmayan çıkış empedansı: φ2 ✗, δ20 ✗, φ0 ✓; Δφ1 ve Δδ21 "?".
  - **Sıfır bileşenli elemanlar** CLC'den etkilenmiyor (s. 4). Ancak komşu devrelerden gelen karşılıklı kuplaja duyarlılar ve faz-faz arızasında sıfır bileşen hiç oluşmuyor.
  - **Röle ayar değerleri** (s. 3):
    - Yön elemanında çalışmama açısı (non-operating angle) φnon tipik olarak 30°–60° [24].
    - Faz seçimi bantları: Δδ21 için ±15°, δ20 için ±30° [26].
  - **Yazarların sonucu** (s. 8):
    - Endüktif sanal empedans "korumayla birlikte çalışabilir" (protection-interoperable) CLC'dir.
    - Akım referansı doyurma yöntemleri pratikte kullanılmamalıdır.
    - Artımsal büyüklüklü denetleyici elemanlar GFM ile "doğrudan kullanılmamalıdır".

- **Varsayımlar ve sınırlamalar:**
  - **Kapsam dar:** Tek GFM ve Thevenin eşdeğeri şebeke, iki bara, 100 km hat, 50 Hz (Tablo II, s. 7). GFL, birden fazla IBR ve SG+IBR karışımı incelenmemiş. SG'li sistem yalnızca türetme için kullanılmış.
  - **DC bara gerilimi sabit** kabul edilmiş (s. 3).
  - **İki bileşende aynı CLC** "basitlik için" seçilmiş (s. 4). Oysa bileşen bazlı ayrı sınırlama, kodun istediği negatif bileşen akımını basmak için tam da gereken şey (bkz. PNNL s. 6).
  - **İlk çevrimler incelenmemiş:** Arıza başlangıcındaki geçici salınımların etkisini atlamak için koruma elemanlarına zaman gecikmesi eklenmiş. Bu dönem "gelecekte ilginç bir araştırma konusu" olarak bırakılmış (s. 6–7). Projenin bir çevrimlik bütçesi tam da bu pencereye düşüyor.
  - **"Yeterince büyük nX/R2" için eşik verilmemiş.** Yalnızca 0,1 ve 20 karşılaştırılmış. Yüksek X/R oranının kararlılıkla çatışması ([15], [16]; s. 1) burada analiz edilmemiş.
  - **Mesafe elemanının kendisi test edilmemiş.** Yalnızca denetleyici elemanlar incelenmiş.
  - **Röle algoritmaları RT BOX üzerinde çalışıyor; ticari bir röle kullanılmamış.** Fazör kestirimi ve filtreleme ayrıntıları verilmemiş.
  - **Küçük tutarsızlıklar:** Arıza direnci benzetimde 30 Ω, CHIL'de 20 Ω. ∠Zad için metin 4,4°, şekil 8,1° diyor.
  - **IEEE 2800 uyumu tartışılmıyor.** Eref2 = 0 olduğu için GFM'nin negatif bileşen akımını tamamen Zv2 belirliyor; inverterin "tasarlanmış" bir I2 basma yeteneği yok.

- **Projeyle bağlantı:**
  - **Fiziksel öncül (en kritik nokta):**
    - Bu makaledeki GFM, negatif bileşende *pasif bir empedans* (Zv2) gibi davranıyor. Yardımcı sinyal bu mimaride kendiliğinden yok.
    - Yardımcı sinyal için ya Eref2 ≠ 0 (tasarlanmış bir negatif bileşen iç gerilimi) ya da negatif bileşende akım kaynağı modu gerekir (PNNL s. 6'daki Nasr–Hooshyar yapısı).
    - Sinyalin limiterden nasıl geçtiği limiterin türüne bağlı. Anlık ve öncelikli limiterde açı tanımsız. Dairesel limiterde ölçek (|σ|) arızaya bağlı.
  - **İP1 (CVXPY tasarım aracı):**
    - Limiterin etkisini, gerçekleşen sinyal = σ·(komut edilen sinyal) biçiminde karmaşık σ belirsizliği olarak modelle.
    - Şekil 12'deki açılar (−51,6° … 36,2°) belirsizlik kümesi için başlangıç olabilir. Bunlar tek bir arıza için örnek değerler, sınır değil.
    - φ2'nin ileri bölgede kalması (φnon 30–60°) ve δ20'nin ±30° bandında kalması kısıt olarak eklenebilir.
  - **İP2 (EMT benzetimi):**
    - Tablo II, tekrar üretilebilir bir GFM test sistemi veriyor: 220 kV, 50 Hz, 100 MW, 33/220 kV trafo, vdc = 40 kV, 100 km hat, Zl1 = 0,03 + j0,34 Ω/km, Zl0 = 0,18 + j1,19 Ω/km.
    - Test arızaları: bcg (m = 0,5, dirençsiz); ag (m = 0,01, Rg = 20 veya 30 Ω).
    - Dört doyurma/empedans yöntemi uygulanıp yardımcı sinyalin her birinde "hayatta kalıp kalmadığı" ölçülebilir.
  - **İP3 (röle tarafı):**
    - φ2, φ0, Δφ1, Δδ21 ve δ20 elemanları, bantlarıyla birlikte geleneksel temel (baseline) dedektör olarak kodlanabilir.
    - Şekil 12–17 beklenen başarısızlık modlarını gösteriyor. Öğrenen dedektörler için senaryo ve etiket çeşitliliği buradan kurulabilir. Aynı arıza farklı CLC ile farklı açı ürettiği için eğitim ve test kümeleri kontrol türüne göre ayrılmalı (dağılım kayması).
  - **İP4 (gömülü gecikme):**
    - Makale 50 Hz'de çalışıyor (çevrim 20 ms). Projenin bütçesi 60 Hz'e göre (≈ 16,7 ms).
    - Sonuçlar ilk çevrimi kapsamadığı için gecikme bütçesine doğrudan veri sağlamıyor.

- **Buradan çıkan açık sorular / araştırma fikirleri:**
  1. ★ **Limiter-farkında (CLC-aware) dayanıklı tasarım.**
     - *Soru:* Gerçekleşen sinyal σ·Iaux, σ belirsizken (dairesel limiter için |σ| ∈ [σmin, 1] ve açı ≈ 0; anlık/öncelikli limiter için bir açı aralığı) ayırma garantisi isteniyor. Bu durumda gereken minimum sinyal büyüklüğü ne kadar artar?
     - *Test:* Aralıkları EMT'den kalibre et ve sonucu dört limiterle doğrula.
  2. ★ **Denetleyici elemanlarla uyumluluk kısıtı.**
     - *Kısıt:* Yardımcı sinyal eklendiğinde φ2 ileri bölgede, δ20 ise ±30° bandında kalmalı.
     - *Soru:* Ayırma garantisi ile bu uyumluluk çatışıyor mu? Çatışıyorsa takas eğrisi nasıl?
  3. **İlk 20 ms'nin karakterizasyonu.** Makalenin atladığı pencerede her CLC için φ2(t) ve δ20(t) yörüngelerini ölç. Yardımcı sinyal bu pencerede ölçülebilir mi?
  4. **Bileşen bazlı limiter.** Negatif bileşen kanalında yardımcı sinyal için ayrılmış bir akım payı (headroom) bırakan bir CLC tasarla. Bunun pozitif bileşen desteğinden ne götürdüğünü ölç.
  5. **(Spekülatif) Artımsal elemanları kurtarmak.** Δφ1'in bozulmasının nedeni I1 ≈ Ipre1 (Denk. 15). Bilinen bir yardımcı sinyal iyi tanımlı bir artımsal bileşen sağlayabilir mi?

- **Kilit şekil/tablo/denklemler:**
  - **s. 2–3:** Denk. 1–4. φ2, φ0, Δφ1, Δδ21 ve δ20'nin tanımları.
  - **s. 3:** Şekil 3 (yön elemanı açı bölgeleri), Şekil 4 (faz seçimi sektörleri), Şekil 5 (devre ve kontrol yapısı).
  - **s. 4:** Denk. 5–7 (güç kontrolü ve etkin empedanslar), Şekil 6.
  - **s. 5:**
    - Denk. 8: Zv2 = (1−σ)/(Kpv σ).
    - Denk. 9–10: sanal admitans/empedans.
    - Şekil 8–10: limiter ve sanal empedans blok şemaları.
  - **s. 6:** Tablo I (özet), Denk. 11–15 ve Şekil 11 (saf-arıza ağı ve Zad).
  - **s. 7:** Şekil 12–14 (benzetim sonuçları), Tablo II (devre parametreleri), Şekil 15 (CHIL düzeneği).
  - **s. 8:** Şekil 16–17 (CHIL sonuçları).
  - **Benim notum:** nX/R2 = 20 için empedans açısı ≈ arctan(20) ≈ 87,1° (benim hesabım). Bu değer SEL'in ~86° homojenlik açısıyla ve IEEE 2800'ün açı penceresiyle tutarlı (bkz. Grup sentezi).

---

## 2. Slane & Mate (2026): IBR'lerin şebeke korumasına etkisi (literatür taraması)

- **Künye:**
  - **Yazarlar ve başlık:** John Slane, Adam Mate, *"Impact of Inverter-Based Resources on the Protection of the Electrical Grid"*.
  - **Kurumlar:** Montana State University. Mate ayrıca Los Alamos National Laboratory'de.
  - **Yayın:** IEEE/IAS 62nd Industrial & Commercial Power Systems Technical Conference (I&CPS), Mayıs 2026. Ayrıca arXiv:2603.27816v1 [eess.SY], 29 Mart 2026. Gönderim 9 Ocak 2026, güncel sürüm 21 Mart 2026.
  - **Boyut:** 11 sayfa (gövde ≈ 7 sayfa, geri kalanı kaynaklar), 163 kaynak.

- **Tek cümlede:** IBR'ler SG'den farklı ve kontrole bağlı arıza davranışı gösterir; şebeke kodları, modelleme araçları ve literatür bu davranışı henüz yeterince kapsamıyor; en acil açık alan doğru modelleme.

- **Problem ve bağlam:**
  - IBR payı arttıkça SG varsayımı üzerine kurulu koruma pratikleri yetersiz kalıyor.
  - Bu çalışma; şebeke kodlarının, modelleme araçlarının ve arıza davranışı literatürünün sistem düzeyinde bir özeti (s. 1–2).
  - Motivasyon olarak verilen olaylar: 2016 Güney Kaliforniya yangını ve 2025 İspanya–Portekiz–Fransa kesintisi (s. 1).

- **Yöntem / yaklaşım:**
  - Anlatı tipi (narrative) bir literatür taraması. Bölümler:
    - Teknoloji arka planı (s. 2–3).
    - Şebeke kodları: IEC, IEEE 1547/2800, NERC (s. 3–4).
    - Modelleme araçları: OpenDSS ve LANL'ın PowerModels ailesi (s. 4–5).
    - Yayın istatistiği ve arıza modları (s. 5–7).
  - Tarama yöntemi (veritabanı, arama terimleri, dahil etme ölçütleri) açıklanmamış. Şekil 2 için yalnızca "kapsamlı değil ama temsilî" deniyor (s. 5).

- **Ana bulgular:**
  - **Akım seviyeleri:**
    - SG kısa devrede ≥ 5 pu akım verir. İnverter termal koruma nedeniyle ≈ 2 pu veya daha azını verir (s. 3, s. 6). Aşırı akıma dayalı korumanın çalışmamasının ana nedeni bu.
    - Alt-geçici (sub-transient) akım ise birkaç ms boyunca nominalin ≈ 5 katına çıkabilir [48] (s. 6).
    - Şebeke kodları yalnızca geçici (transient) ve kalıcı yanıtı tarif ediyor, alt-geçici yanıtı tarif etmiyor (s. 4, s. 6).
  - **Gerilime bağımlılık:** GFL'nin arıza yanıtı bara gerilimine bağlıdır (gerilim kontrolün girdisidir); SG'ninki bağlı değildir (s. 6).
  - **IEEE 2800-2022** (s. 3–4):
    - ABD'de yerel veya eyalet otoritesi zorunlu kılmadıkça bağlayıcı değil.
    - Dengeli arızada reaktif akım öncelikli pozitif bileşen akımı isteniyor.
    - Dengesiz arızada yazarların ifadesiyle "PCC gerilimiyle (pu) orantılı ve PCC gerilimini 90–100° önden götüren negatif bileşen akımı" isteniyor. Bu ifadenin sorunları sınırlamalarda.
    - Bölüm 7.2.2.3.2'den alıntı: İletim sistemi sahibi isterse ve IBR sahibiyle anlaşırsa IBR, LVRT/HVRT sırasında **aktif akım öncelikli** çalışabilir (s. 4). Bu da sahadaki yanıt çeşitliliğini artırıyor.
  - **IEEE 1547-2018, Tablo 14** (Şekil 1, s. 4):
    - 0,88 ≤ V ≤ 1,10 pu: sürekli işletme.
    - 0,70 ≤ V < 0,88 pu: zorunlu işletme. Ride-through süresi TVRT = 0,7 s + (4 s / 1 pu)·(V − 0,7 pu).
    - 0,50 ≤ V < 0,70 pu: izinli işletme, asgari ride-through süresi 0,16 s.
    - V < 0,50 pu ve V > 1,20 pu: enerjiyi kes, maksimum tepki süresi 0,16 s.
    - Makale tablonun hangi performans kategorisine ait olduğunu belirtmiyor. Benim bilgime göre bu tablo Kategori I'e ait; doğrulanmalı.
  - **NERC'in hazırlıktaki (henüz yürürlükte olmayan) üç standardı** (s. 4):
    - PRC-028-1: IBR arıza kaydı ve izleme.
    - PRC-029-1: IEEE 2800'e dayalı ride-through.
    - PRC-030-1: Beklenmedik güç kaybı; "en az 20 MW ve tesisin brüt etiket gücünün en az %10'u, 4 s içinde".
  - **Kodlarla ilgili genel gözlem:** Şebeke kodları GFL ile GFM'yi ayırmıyor. Adalanma moduna geçiş ve dönüş için standart yok (s. 4).
  - **Modeller** (s. 4–5):
    - Üreticiler kontrol algoritmalarını gizli tutuyor; modeller DLL olarak paylaşılıyor. "10 IBR'lık bir şebekede her inverterde farklı algoritma" olabilir (s. 4).
    - Tesis tek bir jeneratör olarak modelleniyor; gerçekte bazı inverterler açarken diğerleri açmayabilir (s. 5).
  - **Araçlar** (s. 5):
    - OpenDSS'in belgeleri GFM modellerinin yalnızca ada mikroşebekelerde kullanılmasını öneriyor.
    - PowerModelsProtection.jl GFL'yi PQ kontrolü ve pozitif bileşen akım kısıtlarıyla modelliyor. Yazarlara göre **GFL negatif bileşen basma seçeneği yok gibi görünüyor**.
    - Aynı araç IBR'yi alt-geçici ve geçici ayrımı yapmayan bir sanal empedansla modelliyor.
  - **Olaylar** (s. 6–7):
    - **2016 Blue Cut yangını:** Arızalar 4 çevrim (≈ 70 ms) içinde temizlendi. Buna rağmen birçok PV inverter momentary cessation'a girdi ve yeniden bağlanmaları saniyeler sürdü. Bir noktada ≈ 1.200 MW üretim kaybedildi.
    - **Faz açısı sıçramaları:** PLL'i bozup akımı saniyelerce kararsız bırakabiliyor [49].
  - **Faz seçimi (FTC)** (s. 7):
    - Khan vd. [52], IBR eklendiğinde FTC'nin arıza tipini yanlış sınıflandırdığı senaryolar gösteriyor.
    - Alman kodu uyarınca negatif bileşen basmak bazen yeterli oluyor, bazen inverterin akım sınırlaması yüzünden yetersiz kalıyor [51].
  - **Literatür istatistiği** (Şekil 2, s. 6): Yıllık yayın sayısı en yüksek ≈ 18 (eksende 23. yıl, yani 2023). Değer çubuk grafikten okundu.
  - **Sonuç** (s. 7):
    - En acil sorun modelleme.
    - Pozitif ve negatif bileşen basma profilleri için daha ayrıntılı FRT rehberi gerekiyor.

- **Varsayımlar ve sınırlamalar (eleştirel):**
  - **Özgün içerik yok:** Yeni analiz, benzetim ya da veri yok. Sistematik bir tarama yöntemi de yok.
  - **Teknik doğruluk sorunları:**
    1. **Momentary cessation kendisiyle çelişen iki tanımla veriliyor.** s. 2'de "akım vermeyi durdurur", s. 3'te ise "şebekeden ayrılır ama akım vermeyi kesmez" deniyor.
    2. **IEEE 2800'ün negatif bileşen gereksinimi eksik aktarılmış.** Makale açıyı "PCC gerilimine" göre veriyor. PNNL raporu (s. 1) bu açıyı *negatif bileşen gerilimine* göre veriyor: tam dönüştürücülü için 90–100°, Tip III için 90–150°. Slane & Mate, Tip III için olan aralığı vermiyor.
    3. **Koruma pratiğine dair bazı ifadeler hatalı ya da aşırı basitleştirilmiş** (benim değerlendirmem). Örnek: "çoğu kesici reklozerdir … birkaç çevrim (milisaniye mertebesinde) sonra tekrar kapanır" ve "diferansiyel röleler çoğunlukla bir hattın iki fazını karşılaştırır".
    4. **"GFL DC gerilimini, GFM DC akımını düzenler" genellemesi tartışmalı.**
  - **Sonuç:** Bu makale teknik referans olarak değil, düzenleyici çerçeve ve araçların durumu için kullanılmalı.
  - **Rakamların dayanağı zayıf:** "≈ 2 pu" ve "≈ 5×" rakamları tek kaynaklara ([14], [48]) dayanıyor. Hangi koşulda (süre, kontrol türü) geçerli oldukları verilmemiş.
  - **Şekil 2'de küçük tutarsızlık:** Metin "2000'den 2025 başına kadar" diyor, eksen ise "2000'den bu yana yıl" olarak 1–26 arasını gösteriyor.

- **Projeyle bağlantı:**
  - **Fiziksel öncül:** IEEE 2800 zaten negatif bileşen basmayı istiyor. Bu nedenle uyumlu IBR'lerde negatif bileşen akım yolunun kontrol düzeyinde var olması beklenir. Ancak üç çekince var:
    - (a) 2800 her yerde zorunlu değil.
    - (b) Aktif akım önceliği anlaşmayla seçilebiliyor; bu da başlık payını değiştirir.
    - (c) Her üreticinin algoritması farklı.
    - Sonuç olarak sahada gerçekleşen yardımcı sinyal tesisten tesise değişebilir.
  - **İP1:**
    - Hazır açık araç PowerModelsProtection.jl GFL negatif bileşen basmayı desteklemiyor (s. 5). Projenin fazör modeli bunu kendisi kurmalı.
    - s. 2–3'teki işletme modları (normal, FRT, momentary cessation, açma, ada), set-tabanlı garantinin hangi modları kapsadığını tanımlamak için bir taksonomi sunuyor.
  - **İP2:** Alt-geçici tepe (≈ 5× nominal, birkaç ms) EMT'de arızanın ilk milisaniyelerini etkiler. İnverter modelinin bu tepeyi gerçekçi biçimde üretip üretmediği (kontrol bant genişliği, filtre) kontrol edilmeli.
  - **İP3:**
    - PRC-028-1 yürürlüğe girince IBR arıza kayıtları öğrenen dedektörler için saha verisi kaynağı olabilir (ileriye dönük).
    - Blue Cut tipi bir olayda IBR momentary cessation'a girerse yardımcı sinyal kaybolur. Dedektör "sinyal yok" durumunda güvenli tarafta kalmalı.
  - **İP4:** "4 çevrimde (≈ 70 ms) temizleme" pratik bir referans. Yardımcı sinyal tabanlı karar bu sürenin ilk çevriminde verilmeli.

- **Buradan çıkan açık sorular / araştırma fikirleri:**
  1. ★ **Moda bağlı garanti.**
     - *Soru:* İnverter arıza sırasında momentary cessation, açma ya da aktif akım öncelikli moda geçerse yardımcı sinyal kaybolur veya küçülür. Garanti bu durumlarda ne olur?
     - *Test:* Set-tabanlı tasarıma "IBR katılım oranı" ∈ [0, 1] belirsizliği ekle. Garantinin hangi oranın altında bozulduğunu bul.
  2. **Tesis içi heterojenlik.** Aynı tesiste bazı inverterler açarken diğerleri açmazsa (s. 5) toplam sinyal genliği değişir. Bunu ölçek belirsizliği olarak modelle. PNNL s. 4'teki "çalışan türbin sayısı" etkisiyle aynı mekanizma.
  3. **Faz sıçraması ve PLL.** Faz sıçraması PLL'i bozar, bu da yardımcı sinyalin açısında hata yaratır.
     - *Test:* EMT'de faz sıçraması senaryoları kur (ör. 10°–30°; bu değerler benim önerim) ve tespit güvenirliğini ölç.
  4. **(Düşük öncelik) Araç katkısı.** PowerModelsProtection.jl'e GFL negatif bileşen modeli ekle. İP1 sonuçlarının bağımsız bir araçla çapraz doğrulanmasını sağlar.

- **Kilit şekil/tablo/denklemler:**
  - **s. 3–4:** IEEE 2800 Bölüm 7 özeti ve 7.2.2.3.2 alıntısı.
  - **s. 4:** Şekil 1 (IEEE 1547-2018 Tablo 14, FRT bölgeleri); NERC PRC-028/029/030.
  - **s. 5:** OpenDSS ve PowerModelsProtection.jl yetenekleri.
  - **s. 6:** Şekil 2 (yıllara göre yayın sayısı); akım seviyeleri ve Blue Cut olayı.

---

## 3. PNNL-36069 (2024): IBR'lerin negatif bileşen akımı üretimi (derleme raporu)

- **Künye:**
  - **Yazarlar ve başlık:** Xue Lyu, Jing Xie (PNNL), Thomas E. McDermott (Meltran, Inc.), *"Impact of Inverter-Based Resources on Grid Protection: A Review of Negative-Sequence Current Generation"*.
  - **Yayın:** Pacific Northwest National Laboratory teknik raporu PNNL-36069; ABD Enerji Bakanlığı (DOE) sözleşmesi DE-AC05-76RL01830.
  - **Tarih:** Raporda basılı değil; PDF meta verisi Haziran 2024.
  - **Boyut:** 15 PDF sayfası, ama içerik kısa: Özet s. v, metin s. 1–7, kaynaklar s. 8–9. 20 kaynak.

- **Tek cümlede:** IBR'nin dengesiz arızada negatif bileşen akımı üretip üretmediği tamamen kontrol yapısına bağlıdır. Bu da 50Q, 67Q ve faz seçimi gibi negatif bileşenli koruma elemanlarının doğru çalışıp çalışmayacağını belirler.
  - CSC'de negatif bileşen akımı neredeyse hiç yoktur.
  - DSC ile bağımsız olarak kontrol edilebilir.
  - GFM için araştırma henüz erken aşamadadır.

- **Problem ve bağlam:**
  - Literatür simetrik arızada pozitif bileşen akımı basmaya odaklanmış. Negatif bileşen üretimi daha az anlaşılmış durumda (Özet, s. v).
  - Şebeke kodları negatif bileşen akımı basmayı şart koşmaya başladı (s. 1).

- **Yöntem / yaklaşım:**
  - Kısa bir derleme; yeni benzetim yok. Bölümler:
    - GFL inverterler: Tip III (DFIG) rüzgâr türbinleri (s. 3); tam dönüştürücülü kaynaklar, yani Tip IV rüzgâr ve PV (s. 4–5).
    - GFM inverterler (s. 6).
    - Sonuç (s. 7).

- **Ana bulgular:**
  - **IBR arıza akımının tipik özellikleri** ([1]'den, s. 1):
    1. Kalıcı arıza akımı düşüktür.
    2. Başlangıçta **0,5–1,5 çevrim** süren bir geçici vardır; sonra akım inverter sınırına iner.
    3. Gerilim–akım açısını kontrol stratejisi belirler.
    4. Genelde sıfır bileşen yoktur. Negatif bileşen, kontrol algoritmasına göre kısmen ya da tamamen bastırılmıştır.
  - **Tip III (DFIG) rüzgâr türbinleri:**
    - Dönüştürücü toplam gücün ≈ %30'u kadar; stator doğrudan şebekeye bağlı (s. 1).
    - Rotor devresi negatif bileşen akımına düşük empedanslı bir yol sunar. Bu yüzden CSC altında bile SG'ye benzer negatif bileşen davranışı görülür (s. 1, s. 3).
    - Benzetimde 50Q ve 67Q doğru çalışmış; ancak saha ölçümleri yanlış çalışma ihtimaline işaret ediyor [5] (s. 3).
  - **CSC ve DSC farkı** (s. 1):
    - CSC'de negatif bileşen akımı doğrudan kontrol edilmez ve şebekeye negatif bileşen akımı basılması beklenmez.
    - DSC, pozitif ve negatif bileşeni bağımsız kontrol eder.
  - **Şebeke kodları** (s. 1–2):
    - **VDE-AR-N 4120/4130:** Negatif bileşen akımının genliği, negatif bileşen terminal gerilimiyle orantılı olmalı. Oransal kazanç **k tipik olarak 2–6**.
    - **IEEE 2800-2022:** Dengesiz düşük gerilimde negatif bileşen *reaktif* akımı isteniyor. Bu akım negatif bileşen gerilimini tam dönüştürücülü kaynaklarda **90°–100°**, Tip III'te **90°–150°** önden götürmeli. Genlik, terminaldeki negatif bileşen gerilimine bağlı olmalı. Standart GFM dahil tüm IBR'lere uygulanıyor.
  - **Tip IV, CSC ile** ([5], s. 4):
    - 50Q açmıyor; negatif bileşen genliği yetersiz.
    - 67Q yönü belirleyemiyor; I2 ile V2 arasındaki açı değişmiş.
    - Faz seçimi başarısız; I2, I0'ı 80° önden götürüyor ve hiçbir sektöre düşmüyor.
    - Devredeki türbin sayısı I2'nin hem genliğini hem açısını değiştiriyor.
  - **Tip IV, VDE-AR-N 4120 uyumlu DSC ile** ([10], s. 4):
    - **k, akım sınırı nedeniyle keyfi olarak artırılamaz.**
    - Id ve Iq için ayrı sınırlar yoksa basılan negatif bileşen akımı **ağırlıklı olarak endüktif olmayabilir**.
    - 50Q sorunu çözülüyor, ancak I2'nin yükselme süresi yüzünden 50Q'da **zaman gecikmesi** var. Gecikmenin büyüklüğü verilmemiş.
    - 67Q ve faz seçimi, zorlanan V2–I2 açı ilişkisi sayesinde düzeliyor.
  - **Negatif bileşen açısının takibi** (s. 4): Negatif bileşen açısı pozitif bileşen açısından kalıcı olarak farklıdır. Takip için DDSRF-PLL [13] ya da her faz için ayrı PLL [12] kullanılıyor.
  - **DFIG kontrolü** (s. 3):
    - RSC akım döngüsünün bant genişliği nedeniyle açı [90°, 100°] aralığından sapıyor.
    - RSC'de çift akım kontrolü kullanılınca açı [90°, 150°] dışına bile çıkabiliyor.
    - [9]'un önerdiği GSC tabanlı çift akım kontrolü 90–100°'yi sağlıyor.
    - [6]'nın karşılaştırması: BPSC, PNSG-Tem ve koordineli kontrol ciddi dengesizlikte gereksinimi karşılamıyor; PNSC-I12R karşılıyor.
  - **Faz seçimini düzelten kontroller** (s. 4):
    - [14]: Üç aşamalı gelişmiş çift akım kontrolü. Önce terminal bileşen gerilimlerinden arıza tipini belirliyor, sonra SG'yi taklit eden bir I2 üretiyor, sonra çift senkron çerçevede açı referansını izliyor. İspanya, Almanya ve Kuzey Amerika kodlarıyla test edilmiş.
    - [15]: Pozitif bileşende adaptif sanal empedans arkasında gerilim kaynağı, negatif bileşende tek bir sanal empedans.
  - **GFM** (s. 6):
    - Çoğu CLC çalışması dengeli arızaya ve pozitif bileşen sınırlamasına odaklanmış.
    - **Asimetrik LVRT'de kodun istediği negatif bileşen akımını karşılamak için her bileşen devresine ayrı akım sınırlaması gerekiyor.**
    - [17]: Bileşen referanslarını doğal (abc) çerçevede birleştirip doyuruyor; dengeli ve dengesiz arızada akımı eşiğin altında tutuyor.
    - [18]: Droop kontrollü GFM PV'de SOGI ile bileşen ayrımı yapılıyor; DC bara salınımını azaltmak için negatif bileşen telafisi ekleniyor.
    - [20] **Nasr & Hooshyar:**
      - Pozitif bileşende empedans arkasında gerilim kaynağı.
      - **Negatif bileşende istenen genlik ve açıyı üreten bir akım kaynağı.**
      - Adaptif bileşen akım paylaştırma: İnverter kapasitesini, arızalı fazları belirlemeye gerek kalmadan I1 ile I2 arasında bölüştürüyor.
      - Adaptif sanal empedans ile kenar tetiklemeli bir darbe üreteci: İlk geçicide I1'in sınırı aşmasını önlüyor.
      - Bir doyurucu I2'yi arıza boyunca sınırlıyor.
      - IEEE 2800 uyumu benzetimle gösterilmiş.
  - **Sonuç** (s. 6–7):
    - GFM'den negatif bileşen üretimi ve bunun korumaya etkisi konusundaki araştırma "henüz erken aşamada".
    - IBR'ler arasında negatif bileşen üretiminde tutarlılık yok.
    - Ayrıntılı EMT çalışmaları gerekli.
    - Röle ile IBR kontrolünün koordinasyonu için daha fazla araştırma ve standart gerekiyor.

- **Varsayımlar ve sınırlamalar:**
  - **Kapsam küçük:** ≈ 7 sayfa içerik ve 20 kaynak. Sistematik bir tarama değil; büyük ölçüde Haddadi vd. (EPRI) çalışmalarına dayanıyor.
  - **Sayısal içerik zayıf:** Karşılaştırma tablosu, eşik, süre ya da genlik değeri yok; yalnızca k aralığı ve açı pencereleri veriliyor. 50Q gecikmesinin büyüklüğü bile yazılmamış.
  - **Kanıt büyük ölçüde benzetim:** DFIG saha ölçümlerine yalnızca değiniliyor.
  - **IEEE 2800'ün zamanlama şartları yok:** Tepki ve oturma süreleri burada verilmiyor; SEL makalesinde var.
  - **Kapsam kod-uyumlu I2 ile sınırlı:** İncelenen, gerilime bağlı olarak basılan I2. Gerilimden bağımsız, keyfi bir I2 (proje için gereken tür) tartışılmıyor.
  - **Küçük yazım hatası:** Bölüm başlıklarında "Gird-Following/Forming" geçiyor. İçeriği etkilemiyor.

- **Projeyle bağlantı:**
  - **Fiziksel öncül için doğrudan kanıt ve koşullar:**
    1. CSC'li bir inverter tasarlanmış I2 basamaz. GFL'de DSC, GFM'de ise negatif bileşende akım kaynağı olarak çalışan bir yapı (Nasr–Hooshyar) gerekir.
    2. Başlık payı sınırlı: kod için gereken k bile akım sınırı yüzünden artırılamıyor.
    3. Limiterin yapısı sinyalin açısını bozabilir. Id ve Iq için ayrı sınır yoksa akım endüktif olmayabilir.
    4. I2'nin yükselme süresi 50Q'yu geciktiriyor. Yardımcı sinyal de ilk çevrimde tam olarak oluşmayabilir.
  - **İP1:**
    - Toplam negatif bileşen akımı = kodun istediği I2(V2) + yardımcı sinyal. Kodun istediği kısım başlık payının bir bölümünü zaten tükettiği için tasarım ikisini birlikte ele almalı.
    - IEEE 2800 açı penceresi (90–100°) kısıt olarak yazılabilir.
    - Negatif bileşen açı takibindeki hata (PLL), bir açı belirsizliği olarak modele eklenmeli.
  - **İP2:**
    - Üç inverter modeli kurulmalı: CSC, DSC ve negatif bileşende akım kaynağı olan GFM (Nasr–Hooshyar tipi).
    - Her birinde tasarlanmış sinyalin gerçekleşme doğruluğu ölçülmeli: genlik ve açı hatası, yükselme süresi.
    - DDSRF-PLL ile her faz için ayrı PLL karşılaştırılmalı.
  - **İP3:**
    - 50Q, 67Q ve I2–I0 açısına dayalı faz seçimi geleneksel temel elemanlar olarak kullanılabilir.
    - Tip IV CSC'nin başarısız olduğu örnek (I2–I0 = 80°) bir test vakası olabilir.
  - **İP4:** Bileşen ayrıştırmanın (DDSRF, SOGI, APF) kendisi de gecikme getirir. Gömülü gecikme bütçesine dahil edilmeli.

- **Buradan çıkan açık sorular / araştırma fikirleri:**
  1. ★ **Kodla uyumlu sinyal ile yardımcı sinyalin birlikte tasarımı.**
     - *Soru:* IEEE 2800 açı penceresi ve VDE k-yasası altında, toplam I2'nin açısı pencere içinde kalırken ayırma garantisini sağlayan en büyük yardımcı sinyal payı nedir?
     - *Neden konveks (benim çıkarımım):* Her senaryo için V2 sabit alınırsa, {I : ∠(I/V2) ∈ [90°, 100°]} kümesi karmaşık düzlemde iki yarı düzlemin kesişimidir; bu iki doğrusal eşitsizlik demektir. Akım sınırı da SOC kısıtıdır. Dolayısıyla problem CVXPY'de konveks kalır.
  2. ★ **GFM'de tasarlanmış I2.**
     - *Test:* Nasr–Hooshyar yapısını EMT'de kur. Negatif bileşen akım kaynağının referansına yardımcı sinyal ekle ve ilk 16,7 ms'deki gerçekleşme hatasını ölç.
     - *Önemi:* Projenin fiziksel öncülünü GFM için doğrudan sınar.
  3. **Negatif bileşen PLL hatasına duyarlılık.** DDSRF ile her faz için ayrı PLL'in takip hatasını karşılaştır. Bu hatanın yardımcı sinyalin açısına ve ayırma marjına etkisini ölç.
  4. **Tesis toplulaştırma.** Devredeki inverter sayısı değişince yardımcı sinyalin genliği ve açısı nasıl değişir? Sonucu tasarıma ölçek belirsizliği olarak ekle.
  5. **Hangi limiter açıyı daha iyi korur?** "Id/Iq ayrı sınır" ile "dairesel" limiteri karşılaştır. Li vd.'deki CLC deneyleriyle birlikte yapılabilir.

- **Kilit şekil/tablo/denklemler:**
  - Raporda şekil, tablo ya da denklem yok. Kilit pasajlar:
    - **s. 1:** Tipik IBR arıza özellikleri; VDE k = 2–6; IEEE 2800'ün 90–100° ve 90–150° pencereleri.
    - **s. 3:** DFIG'de açı sapması.
    - **s. 4:** Tip IV CSC'nin başarısızlıkları; k sınırı; Id/Iq sınırı; 50Q gecikmesi; negatif bileşen PLL'leri.
    - **s. 6:** GFM yaklaşımları ve Nasr–Hooshyar.

---

## 4. Kasztenny, Fischer, Hooshyar (SEL, 2026): IBR arıza yanıtı gereksinimlerinin yeniden çerçevelenmesi

- **Künye:**
  - **Yazarlar ve başlık:** Bogdan Kasztenny, Normann Fischer (Schweitzer Engineering Laboratories, Inc.), Ali Hooshyar (University of Toronto), *"From Complexity to Consistency: Reframing Fault Response Requirements for Inverter-Based Resources"*.
  - **Yayın:** SEL teknik makalesi TP7255-01, "Original edition released February 2026" (kod 20260225). Konferans bilgisi verilmemiş.
  - **Boyut:** 14 PDF sayfası (kapak + 13 sayfa), 6 kaynak.

- **Tek cümlede:** IBR'nin arıza yanıtı fazörlerle, yavaş ve karmaşık biçimde değil, zaman domeninde, anında ve basit biçimde tanımlanmalı. Bunun yolu iki adım:
  - Arıza anında pozitif bileşen kontrolcüsü ve PLL "dondurulur".
  - İnverter terminallerinde sanal bir şönt reaktör taklit edilir.
  - Böylece artımsal ve negatif bileşen akımları gerilimlerle sabit, yüksek endüktif bir empedans üzerinden tutarlı kalır. Klasik röle ilkeleri de IBR'yi ayrıca modellemeye gerek olmadan çalışır.

- **Problem ve bağlam:**
  - **Akım sınırı** (s. 1): Yarı iletkenler faz akımını ≈ 1,2–1,5 pu ile sınırlar; gelecekte ≈ 2 pu'ya çıkabilir. Maliyet baskısı yüzünden bu sınırlar kalıcı olacak.
  - **Kodların zaman toleransları geniş** (s. 1–2):
    - LVRT ve negatif bileşen basma için tipik olarak birkaç çevrim tanınıyor (s. 1).
    - Koruma ise çok daha hızlı. Ultra yüksek hızlı bir röle ve hızlı bir kesici arızayı 1,5 çevrimde (60 Hz'de 25 ms) temizleyebilir (s. 2).
    - IEEE 2800'de basamak tepki süresi 2,5 çevrim, oturma süresi 4 çevrim (s. 2).
  - **IBR kontrol eylemleri milisaniyeler içinde başlıyor** (s. 2). Bu da tam koruma için kritik olan ilk çevrimlerde sinyal bozulmaları yaratıyor.
  - **Ölü bantlar, limitleyiciler, fazör işleme gecikmeleri ve gizli kontrol yazılımı** her kurulumun ayrı ayrı modellenmesini gerektiriyor (s. 2). Yazarların sorusu: "Kurulum-özel modelleme hâlâ gerekiyorsa buna standart denir mi?"
  - **Hedefler** (s. 2):
    - Modellemeye gerek kalmadan ayar yapılabilmesi.
    - Ek maliyet getirmemesi.
    - Standardize edilen kapsamın dar tutulması.
    - Koruma ile IBR'nin rollerinin net ayrılması.
    - Firmware güncellemeleriyle değişmeyen, kalıcı bir yanıt.

- **Yöntem / yaklaşım:**
  - **İlkeler** (s. 2–3):
    - **Hız:** Geleneksel röleler ≈ 1 çevrimlik veriyle çalışır. IBR birkaç ms içinde yanıt verip ilk birkaç çevrim kararlı kalmalı. Röleye uygun yanıt **en az 2 çevrim** sürmeli.
    - **Akım kaynağı bakışı:** İlk çevrimlerde IBR'yi bir akım kaynağı olarak düşün. Gerilimi şebeke dayatır; IBR bu gerilimle tutarlı bir akım üretir.
    - **Artımsal akım:** Toplam akım SG'ninki kadar büyük olamaz ama artımsal akım SG'ninki gibi davranabilir. Yakın arızada artımsal akım için **başlık payı 0,2–0,5 pu** (s. 2).
    - **Negatif bileşen:** Normal işletmede ≈ 0 olduğu için negatif bileşen de bir artımsal büyüklüktür. V2 ile I2 arasındaki ilişki sabit ve **yüksek endüktif** bir empedans olmalı. Bu şekilde şebekenin homojenliği korunur (s. 3).
    - **PLL:** Bellek polarizasyonu için PLL'in açısı ve frekansı ilk çevrimlerde korunmalı. Saha deneyimine göre arıza sırasında açıyı hızlı takip etmek zarar veriyor (s. 3).
  - **Uygulama** (Şekil 1, s. 3; Şekil 2, s. 4). Dört modül var:
    - **Pozitif bileşen kontrolcüsü:**
      - Yalnızca I1'i düzenler.
      - Arızada referansları dondurulur; en az 2 çevrim, tercihen normal temizleme süresi kadar (3–4 çevrim) ya da kesici arızası durumundaki temizleme süresi kadar (9–11 çevrim).
    - **Arıza tespit modülü:**
      - Kısa pencereli fazörlerle çalışan basit bir ani düşük gerilim elemanı.
      - Yükte yanlışlıkla tetiklense bile IBR akımlarını değiştirmez.
    - **Sanal şönt reaktör modülü:** Faz-faz gerilim örneklerinden faz akımlarını hesaplar. Sinyal işleme açısından basit bir IIR filtredir.
    - **İnverter akım kontrolcüsü:**
      - Dondurulmuş pozitif bileşen akımı ile reaktör akımlarının toplamını referans olarak alır.
      - dq çerçevesinde uygulanırken reaktör akımları PLL ile dq'ya dönüştürülüp eklenir (Şekil 2).
  - **Etkin yanıt** (Denk. 1–2, s. 4):
    - ΔI_LOOP = −ΔV_LOOP/Z
    - ΔI1 = −ΔV1/Z
    - I2 = −V2/Z
    - Zaman domeninde: Δi_Z = −Δv/|Z|. Bu, replika akım ilkesidir.
  - **Sanal reaktör filtresi** (Şekil 3, s. 5):
    - Denk. 3: Topraksız, simetrik RL reaktörün diferansiyel denklemleri (iA + iB + iC = 0).
    - Denk. 4: Trapez kuralıyla ayrıklaştırma.
    - **Denk. 5:** iA(k) = GI·iA(k−1) − GV·[vAB(k) − vCA(k) + vAB(k−1) − vCA(k−1)]
    - **Denk. 6:** GV = 1/(6(2·L·fS + R)), GI = (2·L·fS − R)/(2·L·fS + R). R > 0 olduğu sürece GI < 1, yani filtre kararlıdır.
    - Homojenlik açısı örneği: 86°.
    - Gerilimlere isteğe bağlı bir ön alçak geçiren filtre uygulanabilir; önerilen bant genişliği ≈ 500 Hz.
  - **Gecikme telafisi** (Denk. 7, s. 5):
    - Gecikme kaynakları: Kenar yumuşatma (anti-aliasing) filtresi, isteğe bağlı alçak geçiren filtre ve inverterin referansı ≈ 1 ms geriden izlemesi.
    - **Denk. 7:** Θ_COMP = Θ − ΔT·fN·360/1000.
    - Örnek: 60 Hz'de 1,0 ms gecikme, reaktör açısının ≈ 21° azaltılmasıyla telafi edilir.
  - **SG eşdeğerinden türetme** (Şekil 4, Denk. 8, s. 6):
    - SG: E1 arkasında jX'd (Thevenin) → aynı devrenin Norton eşdeğeri → IBR.
    - IBR eşdeğeri: Pozitif bileşende I1 akım kaynağına paralel bir Z, negatif bileşende Z.
    - Koşul: |Z| ≫ X'd ve |Z| ≫ |Z2|.
  - **Benzetim modeli** (Şekil 5, s. 7). PSCAD/EMTDC'de değiştirilmiş CIGRE Kuzey Amerika YG benchmark sistemi (TB 575):
    - Bara 6b'deki 300 MW / 170 MVAR'lık SG yerine 300 MW'lık bir IBR konmuş.
    - Bara 6b'deki şönt kapasitör 180 MVAR'dan 360 MVAR'a çıkarılmış.
    - IBR sisteme 50 km'lik, 230 kV'luk bir hatla bağlanmış.
    - Tesis 300 adet 1 MW'lık inverterden oluşuyor. Biri ayrıntılı modellenmiş, geri kalanlar toplulaştırma (aggregator) modeliyle temsil edilmiş.
    - 34,5 kV toplayıcı sistem π-devre olarak modellenmiş: R = 0,016 pu, X = 0,059 pu, şönt kapasitif reaktans 31,25 pu (300 MVA, 34,5 kV baz).
    - Birim trafolar Δ-Yg, kaçak reaktans 0,05 pu. Tesis trafosu Δ-Yg, kaçak reaktans 0,1 pu (300 MVA baz).
    - İnverter: 480 V, anahtarlama frekansı 9 kHz, DC bara 1,5 kV.
    - Dondurma: Pozitif bileşen referansı ve PLL, bozulmadan **çeyrek çevrim önce** kaydedilen değerlerde dondurulmuş.
    - Sanal reaktör: 1 MVA, 480 V'luk birim için **0,045 + j0,3016 Ω**.
  - **Röle testi** (s. 7–8):
    - Ticari röleler SEL-T401L [1] ve SEL-411L [6], COMTRADE dosyalarıyla dijital geri oynatma yöntemiyle test edilmiş. İkincil büyüklükler 2000:1 VT ve 1600:5 CT ile hesaplanmış.
    - Röle değişken pencereli bir fazör kestirici kullanıyor. Arıza başında pencere çevrimin bir kesrine iner, sonra kaydıkça tam çevrime genişler. Fazörler ≈ yarım çevrimde oturur.
    - TD32 elemanı alçak geçiren filtre ve bir çevrimlik bellek kullanıyor.
    - Artımsal pozitif bileşen grafikleri 50 ms'lik (3 çevrim) bir pencereyle çizilmiş.

- **Ana bulgular** (tüm vakalar 50 km uzaktaki, hattın uzak ucundaki arızalar):

  | Vaka | IBR akımı tepe / oturma | ΔZ1 (ikincil) | Z2 (ikincil) | Diğer |
  |---|---|---|---|---|
  | Simetrik 3 faz (Şekil 6, s. 8–9) | 1,56 / 1,12 pu | ≈ 45 Ω, 85°; ≈ 10 ms'de oturuyor | — | FIDA/B/C doğru; arıza yeri 50,048 km |
  | BC, Rf = 5 Ω primer (Şekil 7, s. 9–10) | 1,62 / 1,27 pu | ≈ 45 Ω, 84° | ≈ 46 Ω, 88°; ≈ ¾ çevrimde oturuyor | ΔI1–I2 açısı 177° (ideal ≈ 180°); arıza yeri 49,8 km; TD32, 32Q, FIDB/FIDC doğru |
  | AG → ABG gelişen arıza (Şekil 8, s. 10–11) | 1,46 / 1,21 pu | ≈ 44,9 Ω, 84° | ≈ 45 Ω, 87° | I2–I0 açısı AG'de −6° (ideal 0°), ABG'de 113° (ideal 120°); tipik FID eşiği 30°; arıza yeri ≈ 49,9 km |

  - **Negatif bileşen akımı gecikmesiz ortaya çıkıyor** (s. 9). Geçici sürenin uzunluğunu yalnızca fazör penceresi belirliyor.
  - **ΔZ1 ile Z2 arasındaki küçük farklar** yazarlarca inverter akım kontrolcüsünün doğruluk sınırına bağlanıyor (s. 9).
  - **Gelişen arıza ve IEEE 2800** (s. 10): IEEE 2800'ün tanıdığı 50 ms'lik ayar payıyla akım, değişen gerilimi hiç yakalayamayabilir. Bu durumda IBR standarda uygun kalır ama I2, V2 ile hiçbir zaman tutarlı olmaz.
  - **Sanal reaktör akımları** (Şekil 9, s. 11): Arızadan önce 0,768 pu. DC ofset içeriyor ama ani sıçrama göstermiyor. Pozitif bileşen referansı dondurulmuş durumda.
  - **Yöntemle bile zorlanan koruma ilkeleri** (s. 7):
    - Faz aşırı akım koruması (50/51, 67).
    - Uzak yedek mesafe koruması (21T). Düşük arıza akımı uzak besleme (remote infeed) etkisini büyütüyor.
  - **Standartlara önerilen eklemeler** (s. 12):
    - Reaktif güç ve sentetik atalet gibi kontrol eylemlerini birkaç çevrim ertele.
    - Negatif bileşen akımı gecikmesiz gelsin; bu da zaman domeni uygulama gerektirir.
    - Artımsal pozitif bileşen empedansı negatif bileşen empedansına eşit olsun.
    - Pozitif bileşen kontrolcüsü ve PLL ilk birkaç çevrimde değişmesin.

- **Varsayımlar ve sınırlamalar (eleştirel):**
  - **Yalnızca uzak uç (50 km) arızaları gösterilmiş.** Reaktör empedansı yakın (close-in), dirençsiz arızaya göre seçilmiş ama yakın arıza, yüksek dirençli arıza ve ters yönlü arıza gösterilmemiş.
  - **Tepe akımlar makalenin kendi sınırını aşıyor.** Örneklerdeki 1,56 ve 1,62 pu tepeler, makalenin verdiği 1,2–1,5 pu yarı iletken sınırının üzerinde. Oturmuş değerler (1,12–1,27 pu) ise sınır içinde. Reaktör akımındaki DC ofset anlık tepeyi büyütüyor. Yarı iletken için anlık tepe önemli olduğu hâlde bu konu tartışılmamış.
  - **Kapsam dar:**
    - Tek ayrıntılı inverter ve toplulaştırma modeli kullanılmış.
    - GFM yok.
    - Zayıf şebeke ya da kısa devre oranı taraması yok.
    - Birden çok IBR'nin etkileşimi incelenmemiş.
  - **Dondurmanın yan etkileri tartışılmamış.** Pozitif bileşen kontrolcüsünü ve PLL'i ≥ 2 çevrim dondurmanın kararlılığa etkisi ve IEEE 2800'ün bugünkü hızlı reaktif akım beklentisiyle çatışması ele alınmamış. Öneri zaten standardın değişmesini istiyor.
  - **Bağımsız doğrulama yok.**
    - Kullanılan röleler yazarların kendi ürünleri (SEL-T401L, SEL-411L).
    - Teşekkür kısmında laboratuvar testlerinden söz ediliyor, ama gerçek bir güç inverteriyle test yok; akımların hepsi PSCAD'den.
  - **Gelişen arızanın zamanlaması belirsiz.** Metin geçişin 96 ms'de olduğunu söylüyor. Ancak Şekil 8'in zaman ekseninde I2–I0 açısındaki geçiş ve FIDB'nin devreye girmesi yaklaşık 60–80 ms arasında görünüyor. Farklı bir zaman referansı olabilir; netleştirilemedi.
  - **"0,2–0,5 pu başlık payı" ile örnekteki 0,768 pu reaktör akımı ilk bakışta çelişiyor.**
    - *Benim hesabım:* 480 V, 1 MVA için baz empedans 0,2304 Ω. |Z| ≈ 0,305 Ω ≈ 1,32 pu. Buna göre 1 pu gerilimde reaktör akımı ≈ 0,76 pu; bu, makaledeki 0,768 pu ile tutarlı.
    - *Açıklama:* Bu akım ağırlıkla reaktif olduğu için 1 pu'luk aktif yük akımına dik eklenir: √(1² + 0,76²) ≈ 1,25 pu. Yani genlik açısından kullanılan başlık payı ≈ 0,25 pu'dur. Makale bunu açıkça yazmıyor.
    - *Ek gözlem:* Reaktörün açısı arctan(0,3016/0,045) ≈ 81,5° (benim hesabım). Bu, 86°'lik homojenlik açısından küçük. Denk. 7'deki gecikme telafisinden kaynaklanıyor olabilir, ama makale bunu belirtmiyor.
  - **Felsefe:** Makale "tasarlanmış" bir sinyal değil, *pasif ve sabit bir empedans* öneriyor. Amaç, IBR'yi modellemeye gerek kalmayacak kadar öngörülebilir kılmak.

- **Projeyle bağlantı:**
  - **Fiziksel öncül:**
    - Bu makale, bir IBR'nin arızada negatif bileşen akımını **gecikmesiz ve kontrollü biçimde** üretebileceğine dair dört kaynak arasındaki en güçlü kanıt (benzetimde, 9 kHz anahtarlamayla).
    - Z2 ≈ ¾ çevrimde oturuyor; inverter gecikmesi ≈ 1 ms. Yani akım kontrolcüsünün bant genişliği tasarlanmış bir sinyal için de yeterli görünüyor.
    - **Koşul:** Kontrol fazör tabanlı ve yavaş değil, zaman domeninde uygulanmalı. Bugünkü IEEE 2800 zamanlaması (2,5/4 çevrim, 50 ms) ilk çevrimde böyle bir davranışı garanti etmiyor.
  - **Felsefi gerilim:**
    - SEL'in tezi: "Negatif bileşen sabit bir sanal empedanstır; IBR pasif ve öngörülebilir olmalıdır."
    - Projenin yardımcı sinyali ise aktif ve tasarlanmış bir bileşen ekliyor. Bu durumda I2 artık −V2/Z ile tutarlı olmayabilir.
    - Etkilenebilecek mekanizmalar: 32Q, FID (I2–I0 açısı), reaktans polarizasyonu ve "normal işletmede I2 ≈ 0" varsayımı.
    - Uyumlu bir tasarım ya bu tutarlılığı korumalı ya da rölenin yardımcı sinyali bilmesini (IBR–röle koordinasyonu) gerektirmeli.
  - **İP1:**
    - Sayısal kısıtlar: Imax 1,2–1,5 pu (ileride ≈ 2 pu); artımsal başlık payı 0,2–0,5 pu; homojenlik açısı ≈ 86°.
    - **Gecikmeyi açıya çevirmek:** Denk. 7'ye göre 60 Hz'de 1 ms gecikme = 21,6° (benim hesabım; makale "yaklaşık 21°" diyor). İP4'te ölçülecek gecikme, İP1'de açı belirsizliği olarak modele girmeli.
    - **Alternatif tasarım değişkeni:** Sanal reaktörün Z değeri. Bu bir "kapalı çevrim yardımcı sinyal" olarak düşünülebilir.
  - **İP2:**
    - Değiştirilmiş CIGRE NA modelinin parametreleri tam verilmiş; model tekrar üretilebilir.
    - Denk. 5–6'daki IIR filtre doğrudan Simulink veya PSCAD'de kodlanabilir.
    - Dondurma mantığı (çeyrek çevrim önceki değerler) da kolayca eklenebilir.
  - **İP3:**
    - Geleneksel temel elemanlar: TD32 (bir çevrimlik bellek), 32Q, FID (30° eşik) ve değişken pencereli fazör kestirici.
    - Replika akım (Denk. 2), model tabanlı bir artık (residual) üreteci için doğal bir başlangıç. Örneğin r(t) = Δi(t) + Δv(t)/|Z| (benim önerim). Z biliniyorsa bu sistem modeli doğrudan Kalman filtresi dedektörüne verilebilir.
    - COMTRADE ile geri oynatma, gerçek bir röleyle test yapmanın yolu.
  - **İP4:**
    - Bir çevrim ≈ 16,7 ms. Z2 ≈ ¾ çevrimde, yani ≈ 12,5 ms'de oturuyor (benim hesabım). Bütçenin büyük kısmı fazörün oturmasına gidiyor. Bu, zaman domenine dayalı artımsal/replika yöntemlere avantaj sağlıyor.
    - IIR filtre örnek başına yalnızca birkaç çarpma ve toplama gerektiriyor. Gömülü kartta maliyeti ihmal edilebilir.

- **Buradan çıkan açık sorular / araştırma fikirleri:**
  1. ★★ **Sanal reaktörü optimize etmek (kapalı çevrim yardımcı sinyal).**
     - *Fikir:* SEL, Z'yi elle seçiyor. CVXPY ile Z'nin (ya da küçük bir FIR/IIR filtrenin) genliği ve açısı, akım sınırı altında arıza/normal ayırma marjını en büyükleyecek şekilde seçilebilir. Sonuç açık çevrimde tasarlanmış enjeksiyonla karşılaştırılır.
     - *Pratik başlangıç:* Z'nin genlik ve açısını bir ızgara üzerinde tara; her noktada konveks alt problemi çöz.
  2. ★ **Hibrit tasarım.** SEL reaktörünün üzerine küçük bir tasarlanmış bileşen ekle.
     - *Soru:* 32Q, FID (30° eşik) ve ΔZ1 ≈ Z2 eşitliği bozuluyor mu?
     - *Test:* EMT ve röle mantığıyla ölç.
  3. ★ **Gecikmeyi açı belirsizliğine çevirmek.** İP4'te ölçülen gecikmeyi (0,5 / 1 / 2 ms) Denk. 7 ile açı hatasına dönüştür ve İP1'in belirsizlik kümesine ekle. Garantinin hangi gecikmede bozulduğunu bul.
  4. **Makalenin göstermediği vakalar.** Yakın dirençsiz arıza, yüksek dirençli arıza, ters yönlü arıza ve zayıf şebeke. Tepe akımı 1,5 pu'yu aşıyor mu? Z2 kararlı kalıyor mu?
  5. **Dondurulmuş PLL'in referans olarak kullanılması.** Dondurma süresince yardımcı sinyalin açısı ne kadar doğru kalıyor? Dondurmasız (hızlı PLL) durumla karşılaştır.

- **Kilit şekil/tablo/denklemler:**
  - **s. 3–4:** Şekil 1 ve Şekil 2 (kontrolcü blok şemaları).
  - **s. 4:** Denk. 1–2: ΔI1 = −ΔV1/Z, I2 = −V2/Z, Δi_Z = −Δv/|Z|.
  - **s. 5:** Şekil 3 ve Denk. 3–6 (sanal şönt reaktör IIR filtresi); Denk. 7 (gecikme telafisi).
  - **s. 6:** Şekil 4 ve Denk. 8 (SG'den IBR eşdeğer ağına türetme).
  - **s. 7:** Şekil 5 (test sistemi).
  - **s. 8–11:** Şekil 6–8 (röle sonuçları).
  - **s. 11:** Şekil 9 (IBR sinyal akışı).

---

## Grup sentezi

### Dört kaynağın birlikte söyledikleri

1. **IBR'nin arıza akımını fizik değil kontrol belirler.** Aynı arıza, farklı kontrol veya limiterle tamamen farklı negatif bileşen ilişkileri üretebilir. Kaynaklar: Li vd. Şekil 12 ve 16; PNNL s. 1, 4; SEL s. 1–2; Slane & Mate s. 4.
2. **Akım sınırı dar.**
   - SEL: ≈ 1,2–1,5 pu (s. 1).
   - Slane & Mate: ≈ 2 pu veya altı (s. 3).
   - SEL'e göre artımsal akım için başlık payı 0,2–0,5 pu (s. 2).
3. **Negatif bileşenli elemanlar hem en kırılgan hem de kontrolle en kolay düzeltilen elemanlar.** 32Q/67Q, 50Q ve I2–I0 açısına dayalı faz seçimi IBR kontrolüne en duyarlı olanlar. Düzeltme yolları: DSC, endüktif sanal empedans, sanal reaktör.
4. **Doğru negatif bileşen davranışı üzerinde yakınsama var: sabit ve yüksek endüktif bir negatif bileşen empedansı.**
   - Li vd.: nX/R2 = 20 (açısı ≈ 87°, benim hesabım) ile φ2 = −92,3°.
   - SEL: Z2 ≈ 87–88°; homojenlik açısı ≈ 86°.
   - IEEE 2800 (PNNL'e göre): I2, V2'yi 90–100° önden götürmeli.
5. **Zamanlama: İlk çevrim belirleyici, ama sıradan IBR'ler için kimse onu iyi karakterize etmiyor.**
   - Li vd. ilk geçiciyi bilerek atlıyor (s. 6–7).
   - PNNL, ilk geçicinin 0,5–1,5 çevrim sürdüğünü ve 50Q'nun I2 yükselme süresi yüzünden geciktiğini söylüyor (s. 1, 4).
   - Slane & Mate alt-geçici tepeyi vurguluyor: ≈ 5× nominal, birkaç ms (s. 6).
   - SEL, standartların 2,5/4 çevrim ve 50 ms toleranslarını yetersiz buluyor. Kendi yöntemiyle negatif bileşen empedansının ¾ çevrimde oturduğunu gösteriyor (s. 2, 9, 10).

> **İşaret kuralları ve açılar arası çeviri (benim çıkarımım; akım yönü IBR'den şebekeye):**
>
> - **Tanımlar:**
>   - Li vd.: φ2 = ∠(v2/i2). İleri arızada ≈ −90°.
>   - SEL: Z2 = −V2/I2.
>   - IEEE 2800: I2'nin V2'ye göre öncülük açısı ψ = ∠(I2/V2).
> - **Bağıntılar:** ψ = −φ2 ve ∠Z2 = 180° − ψ.
> - **IEEE 2800 penceresinin karşılığı:** ψ ∈ [90°, 100°] ⇔ φ2 ∈ [−100°, −90°] ⇔ ∠Z2 ∈ [80°, 90°].
> - **Makalelerdeki değerler bu pencereye göre:**
>   - Li'nin endüktif sanal empedansla ölçtüğü φ2 = −92,3°, yani ψ = 92,3°: pencerede.
>   - SEL'in Z2 = 87–88° değeri, yani ψ ≈ 92–93°: pencerede.
>   - Li'nin dairesel limiterli CHIL sonucu φ2 = −171°, yani ψ = 171°: pencerenin çok dışında, aynı zamanda 32Q ileri bölgesinin de dışında.
> - **Uyarı:** Li'nin ölçüm noktası trafonun YG tarafındaki röle; IEEE 2800'ün referansı ise IBR terminali.
>   - Δ-Y trafonun faz kayması V2 ile I2'yi aynı açıyla döndürür; aradaki açı değişmez.
>   - Trafonun reaktansı ise açıyı bir miktar değiştirir.
> - **Sonuç:** Li'nin "korumayla birlikte çalışabilir CLC" koşulu ile IEEE 2800'ün açı şartı pratikte aynı şeyi istiyor.

### Çelişkiler ve gerilimler

| Konu | Kaynak A | Kaynak B | Değerlendirme |
|---|---|---|---|
| Artımsal elemanlar | Li vd.: GFM + CLC ile "doğrudan kullanılmamalı" (s. 8) | SEL: Uygun IBR kontrolüyle tüm arıza tiplerinde güvenilir yön bulur (s. 8–10, 12) | Koşula bağlı, gerçek bir çelişki değil. Li'de akım sınırı I1 ≈ Ipre1 yapıyor ve Zad'nin açısı tanımsız kalıyor. SEL ise artımsal akımı yapı gereği −ΔV/Z'ye bağlıyor. Bugünkü IBR'ler için Li, önerilen standart için SEL geçerli. |
| IBR'nin modeli | GFM = empedans arkasında gerilim kaynağı (Li s. 2–3; PNNL s. 6) | İlk çevrimlerde akım kaynağı + şönt Z (SEL s. 2, 6) | Thevenin ve Norton eşdeğerleri. Asıl fark limiterin ve kontrolün dinamiğinde. |
| Akım sınırı | ≈ 2 pu veya altı; alt-geçicide ≈ 5× (Slane & Mate s. 3, 6) | 1,2–1,5 pu (SEL s. 1). SEL'in kendi örneklerinde tepeler 1,46–1,62 pu | Kaynaklar anlık tepe ile oturmuş değeri ayırmıyor. Tasarımda hangisinin sınırlandığı açıkça seçilmeli. |
| IEEE 2800 açı tanımı | "PCC gerilimini 90–100° önden" (Slane & Mate s. 4) | "Negatif bileşen gerilimini 90–100° (tam dönüştürücülü), 90–150° (Tip III)" (PNNL s. 1) | PNNL daha kesin. Slane & Mate'in ifadesi eksik ve Tip III aralığını atlıyor. |
| Standartlaşmanın yönü | Daha ayrıntılı pozitif/negatif bileşen basma profilleri (Slane & Mate s. 7); daha fazla araştırma ve standart (PNNL s. 7) | "Daha az ama daha iyi standardize et": zaman domeni ve artımsal büyüklükler (SEL s. 1–2, 12) | Projenin tasarlanmış sinyal yaklaşımı daha fazla özel davranış eklemek demek. Bu, SEL'in "modellemeden öngörülebilirlik" hedefiyle gerilim yaratıyor. |
| Reaktif destek | IEEE 2800: Dengeli arızada reaktif akım öncelikli pozitif bileşen (Slane & Mate s. 3–4) | SEL: İlk çevrimlerde pozitif bileşeni dondur, reaktif desteği ertele (s. 2, 12) | SEL açıkça standart değişikliği öneriyor. |
| Momentary cessation tanımı | "Akım vermeyi durdurur" (Slane & Mate s. 2) | "Şebekeden ayrılır ama akım vermeyi kesmez" (Slane & Mate s. 3) | Aynı makalenin içinde çelişki. |

### Fiziksel öncül: İnverter arıza sırasında tasarlanmış bir negatif bileşen akımı basabilir mi?

**Lehte kanıtlar:**
- **Kontrol yolu var.** GFL'de DSC ile I2 bağımsız olarak kontrol edilebilir (PNNL s. 1, 4). Alman kodu ve IEEE 2800 zaten I2 basmayı şart koşuyor (PNNL s. 1; Slane & Mate s. 3–4).
- **GFM'de de mümkün.** Pozitif bileşende gerilim kaynağı, negatif bileşende istenen genlik ve açıyı üreten akım kaynağı kullanılabilir (Nasr–Hooshyar; PNNL s. 6). Benzetimde IEEE 2800 uyumu gösterilmiş.
- **Akım kontrolcüsünün bant genişliği yetiyor** (SEL s. 5, 7, 9):
  - 9 kHz anahtarlamayla negatif bileşeni temsil eden çift frekanslı dq bileşenleri izlenebiliyor.
  - İnverterin gecikmesi ≈ 1 ms.
  - I2 gecikmesiz ortaya çıkıyor; Z2 ≈ ¾ çevrimde oturuyor.

**Aleyhte kanıtlar / koşullar:**
- **Mimari değişmeli.** CSC'li inverter I2 basmaz (PNNL s. 1). Eref2 = 0 olan GFM, negatif bileşende pasif bir empedanstır (Li s. 4).
- **Başlık payı küçük.**
  - Akım sınırı 1,2–1,5 pu (SEL s. 1).
  - k bile keyfi olarak artırılamıyor (PNNL s. 4).
  - Kodun istediği I2(V2) bu payın bir bölümünü zaten tüketiyor.
- **Limiter sinyali bozuyor.**
  - Dairesel limiterde Zv2 dirençsel; σ'nın büyüklüğü arızaya bağlı, açısı sıfır. Öncelikli ve anlık limiterde açı tanımsız (Li s. 5, Şekil 12).
  - Id ve Iq için ayrı sınır yoksa I2 endüktif olmayabilir (PNNL s. 4).
  - Aktif akım önceliği anlaşmayla seçilebiliyor (Slane & Mate s. 4).
- **Zamanlama yetersiz.**
  - IEEE 2800'de tepki ve oturma süreleri 2,5 ve 4 çevrim (SEL s. 2); 50 ms'lik ayar payı var (SEL s. 10).
  - I2'nin yükselme süresi 50Q'yu geciktiriyor (PNNL s. 4).
  - İlk 0,5–1,5 çevrim geçici (PNNL s. 1).
  - Alt-geçici tepeler var (Slane & Mate s. 6).
  - Faz sıçraması PLL'i bozabiliyor (Slane & Mate s. 6–7). PLL dondurulmazsa referans açı kayıyor (SEL s. 3).
- **Çalışma modu.** IBR momentary cessation'a girerse ya da açarsa sinyal hiç olmaz (Slane & Mate s. 2, 6).
- **Saha belirsizliği.** Üreticilerin gizli algoritmaları ve firmware değişiklikleri (SEL s. 2; PNNL Özet; Slane & Mate s. 4) nedeniyle sahada gerçekleşen sinyal tasarımdan sapabilir.

**Hiçbir kaynağın göstermediği şeyler:**
- **Gerilimden bağımsız, tasarlanmış bir I2'nin arıza sırasında basılması.** Kaynakların hepsinde I2 ya kod uyumlu, yani gerilime bağlı bir I2(V2), ya da pasif bir empedans sonucu.
- **Gerçek güç katında negatif bileşen basma.** Li yalnızca CHIL yapmış: kontrolcü donanımda, güç katı simülatörde. SEL'de ise yalnızca PSCAD benzetimi ve rölede geri oynatma var.
- **Normal işletmede sürekli küçük bir I2 basmanın etkileri.** Akla gelenler: güç kalitesi ve dengesizlik sınırları; 46, 50Q ve 32Q eşikleri; "normal işletmede I2 ≈ 0" varsayımının bozulması (SEL s. 3).
- **Birden fazla IBR'nin aynı anda yardımcı sinyal basması.** Etkileşim ve girişim hiç incelenmemiş.

**Hüküm: Koşullu olarak evet.** Öncül fiziksel olarak makul, ancak dört koşul gerekiyor:
- **(i) Kontrol mimarisi:** Bağımsız bir negatif bileşen akım referansına izin vermeli. GFL'de DSC, GFM'de negatif bileşende akım kaynağı.
- **(ii) Başlık payı:** Yardımcı sinyal için ayrılmış ve kodun istediği I2 ile birlikte hesaplanmış bir pay olmalı.
- **(iii) Limiter:** Sinyalin açısını korumalı. Bunun için bileşen bazlı bir limiter kullanılabilir, sinyal limiterden önce eklenebilir ya da limiter belirsizliği tasarıma katılabilir.
- **(iv) Uygulama:** Fazör tabanlı değil zaman domeninde olmalı; PLL dondurulmuş ya da yavaş olmalı.

Bu koşulların hiçbiri sıradan bir ticari IBR'de garanti değil. Proje bunları ya tasarımın içine almalı ya da açık varsayım olarak yazmalı.

### İş paketlerine göre harita

| İP | Li vd. 2025 | Slane & Mate 2026 | PNNL 2024 | SEL 2026 |
|---|---|---|---|---|
| İP1: CVXPY tasarım | σ (limiter) belirsizliği; φ2/δ20 bölge kısıtları | İşletme modu taksonomisi; hazır araçlarda negatif bileşen basma yok | IEEE 2800 açı penceresi, VDE k-yasası, paylaşılan başlık payı | Imax ve başlık payı; Z optimizasyonu; gecikmenin açıya çevrilmesi (Denk. 7) |
| İP2: EMT | Tablo II GFM sistemi + 4 CLC | Alt-geçici tepe; PLL faz sıçraması | CSC / DSC / GFM-akım kaynağı modelleri; DDSRF-PLL | Değiştirilmiş CIGRE NA modeli; IIR reaktör; dondurma mantığı |
| İP3: Röle | φ2, φ0, Δφ1, Δδ21, δ20 ve bantları | FTC hataları; ileride PRC-028 saha verisi | 50Q, 67Q, I2–I0 tabanlı faz seçimi | TD32, 32Q, FID (30°), replika akım, COMTRADE ile geri oynatma |
| İP4: Gömülü | 50 Hz; ilk çevrim incelenmemiş | 4 çevrim (≈ 70 ms) temizleme referansı | Bileşen ayrıştırma gecikmesi; 0,5–1,5 çevrimlik ilk geçici | ≈ 1 çevrimlik veri; ¾ çevrimde oturma; ≈ 21°/ms; 500 Hz alçak geçiren filtre |

### En umut verici araştırma fikirleri (birleştirilmiş)

1. ★★ **Limiter ve başlık payı farkında, dayanıklı yardımcı sinyal tasarımı** (Li fikir 1 + PNNL fikir 5).
   - CVXPY'de faz akımı sınırını SOC kısıtı olarak yaz.
   - Limiterin etkisini σ belirsizliği olarak modelle.
   - Sonucu dört CLC ile EMT'de doğrula.
2. ★★ **Uyumluluk kısıtları** (Li fikir 2 + PNNL fikir 1 + SEL fikir 2).
   - Toplam I2 için IEEE 2800 açı penceresi; φ2'nin ileri bölgede kalması; FID'in 30° eşiği.
   - Hepsi senaryo başına V2 sabit alınırsa doğrusal kısıtlara dönüşüyor.
3. ★★ **Sanal reaktörün optimize edilmesi** (SEL fikir 1). Açık çevrim ile kapalı çevrim yardımcı sinyali karşılaştır.
4. ★ **Gecikmenin açı belirsizliğine çevrilmesi** (SEL fikir 3). İP4 ile İP1'i doğrudan bağlar.
5. ★ **GFM'de negatif bileşen akım kaynağıyla sinyalin gerçekleşme doğruluğu** (PNNL fikir 2). Öncülü GFM için doğrudan sınar.

### Proje için en önemli 3 çıkarım

1. **Başlık payı ve limiter tasarımın içinde olmalı, sonradan eklenmemeli.**
   - İnverterin akım sınırı (≈ 1,2–1,5 pu) yardımcı sinyalin bütçesini belirliyor; kodun istediği negatif bileşen akımı da bu bütçeyi paylaşıyor.
   - CVXPY'de en azından şu korumacı kısıt yazılabilir: maks. faz akımı ≤ |I1| + |I2,kod + Iaux| ≤ Imax. Bunun nedeni şu (benim çıkarımım): Faz akımı genlikleri |I1 + a^k·I2| (k = 0, 1, 2) olduğundan, üçgen eşitsizliğiyle her faz akımı ≤ |I1| + |I2|. Bu kısıt SOC biçiminde yazılabilir.
   - Limiterin türü sinyalin açısını ve ölçeğini değiştiriyor; bu etki bir belirsizlik kümesi olarak modellenmeli.
   - Kontrol mimarisi bağımsız bir negatif bileşen referansına izin vermiyorsa (CSC ya da Eref2 = 0 olan GFM), projenin öncülü baştan geçersiz.

2. **Mevcut negatif bileşen elemanlarıyla ve IEEE 2800 ile uyum açık bir kısıt olmalı.**
   - Dört kaynak, çalışan sistemin sabit ve yüksek endüktif bir Z2 (≈ 80–90°) olduğunda birleşiyor.
   - Kontrolsüz eklenen bir yardımcı sinyal, mesafe rölesini seçici yapan denetleyici elemanları (32Q, FID, reaktans polarizasyonu) bozabilir.
   - Tasarım ya şu kısıtları sağlamalı: ψ ∈ [90°, 100°], φ2 ileri bölgede, I2–I0 açısı 30° eşiği içinde. Ya da rölenin sinyali bildiğini açıkça varsaymalı.
   - SEL'in sanal reaktörü hem uyumlu bir temel (baseline), hem de optimize edilebilecek bir "kapalı çevrim yardımcı sinyal" adayı.

3. **İlk çevrim belirleyici ve her milisaniyelik gecikme açı hatasına dönüşüyor.**
   - Standartların toleransları (2,5/4 çevrim, 50 ms) projenin ≈ 16,7 ms'lik bütçesinden büyük. Bu yüzden zaman domeni uygulama şart.
   - 60 Hz'de her 1 ms ≈ 21° açı hatası demek (SEL Denk. 7). İP4'te ölçülen gecikmeler İP1'de açı belirsizliği olarak modellenmeli.
   - İP2 benzetimleri, Li vd.'nin bilerek atladığı ilk ≈ 20 ms'yi kapsamalı. Bu pencerede şunlar var: 0,5–1,5 çevrimlik ilk geçici, alt-geçici tepe ve I2'nin yükselme süresi.
