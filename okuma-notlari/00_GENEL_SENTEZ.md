# Genel sentez: 36 makaleden sonra proje nerede duruyor?

Bu dosya `okuma-notlari/` klasöründeki bütün notların üstünde duruyor. Her iddianın kaynağı ilgili not dosyasında, sayfa numarasıyla birlikte var. "Bizim analizimiz" diye işaretlenen yerler makalelerde yazmıyor; benim çıkarımım ve henüz simülasyonla doğrulanmadı.

## Dosyalar

| Dosya | İçerik | Kim okudu |
|---|---|---|
| `T_taylor_cizgisi.md` | Taylor çizgisi: Pirani 2022, Taylor 2023, TAC 2025, Geometry 2025, artımsal 2026, erişilebilirlik 2026 | Ben, tam metin |
| `T7_baeckeland_2026_akim_sinirlayici.md` | GFM akım sınırlayıcı birleşik modeli | Ben, tam metin |
| `A1_problem_sandia_pestr81.md` | Sandia 2024 boşluk analizi, IEEE PES TR-81 | Okuma ajanı |
| `A2_ibr_etkisi_negatif_bilesen.md` | GFM etkisi, IBR koruma taraması, PNNL negatif bileşen incelemesi, SEL 2026 | Okuma ajanı |
| `B_rakip_yontemler_enjeksiyon.md` | Kontrol tabanlı, pasif ve enjeksiyon tabanlı rakipler (9 makale) | Okuma ajanı |
| `C_teori_garantili_aktif_teshis.md` | Scott 2014, Raimondo 2016 | Okuma ajanı |
| `D_ml_veri_setleri.md` | Makine öğrenmesi ve veri setleri (7 makale) | Okuma ajanı |
| `E_pratik_role_ayarlari_SEL.md` | SEL'in mesafe rölesi ayar makaleleri (5 makale) ve adil temel çizgi kontrol listesi | Okuma ajanı |

Ajanların notlarını ben de okudum ve sentezlerini burada birleştirdim. Bir notta bir sayıya dayanmadan önce o makalenin ilgili sayfasına bakmak gerekiyor.

---

## 1. Literatür birlikte ne söylüyor?

1. **En kırılgan kanal negatif bileşen.** IBR'nin arızada verdiği negatif bileşen akımını fizik değil kontrol yazılımı belirliyor. Bu akım bastırılmış, ters fazlı, dalgalı ya da yanlış açılı olabiliyor (A1, A2). %120 sınırlı bir IBR, faz-faz arızasında tam yükte yaklaşık %20 I2 veriyor; senkron generatör ise yaklaşık %200 (TR-81, A1).
2. **IEEE 2800 açıyı sabitliyor, genliği serbest bırakıyor.** I2, V2'nin 90–100° önünde olmalı (A1, A2). Literatürdeki pasif ve kontrol tabanlı çözümlerin hepsi bu "kendiliğinden" gelen I2'ye bağımlı (B). Endüstri bu güvenilmezliği **duyarlılıktan vazgeçerek** çözüyor: SEL'in ayar önerileriyle kapsanan arıza direnci yaklaşık 400 Ω'dan yaklaşık 100 Ω'a düşüyor (B).
3. **Asıl zor sınıf faz-faz ve üç faz arızaları.** Toprak arızalarında transformatör üzerinden gelen sıfır bileşen akımı zaten iyi bir alternatif (A1). Dengeli (üç faz) arızada pasif negatif bileşen elemanları kör (B).
4. **İlk 1–2 periyot hem en önemli hem en belirsiz pencere.** İnvertörün geçici tepkisi, sınırlayıcının devreye girişi ve PLL'in kayması bu pencerede oluyor (A1, A2). IEEE 2800'ün toleransları (2.5–4 periyot, 50 ms) projenin 1 periyotluk bütçesinden geniş. 60 Hz'de her 1 ms gecikme yaklaşık 21° açı hatası demek (SEL, A2).
5. **IBR'nin nasıl modelleneceği çözülmemiş.** Taylor'ın makaleleri IBR'yi bir yerde akım kaynağı, bir yerde gerilim kaynağı, bir yerde Norton eşdeğeri olarak alıyor (T). Baeckeland bu ikisinin aynı sürecin uç halleri olduğunu gösteriyor. Ağır sınırlamada akım genliği i_max'ta sabit, açısı ise tasarımcının seçtiği **sınırlayıcı açısı φ_lim** ile belirleniyor (T7).
6. **"Garanti" her yerde bir yaklaşımla sınırlı.**
   - Taylor: gevşetme, nominal arıza yeri, IBR modeli (T).
   - Pasif ve aktif rakipler: elle seçilmiş eşikler (B).
   - Öğrenilmiş dedektörler: veri sızıntısı ve nedensel olmayan filtreler (D).
   - Konvansiyonel rölede de buna denk bir kavram var: SEL'in 2023 Bölge 1 güvenlik kriteri, aslında en kötü durum hata sınırlarına dayanan bir garanti (E).
