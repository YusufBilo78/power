# Taylor çizgisi: altı makalenin okuma notları ve sentez

Bu notları makaleleri baştan sona okuyarak yazdım. Sayılar makalelerden alındı; "Bizim gözlemimiz" diye işaretlenen yerler benim çıkarımım ve kontrolüm.

| # | Makale | Yer | Uzunluk |
|---|---|---|---|
| T1 | Pirani, Hosseinzadeh, Taylor, Sinopoli, *Optimal Active Fault Detection in Inverter-Based Grids* | IEEE TCST 31(3), 2023 (arXiv 2209.06760) | 7 s. |
| T2 | Taylor, Domínguez-García, *Auxiliary Signal-Based Distance Protection in Inverter-Dominated Power Systems* | ECC 2024 (arXiv 2311.10880) | 5 s. |
| T3 | Taylor, Domínguez-García, *Active Fault Detection in Static Systems* | IEEE TAC 70(8), 2025 | 7 s. |
| T4 | Taylor, Domínguez-García, *Geometry of Distance Protection* (sonraki adı: *Set-based modeling of distance relays*) | arXiv 2510.04379 v2 | 16 s. |
| T5 | Taylor, Domínguez-García, *Distance characteristics for incremental quantities* | arXiv 2604.16668 v2 (IEEE TPWRD 2026 olarak atıf alıyor) | 4 s. |
| T6 | Taylor, Baeckeland, Domínguez-García, *Reachability-based Time-domain Distance Protection* | arXiv 2608.19678 v1 | 7 s. |

T3 ayrıca bölüm bölüm konuşuldu. Burada sadece sentezde yer alıyor.

---

## Büyük resim: çizgi nereden nereye gidiyor?

