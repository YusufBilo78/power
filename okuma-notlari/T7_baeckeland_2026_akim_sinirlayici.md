# Baeckeland, Yang & Seo (2026): akım sınırlayıcılı GFM invertörlerin birleşik modeli

**Künye:** N. Baeckeland, B. Yang, G.-S. Seo, *Unified Model of Current-Limiting Grid-Forming Inverters for Large-Signal Analysis*, IEEE Trans. Power Systems 41(1):198–213, Ocak 2026. DOI 10.1109/TPWRS.2025.3587224. 16 sayfa, NREL. Paywall'lı (NJIT kopyası okundu, repoya konmadı).

**Neden önemli:** Taylor'ın zaman alanı makalesinin (T6) Simulink modeli bu makaleden geliyor. Ayrıca Baeckeland, T6'nın ortak yazarı. Taylor çizgisinde en zayıf halka "invertör akım sınırlamasına girince ne oluyor" sorusuydu. Bu makale o soruya bir model veriyor.

---

## Tek cümlede

Grid-forming (GFM) bir invertörün akım sınırlayıcısı, devreye girdiğinde invertörün **çıkış empedansını** değiştirir. İki yaygın sınırlayıcı tipi aynı **"sınırlayıcı açısına"** (φ_lim) sahipse, büyük işaret davranışları neredeyse aynıdır. Endüktif bir açı (φ_lim → 90°) kararlılığı da gerilim desteğini de iyileştirir.

## Temel kavramlar (kısa)

- **GFM ve GFL farkı:** Grid-following (GFL) invertör şebekenin gerilimine kilitlenir ve bir **akım** basar; akım kaynağına benzer. Grid-forming (GFM) invertör kendi gerilim ve frekans referansını üretir; bir **gerilim kaynağı + empedans** gibi davranır, yani senkron generatöre benzer.
- **Neden sınırlayıcı gerekir:** Yarı iletkenler aşırı yükü kaldıramaz; tipik sınır **1.05–1.20 pu** (s. 1). GFM bir gerilim kaynağı olduğu için arızada akımı kendiliğinden fırlar, bu yüzden kontrol yazılımı akımı kırpmak zorundadır.
- **Kontrol yapısı (Şekil 2):**
  - Primer kontrolcü (droop, VSM veya dVOC) açıyı ve gerilim genliğini üretir.
  - Dış döngüde gerilim PI kontrolcüsü akım referansını üretir.
  - İç döngüde akım PI kontrolcüsü ve LCL filtre var.
  - Droop: dθ/dt = ω₀ + m_p(p* − p̃), e* = e₀ + m_q(q* − q̃).

## İki sınırlayıcı tipi ve birleşik model (Bölüm III)

1. **SatLim (dairesel / akım referansı doyumu):** Akım referansı i_max'a kırpılır: ρ = min(1, i_max/|I*|). Gerilim kontrolcüsünün integratörüne anti-windup geri beslemesi gider. Bu geri beslemenin içinde açısı φ_vi olan bir sanal empedans (VI) vardır.
2. **VI-Lim (eşikli sanal empedans):** Akım i_th'yi (örneğin 1.1 pu) geçince bir sanal empedans devreye girer ve akımı i_max'ın altında tutar. Eşik fonksiyonu Ψ = max(0, (ρ|I*| − σ)/(i_max − i_th)).

**Birleşik model:** İki parametre seçerek ikisinden biri elde ediliyor. σ ≥ i_max seçilirse SatLim; σ = i_th ve 0° < φ_vi < 90° seçilirse VI-Lim (Şekil 3).

**Kilit ilişki (denklem 5):** Sınırlama sırasında invertör, "gerilim kaynağı E* + Z_g + Z_lim" olarak görülebilir (Şekil 4).
- SatLim: Z_lim = ((1 − ρ)/ρ)·Z_vi
- VI-Lim: Z_lim = kΨ·Z_vi

İki durumda da **φ_lim = φ_vi**. Sınırlayıcının "eşdeğer empedans açısı" tasarımcının seçtiği VI açısına eşit.

**Sınırlamadaki toplam empedans (denklem 15):**

$$|Z_{inv}| = \max\left(|Z_g|,\; \frac{|E^* - V_s|}{i_{max}}\right)$$

Sınırlama ağırlaştıkça Z_inv ≈ Z_lim olur ve açısı φ_lim'e yaklaşır (Şekil 7).

## Analitik güç-açı eğrisi (Bölüm IV)