7. **Güvenlik neredeyse hiç ölçülmüyor.**
   - Makine öğrenmesi makalelerinin hiçbiri arıza olmayan olaylarda yanlış açma oranı raporlamıyor (D).
   - Taylor'ın karakteristikleri bilerek "aşırı erişen" kurulmuş, yani komşu hattaki arızayı modellemiyor (T).
   - Hiçbir açık veri setinde yardımcı sinyal basan invertör yok (D).

## 2. Projenin yeri: tek cümlelik gerekçe

> Bugünkü çözümlerin hepsi invertörün kontrolsüz negatif bileşen tepkisine bağımlı ve bunu duyarlılıktan vazgeçerek telafi ediyor. **Bilinen, tasarlanmış ve akım bütçesi içinde garanti verilen** bir uyarım bu ödünleşimi kırabilir. Ama bunun koşulu, sahada zaten çalışan elemanları bozmaması ve 1 periyot içinde etkili olması.

En yakın rakip **Yang–Dyśko 2024 (NSCI)**. İnvertör 80 ms boyunca 0.3 pu I2 basıyor ve haberleşme gerekmiyor. Ama eşikler elle seçilmiş, garanti yok ve karar yaklaşık 140 ms sürüyor (B). Projenin katkısı dört eksende konumlanmalı: **optimizasyon, garanti, hız ve mesafe rölesiyle uyum**.

## 3. İki tasarım paradigması: notlardaki en önemli birleştirici gözlem

Notlarda birbirinden habersiz iki çizgi var.