| | T1 (2022) | T2 (2023) | T3 (2025) | T4 (2025) | T5 (2026) | T6 (2026) |
|---|---|---|---|---|---|---|
| Alan | zaman (dq), dinamik | fazör, statik | fazör, statik | fazör, statik | fazör (artımsal) | zaman |
| Belirsizlik | olasılıksal (Gauss) | küme (norm topu) | küme + çarpımsal | küme (zonotop), Minkowski toplamı | yer + direnç (kaynaklar durağan varsayılıyor) | küme, erişilebilir küme |
| Şebeke | tek invertör | 2 baralı oyuncak | 2 baralı oyuncak | IEEE 14-bara (statik) | 14-bara (statik) | 14-bara **Simulink EMT**, 5 GFM invertör |
| Arıza tipleri | sadece dengeli 3 faz | sadece a-b | sadece a-b | 11 tip + normal | ag, ab | ab |
| **Yardımcı sinyal** | var (optimal dizi) | var | var | var (her IBR'ye) | **yok** | **yok** |
| Çözüm | Bhattacharyya sınırı | CCP (konveks-konkav) | SDP gevşetme + dualite | Farkas + ADMM | dışbükey zarf | model indirgeme + anlık test |
| Doğrulama | basit simülasyon | yok | yok | yok | yok | 3 EMT koşusu |

**Bizim gözlemimiz:** 2026'daki iki makalede yardımcı sinyal hiç geçmiyor. Taylor'ın son çalışmaları "sinyal enjekte et" fikrinden "şebeke modelini kullanarak daha iyi röle karakteristiği çıkar" fikrine doğru genişliyor. Bu bir yön değişikliği mi, yoksa paralel bir kol mu, makalelerden anlaşılmıyor. Danışmana sorulması gereken bir soru.

---

## T1: Pirani ve ark. (2022), *Optimal Active Fault Detection in Inverter-Based Grids*

**Tek cümlede:** Tek bir invertöre, faz sınırı içinde kalan optimal bir pertürbasyon dizisi bastırılıyor; bu dizi, iki Kalman filtresinden (arızasız ve arızalı model) oluşan bir Çoklu-Model Kalman Filtresinin (MMKF) arızayı daha hızlı ve emin tanımasını sağlıyor.

**Model**
- dq ekseninde tek dağıtık üretim birimi; dış döngüde gerilim PI, iç döngüde akım PI kontrolcüsü.
- Akım sınırlayıcı (FCL) bir doyum bloğu.
- **Arızasız mod:** 6 durum. **Arızalı mod:** FCL doyuma giriyor ve gerilim döngüsü devreden çıkıyor; 4 durum (denklem 7–10).
- Sadece **dengeli üç faz-toprak** arızası. Yük direnci R = 10 Ω, L1 = 300 mH, VDC = 150 V (s. 5).

**Dedektör: MMKF (s. 3, denklem 11–16)**
- İki Kalman filtresi paralel çalışıyor. Her adımda artıklar (residual) ölçülüyor.
- Artıklarla her modun **sonsal olasılığı** güncelleniyor. Olasılığı büyük olan mod kazanıyor.
- Bayes güncellemesi e^(−α) ile yapılıyor; burada α artığın normu (karesi değil).

**Sinyal tasarımı (s. 4, denklem 17–24)**
- Hata olasılığı **Bhattacharyya sınırıyla** üstten sınırlanıyor (Teorem 1).
- Kovaryanslar sinyale bağlı olmadığı için problem şuna indirgeniyor: iki modun **beklenen çıktıları arasındaki mesafeyi** maksimize et, kısıt ‖Δu‖∞ ≤ γ.
- Ufuk N = 8, adım 1 ms. Ortalama hesap süresi **0.612 ms** (YALMIP, i7 dizüstü; s. 6).

**Sonuçlar**
- Sinyalsiz MMKF arızayı zayıf tanıyor; sinyalle tanıma **tek 60 Hz periyodu içinde** oluyor (s. 5).
- Sinyalin genliği arttıkça tespit hızlanıyor ama gerilim takip hatası büyüyor. Bu bir ödünleşim.
- Sadece 3., 5. ve 7. harmoniklerle sınırlanmış sinyalden daha iyi (Şekil 8).
- Kontrol parametrelerinde ±%10 ve yükte ±%20 değişime karşı dayanıklı (Şekil 9–10).

**Varsayımlar ve sınırlamalar**
- Tek invertör, dengeli arıza, şebeke yok, arıza direnci veya konumu yok. Yazarlar bunu kendileri de söylüyor (s. 1, s. 7).
- Sinyal sadece akım referansı FCL limitine yaklaşınca devreye giriyor. Yazarlar bunun **ani yük değişimlerinde yanlış alarm** verebileceğini kabul ediyor (Remark 3).
- **Bizim gözlemimiz:** Buradaki "arızalı model" aslında "akım sınırlayıcı doyumda" modeli. Yani MMKF arızayı değil, **sınırlayıcının doyuma girip girmediğini** ayırt ediyor. Çok kaynaklı bir şebekede sınırlayıcı, bölge dışındaki bir arızada veya büyük bir yük basamağında da doyuma girebilir. O yüzden "arıza var" ile "benim bölgemde arıza var" farklı sorular ve bu makale ikincisine cevap vermiyor.

**Projeyle bağlantı:** WP3 planında karşılaştırılacak dedektörlerden biri bu MMKF. Uygulaması kolay: iki Kalman filtresi ve bir Bayes güncellemesi. Gömülü sistemde de hızlı. Ama modeller dengesiz arızaya ve şebekeye genişletilmeden bizim problemimize doğrudan uymuyor.

---

## T2: Taylor ve Domínguez-García (2023), *Auxiliary Signal-Based Distance Protection*

**Tek cümlede:** T3'ün 5 sayfalık ilk hali. Statik iki model; ayırma koşulu dualite ile tek seviyeye indiriliyor; ortaya çıkan bilineer program konveks-konkav prosedürle (CCP) yerel olarak çözülüyor.

**Kurulum (s. 2)**
- Model: Θₖθ + Xₖx = Hₖλₖ, Aₖx ≤ bₖ, ‖λₖ‖ < 1.
- **Ofset yok.** Bu, T3 ile en önemli fark.
- Örnek: z₋ = z₊ = 30 + j35, z_f = 26 + j·x_f, x_f ∈ [12, 58], Q = I. Çözücü Gurobi, her optimizasyon < 1 s.

**CCP hilesi (s. 2–3)**
- Bilineer terim βᵀΘθ, simetrik Ψ matrisinin özdeğeri ψ ile bir konveks ve bir konkav parçanın toplamı olarak yazılıyor.
- Eşitsizliğin sağ tarafındaki konveks parça doğrusallaştırılıyor. Böylece her iterasyon bir SOCP oluyor.
- Doğrusallaştırma konveks bir fonksiyonun alt sınırı olduğu için, her iterasyonda bulunan θ gerçekten ayırıcı (iç yaklaşım). Ama yerel optimumda takılabilir.

**Sonuçlar (Şekil 2–3)**
- x_f = 35 civarında, yani arıza reaktansı normal reaktansa eşit olduğunda, gereken sinyal en büyük. Basılı değer |θ| ≈ 0.354 ve 32–38 arasında düz bir plato var.
- x_f küçük veya büyük olduğunda sinyal ≈ 0.07.

### Bizim bulgumuz 1: ekteki matris karmaşık çarpımı doğru temsil etmiyor

Makalenin ekinde (s. 5) karmaşık empedans çarpımının reel karşılığı şöyle basılmış:

$$M_- = \begin{bmatrix} r_- & -x_- \\ r_- & x_- \end{bmatrix}$$

(r + jx)(μ + jν) çarpımının doğru reel karşılığı ise şu:

$$\begin{bmatrix} r & -x \\ x & r \end{bmatrix}$$

İkinci satır farklı. Bu tek başına bir dizgi hatası olabilirdi. Ama makalenin **şekilleri basılı matrisle birebir örtüşüyor**:

| x_f | Doğru form: \|θ\|min | Basılı form: \|θ\|min | Makaledeki Şekil 3 |
|---|---|---|---|
| 12 | 0.0857 | 0.0615 | ≈ 0.07 (CCP yerel olduğu için biraz üstte) |
| 25 | 0.1857 | 0.1414 | — |
| 35 | **0.5000** | **0.3536** | **≈ 0.354, düz plato** |

Kapalı formlar ve sayısal doğrulama `kod/taylor2023_matris_kontrolu.py` dosyasında. Kapalı formlar şunlar:
- **Doğru form:** |θ|min = 2/|z₋ − z_f|. Sinyalin **yönü önemsiz**, çünkü karmaşık çarpım sadece döndürüp ölçekliyor.
- **Basılı form:** |θ|min = √2 / max(|Δr|, |Δx|). Plato tam olarak |Δx| ≤ |Δr| = 4 bölgesi, yani x_f ∈ [31, 39].

Şekil 2'deki dikey şerit (x_f = 35) ve elips biçimli boşluk (x_f = 25) da basılı formun sonucu. Doğru formda olurlu olmayan bölge orijin merkezli bir **daire** olurdu.

Kısacası makalenin sayısal sonuçları yanlış matrisle hesaplanmış gibi görünüyor. Fikir bozulmuyor ama sayılar ve "sinyalin açısı önemli" izlenimi bozuluyor.

### Bizim bulgumuz 2: ofset olmayınca pozitif bileşen ölçümü hiçbir bilgi taşımıyor

T2'de ofset olmadığı için, kötü niyetli "rakip" i₊ = e₊ = 0 seçerek pozitif bileşen artıklarını sıfırlayabiliyor. Ayırma tamamen negatif bileşen bloğuna kalıyor ve **her durumda sıfırdan büyük bir sinyal** gerekiyor (Şekil 3'te sinyal hiç sıfıra inmiyor). T3 bunu "e₊ = 1" ofsetini ekleyerek düzeltti. T3'teki "ofsetler neden gerekli" paragrafı (s. 2) tam olarak bu dersin sonucu.