p = Γ²(Λ_syn − Λ_lim) (denklem 21). Üç bileşenden oluşuyor:
- **Γ = |E*|/|Z_inv|:** "sanal kısa devre gücü". Sınırlama ağırlaştıkça düşüyor.
- **Λ_syn:** Senkron makineye benzeyen kısım. Sınırlama yokken klasik p = (EV/X)·sin δ biçimine dönüyor.
- **Λ_lim:** Sınırlamanın aktif gücü azaltan katkısı. Endüktif φ_lim bunu küçültüyor.

Analitik ve sayısal model arasındaki fark en fazla **±0.06 pu**. φ_lim = 90° için bu fark ±0.01 pu (s. 7). Fark, |E*| = 1 pu varsayımından kaynaklanıyor.

**Sonuçlar:**
- **Lim0** (dirençli): Sınırlama başlayınca güç hızla düşüyor, kararsız denge açısı küçük, invertör senkronizasyonu kolay kaybediyor.
- **Lim90** (endüktif): Güç anma değerine yakın kalıyor, kararlılık payı büyük, reaktif destek daha iyi.
- **Zayıf şebeke** kararlılığa yardım ediyor (Şekil 12). **Dirençli şebekede** endüktif sınırlayıcı, şebekenin eksik endüktifliğini telafi ediyor (Şekil 13).

## Doğrulama (Bölüm V)

| Deney | Kurulum | Sonuç |
|---|---|---|
| Tek invertör EMT (SMIB) | Tablo I: laboratuvar ölçeği, S_base = 32 VA, i_max = 1.2 pu | 0.5 pu gerilim düşümü, 1 Hz frekans sıçraması, 30° faz sıçraması: **Lim0 üçünde de kararsız, Lim75 üçünü de atlatıyor** (Şekil 16–17) |
| Donanım (SMIB) | φ_vi = 0° ve 50° | 60 → 59.4 Hz sıçramada (0.15 s) φ_vi = 0° senkronizasyonu kaybediyor, 50° kaybetmiyor (Şekil 20) |
| IEEE 14-bara EMT | 5 GFM: bara 1 ve 4'te dVOC, 2 ve 5'te droop, 3'te VSM. Ayar noktaları p = 0.5/0.2/0.9/0.4/0.9 pu. **Hat ve yük verisi standart IEEE 14-bara verisinden birebir alınmış** (s. 12). Tablo III: L_iω = L_gω = 0.0196 pu, R_i = R_g = 0.0139 pu, i_max = 1.2 pu | 3 numaralı hattın ortasında 100 ms'lik faz-faz arızası. **Lim10 senkronizasyonu kaybediyor ve bara gerilimleri çöküyor; Lim85 toparlanıyor** (Şekil 22). Hat empedansları ×2 yapılınca, φ_lim büyüdükçe pozitif bileşen gerilimi artıyor, negatif bileşen gerilimi azalıyor (Şekil 24) |

Arızalı faz akımlarının i_max'ta düzgünce kırpıldığı Şekil 23'te görülüyor.

## Varsayımlar ve sınırlamalar

- **Analiz yarı-durağan (quasi-steady-state).** İç döngüler kararlı durumda varsayılıyor. Yazarlar SatLim ile VI-Lim'in eşdeğerliğinin **küçük işaret ve geçici rejim için geçerli olmadığını** açıkça belirtiyor (s. 6). Koruma ise tam da arızadan sonraki **ilk periyotla** ilgileniyor. O pencerede iki sınırlayıcı farklı davranabilir.
- Analitik model dq ekseninde ve dengeli. Dengesiz arıza için kontrol durağan eksene taşınmış (kaynak [9]), ama negatif bileşenin nasıl sınırlandığı bu makalede ayrıntılı işlenmiyor.
- Koruma ölçülmüyor. Makale korumayı sadece "etkilenen sistem özelliklerinden biri" olarak anıyor.
- Sadece GFM; GFL invertörler kapsam dışı.

---

## Projeyle bağlantı ve bizim çıkarımlarımız

### 1. T6'daki "bolted arıza en geç tespit ediliyor" sonucunun açıklaması
T6, IBR'leri Z_g arkasında gerilim kaynağı olarak modelliyordu. Denklem 15'e göre sınırlama sırasında gerçek empedans çok daha büyük.

Sayısal bir örnek: Tablo III'te |Z_g| = |0.0139 + j0.0196| ≈ **0.024 pu**. İnvertör terminalinde bolted bir arızada |ΔE| ≈ 1 pu olur. O zaman |Z_inv| ≈ 1/1.2 ≈ **0.83 pu**, yani modelde varsayılanın yaklaşık **35 katı**, ve açısı φ_lim'e yakın. Model bu kadar yanlış olunca anlık testin ancak bir periyot sonra tetiklenmesi şaşırtıcı değil.