| | (1) Toplamsal sinyal | (2) Tasarlanmış negatif bileşen empedansı |
|---|---|---|
| Ne | İnvertör akımına sabit bir δ ekle | İnvertör negatif bileşende belirli bir empedans gibi davransın |
| Kim | Taylor (T2–T4), NSCI (B), Saleh | IEEE 2800 (I2 = K·V2), SEL sanal reaktör (A2), Li ve ark. sanal empedans (A2), Baeckeland φ_lim (T7) |
| Bulutlara etkisi | Bulutları **öteler** (C: "yalnızca öteleme" yapısı) | Bulutların **şeklini** değiştirir (çarpımsal) |
| Teorisi | Taylor, Scott ve Raimondo hazır (C) | Küme tabanlı tasarımı yok. Teori notundaki "girişle çarpılan belirsiz parametreler" sorusu (C, açık soru 3) tam olarak bu |
| Uyum | Sabit bir I2, röleler açısından "pasif kaynak" gibi görünmüyor (bkz. bölüm 4) | Endüktif bir Z2, klasik 32Q ile uyumlu (A2: 4 kaynak Z2 ≈ 80–90°'de birleşiyor) |

Standartlar ve endüstri ikinci paradigmaya yöneliyor. Taylor çizgisi ise birincisinde. **İkisini aynı küme tabanlı çerçevede karşılaştırmak** literatürde yapılmamış ve bu projenin doğal sorusu olabilir: aynı akım bütçesinde hangisi daha büyük bir ayırma payı sağlıyor? Baeckeland'ın φ_lim'i ikinci paradigmanın en basit, tek parametreli hali (T7, F6).

## 4. Sahadaki rölelerle etkileşim (bizim analizimiz)

Rakip yöntem ajanı ile SEL ajanı, sürekli bir I2 enjeksiyonunun 32Q üzerindeki etkisi konusunda farklı sonuçlara vardı: biri "ileri", diğeri "geri" yön dedi. **İkisi de doğru, çünkü farklı hat uçlarından bakıyorlar.** Akım yönü kuralını bara → hat alırsak:

- **İnvertörün kendi ucundaki röle (L):** Enjeksiyon rölenin arkasından gelip hatta akıyor. V2/I2 ≈ +Z_ileri, yani 32Q **geri yön** görüyor. DCB şemasında bu, karşı uca **sürekli blok sinyali** gönderilmesi anlamına gelir; gerçek bir iç arızada karşı uç açamayabilir.
- **Hattın öbür ucundaki röle (R):** Enjeksiyon hattan baraya geliyor. V2/I2 ≈ −Z_arka, yani 32Q **ileri yön** görüyor.
- **Arıza sırasında:** Gerilimden bağımsız sabit bir enjeksiyon, arızanın ürettiği (IBR'de zaten küçük olan) I2 ile üst üste biniyor. Enjeksiyon baskın gelirse L'deki 32Q iç arızayı **geri** sanabilir. IEEE 2800 uyumlu I2 = K·V2 ise endüktif bir empedans gibi davrandığı için bu sorunu yaratmıyor. Paradigma (2)'nin uyum avantajı buradan geliyor.

**Sonuç:** Yardımcı sinyal için iki kısıt şart.
- Normal işletmede sinyal 32Q, 46 ve 50Q'nun **devreye girme eşiklerinin altında** kalmalı (A1: ≈ 0.02 pu ve I2/I1 ≈ %10). Ya da sinyal ancak arıza algılandıktan sonra basılmalı.
- Arıza sırasında toplam I2 (standardın istediği + yardımcı sinyal), 32Q'yu ileri bölgede tutmalı (A2: uyumluluk kısıtları).

Bu analiz işaret kurallarına dayanıyor. Basit bir devre simülasyonuyla doğrulanması gerekiyor.

## 5. Araştırma fikirleri, birleştirilmiş ve önceliklendirilmiş

| # | Fikir | Kaynak | Neden | Zorluk |
|---|---|---|---|---|
| 1 | **2 boyutlu tam çözücü:** gevşetme olmadan en küçük sinyal. Taylor'ın SDP'sini ve (1 − ζ)/χ sınırını buna karşı ölçmek | C, T (Taylor 2023 kontrolü bunun basit bir hali) | Küçük, bir öğrencinin uygulayabileceği boyutta; elimize kesin bir referans (ground truth) verir; Taylor çizgisinin açık sorusuna, yani gevşetmenin ne kadar iyi olduğuna doğrudan cevap verir | Düşük |
| 2 | **Bütçe ve sınırlayıcı farkındalıklı, uyumlu tasarım:** faz akım sınırı SOC kısıtı olarak; standardın istediği I2 ile pay paylaşımı; IEEE 2800 açı penceresi ve 32Q ileri bölge kısıtları | A1, A2, B | Fiziksel öncülün koşullarını tasarımın içine koyuyor | Orta |
| 3 | **Bölge içi ve bölge dışı:** Geometry çerçevesine komşu hat senaryosu (m_z > 1) eklemek | T (F2), E | Bölge 1 kararı Taylor çizgisinde açık bir boşluk | Orta |
| 4 | **Paradigma (1) ile (2)'yi karşılaştırmak:** toplamsal δ'ya karşı tasarlanmış Z2 veya φ_lim | Bölüm 3, T7 (F6), A2 | Yeni ve standartların gittiği yöne bağlanıyor | Orta-yüksek |
| 5 | **Geometry'yi yeniden üretmek:** standart IEEE 14-bara verisiyle | T (F1), T7 | Çizginin ana makalesini doğrulamak ve 3–4. fikirler için zemin hazırlamak | Orta |
| 6 | **Adil bir değerlendirme düzeni:** güvenlik test seti, nedensel akış, iki konvansiyonel temel çizgi (geleneksel ve zayıf besleme), NSCI'nin yeniden kurulması | D, E, B | Bu yapılmadan hiçbir karşılaştırma inandırıcı olmaz | Orta, ama sürekli |

## 6. Danışmana sorulacak sorular

1. Taylor'ın 2026 tarihli iki makalesinde yardımcı sinyal yok. **Sinyal hâlâ ana hedef mi**, yoksa küme tabanlı karakteristikler mi?
2. **Grid-forming invertörde sinyal nasıl basılacak?** Sınırlama yokken dışarıdan verilen bir akım referansı yok; sınırlamadayken de akım tavanda (T7).
3. Hedef **arıza tiplerini ayırmak mı** (Geometry'deki gibi), yoksa **Bölge 1'in sınırı mı** (bölge içi ve dışı)?
4. **Sürekli mi, tetiklemeli mi?** Sürekli enjeksiyon sahadaki 32Q ve DCB ile çatışabilir (bölüm 4). Tetiklemeli enjeksiyonsa 1 periyot bütçesini zorluyor.
5. Toplamsal sinyal yerine **tasarlanmış bir negatif bileşen empedansı veya φ_lim** ilgisini çeker mi?
6. Baeckeland'ın 14-bara Simulink modeli paylaşılabilir mi?
7. Taylor 2023'ün ekindeki matris tutarsızlığı (T, bulgu 1).

## 7. Önerilen ilk adımlar (2–4 hafta, küçük ve doğrulanabilir)

1. **TAC 2025'in Şekil 2'sini sıfırdan yeniden üretmek.** Toplamsal ve kısıtsız örnekte hem optimal sinyal hem Teorem 1'deki alt sınır. Bir de yön taramalı tam çözücü (1. fikir). Taylor 2023 kontrol kodu buna başlangıç olabilir.
2. **Bölüm 4'teki 32Q analizini doğrulamak.** İki baralı bir devrede sürekli ve tetiklemeli enjeksiyonla 32Q kararını hesaplamak; yarım günlük bir iş.
3. **Standart IEEE 14-bara için ağ matrislerini çıkarmak** ve Geometry'nin test sonrası karakteristiklerini ag ve ab arızaları için çizmek (5. fikir).
4. Bu üçünden sonra **3. ve 4. fikirler** için bir karar vermek. İdeal olarak bu karar danışmanın 1., 3. ve 5. sorulara verdiği cevaplara göre şekillenmeli.