---

## T3: Taylor ve Domínguez-García (2025), *Active Fault Detection in Static Systems*

Bölüm bölüm konuşuldu. Kısa özet:
- Ofset, ikinci derece kısıt ve çarpımsal belirsizlik ekleniyor. SDP gevşetme ve dualite ile bilineer bir SDP elde ediliyor.
- Toplamsal ve kısıtsız durumda alt sınır: ‖θ‖ ≥ (1 − ζ)/χ.
- Örnek (Bölüm VI.B.1): akım ve gerilim kısıtları eklenince **hiç sinyal gerekmiyor**. Kısıtlardan biri çıkarılınca küçük bir sinyal gerekiyor.

**T2 ile karşılaştırma:** Ofset eklendi, kısıtlar gerçekten kullanıldı, CCP'nin yerine ızgara araması ve SDP geldi. Örnekteki empedanslar pu cinsine çevrildi (z₋ = 0.1 + 0.9j). Bu da birim karmaşasını gideriyor; T2'de empedanslar ohm cinsinden, gürültü sınırı ise birimsiz 1 idi.

---

## T4: Taylor ve Domínguez-García (2025), *Geometry of Distance Protection*

**Tek cümlede:** Rölenin karşılaştığı tüm belirsizlik (arızanın yeri ve direnci, uzak uç akımı, kaynak belirsizliği) **Minkowski toplamı** ile birleştiriliyor. Ortaya çıkan kümeler hem yeni bir röle karakteristiği olarak kullanılıyor hem de IBR'lerin yardımcı sinyali **Farkas lemması** ile tasarlanıyor.