### 2. "İnvertör akım kaynağı mı, gerilim kaynağı mı?" sorusuna bir cevap
Taylor çizgisi bu konuda tutarsızdı (T4: akım kaynağı, T6: gerilim kaynağı). Bu makaleye göre ikisi de bir sürecin uç halleri:
- **Sınırlama yokken:** Gerilim kaynağı E*, arkasında küçük bir Z_g.
- **Ağır sınırlamada:** |I| = i_max, ve **akımın açısı ∠ΔE − ∠Z_inv**. ∠Z_inv de φ_g ile φ_lim arasında.

Yani akımın genliği sabit, açısı ise rastgele değil: şebeke gerilimine ve **tasarımcının seçtiği φ_lim'e** bağlı. T4 IBR akımının açısını [0, 2π/3] aralığında, yani **120°'lik** bir belirsizlik olarak alıyordu. Bu modelle o belirsizlik kümesi ciddi biçimde daraltılabilir. Kümeler küçülünce de gereken yardımcı sinyal küçülür ya da tamamen gereksizleşir (T3'teki "kısıtlar bulutu küçültür" dersi).

### 3. İlk periyotta durağanlık neyin bozulduğuna bağlı
T5'teki durağanlık varsayımı ("kaynaklar periyodik kalır") bugünkü IBR'ler için gerçekçi bulunmuyordu. Ama bu modelde E* droop dinamiğiyle değişiyor ve m_p = %2 ile güç ölçümü filtrelendiği için **ilk periyotta yavaş** değişiyor. Bu yüzden ilk periyottaki "durağan olmama" büyük ölçüde E*'den değil, **sınırlayıcı empedansından** geliyor. Bu bir hipotez; test edilmesi gerekiyor.

### 4. GFM şebekede yardımcı sinyali kim, nasıl basacak?
T4 sinyali "IBR akımına eklenen bir pertürbasyon" olarak tanımlıyor; bu GFL mantığı. GFM bir gerilim kaynağı ve sınırlama yokken dışarıdan verilen bir akım referansı yok. Sınırlama sırasında ise akım zaten i_max'ta doymuş, yani sinyal için **boş pay yok**. GFM'li bir şebekede (T6'nın şebekesi) yardımcı sinyalin nereden ve nasıl enjekte edileceği **tanımsız**. Danışmana sorulması gereken bir soru.

### 5. Yeni bir fikir (F6): sinyal tasarlamak yerine sınırlayıcı açısını tasarlamak
φ_lim zaten her GFM invertörde bulunan, statik bir tasarım parametresi. Bu makale onun kararlılığı ve gerilim desteğini belirlediğini gösteriyor. Aynı parametre, arıza sırasında rölenin arkasındaki kaynak empedansının **açısını** da belirliyor.
- Klasik mesafe ve yön elemanları, kaynak empedansı hatla benzer açıdaysa iyi çalışır. SEL'in Kasztenny 2022 makalesi bu homojenlik koşulunu tartışıyor.
- Öyleyse soru şu: **Taylor'ın küme tabanlı ayırma kriterini φ_lim seçimine uygulayabilir miyiz?** Her invertör için tek bir açı (ya da bütün invertörler için ortak bir açı), 1–5 boyutlu bir arama.
- Bu, her arızada geçici bir sinyal basmak yerine, invertörün zaten var olan bir ayarını röle açısından optimize etmek demek.
- Lim85 hem kararlılık hem de muhtemelen koruma için iyi. İkisinin aynı yöne gitmesi bu fikri çekici kılıyor.
- Bunun gerçekten işe yarayıp yaramadığı **test edilmesi gereken bir hipotez**.

### 6. F1 için iyi haber
Bu makale 14-bara modelinde hat ve yük verisinin **standart IEEE 14-bara** verisinden birebir alındığını söylüyor. Geometry makalesi (T4) de hat verisini Baeckeland tezinin Tablo 3.1'inden alıyor. Büyük ihtimalle o da standart veri, ama tez görülmeden emin olamayız. Standart IEEE 14-bara verisine pandapower ya da MATPOWER üzerinden ulaşılabiliyor; tezi beklemeden F1'e başlanabilir.

### Bu makaleden çıkan sorular
1. Arızadan sonraki **ilk 16 ms'de** SatLim ve VI-Lim aynı φ_lim ile aynı mı davranıyor? Koruma için kritik.
2. Dengesiz arızada sınırlayıcı **negatif bileşen** akımını nasıl şekillendiriyor? φ_lim negatif bileşen empedansının açısını da belirliyor mu? 67Q gibi negatif bileşen yön elemanları buna bağlı.
3. Bu Simulink modeli paylaşılabilir mi? Projenin planında danışmana sorulacak ilk soru buydu.
