# B Grubu — Rakip yöntemler ve en yakın öncüller

**Konu:** kontrol-tabanlı çözümler, pasif artımlı/sekans (bileşen) elemanları, diğer enjeksiyon yöntemleri
**Okuyan / not tarihi:** Claude, 2026-10-22
**Okuyucu:** projeye yeni katılan lisans öğrencisi (NJIT ECE senior design)

Bu notlar, Prof. Joshua Taylor çizgisindeki fikrin (proje tanımına göre: bir inverterin küçük, **optimal tasarlanmış bir negatif-bileşen akım "yardımcı sinyali"** enjekte etmesi ve bir mesafe rölesinin arızayı normal işletmeden **küme-tabanlı bir garantiyle** ayırt edebilmesi; tasarım CVXPY'de konveks optimizasyonla) **rakiplerini ve en yakın öncüllerini** inceliyor. Her makale için ana soru: *Ne başarıyor, hangi varsayımlarla, ve tasarlanmış-garantili bir yardımcı sinyal bunun üzerine ne ekleyebilir (ekleyebilir mi)?*

Notlar yalnızca makalelerin kendisine dayanır. Bir sayı makalede yoksa yazılmadı; şekilden okunan veya emin olunmayan değerler açıkça işaretlendi ("şekilden okunan", "belirsiz").

**Sayfa numarası kuralı:** "s. N" = PDF sayfa numarası. IEEE Access makalesinde (B4) parantez içinde dergi sayfası da verildi. SEL 2022 makalesinde (B7) PDF'in 1. sayfası kapak olduğundan PDF s. = basılı s. + 1.

**Proje iş paketleri (WP):** WP1 tasarım aracı (CVXPY) · WP2 EMT simülasyonu (Simulink/PSCAD) · WP3 röle tarafı tespit (klasik elemanlar, Kalman dedektörü, öğrenen dedektörler) · WP4 gömülü gecikme (tek çevrim ≈16 ms bütçe).

## İçindekiler ve gruplama

| Kod | Kısa ad | Sınıf | Dosya |
|---|---|---|---|
| B1 | Li–Wu–Wang 2025, GFM için koruma-uyumlu FRT kontrolü | Kontrol-tabanlı çözüm | `2025_Protection_Interoperable_Fault_Ride_Through_Control_GFM` |
| B2 | Davi–Oleskovicz–Lopes 2023, IEEE 2800'ün hat korumasına etkisi | Kontrol (şebeke kodu) değerlendirmesi | `2023_IEEE2800_Benefits_Transmission_Line_Protection_IPST` |
| B3 | Opoku–Pokharel–Dimitrovski 2022, artımlı NS admitans (ΔY2) | Pasif sekans elemanı | `2022_Incremental_Negative_Sequence_Admittance_...` |
| B4 | Opoku–Dimitrovski–Ferrari 2025, ΔY2'nin HIL + SEL-411L ile doğrulanması | Pasif sekans elemanı | `2025_Opoku_Sequence_Based_Directional_Detection_...` |
| B5 | Johansson–Xing–Taylor(N.)–Wang 2026, artımlı-büyüklük (IQ) mesafe koruması + GFM | Pasif artımlı eleman | `2026_Incremental_Quantity_Distance_Protection_GFM` |
| B6 | Chowdhury–Fischer (SEL) 2021, IBR'li sistemlerde hat koruması: çözümler | Endüstri: ayar-tabanlı çözüm | `2021_SEL_Line_Protection_IBR_Solutions_WPRC` |
| B7 | Chowdhury–McDaniel–Fischer (SEL) 2022, IBR'li sistemlerde 87L | Endüstri: haberleşmeli diferansiyel | `2022_SEL_Line_Current_Differential_IBR` |
| B8 | Yang–Dyśko–Egea-Àlvarez 2024, NSCI aktif koruma | **Aktif enjeksiyon (en yakın öncül)** | `2024_Yang_Dysko_NSCI_Active_Protection_...` |
| B9 | Mohammadhassani–Mehrizi-Sani–Saleh 2021, sentetik harmonik + SVM | Aktif enjeksiyon + öğrenen | `2021_Directionality_SVM_Synthetic_Harmonic_Injection` |

## Kısa sözlük (ilk okumada başvurmak için)

- **Simetrik bileşenler (sequence components):** Üç fazlı fazörleri pozitif (1), negatif (2) ve sıfır (0) bileşene ayırma. Dengeli işletmede I2 ≈ 0, I0 ≈ 0; dengesiz arızalar (AG, BC, BCG…) I2/V2 üretir. Negatif bileşen (NS) "yükten bağımsız arıza imzası" olarak sevilir.
- **Artımlı / süperpoze büyüklük (incremental / superimposed quantity, Δ):** Arıza anındaki değer eksi arıza öncesi (bellekteki) değer, ör. Δv(t) = v(t) − v(t − pT). Süperpozisyon ilkesiyle yük akımını ayıklar ve "saf arıza ağı"nı (pure-fault network) verir. **Gizli varsayım:** kaynaklar doğrusal ve arıza öncesi ile aynı davranıyor — IBR'lerde bozulan tam da budur.
- **Yön elemanı (directional element, ANSI 32):** Arızanın röleye göre ileride (forward) mi geride (reverse) mi olduğunu söyler. 32Q: negatif-bileşen, 32G/32V: sıfır-bileşen, 32P: pozitif-bileşen. **Faz seçimi (phase selection, FIDS):** Hangi fazların arızalı olduğunu belirler (tek-kutup açma ve doğru mesafe döngüsü için).
- **Mesafe rölesi (21):** V/I'dan görünür empedansı hesaplar; Bölge 1 (Zone 1) hattın ~%75–80'ini gecikmesiz korur, Bölge 2 gecikmeli yedektir. Karakteristikler: mho (daire), quadrilateral (dörtgen). Polarizasyon: self, memory (arıza öncesi gerilim belleği), cross.
- **Dependability / security:** Dependability = açması gereken arızada açması; security = açmaması gereken durumda açmaması. Koruma mühendisliğinde security genelde önceliklidir.
- **GFL / GFM inverter:** Grid-following (şebekeyi izleyen, akım kaynağı gibi) / grid-forming (gerilim kaynağı gibi, iç gerilim kaynağı IVS + çıkış empedansı). **FRT (fault ride-through):** arızada devrede kalma davranışı. **Akım limitleyici (CLC):** inverter akımını ~1.1–1.3 pu ile sınırlar; "doyum (saturation)" veya "sanal empedans (virtual impedance)" tipi olabilir.
- **IEEE 2800-2022:** İletime bağlı IBR'ler için standart; arızada V2'ye orantılı, V2'yi 90–100° önden izleyen NS akım enjeksiyonu ister (B2).
- **87L (hat akım diferansiyeli):** İki uçtaki akımları haberleşme kanalıyla karşılaştırır; alfa düzlemi (alpha plane) bir karakteristik türüdür. Haberleşme gerektirir.
- **POTT / DCB / DZI:** Haberleşmeli koruma şemaları (izinli/engelli transfer trip).
- **SIR / SCR:** Kaynak-hat empedans oranı / kısa devre oranı (şebeke ne kadar "güçlü").
- **HIF (high-impedance fault), Rf:** Yüksek empedanslı arıza, arıza direnci.
- **EMT, HIL/CHIL:** Elektromanyetik geçici rejim simülasyonu; donanım-döngüde (kontrolcü donanım-döngüde) test.

---

## B1 — GFM inverterler için koruma-uyumlu FRT kontrolü (Li, Wu, Wang, 2025)

- **Künye:** Yifei Li, Heng Wu, Xiongfei Wang, "A Protection-Interoperable Fault Ride-Through Control for Grid-Forming Inverters". Yıl 2025 (dosya adına göre). IEEE dergi formatında, 10 sayfa. **PDF'te dergi adı/cilt bilgisi yok** (en yeni kaynaklar 2024; künye doğrulanmalı).
- **Tek cümlede:** GFM inverterin sanal-empedans akım limitleyicisi arıza sırasında çıkış empedansını aniden değiştirdiği için artımlı-büyüklük tabanlı denetleyici elemanların ("kaynak arıza öncesindekiyle aynı") varsayımı bozulur; makale, arıza süresince iç gerilim kaynağını açık-çevrim olarak e_ref1 = e_pre1 + i_tpre1·Z_v1 yapacak şekilde ayarlayıp bu varsayımı yapay olarak geri getiriyor.

**Problem ve bağlam**
- Mesafe rölelerindeki **denetleyici elemanlar (supervising elements)** — yön ve faz seçimi — açmanın sadece ileri yöndeki arızada ve doğru fazlarda olmasını sağlar (s. 1). Yükten bağımsız olmak için **artımlı** büyüklükleri (Δv, Δi) kullanırlar; bunun teorik temeli "compensation theory": arıza sırasında kaynağın iç gerilimi (IVS) ve çıkış empedansı arıza öncesine göre ihmal edilebilir değişir (s. 1).
- Makale iki ön koşul sayar (s. 4): (a) etkin empedans yüksek derecede endüktif; (b) arıza ağı ile arıza öncesi devre arasında kaynak dinamiği (IVS + çıkış empedansı) farkı ihmal edilebilir.
- GFM'de yavaş güç kontrolü sayesinde e_ref1 ≈ e_pre1 kalır, fakat akım limitleyici (CLC) devreye girince seriye bir Z_v1 eklenir; arıza öncesi Z_v = 0'dır. Böylece (b) bozulur (s. 5, Şekil 8).
- Alternatifler: SEL-T400L gibi kaynaktan bağımsız gezici-dalga (traveling wave) yöntemleri 1 MHz örnekleme gerektiriyor (s. 1); önceki kontrol-tabanlı çalışmalar tek bir elemana göre ayar yapıp diğerlerini bozabiliyor ve çoğu GFL içindir (s. 1).

**Yöntem / yaklaşım**
- Yön elemanları (s. 2–3): φ2 = ∠(v2/i2) = ∠−(Z_s2 + jX_SG2), φ0 benzer (denk. 1); ileri arızada φ2 ≈ φ0 ≈ −90°, geri arızada ≈ +90°. Artımlı pozitif-bileşen: Δφ1 = ∠(−Δv1/Δi1) ≈ ∠−(jX_SG1 + Z_s1) (denk. 6). "Açmama bölgesi" φ_non 30°–60° (s. 3).
- Faz seçimi (s. 3–4): Δδ21 = ∠i2 − ∠Δi1 ve δ20 = ∠i2 − ∠i0; bölgeler ±15° ve ±30° genişletilmiş (s. 4).
- Sorunun matematiği (s. 5, denk. 8): ΔZ_e1 = −Δv1/Δi1 = (jn²X_f1 + jX_T1) + Z_ad, burada Z_ad = (n·e_pre1 − n·e_ref1 + n²·i1·Z_v1)/(i1 − i_pre1). Z_ad'nin açısı garanti değil → ΔZ_e1 endüktif olmayabilir.
- İki seçenek (s. 5): (a) arızada IBR'yi arıza öncesi gibi yap → akım limitlemeyi devre dışı bırakır, pratik değil; (b) arıza öncesi devreyi "arızadaki IBR" ile eşdeğer göster → **denk. (9): e_ref1 = e_pre1 + i_tpre1·Z_v1** (s. 6). Sonuç **denk. (10): ΔZ_e1 = jn²X_f1 + jX_T1 + n²Z_v1** → Z_v1 endüktifse etkin artımlı empedans endüktif.
- Negatif bileşen: E_ref2 = 0 ve yüksek endüktif Z_v2 ile Z_e2 endüktif tutulur (denk. 7, s. 4–5).
- Gerçekleme (s. 6–7):
  - İki mod: "koruma-uyumlu" mod (IVS denk. 9'dan; aktif güç kontrolü dondurulur: P1 yerine P_ref) ve normal mod.
  - Geçiş kriteri: I_max = max(I_ta, I_tb, I_tc) (denk. 15) ≥ I_th1 = 1.05·I_N1 → moda gir; I_max < I_th1 durumu t1 = 50 ms sürerse **veya** t_p (rölenin arıza-öncesi bellek süresi) dolarsa normale dön.
  - Akım limitleri: I_t1 ≤ I_lim1, I_t2 ≤ I_lim2 (denk. 16); |Z_v1 + jX_f1| ≥ |v_tpre1 − v_t1|/(I_lim1 − I_tpre1) (denk. 19); V_t2/I_lim2 ≤ |Z_v2 + jX_f2| (denk. 20); adaptif sanal endüktans X_v = K_X(I − I_thX) (denk. 21), kazanç koşulları denk. 22. Sadece endüktans kullanılır (röle için).
  - Geçici akım: en fazla t_r = 50 ms sanal direnç; aynı t_r kadar röleye gecikme eklenir (s. 7).
  - Geçici kararlılık: koruma modunda güç kontrolü açık-çevrim; normal modda adaptif hızlı/yavaş kontrol, I_thf = 0.94 pu (s. 7–8).

**Ana bulgular**
- CHIL düzeneği (s. 8, Şekil 14): üç RT-Box3 (kontrolcü, tesis, röle). Tablo I: 220 kV, 50 Hz, 100 MW, 33/220 kV trafo, v_dc 40 kV, L_f 5 mH, L_T 77 mH (0.05 pu), 100 km hat, Z_l1 = 0.03 + j0.34 Ω/km, Z_l0 = 0.18 + j1.19 Ω/km, Z_g = 200 mH (SCR = 6.8).
- Test vakası: bara 1–2 arasında ag arızası, m = 0.01, R_f = 20 Ω; t_p = 1 s'ye uzatılmış (s. 8).
- Klasik kontrolde (Şekil 15): artımlı elemanlar (Δφ1, Δδ21) doğru bantların dışına çıkıyor; NS/ZS elemanları (φ2, φ0, δ20) doğru bantta kalıyor (endüktif Z_v2 + Δ-Y0 trafo sıfır-bileşeni IBR'den ayırıyor). Şekil etiketlerinde Δδ21 = 63° ve Δφ1 = −9° görünüyor (beklenen ≈0° ve ≈−90°); bu etiketlerin ölçüm mü osiloskop referansı mı olduğu **belirsiz**.
- Önerilen kontrolde (Şekil 16): beş büyüklük de bantlarda; etiketler Δδ21 = 0°, Δφ1 = −90°.
- Deney (s. 9, Tablo II): 1 kW inverter, 86.6 V (0.816 pu), f_s 10 kHz, L_g 6 mH (SCR = 4), L_f 3 mH; Chroma 61850 45 kVA şebeke simülatörü + dSPACE DS1007.
  - Şekil 18: v_g 0.2 s süreyle 0.7 pu'ya düşer, t_p = 0.3 s: mod devreye girer, ∠ΔZ_t1 ≈ −90°, arıza kalkınca t1 = 50 ms sonra çıkar.
  - Şekil 19: 0.3 s süreli v_g → 0.1 pu ve −60° faz sıçraması, t_p = 0.2 s: ∠ΔZ_t1 ≈ −90°, akım < 1.5 pu.
  - Şekil 20: aynı bozucular altında geçici kararlılık korunuyor.

**Varsayımlar ve sınırlamalar**
- Röle elemanları için **tek bir CHIL vakası** (ag, m = 0.01, R_f = 20 Ω) var; arıza tipi, konum, R_f, SCR taraması ve başarı istatistiği **yok**.
- Deneyler hat arızası değil, şebeke simülatöründe gerilim çökmesi/faz sıçraması; röle elemanları değil yalnızca inverter terminalinde ∠ΔZ_t1 gösteriliyor.
- Mod geçişi I_max ≥ 1.05·I_N eşiğine bağlı: akımı bu eşiğin üstüne çıkarmayan yüksek empedanslı arızalarda mod hiç tetiklenmeyebilir; tersine, uzak arızadan kaynaklı gerilim çökmeleri gibi arıza-dışı olaylar modu tetikleyip güç kontrolünü açık-çevrime alabilir (makalede analiz edilmemiş).
- Tek IBR + sonsuz bara; çoklu IBR / %100 IBR şebeke yok. Mesafe elemanının kendisi (sadece denetleyiciler) değerlendirilmemiş.
- Röleye **t_r = 50 ms** gecikme eklenmesi öneriliyor — hızlı koruma ve bizim 16 ms bütçemizle çelişir.
- Yöntem yeni bilgi yaratmaz: IBR katkısı küçükse artımlı büyüklüklerin genliği yine küçüktür; sadece açıları "SG gibi" yapar.

**Projeyle bağlantı**
- **Sınıf:** kontrol-tabanlı rakip. Test sinyali enjekte etmez; inverterin arıza yanıtını, klasik röle "SG görüyormuş gibi" davransın diye yeniden biçimlendirir. Yardımcı sinyal ise (proje tanımına göre) rölenin ayırt etmesi için ölçüme bilinen bir uyarım katar — iki yaklaşım birbirini dışlamaz.
- **WP1:** Denk. (16), (19), (20) bir "akım bütçesi" şablonu: arıza sırasında yardımcı sinyal genliği, FRT akımıyla birlikte I_lim2 içinde kalmalı → CVXPY'de doğrudan doğrusal/SOC kısıt.
- **WP2:** APF ile sekans ayrıştırma, sanal-empedans CLC, E_ref2 = 0 olan GFM modeli (Şekil 6) bir EMT inverter modeli adayı; Tablo I parametreleri (220 kV, 100 km, SCR 6.8) hazır test vakası.
- **WP3:** Δφ1, φ2, φ0, Δδ21, δ20 elemanları açıkça tanımlı bölgelerle (30–60° ölü bölge, ±15°/±30°) — **klasik baseline olarak uygulanmalı**.
- **WP4:** Rölenin arıza-öncesi bellek süresi t_p ve önerilen t_r = 50 ms gecikme, zamanlama referansı.
- **Baseline mı?** Denetleyici elemanlar: evet. Tam FRT kontrolü: ağır; ancak "klasik GFM CLC" ve "B1 kontrolü" iki senaryo olarak EMT'de denenebilir.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★ **Akım bütçesi kısıtı:** (16)–(20)'yi tasarım aracına ekleyip arızada yardımcı sinyal için kalan NS akım payını (I_lim2 − |I_t2,FRT|) hesapla; Tablo I sisteminde EMT ile yardımcı sinyal + B1 kontrolü birlikteyken φ2 ve Δφ1'in bantlarda kalıp kalmadığını test et.
2. **Tetiklenmeme bölgesi:** R_f taraması yaparak I_max < 1.05·I_N kaldığı (mod devreye girmediği) R_f sınırını bul; bu bölgede yardımcı sinyalin tespit sağlayıp sağlamadığını göster. (Yardımcı sinyalin B1'e en net katkısı olabilir.)
3. **Etkileşim:** Yardımcı sinyal NS referansına eklenirse (E_ref2 ≠ 0) ön koşul (b) bozulur mu? Sürekli ve sabit bir sinyal artımlı büyüklüklerde (Δ) iptal olacağı için sorun yaratmayabilir; arızada sinyal yanıtının değişmesi ise artımlı elemanlara ek "bilinen kaynaklı" bilgi verebilir — EMT'de doğrulanacak hipotez.
4. **Zamanlama:** t_p sınırı (artımlı elemanlar bellekleri dolunca devre dışı) ile yardımcı-sinyal kararının 16 ms içinde verilmesi arasındaki ilişki.

**Kilit şekil/tablo/denklemler**
- Denk. (1) φ2, φ0 — s. 2; Denk. (6) Δφ1 ve Şekil 4 (yön bölgeleri) — s. 3; Şekil 5 (faz seçimi) ve ön koşullar — s. 4; Denk. (7) — s. 4.
- **Denk. (8)** ve Şekil 8 (sorunun özü) — s. 5; **Denk. (9)–(10)** — s. 6; Şekil 11–12 (güç kontrolü ve mod geçişi) — s. 6.
- Denk. (16)–(22) akım limitleri — s. 7; Tablo I, Şekil 14–16 (CHIL) — s. 8; Tablo II, Şekil 17–20 (deney) — s. 9.

---

## B2 — IEEE 2800-2022'nin hat koruma fonksiyonlarına faydası (Davi, Oleskovicz, Lopes, IPST 2023)

- **Künye:** Moisés J. B. B. Davi, Mário Oleskovicz, Felipe V. Lopes, "Study on IEEE 2800-2022 Standard Benefits for Transmission Line Protection in the Presence of Inverter-Based Resources", International Conference on Power Systems Transients (IPST 2023), Selanik, 12–15 Haziran 2023. 8 sayfa. (USP / UFPB, FAPESP desteği.)
- **Tek cümlede:** PSCAD'de 8320 arıza senaryosuyla, negatif-bileşen akımını bastıran eski IBR kontrolü (G1C) ile IEEE 2800-2022 uyumlu ve V2'ye orantılı NS akım enjekte eden kontrolün (G2C) yedi klasik hat koruma fonksiyonuna etkisini karşılaştırır: G2C, NS tabanlı yön/faz seçimi elemanlarını ve mesafe korumasını belirgin biçimde iyileştirir.

**Problem ve bağlam**
- IBR'ler termal sınır nedeniyle arıza akımını tipik olarak ≤1.2 pu ile sınırlar ve farklı kontrol stratejileri farklı arıza katkıları üretir (s. 2). Diferansiyel koruma güvenilir ama haberleşme kaybolursa mesafe koruması önemli; literatür şebeke kodlarının etkisini ve özellikle IEEE 2800'ün NS akım gereksinimini sistematik incelememiş (s. 1).
- İki kontrol grubu (s. 2, Şekil 1):
  - **G1C** (coupled sequence control): sadece pozitif bileşen; **NS akımları asimetrik arızada bile bastırılır**.
  - **G2C** (decoupled sequence control, IEEE 2800 uyumlu): arıza tespitinden sonra gerilim değişimine bağlı ek reaktif akım + **V2 ile orantılı (Şekil 1'de I_neg = K·V_neg), V2'yi 90–100° önden izleyen NS akımı**. Amaç: IBR'nin pozitif/negatif bileşen empedanslarını senkron makineye benzetmek.

**Yöntem / yaklaşım**
- Test sistemi (s. 2, Şekil 2, Tablo I): 147 × 1.5 MW tam-dönüştürücülü rüzgâr türbini (FCWG, PMSG), 34.5/138/500 kV; Hat 1-2 100 km, Hat 2-3 147 km; FCWG çıkışı 220.5 MW, 0 var. DC bara 0.015 F, 1450 V; şok 0.003 pu + 0.15 pu; 120 kvar RC filtre; chopper 1.15/1.05 pu.
- Senaryolar (s. 3): 10 arıza tipi (AG…ABC), faz-faz direnci R_ph ∈ {0, 1, 1.5, 2.5} Ω, toprak direnci R_g ∈ {0, 25, 50, 100} Ω, başlangıç açısı 0°/90°, Hat 1-2'de %0–100 (%10 adım), Hat 2-3'te %5 ve %50 → iki kontrolle toplam **8320 senaryo**. Ölçümler P1 (rüzgâr santrali tarafı) ve P2 (şebeke tarafı); 3. dereceden 180 Hz kenar-yumuşatma (anti-aliasing) filtresi.
- Yön ve faz seçimi kararları **arızadan 100 ms sonra** alınıyor (FCWG kontrol yanıtı ~50 ms); bu bölümde sadece Hat 1-2 arızaları (7040 senaryo) (s. 3).
- İncelenen fonksiyonlar ve kuralları:
  - **NS yön (32Q tipi), denk. (1):** Z2 = Re[V2·(1∠θ_L1·I2)*]/|I2|²; Z2 < Z2F (tipik: hattın pozitif-bileşen empedansının yarısı) → ileri; Z2 > Z2R = Z2F + 0.2 Ω → geri; **denetim: 3|I2| > 0.25|I_nominal|** (s. 3).
  - **ZS yön, denk. (2):** Z0 = Re[3V0·(1∠θ_L0·3I0)*]/|3I0|²; denetim 3I0 > 0.5 I_nominal (s. 3).
  - **Artımlı fazör faz seçimi, denk. (3)–(5):** ΔT_ab = Re[ΔV_ab·(1∠θ_L1·ΔI_ab)*] vb.; normalize edilip L_up = 0.7, L_int = 0.5, L_low = 0.35 ile Tablo II'ye göre sınıflandırma (s. 4).
  - **Akım açısı faz seçimi** (Şekil 6): I2–I0 açı farkı; aynı akım seviyesi kısıtları (s. 4–5).
  - **Mho mesafe** (Tablo III, s. 5): self-, memory-, memory-cross-polarized; faz karşılaştırıcı α ±90° içinde ise bölgede; Bölge 1 erişimi %75, **50 ms kasıtlı gecikme**, 150 ms izleme penceresi.
- Ticari röle doğrulaması: PSCAD COMTRADE kayıtları ticari röleye oynatılmış (Şekil 12, s. 7); röle markası belirtilmemiş.

**Ana bulgular**
- **NS yön elemanı (Şekil 3, s. 3):** G1C'de P1'de (IBR tarafı) **incelenen tüm senaryolarda eleman bloke** (NS akım yok); P2'de doğru. G2C'de P1'de PP ve PPG için %100, **PG için %90**; hatalar yalnız **yüksek arıza direncinde**: V2 küçük kalınca kontrol çok az NS akımı enjekte ediyor.
- **ZS yön elemanı (Şekil 4, s. 4):** her iki kontrolde, P1 ve P2'de toprak arızalarında tatmin edici; çünkü P1'deki I0 IBR'den değil şebekeden YNyn0 trafosunun nötründen geliyor.
- **Artımlı fazör faz seçimi (Şekil 5, s. 4):** P2'de %100. P1'de G1C: üç-faz arızada %75; tek-faz arızaların ~%65'i PP/PPG, %25'i "sınıflandırılamadı" (NC); iki-faz arızaların ~%73'ü üç-faz olarak sınıflandırılmış. Ortalama doğru oran tek-faz/iki-faz için **%9.94 / %15.1 (G1C) → %68.56 / %95.31 (G2C)**; üç-faz %75 → %100.
- **Akım açısı faz seçimi (Şekil 7, s. 5):** G1C'de 3I2 > 0.25 I_nom kısıtı yüzünden fonksiyon bloke (tüm vakalar NC); G2C'de ortalama **%88.44 (tek-faz), %81.34 (iki-faz)**.
- **Mesafe (Şekil 8–9, s. 6):** P2'de vakaların %84.61'inde akım konvansiyonel üretimden geliyor. P1'de tek-faz arızada kontrolün etkisi küçük (I0 şebekeden). Self-polarized'da G1C ile PP/PPG/PPP için **ortalama %17.3 gereksiz açma (undue trip)**; G2C ile neredeyse sıfır. Memory-polarized (Şekil 9b): doğru oran G1C PG/PP/PPG/PPP = 57.2/25.7/70.5/76.9 %, G2C = 58.6/93.0/94.6/92.3 %; metne göre G2C PP'de ~%70, PPG/PPP'de ~%20 artış, ortalama ~%93.3.
- **Ticari röle (Şekil 13, s. 7):** %50'de metalik AB arızası, memory-polarized: G1C'de karşılaştırıcı çalışma bölgesine ancak ~100 ms sonra giriyor ve değerlendirme süresinde açma yok; G2C'de ~40 ms'de giriyor ve 50 ms gecikme sonrası açıyor.

**Varsayımlar ve sınırlamalar**
- G2C'nin detayları (K kazancı, akım önceliği, limit) verilmemiş; K'ya duyarlılık incelenmemiş.
- Tek santral, tek ağ; GFL tipi FCWG — **GFM yok**.
- Kararlar arızadan **100 ms** sonra; mesafe 50 ms gecikmeli. Hızlı (≤1 çevrim) performans hakkında bilgi yok.
- Yüzdeler toplu; hangi R_g/konumda hata olduğu (PG %10) yalnızca nitel ("yüksek arıza direnci").
- Ticari röle testi tek vaka; marka/model belirtilmemiş.
- Çoklu IBR ve G2C'lerin birbirinin V2'sine tepki vermesi incelenmemiş.

**Projeyle bağlantı**
- **Bu makale "yeni normal"i tanımlıyor:** IEEE 2800 uyumlu IBR'ler arızada zaten NS akımı enjekte ediyor. Tasarlanmış yardımcı sinyalin değeri **G2C'nin üzerine** ne kattığıyla ölçülmeli — özellikle G2C'nin zayıf olduğu yüksek-R_g PG arızalarında (V2 küçük → NS enjeksiyonu küçük).
- **WP2:** G1C (en kötü durum) ve G2C (standart) iki inverter kontrol seçeneği olarak modellenmeli (Şekil 1 blok diyagramı yeterince açık). Senaryo matrisi (tip × R_ph × R_g × açı × konum) doğrudan kopyalanabilir.
- **WP3:** Yedi fonksiyonun formül ve eşikleri açık → hazır **klasik baseline paketi**: Z2F/Z2R, 3I2 > 0.25 I_nom, L_up/L_int/L_low, mho polarizasyonları.
- **WP4:** 100 ms karar anı vs. bizim 16 ms bütçemiz: "başarı oranı vs. karar gecikmesi" eğrisi bu çalışmada yok — bizim katkımız olabilir.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★ **IEEE 2800'e ek değer deneyi:** Şekil 3a'yı R_g = 25/50/100 Ω PG arızaları için yeniden üret; G2C + yardımcı sinyal ile 32Q (denk. 1) başarısını karşılaştır. "%90 → ?" sorusu, projenin en ikna edici tek grafiği olabilir.
2. **Karar gecikmesi taraması:** Aynı fonksiyonların başarısını karar anı 10–100 ms arasında tarayarak çıkar; 16 ms'de klasik elemanların nerede durduğunu göster.
3. **Etkileşim:** G2C'nin K·V2 enjeksiyonu (Şekil 1'de "Fault Detection" ile anahtarlanıyor) yardımcı sinyalin ürettiği V2'ye normal işletmede tepki veriyor mu? Arızada iki NS kaynağı (G2C + yardımcı sinyal) birbirini maskeleyebilir mi?
4. G1C ile yardımcı sinyal: NS'yi tamamen bastıran eski inverterlerin bulunduğu şebekede, tek bir yardımcı-sinyal inverterinin P1'deki bloke 32Q'yu kurtarıp kuramayacağı.

**Kilit şekil/tablo/denklemler**
- Şekil 1 (G1C vs G2C blok diyagramı, I_neg = K·V_neg) — s. 2; Şekil 2 ve Tablo I (test sistemi) — s. 2.
- **Denk. (1)** NS yön ve **Şekil 3** — s. 3; Denk. (2), Şekil 4–5, Denk. (3)–(5), Tablo II — s. 4; Şekil 6–7, Tablo III — s. 5.
- **Şekil 8–9** (mesafe yüzdeleri) — s. 6; Şekil 10–13 (empedans yörüngeleri, ticari röle) — s. 7; Sonuçlar — s. 8.

---

## B3 — Artımlı negatif-bileşen admitans (ΔY2) yöntemi, ilk sürüm (Opoku, Pokharel, Dimitrovski, 2022)

- **Künye:** Kwasi Opoku, Subash Pokharel, Aleksandar Dimitrovski (University of Central Florida), "An Incremental Negative Sequence Admittance Method for Fault Detection in Inverter-Based Microgrids", arXiv:2205.02962v1 [eess.SY], 5 Mayıs 2022. 6 sayfa. (B4'ün kaynakçasındaki [18] numaralı IEEE PESGM 2022 bildirisinin ön baskısı olması muhtemel; başlıklar birebir aynı değil.) DOE EERE desteği.
- **Tek cümlede:** Dengesiz arızaların yönünü ve varlığını, arıza öncesi ve sonrası negatif-bileşen akım/gerilim farklarının oranı olan süperpoze NS admitansın (ΔY2 = ΔI2/ΔV2) büyüklüğü ve açısıyla belirleyen basit, haberleşmesiz bir yön elemanı önerir ve küçük bir topluluk mikroşebekesinde birkaç simülasyonla gösterir.

**Problem ve bağlam**
- Aktif dağıtım şebekelerinde çift yönlü arıza akımı, sempatik açma ve koruma körleşmesi; IBR'lerin kararlı arıza akımı ~1.2 pu ile sınırlı (IEEE 1547'ye atıfla) (s. 1).
- Adaptif koruma haberleşme ve topoloji bilgisi ister; diferansiyel/mesafe/gezici-dalga dağıtımdaki kısa hatlar ve yanallar nedeniyle sorunlu (s. 1). Süperpoze büyüklükler yükten bağımsız "saf arıza" bilgisi verir (s. 2).

**Yöntem / yaklaşım**
- Süperpoze büyüklükler: ΔV = V_fault − V_pre, ΔI = I_fault − I_pre (denk. 1–2); ΔZ2 = ΔV2/ΔI2 (denk. 8, önceki çalışma).
- **Önerilen eleman, denk. (9):** ΔY2 = (I2f − I2pre)/(V2f − V2pre) = ΔI2/ΔV2 (s. 3). Gerekçe: admitans, ileri arızada daha büyük bir genlik vererek duyarlılığı artırır; şebekeye bağlı modda NS'nin şebekeden gelmesi doğruluğu artırır.
- İdeal kaynak + tamamen endüktif sistemde arg(ΔI2/ΔV2) = +90° (ileri), −90° (geri) (denk. 10).
- Karar (denk. 11–12): ileri: 0° + φ < arg ΔY2 < 180° + φ; geri: 180° + φ < arg ΔY2 < 360° + φ; φ hat açısı kompanzasyonu.
- Başlatma kriteri: |I2/I1| > 0.1 (dengesiz yüke karşı) ve |ΔY2| > Y_set (Şekil 5 akış diyagramı).
- Eşikler (s. 4): normal işletme testlerinden **Y_set = 10 (röle A, B), 5 (röle C)**, **φ = 20°** (ticari röleler tipik 20°–45°). **ΔY2'nin birimi belirtilmemiş.**

**Ana bulgular**
- Test mikroşebekesi (s. 3–4, Şekil 6): 300 kVA 4/0.48 kV trafo; Bara 2'de iki adet 125 kW/kVA inverterli 442 kWh batarya; altı tek-faz + bir üç-faz ticari yük, her birinde çatı PV; MATLAB/Simulink. Arıza 0.2 s'de.
- **Vaka A** (F1'de BCG, şebeke tarafı; beklenen: geri): |ΔY2| röle A 6.89, C 0.88 (Y_set altında); arg −98° ve −24° → geri. Röle B ~0.3, açısı geri bölgede salınıyor (s. 4). Not: metin burada "φ = 30°" diyor, ayarlar bölümünde 20° — **tutarsızlık**.
- **Vaka B** (F2'de BCG): A ve B ileri, |ΔY2| ≈ 19.8 ve 17.9, açı ≈ 100°; C doğru biçimde geri (s. 4).
- **Vaka C** (F3'te BCG): C ileri, |ΔY2| ≈ 48.9, arg 105° (s. 5).
- **Vaka D** (F1, F2, F3'te AG): doğru kararlar; arızaya yakın röle (A) daha büyük |ΔY2| görüyor (s. 5).

**Varsayımlar ve sınırlamalar**
- Sadece **şebekeye bağlı mod**; adalanmış mod yok (B4'te var). Sadece birkaç arıza noktası, R_f taraması yok, başarı istatistiği yok.
- Eşikler (Y_set, φ) deneme-yanılma; genel bir ayar kuralı yok — makalenin kendisi de sonuçta "her sistem için ayrı değerlendirme" gerektiğini söylüyor (s. 5).
- **Şekilden okunan önemli gözlem:** Şekil 7–13'te arıza öncesinde (0.2 s'den önce) |ΔY2| değerleri büyük (ör. Şekil 9'da A ve B için ~15–20, yani Y_set = 10'un üstünde). Makale bunları "simülasyon ve kontrol sistemi gürültüsü" olarak niteliyor ve açmanın yalnızca |I2/I1| başlatma kriteri sayesinde engellendiğini söylüyor (s. 4–5). Yani güvenlik (security) tek bir oran eşiğine dayanıyor.
- Sadece dengesiz arızalar: dengeli (üç-faz) arızada I2 ≈ 0 → eleman tanımsız.
- Dedektörün hızı/gecikmesi raporlanmamış.

**Projeyle bağlantı**
- **Sınıf:** pasif sekans elemanı (yardımcı sinyal enjekte etmez; arızanın ve kaynakların ürettiği NS'ye dayanır).
- **WP3:** Uygulaması çok basit (iki fazör farkı ve bir bölme) → **klasik/pasif baseline** adayı (B4 versiyonu daha olgun).
- **WP1:** İleri/geri kararı bir **açı konisi** (arg ΔY2 ∈ (φ, 180°+φ)) — set-tabanlı tasarımda "ölçüm kümesi bu koni içinde kalsın" tipi bir kısıt olarak ifade edilebilir.
- Yardımcı sinyalle ilişkisi: Pasif ΔY2'nin zayıflığı, ΔI2'nin büyüklüğünün tamamen arızaya ve kaynaklara bağlı olması; yardımcı sinyal ΔI2'yi **bilinen** hale getirebilir.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★ **Aktif ΔY2 / adaptif eşik:** Yardımcı sinyal bilinen bir ΔI2 uyguladığında röle normal işletmede kaynak-arkası NS admitansını ölçebilir → Y_set sabit ve sezgisel olmak yerine canlı kalibre edilebilir. Test: yük dengesizliği değişirken sabit Y_set ile aktif-kalibre eşiğin yanlış alarm / kaçırma oranlarını karşılaştır.
2. **Başlatma kriteri olmadan güvenlik:** |I2/I1| > 0.1 kapısını kaldırınca arıza öncesi ΔY2 gürültüsünün kaç kez Y_set'i aştığını say — pasif tek-eşik yaklaşımının kırılganlığını nicelleştiren basit bir deney.
3. ΔY2 biriminin ve ölçeklemesinin netleştirilmesi (pu tabanı) — B4'te pu kullanılıyor.

**Kilit şekil/tablo/denklemler**
- Denk. (1)–(5) ve Şekil 1–4 (süperpozisyon) — s. 2; **Denk. (9)–(12)** ve **Şekil 5** (akış diyagramı) — s. 3.
- Şekil 6 (test mikroşebekesi), Şekil 7–9, ayarlar (Y_set, φ) — s. 4; Şekil 10–13, Vaka C–D, sonuç — s. 5.

---

## B4 — ΔY2 yönteminin performans değerlendirmesi: HIL + SEL-411L (Opoku, Dimitrovski, Ferrari, IEEE Access 2025)

- **Künye:** Kwasi Opoku, Aleksandar Dimitrovski, Maximiliano Ferrari, "Performance Evaluation of a Novel Sequence-Based Directional Detection Strategy for Protection of Active Distribution Networks", *IEEE Access*, cilt 13, s. 7094–7109, 2025 (DOI 10.1109/ACCESS.2024.3525057). 16 sayfa. UCF + Oak Ridge National Laboratory; DOE EERE desteği.
- **Tek cümlede:** Mevcut yön elemanlarının (T32P, T32Q, Z2, sıfır-bileşen) IBR'li dağıtım şebekesinde nerede yanıldığını gösterir ve ΔY2 = ΔI2/ΔV2 yön elemanını gerçek bir SEL-411L rölesine serbest-biçimli mantıkla (SELogic) programlayıp OPAL-RT HIL'de hem şebekeye bağlı hem adalanmış modda doğrular; röle içi Z2 elemanının yanıldığı vakalarda ΔY2 doğru karar verir.

**Problem ve bağlam**
- IBR'li aktif dağıtım şebekesinde yön elemanlarının sorunları (s. 7, "Summary", s. 7100): (1) aşırı akım-tabanlı yöntemler adalanmışlıkta düşük arıza akımıyla temelden zorlanır; (2) yük seviyesine yakın arıza akımları pozitif-bileşen yöntemlerini bozar; (3) adalanmışlıkta düşük V2/I2 açıları güvenilmez yapar; (4) IBR'ler I0 vermediği için sıfır-bileşen yöntemleri trafo topraklamasına bağımlıdır.
- Somut örnekler (s. 5–6 / 7098–7099): R632 için geri yöndeki BCG arızasında (F1) T32P +188 tork ile yanlışlıkla "ileri" diyor; açı 41.2°. Uzak BCG arızasında (F9) R632'nin gördüğü |V2| = 11.5 V (sekonder), |I2|/|I1| = 0.167 (tipik 0.1–0.2 kısıtlama aralığının içine düşüyor); yakın arızada (F5) |V2| = 31.9 V.
- Kontrol-tabanlı (dual current control, GFM kısa devre akımını artırma) çözümler mevcut kurulu IBR'lere uygulanamayabilir; ayar değişikliğiyle uygulanabilir yöntemler tercih ediliyor (s. 2 / 7095).

**Yöntem / yaklaşım**
- Test sistemi (s. 3 / 7096, Şekil 1): değiştirilmiş IEEE 13-bara besleyici; 115/4.16 kV, 5000 kVA trafo; bara 680'de 250 kW BESS, bara 692'de 125 kW üç-faz PV, bara 646'da 40 kW tek-faz PV. Şebekeye bağlı modda tüm IBR'ler GFL; adalanmışta BESS GFM (P-f / Q-V droop + sanal empedans).
- IBR akım limitleme (s. 3–4): denk. (2) referans ölçekleme; NS için I_max ≤ I1max + I2max (denk. 3) ve kurallar: normalde I1max = 1 pu; V1 + V2 > 1 pu ise I1 ve I2 eşitlenir; < 0.8 pu ise I1max artar, I2max azalır; I1max > 1.5 pu veya I2max < 0 ise sabitlenir. Adalanmışta NS akımı V2'ye göre reaktif olarak veriliyor (VDE-AR-N 4120'ye benzer, ama sabit faktör yerine akım limitleme algoritmasıyla).
- Klasik elemanlar: T32P (denk. 5), T32Q (denk. 6), Z2 (denk. 7 — SEL tipi; **makaledeki formülde payda I2 olması gerekirken payda I1 yazılmış görünüyor, yazım hatası olabilir**), T32I, T32V (denk. 8–9).
- **ΔY2 elemanı (s. 7–8 / 7100–7101):** ΔI2 = I2 − I2m (bir çevrim önceki bellek değeri) (denk. 12), ΔY2 = (I2 − I2m)/(V2 − V2m) (denk. 13). İleri: 0° + φ < arg ΔY2 < 180° + φ (denk. 14); geri: 180° + φ < arg ΔY2 < 360° + φ (denk. 15). |I2|/|I1| kısıtlaması + kilit biti (latch); örnek düzeyinde Δx_k = x_k − x_{k+N} (denk. 16).
- HIL (s. 8 / 7101, Şekil 8): OPAL-RT OP5600, ARTEMiS çözücü, **25 µs** sabit adım; OP5330 analog çıkış → Omicron CMS yükselteç → SEL-411L; açma kontağı OP5353 dijital girişe; DNP3 ile izleme (koruma kararı için haberleşme yok). ΔY2 mantığı SELogic'te dokuz matematik değişkeni (PMV01–PMV09) ile 1 çevrim gecikme oluşturarak yazılmış (Ek B, Şekil 15).
- Ayarlar (s. 9 / 7102): minimum arıza direnci 5 Ω varsayımı; |Y_set| = 1/|Z2| mantığıyla 0.9 pu minimum gerilim için 0.4–0.80 pu aralığı hesaplanmış, **muhafazakâr |Y_set| = 1 pu** (şebekeye bağlı), **0.8 pu** (adalanmış); **kompanzasyon açısı φ = 45°**. Röle içi Z2 için hat açısı 89.85° ve AUTO2 ayarı.

**Ana bulgular**
- Şebekeye bağlı (s. 9–11 / 7102–7104):
  - R2, F2'de BCG (ileri): |ΔY2| = 1.529 pu, arg = −261.6° (≡ 98.4°), PSV05 **2.5 çevrimde** asserted; röle içi Z2 (F32QG, 32QF) de doğru. F3'te BCG (geri): ikisi de açmıyor.
  - R632 / R671, F5'te BCG (metinde "F2" yazıyor fakat şekil başlığı ve Tablo 1 F5 ile tutarlı): R632 |ΔY2| = 1.519 pu, 93.9°, ~2.5 çevrim. R671 BESS'in I2 enjeksiyonuna bağımlı: I2 = 504 A (R632'de 2.9 kA) → **röle içi Z2 başarısız**; ΔY2 doğru: 1.19 pu, −210°, **6 çevrimde** açma.
  - R692, F8: ΔY2 = 1.58, 97.4°; röle içi F32G'den 1 çevrim önce.
  - Tablo 1 (s. 12 / 7105): SLG, 2LG ve 2L arızaları için F1–F9'da tüm rölelerin |ΔY2|, arg ve karar değerleri.
- Adalanmış (s. 11–14 / 7104–7107):
  - Arızalı faz tepe akımı 14.1 kA (bağlı) → 1.4 kA (ada).
  - R2, F2'de BCG: röle içi Z2 = 2.83 > Z2F = −0.94 → **Z2 yanılıyor**; ΔY2 2.5 çevrimde doğru. NS enjeksiyonundaki kontrol dalgalanmaları |ΔY2| ve açısında çukurlar yaratıyor.
  - R671, F5'te BCG: açma anında (2 çevrim) |ΔY2| = 1.141, tepe 1.731 pu; **I2 enjeksiyon dalgalanmaları nedeniyle 3.75 çevrimden sonra 0.8 pu ayarının altına düşüyor** (zaman gecikmeli yedek kullanımını tehlikeye atar). Z2 burada da yanılıyor.
  - R692, F8'de BCG: ΔY2 **1.5 çevrimde** (anlık ayar) doğru; Z2 yanılıyor (bu vakada 50Q1 açmış).
  - Tablo 2 (s. 13 / 7106): adalanmış mod kararları.
- Sonuç (s. 14 / 7107): adalanmışta etkinlik, kontrol sisteminin NS enjeksiyon hızına bağlı; **yüksek empedanslı arızalar ileride incelenmeli**; I2 enjeksiyonunun standartlaşması genel ayar kuralları için gerekli.

**Varsayımlar ve sınırlamalar**
- Doğruluk/hata sayımı yok; Tablo 1–2 kararları listeliyor ama "beklenen vs. gerçek" kolonu yok (okuyucu topolojiden çıkarıyor; görünüşte tutarlı).
- R_f ≥ 5 Ω tek değer; **R_f taraması yok**; HIF açıkça kapsam dışı.
- Eşikler sezgisel (|Y_set| = 1 pu "basitlik için", φ = 45° önceki çalışmadan).
- **Şekilden/tablodan okunan marj gözlemi:** Bazı geri kararlarda açı sınırın çok yakınında, ör. Tablo 2 2LG F9 için R692 arg = 41.5° (sınır 45°), R675 28.9°; bu vakalarda büyüklük çok küçük (≈0.03–0.06) olduğu için büyüklük kriteri de engelliyor. Açı-tabanlı kararın marjı sistematik raporlanmamış.
- Sadece dengesiz arızalar. Frekans makalede açıkça yazmıyor (IEEE 13-bara besleyici 60 Hz sistem; buna göre 1.5–6 çevrim ≈ 25–100 ms).

**Projeyle bağlantı**
- **WP3:** ΔY2 + Z2 (SEL) birlikte, açıkça tanımlı eşiklerle **pasif baseline çifti**. Tablo 1–2 doğrulama referansı.
- **WP4:** Ticari bir rölede (SEL-411L) serbest-biçimli mantıkla 1 çevrim bellekli bir sekans elemanının gerçeklenebildiğini ve 1.5–6 çevrimde karar verdiğini gösteriyor → bizim 16 ms (tek çevrim) hedefimiz bu referansın altında; iddialı ve ayırt edici.
- **WP2:** IEEE 13-bara + BESS (GFL/GFM) + PV yapılandırması ve NS akım limitleme kuralları, Simulink'te yeniden kurulabilir bir dağıtım test vakası.
- Yardımcı sinyalle ilişkisi: Makalenin kendisi "sekans enjeksiyon seviyeleri yön tayini için yeterince büyük olmalı" ve "GFM kontrolü NS katkısını taklit edecek şekilde tasarlanmalı" diyor (s. 11 / 7104) — bu, tasarlanmış NS sinyaline doğrudan bir motivasyon.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★ **Garantili genlik vs. dalgalanan enjeksiyon:** R671 adalanmış vakasında (|ΔY2| 3.75 çevrim sonra eşik altına düşüyor) BESS'in NS enjeksiyonu yerine sabit genlikli tasarlanmış yardımcı sinyal kullanılırsa kararın kalıcılığı ve marjı nasıl değişir? EMT'de aynı vaka.
2. **Açı marjı → konik kısıt:** Tablo 1–2'deki açıların sınırlara uzaklığını hesapla; WP1'de "ölçülen ΔY2 açısı belirsizlik kümesi boyunca ileri konide en az δ marjla kalsın" kısıtını yaz.
3. **SELogic yolu:** Yardımcı-sinyal dedektörünün (ör. bilinen NS sinyaline projeksiyon) aynı SELogic matematik değişkenleriyle ifade edilip edilemeyeceği; WP4'te ticari röle ile edge kart arasında gecikme kıyası.
4. R_f taraması (5–100 Ω) ile ΔY2'nin dependability sınırının çıkarılması — makalenin açıkça bıraktığı boşluk.

**Kilit şekil/tablo/denklemler**
- Şekil 1 (test besleyicisi), denk. (1)–(2) — s. 3 (7096); Şekil 2–3, denk. (3) — s. 4 (7097); denk. (5)–(7), Şekil 4–6 — s. 5–6 (7098–7099).
- **Denk. (12)–(16)** ve sorun özeti — s. 7–8 (7100–7101); **Şekil 7** (ΔY2 röle mantığı), Şekil 8–9, ayarlar — s. 9 (7102).
- Şekil 10–12 — s. 10–11 (7103–7104); **Tablo 1** — s. 12 (7105); **Tablo 2** — s. 13 (7106); Şekil 13–14, sonuç — s. 14 (7107); Tablo 3, Şekil 15 (SELogic kodu) — s. 15 (7108).

---

## B5 — GFM inverterlerle artımlı-büyüklük (IQ) tabanlı mesafe korumasının analizi ve iyileştirilmesi (Johansson, Xing, Taylor, Wang, 2026)

- **Künye:** Henrik Johansson, Qianli Xing, Nathaniel Taylor, Xiongfei Wang, "Analysis and Enhancement of Incremental-Quantity-Based Distance Protection With Grid-Forming Inverters", arXiv:2604.10129v1 [eess.SY], 11 Nisan 2026. 10 sayfa. KTH (Stockholm) + Tsinghua; Hitachi Energy ve İsveç Enerji Ajansı desteği. **Not:** yazar Nathaniel Taylor (KTH), Joshua Taylor değil. Xiongfei Wang B1'in de yazarı.
- **Tek cümlede:** Zaman-alanı artımlı-büyüklük (IQ) mesafe korumasının süperpozisyon (doğrusal kaynak) varsayımını GFM'nin doğrusal olmayan FRT davranışını zamanla değişen kaynak empedansı/iç gerilim olarak modelleyen analitik bir "IQ ağı" ile genişletir; IQ-mesafenin yakın arızalarda quadrilateral mesafeden daha güvenilir ve dış arızalarda daha emniyetli olabildiğini, ama eşik ayarının genellenemediğini gösterir ve eşik yerine "çalışan toplamın ardışık olarak sıfırın üstünde kaldığı süre" (~10 ms) tabanlı yeni bir açma kriteri önerir.

**Problem ve bağlam**
- Sahada IBR'ye bağlı hatlarda Bölge 1'in dış arızada aşırı erişmesi (overreach) ve yakın arızada kaçırması/geç açması gözlenmiş; Bölge 2 salınan görünür empedans nedeniyle düşebiliyor (s. 1).
- Zaman-alanı yöntemler (diferansiyel denklem algoritmaları, IQ tabanlı elemanlar) çözüm olarak savunuluyor; ancak IQ yöntemi saf-arıza ağını süperpozisyonla kurar → **doğrusal kaynak varsayımı**; IBR'ler arızada doğrusal değil. Önceki çalışmalar vaka-özel ve sayısal; genel bir model eksik (s. 1).

**Yöntem / yaklaşım**
- Sistem (s. 2): 66 kV, 300 MW GFM → Δ-Y0 trafo → 220 kV; 50 Hz; 100 km transpoze havai hat (PSCAD frekansa-bağlı faz modeli); uzak kaynak SIR = 0.3, GFM çıkış filtresi SIR = 0.3; röle erişimi hattın %80'i.
- İki GFM (s. 2–3): ikisi de P-f droop güç senkronizasyonu; **GFM1**: 1.2 pu büyüklük doyum (saturation) limitleyici (açı önceliği yok) → güç sistemi açısından adaptif sanal **direnç** gibi davranır; **GFM2**: pozitif/negatif bileşenleri ayrı kontrol eder, adaptif sanal empedans (açısı hattın pozitif-bileşen açısıyla aynı, ağırlıklı endüktif).
- Vakalar (s. 3): yalnız **dengeli ABCG**; m_f ∈ {0.2, 0.45, 0.5, 0.6, 0.7, 0.75, 0.81, 0.9, 0.99}; R_f ∈ {0, 2, 5, 8, 10, 15} Ω; başlangıç açısı 0°; arıza öncesi 1 pu yük → **kaynak başına 54 simülasyon** (GFM1, GFM2, SG).
- IQ-mesafe temelleri (s. 3–4): Δv(t) = v(t) − v(t − pT), T = 20 ms (denk. 1); erişim noktasına kadar artımlı gerilim düşümü (denk. 2); **çalışma büyüklüğü ψ_op = |Δv_s − Δv_m|** (denk. 3); **kısıtlama büyüklüğü ψ_rst = K|v_s(t − pT) − v_m(t − pT)|, K ≥ 1** (denk. 5); çalışan toplam E_x(t) = ∫(ψ_op − ψ_rst)dτ ve ayrık yamuk toplamı (denk. 6–7). Klasik kural: çalışan toplam bir eşiği aşarsa açma.
- **Analitik model (s. 4–6, Şekil 5):** GFM akım limitlemesi ya iç gerilim değişimi Δe_s(t)H(t) ya da kaynak empedansı değişimi ΔR_s(t), ΔL_s(t) olarak modelleniyor; süperpozisyonla "IQ ağı". Kararlı durum çözümleri: ΔI_s (denk. 9), ΔV_s (denk. 10), **ψ_op (denk. 11)**. İdeal doğrusal kaynak + metalik arızada ψ_op,ideal = |−V_f^pre (Z_s + mZ_ℓ)/(Z_s + m_f Z_ℓ)| (denk. 12), ψ_rst = |V_f^pre| (denk. 13); ψ_op > ψ_rst ⇔ m_f < m (iç arıza).
- Faz kayması: ψ_op ile ψ_rst arasında açı farkı varsa çalışan toplama **100 Hz (ikinci harmonik) salınım** biner (s. 6).
- **Önerilen açma kriteri (s. 8):** eşik seviyesi yerine çalışan toplamın **ardışık olarak > 0 kaldığı süre**, "10 ms veya biraz daha uzun" (100 Hz salınımın yarı periyodu 10 ms olduğundan; ψ_op > ψ_rst ise toplam 10 ms'den uzun süre pozitif kalır).

**Ana bulgular**
- Model doğrulaması (s. 6, Şekil 6–7): güçlü kaynakta t = 0'da kaynak empedansı ×5, iç gerilim 1 → 0.33 pu, m_f = 0.2'de 10 Ω arıza; p = 2, 3. dereceden 450 Hz Butterworth alçak geçiren. Kararlı durum analitik ve PSCAD örtüşüyor; Python ile otomatikleştirilmiş "yüzlerce" PSCAD koşusunda denk. (9)–(11) "her zaman mükemmel" eşleşmiş. Δv_s birkaç ms'de, ψ_op ~yarım çevrimde (10 ms) oturuyor; Δi_s'de sönümlü DC ofset var.
- MATLAB parametre taraması (s. 7, Şekil 8): **akım limitleyici ağırlıklı endüktif bir kaynak empedansı değişimi taklit ederse IQ-mesafe daha güvenilir**; doyum limitleyicide (ΔL_s = 0) |I_s| = 1.2 pu'da dokuz vakanın tamamında çalışan toplam aşağı yönlü (açmaz).
- Quadrilateral ile kıyas (s. 7–8, Şekil 9–10): IQ-mesafe yakın arızalarda daha güvenilir, quadrilateral erişim noktasına yakın arızalarda; m_f < 0.2 dirençli arızalarda quadrilateral zorlanıyor. Dış arızada (m_f = 0.81) analitik olarak her zaman ψ_op ≤ ψ_rst (IQ emniyetli); quadrilateral Bölge 1 en az m_f = 0.9'dan itibaren aşırı erişme riski taşıyor, özellikle limitleyici endüktif değilse.
- PSCAD (5 kHz örnekleme, p = 2) (s. 9): **GFM2** ile önerilen kriter R_f = 15 Ω'a kadar m_f = 0.45'te, 10 Ω'a kadar m_f = 0.6'da, 8 Ω'a kadar m_f = 0.75'te güvenilir; m_f ≥ 0.9'daki tüm simüle edilmiş arızalarda emniyetli (quadrilateral çoğunda aşırı erişiyor). GFM2 ile performans SG ile "neredeyse aynı". **GFM1** ile R_f = 8 Ω'a kadar m_f = 0.2'de, 5 Ω'a kadar m_f = 0.7'de güvenilir; m_f ≥ 0.9'da R_f = 2 Ω hariç emniyetli. Şekil 13: GFM1, m_f = 0.5, R_f = 10 Ω'da her iki eleman da yanlış çalışıyor.

**Varsayımlar ve sınırlamalar**
- **Sadece dengeli arızalar**; tek hat, tek GFM, tek SIR değeri (0.3), tek yük (1 pu).
- Analitik model kararlı durum / yarı-statik (quasi-static) — geçici rejim (IQ ağının enerjilenmesi) sırasındaki davranış için garanti vermiyor; makale de ilk enerjilenme anında iç/dış ayrımının zor olduğunu söylüyor (s. 7).
- Önerilen kriterin hızı "10 ms veya biraz daha uzun" — kesin açma süreleri tablo halinde verilmemiş (Şekil 11–13'te görülüyor).
- Gürültü, CVT geçicileri, CT doyması, ölçüm hataları incelenmemiş.
- "Kolay ayarlanır" iddiası iki GFM modeli ve SG ile sınırlı.

**Projeyle bağlantı**
- **WP1 (en önemli bağlantı):** Denk. (8)–(11) GFM'yi **sınırlı belirsizlikli** bir kaynak (ΔZ_s, ΔE_s, R_f, m_f) olarak modelleyen kapalı-form bir harita veriyor. Bu tam da küme-tabanlı tasarımın ihtiyaç duyduğu türden bir model: belirsizlik kümesi üzerinde "ψ_op > ψ_rst marjı" veya yardımcı sinyalin ölçülen yanıtı hesaplanabilir. Makale ayrıca analitik modelin PSCAD ile nasıl doğrulanacağına (Python ile yüzlerce koşu) iyi bir örnek.
- **WP2:** GFM1 (doyum) ve GFM2 (sanal empedans) iki limitleyici tipi, en kötü ve iyi durumu temsil ediyor — EMT'de ikisi de olmalı. Sistem parametreleri (66/220 kV, 300 MW, 100 km, SIR 0.3) yeniden kullanılabilir.
- **WP3:** Zaman-alanı IQ-mesafe + "≥10 ms ardışık pozitif" kriteri, mesafe rölesi bağlamında **güçlü bir pasif baseline**; Kalman dedektörüyle aynı zaman ölçeğinde karşılaştırılabilir.
- **WP4:** 10 ms kriter + 5 kHz örnekleme, tek-çevrim (16–20 ms) bütçeyle uyumlu bir referans.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★ **IQ ağını tasarım aracına taşı:** Denk. (9)–(11)'i, yardımcı sinyal kaynağını da içeren bir ağa genişlet; (ΔZ_s, R_f, m_f) aralıkları üzerinde CVXPY ile en kötü durum marjını hesaplayan bir doğrulayıcı yaz. Ardından aynı vakalarda PSCAD/Simulink ile karşılaştır (makaledeki doğrulama yöntemini kopyala).
2. **Dengeli arıza + NS yardımcı sinyal:** Bu makale dengeli arızaları "en zor" olarak seçiyor; pasif NS elemanları dengeli arızada kördür. B8'e göre NS enjeksiyonunda üç-faz arıza NS ağında Z_f(eq) = R_f olarak görünür → NS yardımcı sinyali dengeli arızayı görebilir. Test: GFM1 ile m_f = 0.5, R_f = 10 Ω (Şekil 13'teki yanlış çalışma vakası) + yardımcı sinyal.
3. **Kriter karşılaştırması:** "≥10 ms ardışık pozitif" kuralı ile yardımcı-sinyal tabanlı karar arasında aynı vaka setinde açma süresi ve hata oranı kıyası (WP3/WP4).
4. Analitik modelin dengesiz arızalara genişletilmesi (makale "unbalanced için de geçerli" diyor ama göstermiyor).

**Kilit şekil/tablo/denklemler**
- Şekil 1–3 (sistem, GFM1, GFM2) — s. 2; vakalar listesi, Şekil 4, **denk. (1)–(5)** — s. 3; denk. (6)–(7) — s. 4.
- **Şekil 5** (doğrusal olmayan FRT modeli), **denk. (8)–(10)** — s. 5; **denk. (11)–(13)**, Şekil 6–7 — s. 6.
- **Şekil 8** (IQ-mesafe güvenilirliği) — s. 7; Şekil 9–10 (quadrilateral), **önerilen kriter** — s. 8; Şekil 11–13 (PSCAD) — s. 9.

---

## B6 — IBR'li sistemlerde iletim hattı koruması: ayar-tabanlı çözümler (Chowdhury, Fischer — SEL, 2021)

- **Künye:** Ritwik Chowdhury, Normann Fischer (Schweitzer Engineering Laboratories), "Transmission Line Protection for Systems With Inverter-Based Resources", SEL teknik makalesi TP6968-01, © 2021, 9 sayfa. Dosya adına göre WPRC 2021 (Western Protective Relay Conference); **PDF'te konferans adı yazmıyor**. Makale, IEEE Trans. Power Delivery'deki "Part I: Problems" makalesinin devamı olarak çözümleri sunuyor (B7'nin kaynakçasında "Part II: Solutions", IEEE TPWRD 36(4), 2021 olarak geçen yayınla içerik olarak örtüşmesi muhtemel).
- **Tek cümlede:** Sandia liderliğindeki, dört üreticinin gerçek firmware'ini içeren kara-kutu EMT modelleriyle üretilmiş 208 arıza vakasında görülen hat koruma sorunlarını, röle ve IBR değiştirmeden yalnızca **ayar değişiklikleriyle** (aşırı akım denetim eşiklerini IBR'nin maksimum akımına göre yükseltmek, mantık blokları ve zamanlayıcılar) güvenli hale getirir; bedeli duyarlılık kaybıdır.

**Problem ve bağlam**
- Part I'de gösterilen sorunlar: IBR'nin enjekte ettiği düşük ve gerilimle "uyumsuz" (incoherent) I2 nedeniyle 32Q'nun yanılması, üç-faz arızada faz yön elemanının güvenlik kaybı, salınan görünür empedansla Bölge 1 aşırı erişmesi ve Bölge 2'nin düşmesi, CVT geçicileri (s. 1–2).
- Çalışma (s. 1, Şekil 1, Tablo I): Sandia liderliğinde dört IBR üreticisinin (OEM1 tip-4 rüzgâr, OEM2 tip-4 rüzgâr, OEM3 tip-3 rüzgâr, OEM4 PV) "gerçek kod" kara-kutu PSCAD modelleri; COMTRADE kayıtları iki röle üreticisinin donanımına oynatılmış. **208 vaka**: 4 arıza tipi (AG, ABG, AB, ABCG), R_F ∈ {0, 5} Ω, 7 konum/olasılık (A–G). 230 kV sistem, 100 MW IBR, 34.5 kV bara SCR = 5.5.

**Yöntem / yaklaşım**
- IBR maksimum akımı (s. 2): IBR'ler akımı 1.10–1.30 pu ile sınırlar. **I_MAX = 1.30·S_IBR/(√3·V_HV·CTR)** (denk. 1).
- **32Q güvenliği:** ileri aşırı akım denetimi **50FP = 1.25·I_MAX** (denk. 2), geri **50RP = 1.00·I_MAX** (denk. 3). Gerekçe: klasik sistemde metalik AB arızada 3I1 = 3I2 = 1.73 pu; bir tip-4 rüzgâr santrali V2 ile uyumsuz 3I2 = 0.50 pu (I_MAX'ın) enjekte ediyor; tip-3 rüzgâr 1.67 pu üretiyor. 1.73 yerine 1.25 seçimi, yeterli ve uyumlu I2 üreten kaynaklarda LL/LLG güvenilirliğini koruyor.
- Eşiklerin yükseltilmesi faz seçimini (FIDS) toprak arızalarında zayıf-besleme düşük gerilim algoritmasına yönlendiriyor (s. 2).
- **Üç-faz arıza mantığı** (Şekil 2): F32P AND NOT F32Q AND I1 < 1.20·I_MAX → faz elemanlarını blokla.
- **Bölge 1 aşırı erişimi:** faz arıza dedektörü **Z50P1 = 2·(1.20·I_MAX)** (denk. 4); CVT geçici bloklama mantığı.
- **Bölge 2 düşmesi:** 6 çevrimlik bırakma (dropout) zamanlayıcısı (Şekil 3).
- Uygulama (s. 3, denk. 5, Tablo II): S_IBR = 100 MVA, 230 kV, CTR = 200 → I_MAX = 1.63 A; 50FP 0.50 → 2.04 A, 50RP 0.25 → 1.63 A, EWFC N → Y, PSV50 = F32P AND (NOT F32Q) AND (LI1FIM < 1.96), Z50P1 0.50 → 3.92 A, CVTBL Y (aktif CVT'de), PCT21DO 6 çevrim.
- Ayrıca (s. 6–8): çoklu IBR santrallerinde I_MAX'ın hat başına hesaplanması (I_MAX-TLBC = 1.36 A, I_MAX-TLAB = 1.90 A; denk. 6–7), düşük gerilim yedeği (27D), haberleşmeli şemalar (POTT vb.) ve sıfır-bileşen karşılıklı kuplajı.

**Ana bulgular**
- Tip-4 rüzgâr dış ABG (s. 3, Şekil 4): elemanlar emniyetli; I2 düşük ve tahmin edilemez olduğu için 32Q artırılmış eşik nedeniyle devreye girmiyor, 32V doğru yönü veriyor.
- Tip-3 rüzgâr (s. 3, Şekil 5–7): daha yüksek I2 sayesinde 32Q doğru; LG arızasında I2 = 90 A primer (3I2 = 1.35 A sekonder) < 1.63 A → röle 32V'ye düşüyor (3I0 = 6.5 A sekonder).
- PV + aktif ferrorezonans bastırmalı CVT: Bölge 1 aşırı erişmesi CVT geçici bloklamasıyla önleniyor (s. 3, Şekil 8).
- **Toplam (s. 6, Tablo III–IV):** "yanlış çalışma yok" (security tam). R1 (zayıf IBR ucu) için yön elemanı (32) D ve G konumlarında **%56**, 21Z2 D ve G'de **%38**; diğer tüm hücreler %100; 87L her yerde %100. R2 (güçlü uç) her yerde %100.
- **Duyarlılık bedeli (Ek, s. 9, Şekil 12):** denetim eşiği 0.5 A'dan ~2 A'ya çıkınca sekans yön elemanlarının toprak arızası direnci kapsamı **~400 Ω'dan ~100 Ω'a** düşüyor (yazarlar 100 Ω'u çoğu uygulama için yeterli buluyor).
- Haberleşmesiz beklenen açma süreleri (s. 7, Tablo V): IBR radyal bağlıyken zayıf uçta LL/LLG "0 s veya 27D (IBR'ye bağlı)", 3P'de 27D; düşük gerilim yedeğiyle yerel açma **1.0–1.5 s**. Z2D örneği 0.3 s. Haberleşmeyle (Tablo VI) çoğu 0 s.

**Varsayımlar ve sınırlamalar**
- Çözüm, IBR'nin kötü davranışını "görmezden gelerek" emniyet sağlıyor: zayıf uçta güvenilirlik (dependability) IBR'nin ürettiği I2'ye bağlı kalıyor (LL/LLG), 3P'de kör (27D'ye kalıyor).
- Sadece 2 R_F değeri (0, 5 Ω); tek IBR santrali; GFM yok.
- Ayarlar belirli SEL röle ailesine özgü (ORDER, EWFC, PSV50 vb.); ilkeler genel ama birebir taşınabilir değil.
- Endüstriyel makale: istatistiksel detay sınırlı (yüzde tabloları), model ayrıntıları Part I'de.

**Projeyle bağlantı**
- **Endüstrinin bugünkü cevabı:** "Ayarları IBR'nin maksimum akımına göre koy, emniyeti koru, duyarlılıktan vazgeç." Yardımcı sinyalin akademik iddiası, bu ödünleşimi (security vs. sensitivity) **kırabilmesi** olmalı.
- **WP3:** Tablo II ayarlarıyla "SEL-tarzı ayarlanmış 32Q/21" **pratisyen baseline**'ı olarak uygulanmalı (eşik formülleri açık: denk. 1–4).
- **WP1 (uyum kısıtı):** Yardımcı sinyal normal işletmede mevcut rölelerin NS denetim eşiklerini (50FP/50QF benzeri, ve tipik I2/I1 kısıtlama faktörleri) tetiklememeli → sinyal genliğine üst sınır kısıtı.
- **WP2:** 208 vakalık senaryo yapısı (OEM tipi × arıza tipi × R_F × konum) senaryo matrisi için iyi bir şablon.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★ **Ödünleşimi kırmak:** 50FP düşük (duyarlı, ör. 0.5 A) bırakılıp 32Q yön kararının yardımcı sinyalle doğrulanması güvenliği korur mu? Test: Şekil 12'deki R_F kapsamı (~400 Ω vs ~100 Ω) yardımcı sinyalli eleman için yeniden hesaplansın.
2. **Zayıf uç 3P körlüğü:** Tablo V'te 3P için tek seçenek 27D (1.0–1.5 s). NS yardımcı sinyali dengeli arızada NS ağında R_f'yi görür (B8) → zayıf uçta 3P arızasının saniyeler yerine çevrimler içinde tespiti mümkün mü?
3. **Birlikte var olma (bizim hipotezimiz, makalede test edilmemiş):** Sürekli bir NS yardımcı sinyali IBR ucundaki 32Q'ya "geri yönde NS kaynağı" gibi, **uzak uçtaki** 32Q'ya ise "ileri yönde NS kaynağı" gibi görünebilir; genlik 50QF/50FP ve I2/I1 kısıtlamasının altında kalmazsa uzak uçta yanlış ileri karar riski. EMT'de iki uçlu röle modeliyle kontrol edilmeli.

**Kilit şekil/tablo/denklemler**
- Şekil 1 ve Tablo I (çalışma sistemi, 208 vaka) — s. 1; **denk. (1)–(4)**, Şekil 2–3 — s. 2; denk. (5), **Tablo II** (ayarlar) — s. 3.
- Şekil 4–5 — s. 4; Şekil 6–7 — s. 5; **Tablo III–IV** (performans), Şekil 9 — s. 6; denk. (6)–(7), Şekil 10, Tablo V — s. 7; Tablo VI–VII, sonuç — s. 8; **Şekil 12** (R_F kapsamı vs 50FP) — s. 9.

---

## B7 — IBR'li sistemlerde hat akım diferansiyel (87L) koruması (Chowdhury, McDaniel, Fischer — SEL, 2022)

- **Künye:** Ritwik Chowdhury, Ryan McDaniel, Normann Fischer (SEL), "Line Current Differential Protection in Systems With Inverter-Based Resources—Challenges and Solutions". İlk sunum: 49. Western Protective Relay Conference, Ekim 2022; sonra 76. CPRE (Mart 2023) ve 76. Georgia Tech Protective Relaying Conference (Mayıs 2023). SEL TP7071-01. PDF 10 sayfa (kapak + 9 basılı sayfa).
- **Tek cümlede:** IBR'li sistemlerde de "mükemmel bir seçim" olan 87L'nin iki yeni sorununu — zayıf IBR kaynağı nedeniyle sağlam fazlardaki akım değişiminin dış-arıza dedektörünü (87EFD) tetikleyip iç arızada açmayı >1 s geciktirmesi ve IBR harmoniklerinin hassas 87LQ'yu arızasız açtırması — saha olayı ve simülasyonla gösterir; hata bütçesine dayalı ayar kılavuzu ve faz-ayrık 87EFD önerir.

**Problem ve bağlam**
- 87L, güç salınımı, yük tecavüzü, hat parametre belirsizliği, karşılıklı kuplaj gibi mesafe sorunlarına bağışık; karşılığında **güvenilir bir haberleşme kanalı gerektirir ve uzak yedek sağlamaz** (s. 2 / basılı s. 1).
- Alfa düzlemi (87AP): yerel/uzak akım oranı I_L/I_R düzleminde yarıçap ve açı ayarlarıyla bir kısıtlama bölgesi; kanal asimetrisi açı hatası, CT doyması hem genlik hem açı hatası yaratır (Şekil 2–3, Tablo I).
- Alt elemanlar: 87LP (faz), 87LG (sıfır-bileşen), 87LQ (negatif-bileşen) (s. 2). Varsayılan ayarlar (Tablo II, s. 3): pickup 87LP 1.20 pu, 87LG ve 87LQ 0.25 pu; yarıçap 6; açı 195° (≈87PCT %90 eğim — güvenliğe çok yatkın).

**Yöntem / yaklaşım**
- Kanal asimetrisi → açı: **Açı = Asimetri·Frekans·360°** (denk. 1); 5 ms asimetri 60 Hz'de 108° (s. 4 / basılı s. 3). Tipik kanallarda asimetri < 2 ms, nadiren 5 ms.
- CT doyması çalışması (s. 5 / basılı s. 4): 500 kV sistem, hat 1–200 km, X/R ≤ 100, tek CT doyuruluyor, %80'e kadar remanans, 5° nokta-dalga adımları; sonuç Şekil 8: gerekli yarıçap/açı toplam boyutlandırma faktörü K_TOT'un fonksiyonu; 87AP için gerekli K_TOT = 4, 87EFD'li rölede güvenlik için minimum K_TOT = 2.
- Ayar kılavuzu (s. 6 / basılı s. 5, Tablo III–IV):
  - Hassas mod (87EFD = 0): 87LP 0.30 pu, 87LG 0.20 pu, 87LQ **1.25 pu (denk. 2)**; yarıçap 1.35; açı 90°.
  - Emniyetli mod (87EFD = 1): 87LP 0.75 pu, 87LG 0.30 pu, 87LQ **1.63 pu (denk. 3)**; yarıçap 5.00; açı 170°.
  - **87LQP_SENS = 1.25·S_IBR/(√3·V_HV·(CTR·I_NOM)) pu** (denk. 2), **87LQP_SECURE = 1.30·87LQP_SENS** (denk. 3) — amaç IBR'nin "kötü" NS akımını görmezden gelmek.
- Röle tasarımı (s. 7 / basılı s. 6): 87EFD'yi faz-ayrık yapmak (pakette 1 yerine 3 bit; 64 kbps kanalda mümkün).

**Ana bulgular**
- **Güvenilirlik sorunu (s. 4 / basılı s. 3, Şekil 6):** ~1,700 MVA tip-4 rüzgâr santrali yakınında (EPRI simülasyonu) 15 Ω AG iç arıza: arızalı olmayan B ve C fazlarındaki büyük akım değişimi 87EFD'yi tetikliyor → röle emniyetli moda geçiyor → **87L >1 s açmayabiliyor**. Nedeni: IBR zayıf pozitif/negatif kaynak, trafosu ise düşük empedanslı sıfır-bileşen yolu.
- **Güvenlik sorunu (s. 4–5 / basılı s. 3–4, Şekil 7):** Ağustos 2019, 184 MVA tip-3 rüzgâr santrali yakınında 0.2 mil, 138 kV hat: 87LQ minimum ayar 0.10 pu ile **arıza yokken açtı**; neden: aşırı akım harmonikleri sahte NS diferansiyel akımı üretti.
- İyileştirilmiş ayarlarla (s. 7 / basılı s. 6, Şekil 11): 1700 MVA, 500 kV, CTR 400, I_NOM 5 A → 87LQ 1.23 / 1.60 pu; 87EFD assert olsa da 87LP, 87LG, 87LQ açıyor (87LQ gecikmeli — IBR'nin uyumsuz NS akımı). Saha olayı için 184 MVA, 138 kV → 0.48 / 0.63 pu; 0.48 pu bu olay için yeterli güvenlik sağlıyor.
- 87AP vs 87PCT (s. 8 / basılı s. 7, Şekil 12–13): 230 kV, 50 km hat, zayıf uç SIR1 = 5, SIR0 = 0.5; 87PCT eşdeğer %40 eğim. 87AP daha duyarlı ve kanal asimetrisi arttıkça duyarlılığı 87PCT kadar düşmüyor.
- CT örneği (s. 8–9 / basılı s. 7–8): 138 kV, 20 km bağlantı hattı, CTR 200, R_CT 0.5 Ω, R_B 1 Ω: V_SAT CT1 = 150 V, CT2/CT3 = 300 V; C400 seçiminde K_TOT 12 ve 6 → yarıçap 5, açı 170°; C800'de K_TOT 11.33 → yarıçap 4.6, açı 150°.

**Varsayımlar ve sınırlamalar**
- Haberleşme kanalı şart; kanal kaybında yedek gerekir.
- Güvenlik çözümü 87LQ'yu **duyarsızlaştırarak** (IBR derecesine göre) sağlanıyor — NS bilgisinden kısmen vazgeçiş.
- Kanıt tek simülasyon olayı + tek saha olayı + parametrik CT çalışması; istatistiksel kapsam yok.
- Ürün-özel (SEL 87AP/87EFD).

**Projeyle bağlantı**
- **Referans tavan:** 87L haberleşmeli "altın standart". Proje (varsayılan olarak tek uçlu, haberleşmesiz yardımcı-sinyal tespiti) sonuçlarını "haberleşme olmadan 87L'ye ne kadar yaklaşıyoruz" diye çerçevelemeli.
- **WP3/WP4 dersi:** IBR harmonikleri gerçek sahada sahte NS büyüklükleri üretiyor. Röle tarafındaki NS çıkarımı (fazör filtresi, Kalman, öğrenen dedektör) **harmonik içeriğe dayanıklı** olmalı; yardımcı sinyal tespiti harmonik bozulma altında yanlış alarm üretmemeli.
- **WP1:** Hata bütçesi mantığı (asimetri → açı, CT doyması → yarıçap, her birine marj) küme-tabanlı tasarımda "ölçüm belirsizlik kümesi"ni kurmak için iyi bir sezgi kaynağı.
- **Doğrudan baseline değil** (haberleşmeli, farklı sınıf), ama karşılaştırma tablosunda yer almalı.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★ **Harmonik dayanıklılık testi:** Saha olayındaki gibi harmonik içerikli akım/gerilimlerde (EMT'de zayıf şebeke veya açık-faz koşulu) yardımcı-sinyal dedektörünün yanlış alarm oranı; dedektörün harmonikleri bastıran ön filtre gereksinimi ve bunun gecikme bütçesine maliyeti (WP4).
2. **87LQ ile birlikte var olma:** IBR'nin enjekte ettiği NS yardımcı sinyali hat boyunca geçen akımdır (through current) → ideal olarak 87LQ'da diferansiyel üretmez; ancak kanal asimetrisi/CT hatalarıyla çarpılınca sahte diferansiyel oluşur mu? Basit hesap: sinyal genliği × (asimetri açı hatası) < 87LQ pickup.
3. Faz-ayrık 87EFD fikrinin tek uçlu yardımcı-sinyal yaklaşımında karşılığı: arızalı olmayan fazlardaki değişimlerin (zayıf kaynak) tespit mantığını bozmaması.

**Kilit şekil/tablo/denklemler**
- Şekil 1–2, Tablo I (hata kaynakları) — s. 2; Şekil 3 (alfa düzlemi), **Tablo II**, Şekil 4 — s. 3; Şekil 5, **denk. (1)**, **Şekil 6** (güvenilirlik sorunu) — s. 4.
- **Şekil 7** (87LQ saha yanlış açması), Şekil 8 (K_TOT) — s. 5; Şekil 9, **Tablo III–IV**, **denk. (2)–(3)** — s. 6; Şekil 10–11 — s. 7; Şekil 12–14 — s. 8; denk. (4)–(6), sonuç — s. 9. (PDF sayfaları.)

---

## B8 — Negatif-bileşen akım enjeksiyonu (NSCI) tabanlı aktif koruma (Yang, Dyśko, Egea-Àlvarez, IJEPES 2024) — **en yakın öncül**

- **Künye:** Zhenkun Yang, Adam Dyśko, Agustí Egea-Àlvarez (University of Strathclyde), "A negative sequence current injection (NSCI)-based active protection scheme for islanded microgrids", *International Journal of Electrical Power and Energy Systems* 158 (2024) 109965, DOI 10.1016/j.ijepes.2024.109965. 12 sayfa. Açık erişim (CC BY-NC-ND).
- **Tek cümlede:** Adalanmış bir mikroşebekede arıza tespit edildikten sonra **tek bir adanmış inverterin** 80 ms boyunca 0.3 pu genlikli, açısı arıza öncesi NS akımına kilitli bir negatif-bileşen akımı enjekte ettiği, her rölenin bu enjeksiyonun yarattığı NS akım artışının reel kısmının işaretinden (veya dengeli arızada büyüklüğünden) arızanın hangi tarafta olduğunu haberleşmesiz belirlediği ve zaman kademeli açtığı bir aktif koruma şeması önerir.

**Problem ve bağlam**
- Adalanmış mikroşebekede çok kaynaklı, belirsiz yönlü arıza akımı → aşırı akım koordinasyonu zor; diferansiyel/gezici dalga pahalı (haberleşme, yüksek örnekleme); adaptif ve yapay zekâ yöntemleri ağ bilgisi/veri ister (s. 1).
- Aktif koruma literatürü (s. 1–2): ara-harmonik enjeksiyonlu diferansiyel (haberleşme gerekli), 5. harmonik enjeksiyonu (sadece tespit, bölüm tanımlama yok), tüm DG'lerin farklı harmonik enjekte etmesi, sentetik harmonik (haberleşme gerekli; bkz. B9), gezici dalga enjeksiyonu (her ölçüm noktası enjeksiyondan >30 km). Yazarlara göre **koruma amacıyla aktif NS akım enjeksiyonu kullanan yayınlanmış yöntem yok** (s. 2).
- Kapsam: yalnızca adalanmış mod; şebekeye bağlı modda klasik pasif yöntemlerin yeterli olduğu varsayılıyor (s. 2).

**Yöntem / yaklaşım**
- Test mikroşebekesi (s. 3, Şekil 1, Tablo 1): 5 bara, 11 kV, 50 Hz; her DG 10 MVA; filtre 0.242 + j2.42 Ω; DG referansları 5 MW (bara 1, 2, 4), 10 MW (bara 3); hatlar 0.1 + j0.1 Ω/km, 2.5 km; her barada 5 MW yük. VSC1 gerilim-kontrollü (GFM), diğerleri akım-kontrollü; **VSC3 adanmış NSCI kaynağı**.
- Akış (s. 2–3, Şekil 2):
  1. **Arıza tespiti** (her röle bağımsız): V1 < 0.95 pu **veya** V2/V1 > 0.05 (ANSI C84.1'e göre; 5 MW'a kadar yük anahtarlamasına karşı emniyet).
  2. **Arıza tipi ayrımı:** I2max > I2th = 0.2·I2min = 0.2·N21·V_LL/(√3·Z_line,max) (denk. 1; N21 = 0.05; %80 duyarlılık marjı).
  3. **Akım açısı seçimi (CAS):** Δθ2(CAS) = |θ2Rpre − θ2Vpre| (denk. 2); > 90° → arıza sağda.
  4. **NSCI:** enjeksiyon; her röle ΔI2 = I2gen − I2pre (denk. 3) hesaplar; **FDI = |ΔI2| (dengeli), Re{ΔI2} (dengesiz)** (denk. 4).
  5. **Zaman kademeli açma** (Tablo 2, s. 4): sol taraf CB'ler bara 2/3/4 için 0.05/0.2/0.35 s; sağ taraf bara 1/2/3/4 için 0.5/0.35/0.2/0.05 s.
- NSCI kontrolü (s. 4–5, Şekil 4–5): arıza 0.05 s'de; ~3 ms tespit gecikmesi; pozitif-bileşen akımı ~20 ms'de sıfıra rampalanır; **40 ms bekleme** (arıza akımı otursun, "pre-injection" fazörleri ölçülsün); sonra **80 ms trapez zarflı, 0.3 pu genlikli** NS akımı. Açı kontrolü (denk. 5): θ2inj = (θ2gref − θg)(k_p + k_i/s) eğer I2 > I2th, aksi halde 0; dengeli arızada açı kontrolü kapalı. Kutupsal → kartezyen: I_d2ref = I2inj·cos θ2inj, I_q2ref = I2inj·sin θ2inj (denk. 6–7).
- Ayar teorisi (s. 5–6, Şekil 6): NS ağında eşdeğer arıza empedansı **Z_f(eq) = R_f (üç-faz dengeli)**, > R_f (LL, LLG), > 3R_f (SLG). Akım bölücü:
  - Kaynak-arıza yolunun (SFP) içinde: **ΔI2(in) = I2inj·Z_n/(Z_m‖Z_f(eq) + Z_n)** (denk. 8)
  - Dışında: **ΔI2(out) = I2inj·(Z_n‖Z_f(eq))/(Z_m + Z_n‖Z_f(eq))** (denk. 9)
  - R_f → ∞'da ikisi de **C = I2inj·Z_n/(Z_m + Z_n)**'ye yakınsar (denk. 10). Z_m, Z_n: ölçüm noktasının iki yanındaki toplam yük empedansları.
- Eşikler (s. 6–7, Tablo 3): dengeli: |ΔI2| > C → SFP içi; dengesiz: **Re{ΔI2} > 0.2C** (yük dağılımı belirsizliğine karşı %80 marj); enjeksiyon barasında CAS 90°. Dengesiz arızada SFP dışında Re{ΔI2} negatif ve −C'ye yakınsadığından ayrım marjı büyük.

**Ana bulgular**
- **Maksimum tespit edilebilir arıza direnci** (s. 8, Tablo 5; 5 yük vakası × 4 arıza tipi × 4 hat): en yüksek **~18.8 Ω** (dengeli), en düşük **~3.8 Ω** (B-toprak). Vaka 1 (eşit yük) örneği: dengeli 13.1/15.5/17.2/16.7 Ω, B-toprak 3.9/5.9/6.6/6.2 Ω, BC-toprak 8.0/8.9/10.2/9.8 Ω, B-C 9.0/11.9/13.1/12.4 Ω (hat 1–4). Yük aktif/reaktif güç dağılımı Rfmax'ı belirgin etkilemiyor. Hat 1 (en güçlü kaynak VSC1'e yakın) en düşük Rfmax — düşük gerilim dedektörü orada daha az etkili.
- **FDI ayrımı** (s. 8–9, Şekil 9–10): dengesiz arızada SFP dışında FDI daima negatif → büyük marj, yük dağılımından etkilenmiyor. **Dengeli arızada marj R_f ile daralıyor**: Vaka 2'de bara 3 sağ FDI R_f = 17 Ω'da eşiğe (C) ulaşıyor; Vaka 3'te bara 4 sol R_f ≈ 13 Ω'da.
- **Senkron jeneratör** (s. 9–10, Şekil 11): VSC1 yerine SG; C azalıyor, dengeli HIF'lerde (> 4 Ω) performans etkileniyor; dengesiz arızalarda 30 MW'a kadar (toplam yükün 1.2 katı) SG ile doğru yön.
- **Daha büyük ağ** (s. 10–11, Şekil 12–13, Tablo 7): değiştirilmiş IEEE 13-bara (1 km hatlar, VSC6 gerilim-kontrollü, VSC8 adanmış DG): ölçüm noktası SFP içindeyken FDI eşik üstünde, dışındayken altında.
- Kendi belirttikleri sınırlamalar (s. 9–10): ağır tek-faz yük bozucusunda gerilim-tabanlı tespit yanılabilir; büyük ağda yüksek dirençli arıza görülmeyebilir; enjeksiyon sürecinden kaynaklı **uzun çalışma süresi**. Büyük ağ için öneriler: ağı bölgelere ayırıp her bölgeye bir aktif DG; uzak baraları gruplamak (s. 10).

**Varsayımlar ve sınırlamalar**
- **Hız:** arıza → tespit (~3 ms) → rampa (~20 ms) → bekleme (40 ms) → enjeksiyon (80 ms): FDI ancak arızadan **≈140 ms** sonra hazır (metindeki sürelerin toplamı; FDI'nin enjeksiyon penceresinin hangi anında hesaplandığı tam belirtilmemiş), üstüne 0.05–0.5 s zaman kademesi. Bizim 16 ms hedefimizin çok ötesinde.
- **Tetiklemeli:** önce pasif bir dedektörün (V1 < 0.95 veya V2/V1 > 0.05) arızayı görmesi gerekiyor → Rfmax sınırları büyük ölçüde bu dedektörden kaynaklanıyor (makale de belirtiyor, s. 7).
- **Tasarım elle:** 0.3 pu genlik, 80 ms süre, trapez zarf, 0.2C eşiği ve %80 marj sezgisel; optimizasyon veya garanti yok.
- Akım bölücü analizi süperpozisyon varsayımına dayanıyor: **"enjeksiyonla aynı anda NS akım artışı üreten başka kaynak yok"** (s. 5). IEEE 2800 benzeri NS enjekte eden diğer IBR'ler bu varsayımı bozar.
- Enjeksiyon sırasında aktif DG'nin pozitif-bileşen akımı sıfıra çekiliyor — FRT gereklilikleriyle çatışabilir (makalede tartışılmamış).
- Simülasyon aracı belirtilmemiş; HIL ileride yapılacak (s. 11). Gürültü, ölçüm hatası, harmonik yok.
- Sadece adalanmış mod.

**Projeyle bağlantı**
- **Fikir olarak en yakın akraba:** aynı fiziksel mekanizma (bir inverterden NS akımı enjekte et, ölçülen NS yanıtıyla arızayı ayır), haberleşmesiz. Taylor çizgisinin bu çalışmaya göre konumlanması gereken eksenler: (i) **optimizasyonla tasarım** (genlik/faz/zaman şekli), (ii) **küme-tabanlı garanti** (0.2C + %80 marj gibi sezgisel marj yerine), (iii) **hız** (≈140 ms + kademe yerine tek çevrim), (iv) **mesafe rölesiyle uyum** (burada yönlü bölüm tanımlama + zaman kademesi var).
- **WP1:** Denk. (8)–(10) kapalı-form ve doğrusal (fazörlerde) → CVXPY tasarım aracının ilk **birim testi** için mükemmel: Z_m, Z_n, R_f aralıkları üzerinde Re{ΔI2} marjını hesapla ve 0.2C kuralıyla kıyasla.
- **WP2:** Şekil 5 NSCI kontrol blok diyagramı (rampa, trapez, açı PI, kutupsal→kartezyen) Simulink'te yeniden kurulabilecek kadar ayrıntılı; Tablo 1 parametreleri ile 5-bara ada mikroşebekesi kurulabilir. **Yeniden gerçeklenmesi gereken bir baseline.**
- **WP3:** FDI kuralı (Re{ΔI2} işareti) basit bir aktif-dedektör baseline'ı.
- **WP4:** Zaman çizelgesi (Şekil 4) bize "aktif ama yavaş" referans noktası veriyor.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★★ **NSCI'yi optimizasyon problemi olarak yeniden yaz:** Karar değişkenleri: NS genlik, faz, (ayrık zamanlı) zarf; kısıtlar: akım limiti (I1 + I2 ≤ I_max tipi), Z_m/Z_n (yük) ve R_f belirsizlik kümeleri üzerinde SFP içi/dışı Re{ΔI2} ayrım marjı ≥ δ; amaç: minimum enjeksiyon enerjisi veya minimum süre. Yang'ın elle seçtiği nokta (0.3 pu, 80 ms) bu problemin bir uygun (feasible) noktası mı, ne kadar optimal-dışı? Bu, projenin "neden optimizasyon?" sorusuna en doğrudan cevabı olur.
2. **Sürekli vs. tetiklemeli:** Küçük, sürekli bir sinyal (normal işletmede de var) ile Yang'ın tetiklemeli büyük sinyali arasında hız/enerji/uyum ödünleşimi. Sürekli sinyal pasif tespit aşamasını (ve onun Rfmax sınırını) ortadan kaldırabilir mi?
3. **Çoklu NS kaynağı:** Aynı mikroşebekede IEEE 2800 benzeri K·V2 enjeksiyonu yapan başka IBR'ler varken FDI ve akım bölücü analizinin bozulup bozulmadığı (EMT).
4. **Dengeli arıza marjı:** Dengeli arızada |ΔI2| ile C'nin yakınsaması (Vaka 2'de R_f = 17 Ω'da marj sıfır) — tasarlanmış faz/zaman şekli bu marjı genişletebilir mi?

**Kilit şekil/tablo/denklemler**
- **Denk. (1)** (tip ayrımı eşiği) — s. 2; Şekil 1–2, Tablo 1, **denk. (2)–(4)** (CAS, ΔI2, FDI) — s. 3; Şekil 3, Tablo 2 (zaman kademesi), **Şekil 4** (NSCI zaman çizelgesi) — s. 4.
- **Şekil 5** (NSCI kontrol algoritması), **denk. (5)–(7)**, **Şekil 6** (eşdeğer devre) — s. 5; **denk. (8)–(10)** (akım bölücü), Şekil 7 (açma mantığı) — s. 6; Şekil 8, Tablo 3–4 — s. 7.
- **Tablo 5** (Rfmax), Şekil 9 — s. 8; Şekil 10 — s. 9; Şekil 11, Tablo 6 (karşılaştırma), büyük ağ — s. 10; Şekil 12, Tablo 7, sonuç — s. 11; Şekil 13 — s. 12.

---

## B9 — Ada mikroşebekelerde SVM ve sentetik harmonik enjeksiyonu ile arıza akımı yönü (Mohammadhassani, Mehrizi-Sani, Saleh, 2021)

- **Künye:** Ardavan Mohammadhassani, Ali Mehrizi-Sani (Virginia Tech), Khaled Saleh (CanmetENERGY, Natural Resources Canada), "Fault Current Directionality in Islanded Microgrids Using SVM and Synthetic Harmonic Injection", IEEE konferans bildirisi, 2021 (ISBN 978-1-7281-9023-5; **konferans adı PDF'te yazmıyor**). 5 sayfa. NSF ve CCI desteği.
- **Tek cümlede:** IBR'lerin gerilim 0.88 pu altına düşünce 3./5./7. harmonik "desenleri" enjekte ettiği önceki bir yöntemin kosinüs-benzerliği tabanlı (ve haberleşmeli) yön kararını, her röle için eğitilen doğrusal bir destek vektör makinesiyle (SVM) değiştirerek dengeli arızalarda yerel (haberleşmesiz) yön tayini yapmayı önerir.

**Problem ve bağlam**
- Ada IBR mikroşebekelerinde arıza akımı küçük; tork/empedans tabanlı yön röleleri bozuk fazör kestirimi nedeniyle başarısız; mesafe kısa hatlarda önerilmiyor; diferansiyel her hat için pahalı (s. 1).
- Temel aldıkları yöntem [6] (Saleh vd., IEEE TPWRD): IBR'ler arızada sentetik harmonik deseni enjekte eder; röle ölçülen deseni (MP) önceden hesaplanmış karakteristik desenle (CP) kosinüs benzerliğiyle karşılaştırır; λ = 0.85; birincil koruma POTT, yedek DZI — **haberleşme gerekli**; 15 çevrimde temizlenmezse tüm IBR'ler düşük gerilimle açar (s. 2–3).

**Yöntem / yaklaşım**
- Harmonik enjeksiyonu (s. 2): i_inj^h = Î_inj^h·sin(hωt + θ), h = 3, 5, 7 (denk. 1); toplam rms akımı nominalin %120'siyle sınırlamak için **Î_inj^h = 0.38·I_DG^rated** (denk. 2); faz kayması hθ yerine θ → 3. ve 5. harmonikler pozitif-bileşen olur. Tetik: IBR terminal gerilimi < 0.88 pu (IEEE 1547-2018 LVRT). PR (proportional-resonant) kontrolcüler (denk. 3).
- Özgün mantık (s. 2): cos θ = ⟨MP, CP⟩/(‖MP‖‖CP‖) (denk. 4) ≥ λ.
- **Önerilen (s. 3–4):** her röle için doğrusal çekirdekli SVM (MATLAB `fitcsvm`), denk. (5)–(7). Özellikler: pozitif-bileşen akımındaki üç harmoniğin genlikleri, tespitten sonra **bir çevrim** boyunca 30 µs aralıkla örneklenmiş (60 Hz'de 10⁶/(30×60) = 556 örnek/arıza).
- Eğitim (s. 4): ileri örnekler: hat 9-10 ortasında metalik üç-faz arıza; geri örnekler: R910 için hat 9-8, R109 için hat 11-10 ortasında; giriş X ∈ ℝ^{1121×3} (556 × 2 = 1112 olması beklenirdi; makaledeki 1121 küçük bir **tutarsızlık**). Tablo I: hangi IBR'nin hangi harmoniği enjekte ettiği ([6]'daki optimizasyondan).
- Test sistemi: CIGRE 12.47 kV benchmark dağıtım ağı, ada modunda, gözlü (3 alt anahtar kapalı), PSCAD/EMTDC (s. 3, Şekil 3).

**Ana bulgular**
- Eğitim verisi doğrusal ayrılabilir (Şekil 4, s. 4). Tablo II: doğrusal SVM katsayıları (R910: β = [−0.0845, 2.4394, 0.1618], b = −1.4340; R109: β = [0.0793, −0.1904, 0.0146], b = 1.0172) (s. 5).
- **Doğrulama — tek arıza:** hat 8-3 ortasında metalik dengeli arıza (s. 4–5, Şekil 5, Tablo III): R910 doğru yön geri, **örnek bazında %100**; R109 doğru yön ileri, **%88**. Kosinüs benzerliği: R910'da %91 (> 0.85 → yanlışlıkla ileri), R109'da %98 (doğru).

**Varsayımlar ve sınırlamalar**
- **Çok küçük veri:** eğitim için röle başına yalnızca 2 arıza (1 ileri + 1 geri), test için **tek arıza**; R_f, yük, IBR durumu, topoloji varyasyonu yok. "Doğruluk" tek olayın 556 örneği üzerinden **örnek-bazlı**; olay-bazlı karar kuralı (ör. çoğunluk oyu) tanımlanmamış.
- **Şekilden okunan gözlem:** Şekil 5'te yeni (test) verinin eğitim kümelerinden uzakta, orijine yakın düşük harmonik genliklerinde toplandığı görülüyor → karar esasen **dağılım-dışı (out-of-distribution) ekstrapolasyon**.
- Sadece dengeli arızalar.
- Enjeksiyon büyük: harmonik başına 0.38 pu; ve arıza tespitinden (gerilim < 0.88 pu) sonra tetikleniyor.
- SVM'in "daha iyi genelleme" ve "ANN örnekleme aralığında zor çalışır" iddiaları kanıtlanmamış.

**Projeyle bağlantı**
- **WP3 (öğrenen dedektör) için ders:** Değerlendirme protokolü nasıl **olmamalı** örneği. Bizim öğrenen dedektörlerimiz için: eğitim/test ayrımı konum, R_f, yük, inverter kontrol tipi (G1C/G2C/GFM) ve topolojiye göre yapılmalı; olay-bazlı metrik (doğru karar oranı, karar süresi) ve dağılım-dışı test raporlanmalı.
- **Aktif enjeksiyonun alternatif bir biçimi:** farklı frekanslarda (harmonik) enjeksiyon, temel frekansta NS enjeksiyonuyla (B8, Taylor) kıyaslanabilir: harmonikler temel-frekans fazörlerinden ayrılması kolay ama akım bütçesinin büyük kısmını yiyor (0.38 pu/harmonik).
- **WP4:** Bir çevrimlik özellik penceresi ve 30 µs örnekleme, hesaplama yükü için referans.

**Buradan çıkan açık sorular / araştırma fikirleri**
1. ★ **Garantili vs. öğrenilmiş ayrıştırıcı, dağılım-dışı testte:** Aynı yardımcı-sinyal yanıt özellikleri üzerinde (ör. ölçülen NS yanıtının bilinen sinyale projeksiyonu) bir SVM/küçük sinir ağı eğit ve küme-tabanlı (garantili) ayrıştırıcıyla, eğitimde görülmemiş konum ve R_f'lerde karşılaştır. Beklenti: garantili yöntem model kümesi içinde hatasız, öğrenilmiş yöntem dışarıda bozuluyor — bunu sayısal göstermek WP3'ün güçlü bir sonucu olur.
2. Harmonik desen ile NS yardımcı sinyalinin **akım bütçesi ve tespit süresi** kıyası (aynı ağda).
3. Olay-bazlı karar kuralı (ör. ilk k örnekte çoğunluk) ile bir çevrim içinde karar.

**Kilit şekil/tablo/denklemler**
- Şekil 1 (harmonik enjeksiyonlu IBR kontrolcüsü), **denk. (1)–(4)**, Şekil 2 — s. 2; denk. (5)–(7) (SVM), Şekil 3 (CIGRE ağı) — s. 3; Şekil 4–5 (eğitim, tahmin) — s. 4; **Tablo I–III** — s. 5.

---

## Grup sentezi

### Karşılaştırma tablosu

| | Yöntem | Aktif / pasif / kontrol | Haberleşme | Arıza tipleri | Şebeke | Nasıl doğrulandı | Karar süresi (makaleye göre) | Eşik / garanti türü |
|---|---|---|---|---|---|---|---|---|
| B1 | GFM IVS'yi denk. (9)'a göre ayarlayan FRT | Kontrol-tabanlı (test sinyali yok) | Yok | Asimetrik (CHIL'de yalnız ag); simetrik için artımlı pozitif-bileşen | 220 kV, tek GFM + sonsuz bara, 100 km | CHIL (3× RT-Box3), tek vaka + 1 kW lab deneyi | Röleye t_r = 50 ms gecikme önerisi | Klasik faz bantları; analitik ön koşul, garanti yok |
| B2 | IEEE 2800 (G2C, I_neg = K·V_neg) vs G1C; 7 klasik fonksiyon | Kontrol (şebeke kodu) değerlendirmesi | Yok | 10 tip; R_ph 0–2.5 Ω, R_g 0–100 Ω | 500/138/34.5 kV, 220.5 MW tip-4 rüzgâr | PSCAD 8320 senaryo + ticari röle (COMTRADE) | Kararlar 100 ms'de; mesafe 50 ms gecikmeli | Ticari eşikler (Z2F, 3I2 > 0.25 I_nom, …) |
| B3 | ΔY2 = ΔI2/ΔV2 | Pasif | Yok | BCG, AG | 480 V topluluk mikroşebekesi (şebekeye bağlı) | Simulink, birkaç vaka | Raporlanmamış | Deneysel Y_set (10/5), φ = 20° |
| B4 | ΔY2 + SEL-411L'de gerçekleme | Pasif | Yok (DNP3 sadece izleme) | SLG, 2LG, LL | Değiştirilmiş IEEE 13-bara 4.16 kV; bağlı + ada | OPAL-RT HIL + SEL-411L; Tablo 1–2 | 1.5–6 çevrim | |Y_set| 1 / 0.8 pu, φ = 45° (sezgisel) |
| B5 | Zaman-alanı IQ-mesafe + "≥10 ms ardışık >0" kriteri | Pasif | Yok | Yalnız dengeli ABCG | 66/220 kV, 300 MW GFM, 100 km | Analitik + MATLAB tarama + PSCAD (54 vaka/kaynak) | ~10 ms+ (kriter) | Analitik ψ_op > ψ_rst (yarı-statik), garanti değil |
| B6 | Ayar değişiklikleri (50FP = 1.25·I_MAX, Z50P1, zamanlayıcılar) | Pasif / ayar | Çekirdek yok; POTT opsiyonel | AG, ABG, AB, ABCG; R_F 0/5 Ω | 230 kV, 4 OEM kara-kutu modeli | PSCAD + röle donanımı, 208 vaka | Z1 anlık; Z2D ~0.3 s; 27D 1.0–1.5 s | I_MAX tabanlı marjlar |
| B7 | 87L alfa düzlemi ayar kılavuzu + faz-ayrık 87EFD | Pasif, diferansiyel | **Evet (şart)** | Tümü | 500 kV 1700 MVA tip-4 (sim.) + 138 kV saha olayı | Röle donanımına oynatma + saha kaydı | Kanala bağlı; 87EFD >1 s gecikme yaratabiliyor | Hata bütçesi (asimetri, K_TOT) |
| B8 | NSCI: tek DG, 0.3 pu, 80 ms NS enjeksiyonu; FDI = Re{ΔI2} | **Aktif** (arıza sonrası tetiklenen) | Yok; zaman kademeli | Dengeli + dengesiz; HIF (R_fmax 3.8–18.8 Ω) | 11 kV, 5 bara ada + IEEE 13-bara | Simülasyon (araç belirtilmemiş) | FDI ≈140 ms sonra + 0.05–0.5 s kademe | Akım bölücü analizi; eşik 0.2C (%80 marj) |
| B9 | 3./5./7. sentetik harmonik + doğrusal SVM | **Aktif** (arıza sonrası) + öğrenen | SVM yerel; temel yöntem POTT/DZI | Yalnız dengeli | CIGRE 12.47 kV, ada, gözlü | PSCAD + MATLAB, **tek** test arızası | 1 çevrim özellik penceresi | Doğrusal SVM, garanti yok |

### Tasarlanmış, garantili bir yardımcı sinyalin doldurabileceği boşluk

1. **Uyarımın kontrolü (excitation).** Pasif yöntemlerin hepsi ve kontrol-tabanlı çözümlerin bir kısmı, arızada IBR'nin ürettiği NS akımına bağımlı; bu akım OEM kontrolüne, V2 büyüklüğüne ve adalanmışlıkta kontrol dinamiğine bağlı. Kanıtlar: G1C'de IBR tarafında 32Q tüm senaryolarda bloke (B2); G2C'de bile yüksek-R_g PG arızalarında %90 (B2); tip-4 rüzgârın V2 ile uyumsuz 3I2 = 0.50 pu enjeksiyonu (B6); adalanmış GFM'de dalgalanan NS enjeksiyonu yüzünden |ΔY2|'nin 3.75 çevrimde eşik altına düşmesi (B4); R671'de I2 = 504 A ile Z2'nin başarısızlığı (B4). Tasarlanmış sinyal, uyarımı **bilinen ve kontrollü** hale getirir.
2. **Dengeli (üç-faz) arızalar.** Pasif NS elemanları (32Q, ΔY2, 87LQ) dengeli arızada kördür; B5 ve B1 dengeli arızayı en zor durum olarak işler; B6'da zayıf uçta 3P için tek seçenek 1.0–1.5 s'lik düşük gerilim yedeği. B8'e göre NS enjeksiyonunda üç-faz arıza NS ağında Z_f(eq) = R_f olarak görünür → **aktif NS sinyali dengeli arızayı da görebilir**.
3. **Garanti.** Tüm eşikler sezgisel veya deneysel: Y_set = 10/5 (B3), |Y_set| = 1/0.8 pu ve φ = 45° (B4), 0.2C + %80 marj (B8), 50FP = 1.25·I_MAX (B6), λ = 0.85 (B9 temel yöntemi), K ≥ 1 (B5). Doğrulamalar ne kadar büyük olursa olsun (8320 senaryo, B2) sonlu senaryo kümeleri. Küme-tabanlı tasarım, **modellenen belirsizlik kümesinin tamamı üzerinde** bir sertifika verir. Uyarı: sertifika modelin geçerli olduğu yere kadar; EMT ve HIL ile model-dışı etkiler (harmonikler, CT/CVT, kontrol geçicileri) ayrıca test edilmeli.
4. **Hız.** Aktif rakipler yavaş (B8: ≈140 ms + kademe; B9: tetik + POTT); pasif ΔY2 1.5–6 çevrim (B4); B2'de kararlar 100 ms'de. Tek çevrimlik (≈16 ms) bir hedef bu literatürde ayırt edici.
5. **Optimizasyon.** Enjeksiyon parametreleri (B8'de 0.3 pu / 80 ms / trapez, B9'da 0.38 pu/harmonik) elle seçilmiş; minimum enerji veya minimum bozucu etki için tasarım yapan yok.
6. **Haberleşmesizlik.** Haberleşme varsa 87L en iyi seçenek (B7); yardımcı sinyalin doğal alanı haberleşmesiz (tek uçlu) koruma — B3–B6, B8 ile aynı ligde ama garantili.

### Yardımcı sinyalin karşılaşacağı zorluklar (rakiplerin güçlü yanları)

- **IEEE 2800 bedava ve zorunlu.** G2C zaten NS akımı veriyor ve klasik fonksiyonları çoğu durumda düzeltiyor (B2). Yardımcı sinyalin katkısı G2C'nin zayıf kaldığı yerlerde (yüksek R_f, dengeli arıza, hız) gösterilmeli.
- **Akım bütçesi.** Arızada inverter akımı sınırlı (I_t1 ≤ I_lim1, I_t2 ≤ I_lim2: B1; I_max ≤ I1max + I2max: B4); yardımcı sinyal FRT akımıyla bu bütçeyi paylaşır → tasarımda açık kısıt.
- **Birlikte var olma (coexistence).** Sahadaki 32Q/50Q/87LQ/ΔY2 elemanları ve I2/I1 kısıtlama faktörleri (0.1–0.2, B4) var; sürekli bir NS sinyali mevcut röleleri yanıltmamalı (B6 notundaki hipotez: uzak uç 32Q riski).
- **Harmonik ve gürültü.** Sahada IBR harmonikleri sahte NS büyüklükleri üretip 87LQ'yu açtırdı (B7) → dedektör dayanıklı olmalı.
- **Çoklu NS kaynağı.** B8'in süperpozisyon analizi "başka NS artış kaynağı yok" varsayımına dayanıyor; G2C uyumlu IBR'ler bunu bozar.
- **Model doğruluğu.** Garantinin değeri, kullanılan modelin (ör. B5'in IQ ağı, B8'in akım bölücüsü) EMT'ye ne kadar uyduğuna bağlı; B5'in "analitik model + otomatik yüzlerce PSCAD koşusu" doğrulama yöntemi örnek alınmalı.

### Projeye somut öneriler

- **WP3 baseline paketi (öncelik sırasıyla):** (1) 32Q/Z2 (B2 denk. 1; B6 SEL ayarlarıyla), (2) ΔY2 (B4), (3) zaman-alanı IQ-mesafe + 10 ms kriteri (B5), (4) NSCI + FDI (B8, aktif baseline), (5) artımlı tork faz seçimi (B2 denk. 3–5). 87L (B7) karşılaştırma tablosunda "haberleşmeli tavan" olarak.
- **WP2 senaryo matrisi:** arıza tipi (10 tip) × R_f (0 → en az 100 Ω; B2 ve B6 aralıkları) × konum × inverter kontrolü {G1C, G2C, GFM-doyum, GFM-sanal empedans} × {şebekeye bağlı, ada}. B2 (8320 senaryo) ve B6 (208 OEM vakası) şablon.
- **WP4 gecikme referansları (makalelerden):** ΔY2 1.5–6 çevrim (B4); IQ-mesafe ~10 ms+ (B5); G2C ile mho karşılaştırıcısı ~40 ms'de bölgede (B2); NSCI ≈140 ms + kademe (B8); gezici-dalga rölesi 1 MHz örnekleme ister (B1'de SEL-T400L notu).

### En önemli 3 çıkarım

1. **Pasif elemanların ortak zaafı, IBR'nin kontrolsüz NS yanıtına bağımlılık** (B2, B4, B6, B7). Endüstri bunu duyarlılıktan vazgeçerek (50FP'yi yükseltip R_F kapsamını ~400 Ω'dan ~100 Ω'a düşürerek, 87LQ'yu IBR derecesine göre körleştirerek) çözüyor. Bilinen, tasarlanmış bir uyarım bu ödünleşimi kırabilecek en doğal araç — projenin ana motivasyon cümlesi bu olmalı.
2. **En yakın öncül (B8, NSCI) fiziksel konsepti kanıtlıyor ama sezgisel, tetiklemeli ve yavaş.** Tek bir DG'den 0.3 pu NS enjeksiyonu haberleşmesiz bölüm tanımlamaya yetiyor; dengeli arızaları da görüyor; ancak eşikler elle, garanti yok, karar ≈140 ms + zaman kademesi. Taylor çizgisinin katkısı açıkça bu dört eksende (optimizasyon, garanti, hız, mesafe rölesi uyumu) konumlandırılmalı ve **B8 yeniden gerçeklenip baseline olarak kullanılmalı**.
3. **Değerlendirme çıtası yüksek:** büyük senaryo taramaları (B2, B6), gerçek röle donanımıyla HIL (B4) ve analitik modelin otomatik EMT taramasıyla doğrulanması (B5). Garantili tasarım bile bu çıtayla raporlanmalı (dependability/security yüzdeleri + karar süresi), ayrıca **dağılım-dışı** vakalarda (B9'un tersine) ve IEEE 2800 uyumlu (G2C) inverterlerin varlığında test edilmeli.