### Ana fikir: karakteristik = Minkowski toplamı (Bölüm II–IV)
- Arıza döngüsünde Kirchhoff gerilim yasası: z_A = m_z·z (hat kısmı) + z_F (arıza kısmı).
- z_F = m_r(ξ + Ξ·i_R) ifadesinde i_R, ölçülemeyen uzak uç akımı.
- Dörtgen karakteristik aslında bu toplamın elle yapılmış bir hali. Uzak uç akımı için yapılan "ad hoc" düzeltme, senkron generatörlü şebekede uç gerilimlerinin açılarının benzer olduğu varsayımına dayanıyor. IBR'li şebekede bu varsayım bozuluyor (s. 7–8).
- **Test sonrası küme** (post-test, i_L ölçüldükten sonra): Kaynak belirsizliği zonotop olarak alınırsa küme bir zonogon oluyor. Köşeleri "gift wrapping" algoritmasıyla bulunuyor; 11 arıza tipi için toplam yaklaşık 0.9 s. Analitik zonogon gevşetmesi ise yaklaşık 1 ms sürüyor (s. 7).
- Bu kümeler **uyarlamalı karakteristik**: ölçülen i_L'ye bağlı oldukları için çalışma sırasında yeniden hesaplanması gerekiyor.

### Yaklaşımlar (s. 4–5): "garanti"nin sınırlarını çizen yerler
- **Yaklaşım 1:** Senkron generatörler dengeli gerilim kaynağı, IBR'ler dengeli **akım kaynağı**, yükler afin. Yazarlar bunu "kaba" (crude) diye niteliyor.
- **Yaklaşım 2:** Şebeke matrisleri (Γ, Θ, Φ, Ψ) **nominal arıza yeri ve direncinde** (m̂_z = m̂_r = 1/2) hesaplanıyor. Yani uç akımlarının arızanın yerine bağımlılığı **yok sayılıyor**.

**Bizim gözlemimiz:** Yaklaşım 2 küçük bir ayrıntı değil. Uzak uç akımı, arızanın hattın neresinde olduğuna güçlü biçimde bağlı. Bu bağımlılık yok sayıldığı için kümeler "her arıza yeri için doğru" olmuyor ve garanti, bu yaklaşımın geçerli olduğu ölçüde geçerli. Yazarlar sonuç bölümünde (s. 12) bunu iyileştirme yönü olarak anıyor. T5 de bu bağımlılığı doğrudan hesaplıyor.

### Test öncesi kümeler ve sinyal tasarımı (Bölüm V–VI)
- Sinyal **önceden, çevrimdışı** tasarlanıyor. O anda i_L de bilinmediği için kümelerde m_z·λ ve m_r·λ gibi **bilineer** terimler oluşuyor.
- Bu terimler için üç gevşetme (W_Rel,1/2/3), bir kısıtlama (W_Res) ve bir SOC yaklaşımı tanımlanıyor. Lemma 6 bunların iç içe geçme ilişkisini veriyor.
- **Lemma 7: iki yönlü sertifika.** Kısıtlanmış küme olurluysa sinyal **ayırmıyor**. Gevşetilmiş küme olursuzsa sinyal **ayırıyor**. Bu güzel bir yapı: hem "işe yarıyor" hem "yaramıyor" diyebiliyorsun.
- Tasarım: min Δ†QΔ, kısıt her model çifti için Farkas dual sistemi S(Δ) boş değil. Problem bikonveks ve ADMM ile çözülüyor (Ek C).

### Örnek (Bölüm IV-C ve VI-D)
- IEEE 14-bara. Hat verisi Baeckeland'ın doktora tezinin 3.1 tablosundan alınmış (**elimizde yok**). SG'ler {1, 3, 5, 14}, IBR'ler {2, 4, 7, 8, 12}. Röle bara 2'de, 2–3 hattında. k = 2, r_F = 1, m_z alt sınırı 0.15. Kaynak gürültüsü 20 kenarlı düzgün çokgen, Σ = 0.1·I.
- Sinyal tasarımı için problem bilerek zorlaştırılmış: **Σ = I** (kaynak belirsizliği %100) ve **bütün kaynaklar IBR**.
- Sonuçlar (s. 12):
  - N, ag ve ab'yi ayıran en küçük ortak sinyal δ = j0.2. Toplam ‖Δ‖ ≈ 0.53 (7 IBR × 0.2).
  - N ile tüm LG ve LL arızalarını ayırmak için δ = 1.6 + j0.6, ‖Δ‖ ≈ 4.52.
  - ADMM ile ‖Δ‖ ≈ 4.35, yani yaklaşık %4 daha iyi.

**Bizim gözlemlerimiz**
1. **4.35 / √7 ≈ 1.64 pu**, invertör başına düşen sinyal. Bu, tipik 1.1–1.2 pu akım limitinin **üstünde**. Örnekte akım limiti kısıtı da kullanılmamış (Bölüm II-B'de opsiyonel olarak tanımlı).
2. **Sadece aşırı erişim (overreach) var.** Kümeler m_z ∈ [m_z alt sınırı, 1] için kuruluyor. Komşu hattaki bir arıza (m_z > 1) bir senaryo olarak **hiç modellenmemiş**. Yazarlar bunu kendileri yazıyor (Bölüm IV-E): kümeler aşırı erişime izin veriyor, eksik erişime vermiyor. Yani tasarlanan sinyal **arıza tiplerini normal işletmeden ve birbirinden** ayırıyor, **bölge içi ile bölge dışı arızayı değil**. Zone-1 kararının asıl sorusu ise ikincisi.
3. Bu makale yardımcı sinyali **bir EMT simülasyonunda hiç denemiyor**. Yazarların "açık bir sonraki adım" dediği şey (s. 12) tam da bu.

---

## T5: Taylor ve Domínguez-García (2026), *Distance characteristics for incremental quantities*

**Tek cümlede:** Kaynaklar arızadan sonraki bir periyot boyunca periyodik kalırsa (durağanlık), artımsal büyüklükler (v(t) − v(t − δ)) sadece arıza noktasının arızadan önceki gerilimine ve şebeke yapısına bağlı kalıyor. Böylece kaynak belirsizliği tamamen kayboluyor ve karakteristik **çalışma noktasından bağımsız** hale geliyor.

- Uzak uç akımının artımsal hali, σ(m) = Ω(m)[v_L(t−δ); i_L(t−δ)]. Ω(m) çevrimdışı hesaplanabiliyor (denklem 3).
- Karakteristik Z = {z_A(m) : m ∈ [0,1]²} basit bir biçime sahip değil, çünkü m'ye doğrusal olmayan biçimde bağlı. İki yaklaşım öneriliyor:
  - **Nokta tahmini:** σ'yı m̂ = (0.5, 1)'de sabitleyip bir paralelkenar elde etmek.
  - **Dışbükey zarf:** 8×8 ızgaradaki z_A noktalarının dışbükey zarfı; yaklaşık 17 ms, 4 köşeyle yaklaşık 1 ms (s. 3).
- Gerçek küme sol üstte biraz konveks değil. Dışbükey zarf bu yüzden muhafazakâr kalıyor (s. 3).
- **Yazarların kendi kabulü (s. 2):** Durağanlık varsayımı bugünkü IBR'ler için **genellikle gerçekçi değil**. Akım sınırlama devreye giriyor; frekans ve faz kayıyor. Kasztenny ve ark. (2026), standartların IBR'leri daha öngörülebilir yapacağını umuyor.

**Bizim gözlemimiz:** Izgara noktalarının dışbükey zarfı, noktalar arasında kalan gerçek kümeyi kapsamayabilir. Bu yüzden bu karakteristik de katı bir garanti vermiyor. Ama T4'teki Yaklaşım 2'nin (nominal m) zayıflığını doğrudan hedefliyor, çünkü σ'yı m'nin fonksiyonu olarak hesaplıyor.

---

## T6: Taylor, Baeckeland ve Domínguez-García (2026), *Reachability-based Time-domain Distance Protection*

**Tek cümlede:** Arızadan sonra rölenin görebileceği gerilim ve akımlar bir **erişilebilir küme** (reachable set) olarak tanımlanıyor. Her arıza tipi için 2 durumlu indirgenmiş bir model kuruluyor ve röle, ölçümünün "çözülmemiş diferansiyel denklemi" sağlayıp sağlamadığına bakıyor (anlık test, denklem 7–9).

- Şebeke π-eşdeğerli RLC devresi olarak modelleniyor. Artımsal modelin tek girdisi arıza noktasının arızadan önceki gerilimi v_F(t−δ) (ve varsa kaynak kayması λ).
- **Model indirgeme:** Tekil pertürbasyonla 2 boyuta (görünür gerilim ve akım) indiriliyor. Yazarlar bunun bir **dış yaklaşım olmadığını** açıkça yazıyor (s. 1), yani garanti yok.
- **Test:** Ξ(t) = dışbükey zarf {ε_m̂k(t) ⊕ Υ}. 0 ∈ Ξ(t) ise arıza var. En basit hali, birim karenin 4 köşesindeki m değerleri.
- **Doğrulama:** Baeckeland ve ark.'ın (2026, TPWRS) Simulink modeli. IEEE 14-bara, akım sınırlayıcılı 5 grid-forming invertör (droop, VSM, dVOC). Röle bara 2'de, ℓ3 hattının ortasında ab arızası, R_F en fazla 10 Ω. **IBR'ler gerilim kaynağı olarak modellenmiş.**
- **Sonuçlar (s. 4):**

| Arıza direnci | Sınırlayıcılar | Tespit süresi |
|---|---|---|
| 10 Ω | hiçbiri aktif değil | ≈ 1/8 periyot |
| 1 Ω | bazıları aktif | ≈ 3/8 periyot |
| 0.01 Ω | hepsi aktif | bir periyottan biraz fazla |

- **Sınırlamalar:** Sadece 3 koşu, tek arıza tipi, tek konum. Test sadece aşırı erişen türden (komşu hattaki arızada da tetikleyebilir) ve güvenlik (yanlış açma) hiç ölçülmemiş. Yazarlar "IBR için en uygun modelin akım kaynağı mı, gerilim kaynağı mı, yoksa daha karmaşık bir devre mi olduğu belli değil" diyor (s. 5).

**Bizim gözlemimiz:** En kolay görünmesi gereken düşük dirençli (bolted) arıza en geç tespit ediliyor. Çünkü bütün sınırlayıcılar aktifken IBR'ler artık gerilim kaynağı gibi davranmıyor ve model bozuluyor. Yani **sınırlayıcı modu**, modelin en zayıf halkası.

---

## Sentez: çizgi boyunca tekrar eden temalar

1. **IBR'nin nasıl modelleneceği çözülmemiş ve makaleler arasında tutarsız.**
   - T4'te akım kaynağı, T5'te Norton eşdeğeri, T6'da gerilim kaynağı.
   - T1'de ise "arıza modu" doğrudan "sınırlayıcı doyumda" demek.
   - Sınırlayıcının aktif olup olmaması modeli değiştiriyor ve T6'da en kötü performans tam bu durumda.
   - Bu yüzden Baeckeland ve ark.'ın (2026, TPWRS) "birleşik akım sınırlayıcı modeli" bu çizginin bir sonraki adımı için kilit makale.
2. **Hiçbir makale bölge içi ve bölge dışı arızayı ayırmıyor.** T4, T5 ve T6'nın hepsi açıkça "aşırı erişen" karakteristik kuruyor. T4'ün sinyal tasarımı arıza tiplerini normalden ayırıyor. Zone-1 kararı (komşu hat arızasına karşı güvenlik) çizgide açık bir boşluk.
3. **"Garanti" her makalede bir yaklaşımla sınırlı.**
   - T2: CCP yerel optimum.
   - T3: SDP gevşetme (bu muhafazakâr, yani güvenli yönde).
   - T4: nominal m̂ (Yaklaşım 2) ve IBR'nin akım kaynağı varsayımı.
   - T5: ızgara noktalarının dışbükey zarfı.
   - T6: dış yaklaşım olmayan model indirgemesi.
4. **Sinyal büyüklükleri invertör sınırlarıyla yan yana konmamış.** T4'te invertör başına ≈ 1.64 pu çıkıyor. T3'te ise akım limiti problemin içine konunca sinyal gereksizleşiyor. Kısıtların sinyali küçülttüğü fikri (T3), T4'ün örneğinde uygulanmamış.
5. **EMT doğrulaması:** Yardımcı sinyal hiçbir makalede EMT'de denenmemiş. EMT kullanan tek makale (T6) sinyal kullanmıyor.

## Buradan çıkan fikirler (konuşmak için)

- **F1: T4'ü yeniden üretmek.** 14-bara örneğini (post-test karakteristikler ve sinyal tasarımı) bağımsız olarak kodlamak. Baeckeland tezinin 3.1 tablosu gerekiyor. Tablo yoksa standart IEEE 14-bara verisiyle yaklaşık bir sürüm yapılabilir. Çizginin en çok atıf alacak makalesini yeniden üretmek ekibe sağlam bir temel verir.
- **F2: T4'e bölge dışı senaryo eklemek.** m_z ∈ (1, 1 + a] (komşu hat) için ayrı bir model kurup sinyalin zone-1 sınırını çözüp çözemediğini Taylor'ın **kendi çerçevesinde** test etmek. Çizgideki en net boşluk bu.
- **F3: Yaklaşım 2'nin maliyetini ölçmek.** Nominal m̂ yerine m'nin bütün aralığında hesaplanan kümelerle, garantinin hangi arızalarda bozulduğunu göstermek.
- **F4: Sınırlayıcı modunu belirsizliğe katmak.** IBR'yi "sınırlayıcı aktif: akım kaynağı / değil: gerilim kaynağı" diye iki modlu bir belirsizlik olarak modellemek; Baeckeland'ın sınırlayıcı açısı (limiter angle) parametresiyle. T1, T4 ve T6'yı birbirine bağlıyor.
- **F5: T2'deki matris tutarsızlığı.** Kısa ve doğrulanmış bir not olarak yazara iletilebilir. İletme kararı ekibin.
