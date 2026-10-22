# E — Pratik mesafe rölesi ayarları: SEL makaleleri okuma notları

*Sayfa numaraları ("s.") makalelerin kendi baskı numaralarıdır, kapak sayılmaz (PDF sayfası = baskı no + 1; 2012 makalesinde + 2). "(Benim çıkarımım)", "(benim hesabım)" ya da "(genel bilgi)" diye işaretlenen cümleler makalelerden alınmadı.*

## Kavramlar sözlüğü

**Mesafe elemanı, görünür empedans ve IZ–V çalışma sinyali (distance element, apparent impedance, operating signal).** Röle bir ölçüm çevriminin (AG, BG, CG, AB, BC, CA) gerilimini (V) ve akımını (I) ölçer. Metalik arızada V/I, röle ile arıza arasındaki hat empedansına (m·Z1) eşittir; erişimin arıza akımından bağımsız olması, mesafe rölesinin aşırı akım rölesine göre temel üstünlüğüdür (2021, s.1). Her elemanın kalbinde S_OP = I·Z_R − V sinyali vardır ve eleman, polarize sinyal S_POL ile arasındaki açı |∠(S_OP, S_POL)| < 90° olduğunda çalışır (2021, s.2). Metalik arızada S_OP(pu) = (m0 − m)/(SIR + m) olur: bölge içinde pozitif, dışında negatif; bu notlardaki bütün hata analizleri bu "sinyal marjı" üzerinden yapılır (2021, s.13).

**Bölgeler (zones: Zone 1/2/3).** Bölge 1 hattın uzak ucuna varmayacak şekilde ayarlanır (underreaching; tipik olarak faz %80, toprak %75); kanal kullanmadan ve gecikmesiz açtırdığı için önceliği güvenliktir (security, yani yanlışlıkla açtırmamak) (2021, s.7). Bölge 2 uzak ucu aşar (overreaching; tipik %120) ve zaman gecikmeli kademeli mesafe yedeği ya da pilot şemada ani eleman olarak kullanılır; önceliği güvenilirliktir (dependability, yani gerektiğinde mutlaka açtırmak) (2021, s.14, s.22). Bu SEL makalelerinde Bölge 3 geriye bakan bir bloklama bölgesidir: DCB şemasında yerel Bölge 3, karşı uçtaki Bölge 2'nin gördüğü her dış arızayı görmelidir (2021, s.22). *(Genel bilgi: klasik ders kitaplarında Bölge 3 çoğu zaman ileriye bakan uzak yedek bölgesidir; hangi anlamın kastedildiğini her seferinde kontrol edin.)*

**Erişim; eksik ve aşırı erişim (reach; underreach, overreach).** Erişim ayarı Z_R = Z_SET∠MTA'dır; MTA (maksimum moment açısı) genellikle hattın pozitif bileşen empedans açısıdır (2021, s.3–4). Aşırı erişimde eleman ayarın ötesindeki bir arızada çalışır, ki bu Bölge 1 için tehlikelidir; eksik erişimde ise ayarın içindeki bir arızayı görmez, ki bu da Bölge 2 için tehlikelidir. Hatalar δZ = δV − δI şeklinde birleşir: gerilim %1 düşük okunursa eleman %1 aşırı erişir, akım %1 düşük okunursa %1 eksik erişir (2021, s.4).

**Mho ve dörtgen karakteristik (mho vs. quadrilateral).** Mho karşılaştırıcısı gerilimle polarize edilir ve empedans düzleminde bir daire çizer; dörtgenin üst kenarı olan reaktans karşılaştırıcısı ise akımla polarize edilir ve düz bir çizgi verir (2021, s.2–3). Rezistif arızada mho dairesi erişim noktasından aşağı ve dışarı doğru kıvrılır; bu Bölge 1'e doğal bir güvenlik payı sağlar ama Bölge 2'nin güvenilirliğini azaltabilir (2021, s.8). Dörtgende rezistif erişim reaktif erişimden bağımsız ayarlanabilir; kısa hatlarda tercih edilmesinin nedeni budur, buna karşılık polarizasyon açısı hatalarına çok duyarlıdır (2021, s.10–11, s.17–18).

**Rezistif erişim (resistive reach / resistive blinder).** Dörtgenin sağ (ve sol) kenarıdır ve ne kadar arıza direncinin (R_F) kapsanacağını belirler. Uzak uçtan da akım geliyorsa görünür empedans hatası Z_ERR = R_F·(1 + I_Y/I_X) olur ve yük akışının yönüne göre eğilir: load-in durumunda yukarı (eksik erişim), load-out durumunda aşağı (aşırı erişim) (2021, s.7–8). Polarize akımda Θ kadar açı hatası varsa reaktif marj ΔZ > 2·R_B·sin(Θ/2) olmalıdır; yani rezistif erişimi büyütmenin bedeli Bölge 1 güvenliğidir (2021, s.11).

**Yük tecavüzü (load encroachment).** *(Genel bilgi.)* Ağır yükte yükün görünür empedansı (yaklaşık V²/S) küçülür; büyük bir mho dairesinin ya da geniş bir dörtgenin içine girerse arıza yokken açtırmaya yol açabilir. Yük tecavüzü mantığı ve kör çizgiler bu yük bölgesini karakteristikten keser. Bu makalelerde konu yalnızca dolaylı olarak geçiyor: ofset mho'nun büyük ayarlanmış geri erişimi yük empedansına girebilir ve dörtgenin sağ kör çizgisi "hat yüklenebilirliği kriterine göre" ayarlanır (2022, s.7–8); 2021 makalesi ise yük tecavüzü kör çizgilerine yalnızca kaynak [13]'e atıfla değinir (2021, s.22).

**Polarizasyon (polarization: memory, negative-sequence, cross-phase).** Polarize sinyal, arızanın yönü ve arıza noktasındaki gerilimin fazı için bir referanstır. Mho için seçenekler şunlardır: self (çevrimin kendi gerilimi), çapraz-faz (sağlam fazın gerilimi), pozitif bileşen gerilimi, hafıza (arıza öncesi gerilim, açısı ve frekansıyla birlikte hatırlanır) ya da bunların birleşimi (2021, s.2). Hafıza polarizasyonu, gerilimin sıfıra yakın olduğu yakın üç fazlı arızalarda yön bilgisini sağlar ve mho'yu dinamik olarak genişletir; ancak kaynağın arıza boyunca açısını ve frekansını koruduğunu varsayar: senkron makinenin ataleti bunu sağlar, invertör sağlamaz (2022, s.2–3). Reaktansın I2 ile polarize edilmesi ("adaptif polarizasyon") rezistif kapsamı güvenliği bozmadan artırır (2021, s.3; 2022, s.5); bunun koşulu, röle yerindeki I2 fazının arıza noktasını temsil etmesidir, bu da homojen bir negatif bileşen şebekesi ve endüktif bir kaynak Z2 gerektirir (2022, s.5).

**Yön elemanları (directional elements: 32P/32Q/32G).** ANSI kodunda 32 "yön" demektir.
- **32Q** negatif bileşen yön elemanıdır: Z2ölç = Re[V2·(1∠Z1ANG·I2)*]/|I2|² hesaplar; değer Z2F'den küçükse "ileri", Z2R'den büyükse "geri" kararı verir. İleri arızada arkadaki kaynağın −Z_S2'sini, geri arızada hat ile karşı sistemin +Z2'sini görür (2012, s.7 ve Şekil 24). Dörtgen için yön denetimi zorunlu, mho için isteğe bağlıdır (2022, s.5).
- **32G** sıfır bileşen yön elemanıdır. Sıfır bileşen şebekesi pasif olduğundan ve yalnızca arıza noktasında uyarıldığından, invertörden, salınımdan ve frekans sapmasından büyük ölçüde bağımsızdır (2022, s.9).
- **32P** faz (çoğunlukla pozitif bileşen) yön elemanıdır ve dengeli üç fazlı arızalar için kullanılır. *(Genel bilgi: "32P" adı bu makalelerde geçmiyor; 2022 faz arızaları için bunun yerine 32WI ve TD32'yi öneriyor, s.9–11.)*

**Toprak çevrimi k0 kompanzasyonu (zero-sequence compensation).** AG çevriminde V = VA ve I = IA + k0·(IA+IB+IC) alınır; burada k0 = (Z0/Z1 − 1)/3 (2021, s.4). Böylece faz-toprak arızasında da V/I = m·Z1 olur ve toprak elemanı faz elemanıyla aynı Z1 ölçeğinde ayarlanabilir. *(Benim açıklayıcı örneğim: Z0 = 3·Z1 ise k0 ≈ 0,67.)* Z0 değeri toprak teline, toprak özdirencine ve mevsime bağlı olduğundan belirsizdir ve toprak Bölge 1'ine yaklaşık %5 ek marj gerektirebilir (2021, s.6).

**SIR (kaynak/hat empedans oranı, source-to-line impedance ratio).** Klasik tanımda SIR, homojen bir modelde kaynak empedansının hat empedansına oranıdır. Kasztenny'nin önerdiği daha kesin tanımda, uzak barada metalik arızada röledeki çevrim gerilimi V_PU (pu) ise SIR = 1/V_PU − 1'dir; toprak elemanı için SIR_G faz-toprak arızasından, faz elemanı için SIR_P faz-faz arızasından hesaplanır (2021, s.14). V_PU = 1/(SIR+1) olduğundan, uzak bara arızasında röle gerilimi SIR 0,5'te nominalin 2/3'ü, SIR 4'te 1/5'i, SIR 10'da %9'u, SIR 30'da %3'üdür (2023, s.17; 2021, s.13); gerilim düştükçe IZ–V sinyali küçülür ve her hata göreli olarak büyür. Makalenin örneği: uzak bara faz-toprak arızasında 0,081 pu ise SIR_G = 11,3, faz-faz arızasında 0,053 pu ise SIR_P = 17,9 (2021, s.15).

**CVT/CCVT geçicileri ve geçici aşırı erişim (CVT/CCVT transients, transient overreach).** CVT ile CCVT aynı cihazdır: kapasitif bölücü, ayar reaktörü, ara transformatör ve ferrorezonans bastırma devresinden oluşur ve yaklaşık 150 kV'un üzerinde manyetik VT'den daha ekonomiktir (2021, s.18; 1996, s.2). Gerilim aniden çöktüğünde depolanmış enerji çıkışta bir geçici üretir: nominalin %25–40'ına kadar çıkabilir, 1–2 çevrim boyunca aynı polaritede kalabilir ve frekansı şebeke frekansına yakın olduğu için zor filtrelenir (2021, s.18–19). Bu geçici temel bileşen gerilimini küçük gösterir; hesaplanan empedans küçülür ve Bölge 1 bir dış arızada çalışır, buna geçici aşırı erişim denir (1996, s.1). Ölçümü için elemanın hiç çalışmadığı erişim mX ve her zaman çalıştığı erişim mY bulunur; TO = (mY − mX)/(0,5·(mY+mX))·%100 (2021, s.6–7).

**Kısa ek terimler.**
- *Infeed / outfeed:* Çok uçlu bir hatta ya da rezistif arızada başka bir uçtan gelen akım röle gerilimini değiştirir; infeed eksik erişime, outfeed aşırı erişime yol açar (2021, s.9–10).
- *Karşılıklı kuplaj (mutual coupling):* Aynı koridordaki hatların akımları, en güçlü olarak sıfır bileşen akımı, korunan hatta gerilim indükler (2021, s.8; 2023, s.14).
- *GPR (ground potential rise):* Toprak akımı merkez topraklamasının potansiyelini değiştirir ve VT, gerilimi uzak toprağa göre değil merkez toprağına göre ölçer. 2021 makalesi bunun VT'yi düşük okutup aşırı erişime yol açtığını söylüyor (s.16). 2023 makalesi ise toprak elemanlarında tipik sonucun eksik erişim olduğunu, aşırı erişimin şebekenin homojen olmamasından kaynaklanan bir açı eğilmesiyle ortaya çıkabileceğini söylüyor (s.13). *(Benim yorumum: işaret, toprak akımının merkez topraklamasına giriş ya da çıkış yönüne bağlı olmalı. Güvenlik analizinde en kötü işaret alınmalı.)*
- *Pilot şemalar:* DCB (directional comparison blocking), POTT/PUTT (permissive over-/underreaching transfer trip) ve 87L (hat diferansiyel) (2021, s.22; 2012, s.11).
- *Dalga üzerindeki nokta (point on wave, POW):* Arızanın gerilim dalgasının hangi anında başladığıdır; CVT geçicisi için en kötü durum gerilimin sıfırdan geçtiği andır (1996, s.16).

---

## 1. Kasztenny (2021) — Hat korumasında mesafe elemanlarının ayarı

- **Künye:** Bogdan Kasztenny (SEL), "Settings Considerations for Distance Elements in Line Protection Applications". İlk olarak 74th Annual Conference for Protective Relay Engineers'da (Mart 2021) sunuldu; ardından 74th Georgia Tech PRC (Nisan 2021) ve 48th WPRC'de (Ekim 2021, çevrim içi). 24 numaralı sayfa ve kapak (PDF 25 sayfa).
- **Tek cümlede:** Mesafe elemanını ayarlamak, ölçüm zincirindeki her hata kaynağını belirleyip IZ–V sinyalinin işaretini çeviremeyecek kadar marj bırakmaktır; yüksek SIR'de bu sinyal nominalin %1'inin altına inebildiğinden, normalde ihmal edilen GPR, kablo gürültüsü ve CCVT geçicisi gibi etkiler Bölge 1'i kullanılamaz hâle getirebilir.

### Ne öğretiyor

**a) IZ–V: bütün mesafe elemanlarının ortak dili (s.2–4).**
- Eleman S_OP = I·Z_R − V (1) sinyalini hesaplar ve |∠(S_OP,S_POL)| < 90° ise (2) çalışır (s.2). Elektromekanik röle bunu replika empedans, toplama transformatörü ve silindir tipi bir röleyle; statik röle çeyrek çevrimlik bir çakışma zamanlayıcısıyla gerçekler. Sayısal röle aynı karşılaştırmayı doğrudan yazılımda yapar (s.2).
- Bu koşulu cebirle düzenleyince bilinen "m-hesabı" çıkar: m = Re(V·S_POL*)/(|Z1|·Re(I·1∠MTA·S_POL*)) < m0 (8c). Ancak çözüm ayrıca Re(I·1∠MTA·S_POL*) > 0 (8b) koşulunu da içerir. Bu koşul aslında gizli bir yön elemanıdır ve pek çok uygulayıcı (8b) ile denetim yapılması gerektiğini bilmez (s.3).
- Oran biçimi sinyal seviyesini gizler: 20 V/10 A ile 1 V/0,5 A aynı m değerini verir, ama hataların ve parazitlerin etkisi bu iki durumda çok farklıdır. Ayrıca payda 90°'ye yaklaştığında sıfıra bölme yaklaşır ve sonuç gürültüye duyarlı hâle gelir (s.3). **Ders:** analiz yaparken V/I oranına değil, IZ–V sinyalinin büyüklüğüne bakın.
- Erişimi etkileyen ayarlar (s.4):
  - Z_SET ve MTA;
  - k0;
  - reaktans polarize akımı (çevrim akımı, I2, I0 ya da tasarımca sabitlenmiş I2+I0);
  - homojen olmama düzeltme açısı (aşağı eğim güvenliği, yukarı eğim güvenilirliği artırır);
  - aşırı akım denetim eşiği.

**b) Bölge 1 felsefesi (s.4).** Bölge 1'de güvenlik her şeydir; hız ve güvenilirlik bunun sonucudur. Hatalar iki türe ayrılır:
- *Geçici hatalar* röle tasarımıyla (üreticinin sorumluluğu) çözülür; kısa bir gecikme de çözebilir.
- *Kalıcı (steady-state) hatalar* ancak ayarla (kullanıcının sorumluluğu) çözülebilir. Gecikme bunlara yardımcı olmaz, meğer ki komşu bölgelerle zaman koordinasyonu sağlayacak kadar uzun olsun.

Bölge 1'in uygulanabilirliği evet/hayır sorusu değil, bir maliyet/fayda kararıdır.

**c) Hata bütçesi ve gerekçeleri (s.4–7).**

| Hata kaynağı | Tablo I'deki tipik erişim hatası | Gerekçe (sayfa) |
|---|---|---|
| Gerilim transformatörü (VT) | %5 | Koruma sınıfı VT'nin geniş gerilim aralığında oran hatası %3–6 olabilir. Doğruluk ancak belirli bir minimumun (ör. nominalin %5'i) üstünde geçerlidir. Açı hatası (2–4°) zayıf sistem dışında ihmal edilebilir. Yaklaşık %5 marj bırakın (s.5). |
| Akım transformatörü (CT) | %10 | Arıza sırasında %5–10 oran hatası beklenir. Doyma, akımı düşük ve ileri fazda gösterir: genellikle eksik erişim olur, ama açı kayması aşırı erişime de yol açabilir. Yaklaşık %10 marj bırakın (s.5). |
| Hat empedansı verisi | %5 (faz) / %10 (toprak) | Z1 ancak %1–2 büyüklük ve 1–2° açı doğruluğuyla bilinebilir. Z0 belirsizliği %5'e kadar ek marj gerektirebilir. Transpoze olmayan hatta en kısa ve en uzun çevrim arasındaki fark %10'a varabilir; en kısa çevrime göre ayarlayın. Veri yoksa Z1'i kullanıp yaklaşık %5 ek marj bırakın. Tam transpoze hatta bile %2–3 ek marj gerekebilir (s.6). |
| Rölenin kalıcı doğruluğu | %1 | Mikroişlemcili röle yüzde birin altında hata yapar. Ancak çok düşük gerilim (zayıf sistem), çok yüksek akım veya çok küçük erişim ayarı durumunda spesifikasyonu ayrıca kontrol edin (s.6). |
| Rölenin geçici doğruluğu (TO) | %5 | Tipik üretici beyanı "SIR < 30 için %5 TO" şeklindedir. Bu beyanın CCVT'yi de kapsayıp kapsamadığını kontrol edin (s.7). |
| **En kötü durumda toplam** | **%26 faz / %31 toprak** | Bu toplam en fazla %74 / %69 erişime izin verir (s.7). |

- **Uygulamadaki karşılığı:** faz %80, toprak %75. Gerekçe, hataların kısmen birbirini götürmesidir: VT ve CT aynı yönde hatalıysa empedans etkilenmez; yüksek akımda CT düşük okur ve bu eksik erişime yol açar (s.7). Hat empedansı arıza kayıtlarından, özellikle iki uçtan alınmış zaman senkron kayıtlardan iyi biliniyorsa erişim %85–90'a çıkarılabilir; bu özellikle faz elemanları için geçerlidir (s.7).
- **Küçük örnekler:** %3 düşük okuyan bir VT %3 aşırı erişime yol açar (s.4). %5 düşük okuyan bir CT %5 eksik erişime yol açar (s.5).
- **CT boyutlandırma:** CT'ler hat sonu arızasında, yedek korumanın temizleme süresi boyunca doymamalıdır (s.5). Çift kesicili düzende yakın bir dış arızada CT doyarsa, bu sorun erişimi kısaltarak çözülemez; özel bir güvenlik mantığı ya da uygun CT seçimi gerekir (s.5).
- **Frekans (s.6):** Hat sabit endüktanslı bir elemandır. 58 Hz'de hat %3,3 kısa görünür, bu yüzden Bölge 1'e %3,3 ek marj gerekir. Adalanabilecek bölgelerde rölenin sabit-reaktans mı yoksa sabit-endüktans (frekans kompanzeli) mı olduğunu kontrol edin. *(Makale 59/61 Hz için reaktansın "sırasıyla %1,7 büyük/küçük" olduğunu söylüyor. X = 2πfL olduğundan 59 Hz'de reaktans aslında küçülür ve makalenin kendi 58 Hz örneği de bununla tutarlı; ifadedeki sıra bence bir dikkatsizlik.)*
- **TO testi (s.6–7):** Bölge 1'i, hat sonunda farklı POW'larda başlayan arızalarla test edin. Elemanın hiç çalışmadığı erişim mX'i ve her zaman çalıştığı erişim mY'yi bulun; TO = (mY − mX)/(0,5(mY+mX))·%100 (11). %5'lik TO, kalıcı hata marjının üstüne %5 daha marj eklemek demektir.

**d) Rezistif arıza ve yük akışı (s.7–8).**
- Rezistif arızada V_X = m·Z·I_X + R_F·(I_X + I_Y) (12) olduğundan Z_APP = mZ + R_F + R_F·I_Y/I_X (13) çıkar (s.7).
- Uzak uç akımı yerel akımın önünde ise (load-in) hata çizgisi yukarı eğilir ve eksik erişim olur. Gerisinde ise (load-out) aşağı eğilir ve aşırı erişim olur (s.7–8).
- Mho dairesi bu durumda erişim noktasından uzaklaşacak şekilde aşağı kıvrılır. Bu Bölge 1 için genellikle yeterlidir, ama Bölge 2 load-in'de bile güvenilirlik kaybedebilir (s.8).
- Dörtgende reaktans çizgisi, polarize akımın seçimiyle eğilir. Bölge 1'de yalnızca aşağı eğime, Bölge 2'de her iki yöne de izin verilebilir (s.8).

**e) Karşılıklı kuplaj (s.8–9).** Paralel hatlarda sıfır bileşen akımı eşit bölündüğü sürece k0 değiştirilerek telafi edilebilir. Ancak paralel hat servis dışıyken, tek ucundan topraklıyken veya iki ucundan topraklıyken bu telafi bozulur (s.8). Önerilen prosedür (s.9):
1. Varlıkların servis içi ve dışı hâlleri dahil, bütün makul olasılıkları (contingency) düşünün.
2. Servis dışı kuplajlı hattı hem topraklı hem topraksız modelleyin.
3. Hem uzak barada hem de uzak baraya yakın kuplajlı hatlarda toprak arızaları uygulayın. Görünür empedansı hesaplarken rölede kullanılacak k0'ın aynısını kullanın.
4. Bölge 1 için en küçük görünür empedansı alıp **%25 marj** bırakın.
5. Bölge 2 için en büyük görünür empedansı alıp marj ekleyin.

**f) Infeed/outfeed (s.9–10).**
- Üç uçlu hatta görünür empedans hatası Z_ERR = m·Z_Y·I_W/I_X'tir (17). Infeed eksik erişime, nadir görülen outfeed aşırı erişime yol açar (s.10).
- **Kural:** Bölge 1 infeed'i telafi edecek şekilde uzatılmaz, çünkü kesici açık olduğunda infeed ortadan kalkar. Bölge 1 elektriksel olarak en yakın uzak ucun gerisinde kalmalıdır: erişim ≤ min(|Z_X+Z_Y|, |Z_X+Z_W|) (s.10).
- Topraklı ara bağlantılar (grounded taps) sıfır bileşen akımını röleden uzağa saptırır; bu yüzden toprak elemanları eksik erişir (s.10).

**g) Dörtgen ve polarizasyon açısı hatası (s.10–12).**
- Θ hatasının kaynakları: CT oran hatası, CT doyması, hat şarj akımı, sistemin homojen olmaması ve birden fazla dirençli karmaşık arızalar (s.11).
- Güvenlik koşulları: ΔZ > 2·R_B·sin(Θ/2) (18); buradan m0 < 1 − 2·r_B·sin(Θ/2) (19) ve küçük açılar için ΔZ/R_B > Θ·π/180 (20b) çıkar (s.11). Burada ΔZ reaktif erişim marjı, R_B rezistif erişim (kör çizgi), r_B onun hat empedansına göre pu değeridir.
- **İşlenmiş örnek (s.11):** Θ = 5° için ΔZ/R_B > 0,087 olmalıdır.
  - Reaktif erişim %80 isteniyorsa r_B en fazla yaklaşık 2,3 olabilir (0,2/(2·sin 2,5°) ≈ 2,3).
  - R_B = 4·Z isteniyorsa ΔZ ≥ 0,35 olmalı, yani reaktif erişim %65'in altında kalmalıdır.
- BCG gibi iki dirençli bir arızada röledeki I2 hiçbir çevrimin doğru polarize sinyali değildir. Adaptif polarizasyon yalnızca tek dirençli arızalarda (faz-toprak veya faz-faz) tam doğrudur (s.12).
- Üç fazlı arızada I2 neredeyse sıfırdır ve sahte I2'nin açısı rastgeledir. Bu yüzden Bölge 1 dörtgeni bu arızalarda mho karakteristiğine geri dönebilir (s.12).
- Bir tasarım çözümü: sıralı polarize akımı küçük bir pozitif bileşen gerilim sinyaliyle "desteklemek" (s.12).

**h) Zayıf sistemin matematiği (s.12–14).**
- Röle akımı I = E/(Z_L(SIR+m)) (21), röle gerilimi V = mE/(SIR+m) (22), pu olarak V_PU = m/(SIR+m) (23) (s.12).
- Hat sonu arızasında röle gerilimi SIR 5'te %15'in üstünde, SIR 10'da %9, SIR 30'da %3'tür (s.13).
- Çalışma sinyali S_OP(pu) = (m0 − m)/(SIR + m)'dir (25). %80 ayarda hat sonu arızası için marj SIR 5'te "%3,5", SIR 10'da %2'nin altında, SIR 20'de %1'in altında, SIR 30'da yaklaşık %0,6'dır (s.13). *(Formül SIR 5 için 0,2/6 ≈ %3,3 veriyor; makaledeki değer figürden okunmuş olabilir.)*
- **Kilit denklem (s.13):** Ölçülen sinyal S_OP(ölç) = S_OP(gerçek) + V_ERR'dir (27). Gerilimi düşüren her hata çalışma sinyalini büyütür.
- **Örnek:** SIR 20'de uzak uç arızası için sinyal nominalin %1'inden azdır. Bu yüzden nominalin %1'i kadar bir gerilim hatası sinyalin işaretini çevirebilir; dış arıza iç arıza gibi görünür ya da tersi olur (s.13).
- Bölge 2 (m0 = 1,2) için S_OP = 0,2/(SIR+1)'dir (29). SIR 20'de bu değer %2'nin altındadır, yani %2'lik bir hata güvenilirliği bozmaya yeter (s.14).

**i) SIR'in yeni tanımı (s.14–15).** Hat sonu arızasındaki çalışma koşullarını beş karmaşık sayı belirler: (Z0, Z1, Z2)_SYS ve (Z0, Z1)_LINE. Bunları tek bir oranla temsil etmek bir basitleştirmedir (s.14). Tanım: SIR_G = 1/V_PU(LG) − 1 (30a), SIR_P = 1/V_PU(LL) − 1 (30b). Hesap adımları:
1. Uzak barada metalik faz-toprak arızası uygulayın ve rölede faz-toprak geriliminin pu değerini bulun.
2. SIR_G'yi (30a) ile hesaplayın.
3. Bunu bir dizi sistem durumu ve olasılık için tekrarlayın.
4–6. Aynı adımları faz-faz arızası ve SIR_P için uygulayın (s.14–15).

Makaledeki örnekte SIR_G = 11,3, SIR_P = 17,9 çıkar; sıfır bileşen sistemi daha güçlü olduğu için toprak elemanının koşulları daha iyidir (s.15). Kısa devre programıyla hesaplamak homojen olmamayı, kuplajı, hat dengesizliğini, senkron makinenin subtransient/transient davranışını ve rüzgâr ile invertörlü kaynakların arıza tepkisini hesaba katmaya izin verir (s.15).

**j) Zayıf sistemde Bölge 1'i bozan "küçük" etkiler (s.15–18).**
- **Ölçüm doğruluğu:** SIR > 20'de röle gerilimi nominalin %5'inin altındadır; bu kadar düşük gerilimde VT ve rölenin doğruluğunu ayrıca sorgulayın (s.15). CT'ler en az bir koordinasyon basamağı (300–500 ms) boyunca doymamalıdır (s.15).
- **Sekonder kabloya indüklenen gerilim:** SIR 20 ve %80 ayarda sinyal %1'in altındadır. 66,4 V'luk sekonder sistemde %0,5 hata yalnızca 330 mV eder ve bu kadar gerilim ekransız kablolarda kolayca indüklenebilir (s.15). Önlemler: yüksek sekonder tap, ekranlı kablo, merging unit; kabloya güvenilemiyorsa toprak Bölge 1'inden vazgeçin (s.16).
- **GPR, işlenmiş örnek (s.16):** GPR 0,5 kV olsun. Güçlü sistemde çalışma sinyali nominalin yaklaşık %10'udur. 69 kV'ta bu 69 kV·0,1/√3 = 4 kV eder ve GPR sinyalin %12'si olur; 500 kV'ta yalnızca %1,7'sidir. SIR 20 ve %80 ayarda ise 69 kV'ta GPR (0,5 kV) sinyalden (0,4 kV) büyüktür; 500 kV'ta 0,5 kV'a karşı 2,9 kV'tur. GPR faz-faz geriliminde birbirini götürür, yani yalnızca toprak elemanlarını etkiler. Toprak Bölge 1'inin fazdan kısa ayarlanmasının (%75'e karşı %80) bir nedeni budur. Zayıf sistemde GPR yüksekse toprak Bölge 1'ini kullanmaktan kaçının (s.16).
- **Kısa hatta Z0:** Arıza noktasının ve merkez topraklamasının "uç bileşenleri" baskın hâle gelebilir; o zaman Z0 artık mesafenin bir ölçüsü değildir (s.16–17).
- **Kuplaj:** Zayıf uçta pozitif ve negatif bileşen kuplajı bile önem kazanır ve faz elemanlarını da etkiler. Kısa devre programları bu kuplajı modellemeyebilir (s.17).
- **Polarizasyon:** Zayıf sistemde açı hatası çalışma sinyalinde de ortaya çıkar. Çalışma sinyalindeki +θ hatasının etkisi, polarize sinyaldeki −θ hatasıyla aynıdır. Hafıza polarizeli mho bile bu yüzden rezistif arızalardaki doğal güvenlik marjını kaybedebilir (s.17). Örnek: 5° CT hatası ve 10° gerilim hatası toplam 15° eder; reaktif erişim %70 ise rezistif erişim "yaklaşık 1,5×Z" ile sınırlanır (s.17). *(Dikkat: (19) denklemi bu değerler için r_B ≈ 0,3/(2·sin 7,5°) ≈ 1,15 veriyor ve s.11'deki Şekil 12'nin Θ = 15° eğrisi de buna uyuyor. Makaledeki 1,5 değeri bence bir yuvarlama veya okuma hatası; emin değilim.)*
- **Kısa hatta dörtgen ve 4. bölge:** Yakın bir rezistif arıza ağır load-out ile birleşince görünür empedans 4. bölgeye kayabilir ve yön ya da çevrim seçimi sorun çıkarabilir. Sıralı (negatif ve sıfır bileşen) yön elemanları bu durumdan etkilenmez (s.18).

**k) CCVT (s.18–19).**
- Ara gerilim 5–35 kV'tur. Depolanan enerjinin sönümlenmesi 1–2 çevrim sürebilir (s.18). IEC 61869-5 standardı üç geçici sınıfı tanımlar; bazı eski CCVT'ler bu sınıfları karşılamaz (s.18).
- **İşlenmiş örnek (s.19):** SIR 10 ve %80 ayarda sinyal %2'nin altındadır. PT2 sınıfı bir CCVT'nin 30 ms'deki hatası %10'a kadar çıkabilir. Gürültü/sinyal oranı 5:1 olur; gürültü şebeke frekansına yakın olduğu için genel bir filtre onu temizleyemez.
- **Güçlü sistem karşılaştırması (s.19):** SIR 0,25'te hat sonu gerilimi %80'dir. Gerilimdeki değişim %20 olduğu için CCVT geçicisi 0,2·(%25–40) = %5–8 kadardır; oysa sinyal %10–20'dir ve eleman güvenli kalır.
- **Son çare (s.19):** Bölge 1'e 30–50 ms gecikme eklemek. Bu kalıcı hataları çözmez ve SIR düştüğünde gereksiz bir gecikme olarak kalır.

**l) Röle tasarımı ve "neden elektromekanik röleler idare ediyordu?" (s.19–21).**
- Rölelerin CCVT'ye karşı kullandığı yaklaşımlar (s.19–20):
  - (a) Moment (torque) eşiği: sinyal küçüldükçe eleman yavaşlar ve ters zamanlı bir gecikme oluşur.
  - (b) Görünür empedansın hareketini izlemek; yerleşene kadar beklemek. Bu mantık çoğunlukla kullanıcının SIR'e göre açması gereken bir ayardır.
  - (c) Gerilim ölçüm zincirine özel bir filtre; SIR 5–10 aralığında biraz hız kaybettirir.
  - (d) CCVT geçicisinin "parmak izlerine" bakmak: sinyal seviyesi, uzun süre değişmeyen polarite, çevrim gerilimi seviyesi, ani değer ile filtrelenmiş değer arasındaki fark.
  - (e) CCVT transfer fonksiyonunu ters çeviren bir filtre; sahada ilgili CCVT'ye göre ayarlanması gerekir.
  - (f) Kapasitör akımını, kolonun altına takılan düşük oranlı bir CT ile ölçmek.
- Elektromekanik rölede çalışmak için gereken enerji yaklaşık sabittir. Buradan T_OP = C·(SIR+m)/(m0−m) + D (33) çıkar: eleman erişim noktasına yakın arızalarda ve yüksek SIR'de yavaşlar. Bu sayede CCVT geçicisini kendiliğinden atlatır ve fiilen bir zaman koordinasyonu yapmış olur (s.20–21).
- Mikroişlemcili röle (34) sinyal seviyesine bakmaz ve çalışma süresi eğrisi düzdür. Güvenli olması için açıkça "yavaşlatılmalıdır" (s.21). **Ders:** İyi bir TO spesifikasyonu, çalışma süresinin SIR ile ve arıza erişim noktasına yaklaştıkça arttığı anlamına gelir (s.21).

**m) Bölge 2 ve DCB koordinasyonu (s.22–23).**
- Bölge 2 için de bir hata bütçesi yapın, ama hataların bu kez eksik erişim yönünde olduğunu varsayın (s.22).
- Toprak mesafe elemanlarının rezistif arızalara duyarlılığı sınırlıdır. Bu yüzden toprak yönlü aşırı akım elemanları onları yedekler ve Bölge 2'nin güvenilirliği Bölge 1'in güvenliği kadar kritik değildir (s.22).
- Bölge 2'yi kısa devre programından alınan görünür empedanslarla ayarlayın (s.22).
- DCB'de yerel Bölge 2, karşı uçtaki Bölge 3'ten daha hassas olamaz (s.22). İki bölge aynı noktaya ayarlandığında sinyalleri aynıdır: S_OP = (m0−m)/(SIR+1+m) (35). Bölge 3 normalde daha uzağa ayarlandığı için sinyali daha büyüktür ve bu koordinasyonu kolaylaştırır (s.23).
- Zayıf sistemde yalnızca mesafe elemanına dayanan bir DCB hem güvenlik hem güvenilirlik sorunu yaşayabilir; izin verici (permissive) şema ise güvenilirlik sorunu yaşar. Yönlü aşırı akım elemanları yardımcı olur (s.23).

### Ana bulgular / öneriler
- **Ayarın temeli:** Gözlü (meshed) şebekelerde, kuplajlı hatlarda, çok uçlu hatlarda ve ara bağlantılı hatlarda erişim ayarını hat empedansına göre değil, kısa devre programından alınan en kötü durumdaki **görünür empedansa** göre yapın (s.21, s.23).
- **Bölge 1 için 13 öneri (s.21–22), özet:**
  1. Genel hata kaynaklarının hepsi zayıf sistemde de geçerlidir, üstelik etkileri orantısız biçimde büyür.
  2. Marjı hesaplamak için veri toplayın; gerekirse üreticiye başvurun. Kabloya indüklenen gerilim ya da GPR gibi belirsizlikleri ele alın.
  3. Faz ve toprak Bölge 1'inin SIR değerleri farklı olabilir.
  4. Kuplaj karmaşıksa toprak Bölge 1'ini kullanmayın.
  5. Kısa devre çalışmalarını servis dışı ve topraklı hat durumlarıyla birlikte yapın.
  6. Yeni tesislerde ve CCVT değişikliklerinde performansı modelleme ve geçmiş kayıtlarla kanıtlayın.
  7. Röle marka veya modelini değiştirirken eski ayarları doğrudan kopyalamayın.
  8. Şüphe varsa Bölge 1'i kullanmayın; yönlü karşılaştırma şemasına ve 87L'ye güvenin. Gerekirse Bölge 1 uzatma (extension) mantığını kullanın ve tekrar kapama sırasında devre dışı bırakın.
  9. Alt kademedeki koruma hızlıysa Bölge 1'e kesici süresi artı bir marj kadar gecikme vererek erişim doğruluğundan bağımsız bir zaman koordinasyonu kurun.
  10. SIR çok değişkense, aşırı akım denetimiyle Bölge 1'in yalnızca sistem güçlüyken çalışmasına izin verin.
  11. Dörtgende büyük bir aşağı eğim kullanın ve rezistif erişimi sınırlayın.
  12. Röleleri değiştirirken CCVT yükünü doğrulayın; gerekirse yük direnci ekleyin.
  13. Yeni tesislerde düşük ve hızlı sönümlenen geçicili CCVT, ekranlı kablo, iyi topraklama ve en yüksek sekonder tap kullanın.
- Zayıf sistemlerde bazı verileri elde etmek zor ya da imkânsızdır. Marjlar çok büyürse mesafe elemanı yerine yönlü aşırı akım elemanlı pilot şemaları ya da 87L kullanmak daha iyi olabilir (s.24).

### İnvertörlü şebekeler için anlamı
- Makale invertörden yalnızca bir kez söz ediyor: SIR'i kısa devre programıyla hesaplamak, rüzgâr ve invertör kaynaklarının arıza tepkisini hesaba katmayı mümkün kılar (s.15).
- *(Benim çıkarımım; 2022 makalesi de bunu destekliyor, 2022 s.13.)* İnvertör baskın bir bara doğası gereği zayıf, yani yüksek SIR'li bir sistemdir. Bu yüzden makalenin Bölüm IV–VI'daki uyarılarının hepsi geçerlidir: küçük IZ–V sinyali, GPR, kablo gürültüsü, CCVT.
- *(Benim çıkarımım.)* Dörtgenin I2 ile adaptif polarizasyonu, röle yerindeki I2 fazının arıza noktasını temsil etmesine dayanır (s.11–12). İnvertör I2'yi kendi kontrolüyle belirlediğinde bu varsayım bozulur ve Θ hatası büyür; (18)–(19) bu durumda rezistif erişimi çok sınırlar.
- Frekans sapması (s.6) ve sabit-reaktans/sabit-endüktans ayrımı, frekansın oynak olduğu düşük ataletli şebekelerde doğrudan önem kazanır.

### Projeyle bağlantı
- **Ortak dil:** IZ–V marjı, küme tabanlı garantinin konvansiyonel karşılığıdır. Bölge 1 güvenliği, olası bütün hatalar için S_OP'un işaretinin korunması demektir; bu koşul |V_ERR| < (1−m0)/(SIR+1) şeklinde yazılabilir (s.13, (27)–(28)). Taylor'ın yaklaşımında "normal çalışma/dış arıza" ile "iç arıza" çıktı kümelerinin ayrık olması aynı rolü oynar. Konvansiyonel röle bu ayrıklığı sabit bir yüzde marjla (%20–25) satın alır.
- **Belirsizlik kümesi için hazır sayılar:** Tablo I'deki marjlar (VT %5, CT %10, hat verisi %5/%10, röle %1+%5), Θ açı hatası (5° ile 15° arası örnekler), 0,5 kV'luk GPR örneği, 66,4 V'ta 330 mV kablo gürültüsü ve Hz başına yaklaşık %1,7 frekans etkisi. Yardımcı sinyal tasarımındaki belirsizlik kümeleri en azından bu büyüklükleri kapsamalıdır *(benim önerim)*.
- **Adil bir baseline için bu makaleden çıkanlar:**
  - Zone 1: faz %80, toprak %75 ya da açık bir hata bütçesinden hesaplanmış değer.
  - Zone 2: kısa devre programından alınan görünür empedansla ≥%120.
  - k0 doğru ayarlanmış olmalı.
  - Infeed kuralı (en yakın uzak uç) ve kuplaj olasılıkları uygulanmalı.
  - Dörtgende rezistif erişim (19)'a göre sınırlanmalı.
  - Bölge 1 için SIR'e bağlı CCVT güvenlik mantığı (gecikmesi dahil) açık olmalı.

  Bu öğelerin herhangi biri eksik bırakılırsa, öğrenilmiş dedektör ya da yardımcı sinyal yöntemi "kötü ayarlanmış" bir röleyle karşılaştırılmış olur.
- **Negatif bileşen enjeksiyonu ile etkileşim** *(benim çıkarımım)*:
  - (i) Reaktans karşılaştırıcı I2 ile polarize ediliyorsa, arıza sırasında süren bir enjeksiyon röle yerindeki I2'nin açısını değiştirir. Bu ek açı Θ'ya eklenir ve (18) üzerinden rezistif erişim sınırını küçültür. Örneğin toplam Θ = 5° olursa, %80 reaktif erişimde R_B yaklaşık 2,3·Z ile sınırlanır (s.11).
  - (ii) Metalik arızada enjeksiyon çevrimin V/I oranını bozmaz (bkz. 2022 bölümü). Rezistif arızada ise I_Y/I_X oranını, dolayısıyla Z_ERR = R_F(1 + I_Y/I_X)'i (13) değiştirir. Zayıf sistemde S_OP SIR 20'de %1'in altında olduğundan (s.13), bu ikinci dereceden etkiler bile Bölge 1 marjı içinde hesaba katılmalıdır.
  - (iii) I2–I0 açısına dayanan arızalı çevrim seçimi de etkilenebilir; bkz. 2022, s.5.

### Açık sorular / fikirler
- Tablo I'deki marjlar kullanılarak bir "belirsizlik politopu" kurulabilir. Konvansiyonel rölenin bu politop altındaki en büyük güvenli erişimi ile yardımcı sinyal yönteminin garanti ettiği kapsama aynı tablo üzerinde karşılaştırılabilir.
- Makale, mikroişlemcili rölenin çalışma süresinin SIR ve arıza konumuyla artmasını istiyor (s.21). Yardımcı sinyal yöntemi için de "karar süresi – SIR – konum" eğrisi çıkarılabilir mi?
- 15° örneğindeki 1,5 ile 1,15 farkı: (19) ve Şekil 12 tutarlı biçimde yaklaşık 1,15 veriyor. Projede metindeki sayı değil, (19) kullanılmalı.
- GPR ve kabloya indüklenen gerilim, simülasyonlarda genellikle hiç modellenmiyor. Test düzeneğine bunlar için "sabit gerilim hatası" kanalları eklenmeli.

---

## 2. Kasztenny (2022) — Alışılmadık kaynakların yakınında mesafe elemanları

- **Künye:** Bogdan Kasztenny (SEL), "Distance Elements for Line Protection Applications Near Unconventional Sources". 58th Annual Minnesota Power Systems Conference'ta (Kasım 2022) sunuldu; daha önce 49th WPRC (Ekim 2022), 75th Georgia Tech PRC (Mayıs 2022) ve 75th CPRE'de (Mart 2022). Kapakta "original/revised edition released June 2021" yazıyor. 18 numaralı sayfa ve kapak (PDF 19 sayfa).
- **Tek cümlede:** Bugünkü mesafe elemanlarının hafıza polarizasyonu ve negatif bileşen akımı gibi "senkron makineye özgü" varsayımları rüzgâr ve invertör kaynaklarının yakınında çöker; makalenin çözümü, yalnızca çevrimin V ve I değerlerini kullanan ofset görünür-empedans karakteristiklerini kaynağın değil sistemin arıza katkısına dayanan yön elemanlarıyla (32G, 32WI, TD32) yönlendirmektir.

### Ne öğretiyor

**a) Bugünkü pratik (s.1).** Alışılmadık kaynakların yakınındaki hatlar bugün şöyle korunuyor:
- 87L ve zayıf-besleme (weak-infeed) pilot mantığı; ikisi de güçlü uçtan gelen arıza akımına dayanır.
- 32Q yerine 32G; sıfır bileşen akımı, bağlantı transformatörünün topraklı yıldız sargısından gelir.
- Faz arızaları için artımsal (incremental) yön elemanları.
- Mesafe elemanları çoğu zaman kanal varken kapalı tutulur ve ancak kanal kaybolunca devreye alınır.
- Zaman gecikmeli toprak aşırı akım yedeği ve kaynak ucunda düşük gerilim (undervoltage) yedeği.
- Zaman gecikmeli mesafe yedeği zor ya da imkânsız olabilir; o zaman yerel yedek (yedeklilik, kesici arıza koruması, DTT) gerekir.

Kanal arızalanınca hem hat koruması hem sistem yedeği sorunlu hâle gelir. Hattı servis dışı bırakmak da istenmez, çünkü kaynağın yakınında çoğu zaman ağ yedekliliği yoktur (s.1–2).

**b) Senkron makinenin "sessiz" varsayımları ve bozulmaları (s.2–6).**
1. **Hafıza polarizasyonu ve atalet (s.2–3).** Senkron rotor, arızadan sonra en az birkaç yüz ms boyunca hızını korur; röle de bu sayede kaynak geriliminin açısını takip edebilir. Hafızanın asıl amacı yön bilgisidir; ikincil faydası, dinamik genişleme sayesinde rezistif kapsamadır. Ayrıca yakın üç fazlı arızaya karşı güvenlik ve güvenilirlik sağlar. İnvertörün ise mekanik ataleti yoktur: arızada açısı kayabilir ve frekansı yanlış ölçebilir. Üç fazlı arızada frekansı ölçebileceği güvenilir bir sinyal kalmayınca kendi frekansına tepki verir ve kararsız bir geri besleme döngüsünde frekansı yükseltip alçaltabilir. Sonuç güvenlik kaybı (geri arıza ileri görünür), güvenilirlik kaybı ya da çatırdama (chattering) olur; çatırdama zaman gecikmeli yedeğin çalışmasını engeller. **Kural:** Alışılmadık kaynakların yakınında hafıza polarizasyonundan kaçının (s.3, s.6). Tarihsel not: ilk mesafe elemanları ofset ve self-polarize idi; hafıza polarizasyonu ancak mikroişlemcili rölelerle yaygınlaştı (s.3).
2. **Düşük atalet ve infeed: "arıza devam ederken başlayan güç salınımı" (s.3–5).** Rezistif iç arızada Z_ERR = R_F·(1 + I_Y/I_X) (3), dış arızada Z_ERR = Z_W·I_Y/I_X (4) olur. Yüksek ataletli bir sistemde I_Y/I_X oranı sabittir. Düşük ataletli bir sistemde ise I_Y/I_X = K_XY·1∠(360°·Δf·Δt) (5) şeklinde döner.
   - **İşlenmiş örnek (s.4):** 60,00 Hz ile 60,25 Hz arasındaki fark saniyede 90° döndürür, yani 0,5 s'de 45°.
   - Yerel frekans daha yüksekse görünür empedans saat yönünde döner ve önce aşırı erişim olur; daha düşükse saat yönünün tersine döner ve önce eksik erişim olur (s.4).
   - Zayıf yerel kaynakta K_XY değeri 1'den büyüktür, bu yüzden dönüş dairesi büyüktür (s.4).
   - Bu bir polarizasyon sorunu değildir: mho'yu da dörtgeni de etkiler. Bu yüzden eksik erişimli bölgeler yalnızca kısa bir süre devrede tutulabilir. Güç salınımı bloklaması burada işe yaramaz, çünkü salınım arıza hâlâ sürerken çok hızlı başlar (s.5).
3. **Negatif bileşen tepkisi (s.5).** Senkron makinede I2, V2'yi sabit ve düşük bir Z2 üzerinden izler. Üç koruma ilkesi buna dayanır: 32Q, I2–I0 ve I2–V1 açılarıyla arıza tipi ve arızalı çevrim seçimi, dörtgende I2 ile reaktans polarizasyonu. İnvertörde I2, V2'yi izlemez; büyüklüğü düşük olabilir ve açısı V1, V2 ve I0'a göre hızla değişebilir. **Kural:** Kaynaklar senkron makineye benzer bir negatif bileşen açı tepkisi verene kadar, mesafe mantığında I2 kullanmaktan kaçının (s.5–6).
4. **Mho genişlemesi (s.5).** Senkron makinenin Z1'i endüktif ve sabit olduğu için mho, −90° doğrultusunda aşağı doğru uzar, orijini güvenle içine alır ve sağa doğru genişler. İnvertörün arıza akımı ise nominalin yaklaşık iki katıdır ve gerilimden 90° geri olmayabilir; Z1'i rezistif ve değişken olabilir. Bu yüzden mho aşağıya değil yana doğru uzayabilir (s.5–6).
5. **Düşük ve bozuk sinyaller (s.5–6).** Gerilim çok düşer; akımda gecikmiş sıfır geçişleri ve şebeke frekansının altında ve üstünde enerji bulunur. Ayrıca iki baskın frekans aynı anda görülebilir (örneğin 60,25 Hz ve 60 Hz) (s.6).

İnvertörlerin arıza davranışı yazılım güncellemeleri ve yeni şebeke kurallarıyla zaman içinde değişmektedir. Doğru yaklaşım bu davranışı öğrenip kullanmaya çalışmak değil, kaynaktan olabildiğince bağımsız ilkeler tasarlamaktır (s.6).

**c) Görünür empedans hâlâ çalışır (s.6–7).** Yaklaşık 250 Hz'in altında hat bir R-L devresidir: v = R·i + L·di/dt. Bu ilişki akımın biçiminden bağımsızdır; kaynak ne kadar tuhaf bir akım verirse versin V = Z_APP·I geçerlidir (s.6–7). Saha kaydı: rüzgâr çiftliğinin beslediği bir BG arızasında akım çok bozuktu, ama görünür empedans sabit kaldı ve arızayı doğru yerde, yaklaşık 7,4 Ω sekonderlik hattın %30'unda gösterdi (s.7).

**d) Ofset (yönsüz) karakteristikler (s.7–8).**
- Yakın bolted (sıfır dirençli) arızada gerilim sıfıra yakın olduğu için karakteristik geriye doğru ofsetlenir ve orijini içine alır. Bunun bedeli elemanın yönsüz olmasıdır; yön bilgisi ayrı elemanlardan alınır (s.7).
- Ofset mho'nun yakın rezistif arızalardaki kapsamı sınırlıdır. Geri erişim büyük ayarlanırsa da yüke tecavüz edebilir. Çözüm ofset dörtgendir: sağ kör çizgi rezistif kapsamı açıkça belirler, sol kör çizgi sağdakine eşit ya da daha küçük olur (s.7).
- Bölge 1'de reaktans çizgisi kalıcı olarak aşağı eğilir; Bölge 2'de yukarı eğilir (s.8). Bölge 1'de I2 ya da I0 ile polarizasyon kullanılamadığı için güvenliği bu sabit eğim sağlar.
- **Ayar kuralları (s.8):** İleri erişim standart pratiğe göre ayarlanır. Geri erişim orijini güvenle kapsayacak kadar, tipik olarak hat empedansının %10–30'u olur. Sağ kör çizgi hat yüklenebilirliğine göre ayarlanır.
- Bu karakteristiklerin hepsi self-polarizedir, yani yalnızca çevrimin V ve I değerlerini kullanır. Kaynak frekansı tutamıyorsa aşağı eğim güvenliği garanti etmez. Bu durumda Bölge 1 kısa bir süre sonra devre dışı bırakılmalıdır (s.8).

**e) Kaynaktan bağımsız yön elemanları (s.9–12).**
- **32G (s.9):** Bağlantı transformatörü sistem tarafında topraklı yıldızdır. Transformatörün sıfır bileşen empedansı V0 ile I0'ı birbirine bağlar; bu yüzden salınım ya da frekans sapması olsa bile V0, I0'ı izler. Bilinen zayıflıkları kuplaj ve faz arızalarındaki CT doymasıdır. Toprak elemanlarında izin verici (permissive) mantıkla kullanılır.
- **32WI (zayıf-besleme yön mantığı, s.9–10):** Bu bir pilot şema değil, mesafe elemanı için yeni bir yön denetimidir. Fikir şudur: ileri arızayı tespit etmeye uğraşmak yerine geri arızayı tespit edip bloklamak; çünkü geri arızayı kaynak değil güçlü sistem besler. Faz-faz akımı çalışma sinyali olarak kullanılır ve sağlam faz gerilimi ya da V1 ile çapraz-faz polarize edilir. Yakın üç fazlı geri arızada hafıza polarizasyonu kullanılabilir, çünkü geri arızada hat ucu gerilimini sistem ayakta tutar (s.9). İleri arızada 32WI'nın kesinlikle çalışmaması gerekir; bunu aşırı akım eşiği sağlar:
  - **Ayar kuralı (6):** 1,25·I_FWD(MAX) < 50WI < 0,8·I_REV(MIN). Bu %25 marj demektir ve kaynak zayıf olduğu için genellikle sağlanması zor değildir (s.9–10).
  - Alternatif olarak, ofset karakteristiğin geri erişiminden daha uzağa ayarlanmış ve (6)'ya göre aşırı akım denetimli, geriye bakan bir faz mesafe elemanı kullanılabilir (s.10).
  - *(Benim açıklayıcı örneğim: İnvertör ileri arızaya en fazla yaklaşık 2 pu besliyorsa — makale yaklaşık 2 kat diyor, s.5 — 50WI > 2,5 pu olmalıdır. Bu durumda en zayıf geri arızanın akımı 2,5/0,8 ≈ 3,1 pu'nun üzerinde olmalıdır.)*
- **TD32 (artımsal yön elemanı, s.10–12):**
  - Arızanın karşı tarafındaki devre ilk birkaç ms boyunca endüktifse doğru çalışır (s.10).
  - İnvertör tarafında bağlantı transformatörü her zaman vardır (s.10). İnvertördeki L-C devresinde, artımsal devrede kapasitör kısa devre gibi davranır; bu yüzden kaynak, kontrol algoritmaları devreye girene kadar endüktif görünür (s.10–11).
  - Tip III rüzgâr türbininde endüktif tepki uzun sürer (s.11).
  - Artımsal gerilim ile artımsal replika akımı zıt polaritedeyse TD32 "ileri" kararı verir (s.11).
  - Uzak uç daha güçlüyse TD32'yi bloklama mantığında (TD32R) kullanmak avantajlıdır; yerel uç daha güçlüyse izin verici mantıkta (TD32F). İnvertör ucu bugün genellikle zayıf taraf olduğu için orada bloklama mantığı önerilir (s.11).
  - TD32 kararı yalnızca anlık olarak verdiği için zamanlayıcılar gerekir. T1 (pickup) yaklaşık 1/8–1/4 çevrimdir. T2 (dropout), kesici arıza dahil, yakın geri arızaların en kötü temizleme süresinden uzun olmalıdır (s.11).
  - **Bölge 1 penceresi (s.11–12):** T3 (dropout) yaklaşık 2–3 çevrimdir ve Bölge 1'e iç arızada çalışabilmesi için kısa bir pencere açar. Pencere kapanınca Bölge 1, T4 (dropout, yaklaşık 1 s) boyunca devre dışı kalır. TD32.REV kararı çok hızlıdır (1–2 ms); TD32 yoksa yaklaşık yarım çevrimlik bir koordinasyon gecikmesi gerekir (s.13).
  - TD32'nin ARMED (kurulu) biti, güvenilirlik ya da güvenlik lehine eğilim seçmek için kullanılabilir. Bu, hafıza devresinin canlı gerilime kilitli olup olmadığını izlemeye benzer (s.12).

**f) Arızalı çevrim seçimi: düşük gerilim (s.12).** Kaynak zayıf olduğu için arızalı çevrimin gerilimi belirgin biçimde düşer. Seçim ya çevrim başına eşiklerle (THRS.LG / THRS.LL) ya da en düşük çevrim gerilimiyle yapılır. İkinci yöntemde 1,1 çarpanı, gerilimi birbirine yakın birden fazla çevrimi birlikte serbest bırakır ve seçimin bu çevrimler arasında gidip gelmesini (chatter) önler (s.12).

**g) Aşırı akım denetimi (s.12–13).** Bu denetimin asıl amacı, sistem enerjisizken elemanın sahte çalışmasını önlemektir. İnvertörlü kaynakta seçenekler şunlardır:
- çok düşük bir eşik ve kısa bir dropout zamanlayıcısı;
- artımsal aşırı akım elemanı ve bir uzatma zamanlayıcısı (bunun dezavantajı, akım sıfıra düştükten sonra da izin vermesidir);
- toprak elemanları için 3I0 dengesizlik denetimi (yararlıdır).

Faz elemanları için 3I2 ile yapılan dengesizlik denetimi güvenilir değildir, çünkü I2 düşük ve modüle edilmiştir (s.13).

**h) Tam mantık ve bölgelere göre uygulama (s.13–15).** Bir mesafe elemanının altı alt bileşeni vardır:
1. ölçüm (mho veya reaktans karşılaştırıcı);
2. yön denetimi;
3. arızalı çevrim seçimi;
4. rezistif kör çizgi;
5. aşırı akım denetimi;
6. güvenlik mantığı (dış arızanın temizlenmesi sırasındaki geçiciler, CCVT geçicileri vb.).

Bunlardan 1–3 invertör yakınında temelden sorunludur; 4–6 düşük sinyale rağmen çalışır (s.13).
- **Bölge 1:** Zayıf sistemin geçici aşırı erişim sorunlarına (CCVT geçicileri, GPR, kuplaj; makale bunlar için 2021 makalesine atıf yapıyor) karşı ek denetim gerekir. Ayrıca kısa pencereden (TD32.Z1) sonra ya da biriken frekans farkı bir eşiği aşınca devreden çıkarılmalıdır. Arızanın başındaki infeed etkisine karşı ya mho ya da saat yönünde (aşağı) eğilmiş bir dörtgen kullanılmalıdır (s.13–14).
- **Bölge 2:** Saat yönünün tersine (yukarı) eğim kullanılmalı, erişime cömert bir marj ya da bileşik bir karakteristik verilmelidir (s.14).
- **Kademeli mesafe:** Yönsüz bırakılabilir. Bir koordinasyon basamağı kabul edilebilir, iki basamak kesinlikle iyidir. İki bara öteye ulaşmak gerektiğinde bileşik karakteristik kullanılır: ileri ofsetli mho (B) ile geri ofsetli dörtgen (A). B'nin dairesel biçimi bir sadeleştirme değildir; frekans sapmasıyla dönen infeed hatası düşünüldüğünde en uygun biçim budur (s.14).
- **Uygulama notları (s.14–15):**
  - Toprak elemanlarında 32G izin verici, faz elemanlarında 32WI bloklayıcı mantıkla kullanılır. 32WI ancak (6) sağlanabiliyorsa kullanılabilir; sağlanamıyorsa TD32 onun yerine geçer.
  - Bu "zayıf-besleme mesafe elemanları", ataleti yüksek geleneksel sistemlerde bugünkü elemanlardan **kötü** performans gösterebilir. Bu yüzden Şekil 25'teki gibi aşırı akım denetimiyle sistem güçlüyken geleneksel elemanlar, zayıfken zayıf-besleme elemanları seçilmelidir (s.15).

**i) Ek bölüm: zaman alanında geniş bantlı R-L tahmini (s.16–18).**
- Yöntem min Σ(v − R·i − X·i_DER)² problemini en küçük kareler yöntemiyle çözer: (7)–(11). Kapalı form çözüm R = (D·C − B·E)/(A·C − B²), X = (A·E − B·D)/(A·C − B²) biçimindedir (s.16–17).
- Faydaları (s.16):
  - pencere zaman geçtikçe uzar: örneğin arızadan 5 ms sonra başlar, T = 25 ms'de 20 ms, 40 ms'de 35 ms uzunluğa ulaşır;
  - birkaç yüz Hz'lik bir bandın enerjisini kullanır;
  - frekans ölçümüne ihtiyaç duymaz;
  - sabit-endüktans yöntemidir, yani frekans kompanzelidir.
- **Saha örneği, işlenmiş (s.17–18):**
  - Bir CA arızasında çevrim gerilimi 2,7 V tepe değere düştü; arıza öncesi değer 168 V tepeydi. Arızalı çevrimin akımı yük akımının yalnızca iki katıydı (s.17).
  - Hat Z1 değeri yaklaşık 0,41 Ω sekonderdi. Ölçülen X ≈ 0,25 Ω (%61) ve R ≈ 0,6 Ω çıktı; yani arıza hat üzerinde ve rezistifti (s.18).
  - 0,0161 pu gerilimden SIR ≈ 0,61·(1/0,0161 − 1) = 37 bulunur (s.18).
  - Arıza uzak uçta olsaydı çevrim gerilimi 1/38 = 0,026 pu olurdu (s.18).
  - Pencere, arızadan 5 ms sonra 10 ms ile başlayıp 40 ms'ye kadar büyür, sonra kayar (s.18).

### Ana bulgular / öneriler
- Alışılmadık kaynakların yakınında şunlardan kaçının (s.15): hafıza polarizasyonu, I2 ile reaktans polarizasyonu, 32Q yön denetimi ve I2 ile çevrim seçimi.
- Görünür empedans ilkesi, kaynak çok düşük ve bozuk akım verse bile çalışır (s.6–7, s.15).
- Düşük ataletli bir kaynak frekansı tutamazsa infeed hatası döner. Bu "arıza temizlenmeden başlayan güç salınımı", yavaş temizlenen dış arızalarda Bölge 1'i, zamanlayıcı dolarken de kademeli mesafeyi tehdit eder (s.4–5, s.15).
- Çözüm paketi (s.15–16):
  - ofset karakteristikler;
  - 32G (izin verici), 32WI (bloklayıcı) ve TD32 (izin verici ya da bloklayıcı);
  - düşük gerilime dayalı çevrim seçimi;
  - zaman penceresiyle sınırlı Bölge 1;
  - yönsüz kademeli mesafe.
- Sayısal ayarlar: 50WI için (6); geri erişim %10–30; T1 1/8–1/4 çevrim; T3 2–3 çevrim; T4 yaklaşık 1 s; TD32.REV 1–2 ms (s.8–13).
- Kullanıcı bu elemanları bugün de, birçok rölede bulunan altı çevrimli ofset karakteristikler, programlanabilir mantık ve gerilim elemanlarıyla kurabilir (s.16).

### İnvertörlü şebekeler için anlamı
Bu makale doğrudan bu konuyla ilgili. Özetle:
- Bir **yöne karar vermek** için kaynağa değil sisteme ve pasif sıfır bileşen şebekesine dayanılmalıdır.
- **Erişimi ölçmek** için polarizasyona değil yalnızca V/I'ya dayanılmalıdır.
- **Zamanı sınırlamak** gerekir: Bölge 1 için kısa bir pencere, ardından devre dışı.
- **I2'ye güvenilmemelidir.**

Makalenin önemli bir uyarısı: invertörlerin arıza davranışı zamanla değişiyor (s.6). Kaynağın davranışına dayanan her yöntem, sonraki bir yazılım güncellemesiyle geçersiz hâle gelebilir.

### Projeyle bağlantı
- **Merkezi gerilim:** Makale "kaynaklar senkron makineye benzer bir negatif bileşen açı tepkisi verene kadar I2 kullanmayın" diyor (s.5). Yardımcı sinyal yöntemi ise tam olarak invertörün I2'sini bilerek **tasarlıyor**. Bu iki şekilde sonuçlanabilir *(benim çıkarımım)*:
  - (a) Enjeksiyon öngörülebilir, bilinen bir I2 imzası üretir; bu, makalenin aradığı "kontrollü negatif bileşen davranışının" bir biçimi olabilir.
  - (b) Enjeksiyon V2'den bağımsız bir akım kaynağı gibi davranırsa, 32Q'nun ölçtüğü Z2 değeri anlamsızlaşır.
- **Normal çalışmada sürekli enjeksiyon** *(benim çıkarımım; makalelerde test edilmemiş)*: Röle arkasındaki invertör I2 enjekte ederse, basit iki uçlu bir sistemde röle ileri yönde akan bir I2 ve V2 ≈ (Z_L2 + Z_R2)·I2 görür. 2012 makalesindeki (5) formülüne göre Z2ölç pozitif olur ve bu bir **geri arıza** imzasıdır (2012, Şekil 24). 32Q'yu etkinleştiren eşikler aşılırsa (I2 büyüklüğü veya I2/I1 oranı; *genel bilgi*) şu sonuçlar olabilir:
  - DCB şemasında invertör ucundaki geri eleman sürekli blok sinyali gönderir ve karşı ucun iç arızadaki güvenilirliği bozulur;
  - POTT şemasında izin sinyali kesilir;
  - negatif bileşen aşırı akım (46/50Q/51Q) elemanları çalışabilir.

  Baseline senaryolarında bu durumlar mutlaka test edilmeli ve enjeksiyon genliği röle eşikleriyle koordine edilmelidir.
- **Metalik arızada görünür empedans enjeksiyondan etkilenmez** *(makalenin s.6–7 bulgusundan benim çıkarımım)*: Metalik arızada arızalı çevrimin arıza noktasındaki gerilimi sıfırdır. Bu yüzden röleden hangi akım akarsa aksın V_çevrim = m·Z_L·I_çevrim geçerlidir; örneğin BC arızasında V1 − V2 = m·Z_L1·(I1 − I2) olur. Self-polarize ofset elemanların görünür empedans ölçümü bu nedenle metalik arızada enjeksiyondan bağımsız kalır. Rezistif arızada ise enjeksiyon I_X'i, dolayısıyla I_Y/I_X oranını ve Z_ERR'yi değiştirir; (3) bunu hesaplamaya izin verir.
- **50WI ile etkileşim** *(benim çıkarımım)*: İnvertör arıza sırasında ek akım enjekte ediyorsa, bu akım (6)'daki I_FWD(MAX) içine dahil edilmelidir; yoksa 32WI ileri arızada yanlışlıkla çalışabilir.
- **TD32 ile etkileşim** *(benim çıkarımım)*: TD32, arıza öncesi değerlerden farkları kullanır. Arızadan önce sabit duran bir enjeksiyon bu farklarda kaybolur. Ancak zamanla modüle edilen bir yardımcı sinyal ya da arıza anında değişen bir enjeksiyon "artımsal" görünür. Enjeksiyon kontrolcüsünün ilk birkaç ms içinde kaynağın endüktif görünmesini bozmadığı doğrulanmalıdır (s.10–11).
- **Adil baseline'a eklenmesi gerekenler:** İnvertör ağırlıklı senaryolarda baseline yalnızca "geleneksel" röle olmamalıdır (hafıza polarizeli mho, I2 polarizeli dörtgen, 32Q). Bu makaledeki zayıf-besleme tasarımını da içermelidir: ofset karakteristikler, 32G, (6)'ya göre ayarlı 32WI, T1/T2/T3/T4 zamanlayıcılı TD32, düşük gerilime dayalı çevrim seçimi ve isteğe bağlı olarak zaman alanı R-L tahmincisi. Aksi hâlde karşılaştırma bir "saman adam" ile yapılmış olur. Şekil 25'teki güçlü/zayıf anahtarlama da baseline'ın bir parçası olmalıdır.
- **Öğrenilmiş dedektör için uyarı:** İnvertörlerin arıza davranışı yazılım güncellemeleriyle değişiyor (s.6). Bu yüzden eğitim ve test verisi farklı kontrol sürümlerinden veya parametrelerinden gelmeli, dağılım kaymasına karşı dayanıklılık ayrıca ölçülmelidir *(benim önerim)*.

### Açık sorular / fikirler
- Yardımcı sinyal, invertörün negatif bileşen tepkisini "endüktif Z2 benzeri" yapacak biçimde tasarlanabilir mi? Öyle olursa 32Q ve I2 polarizasyonu yeniden kullanılabilir hâle gelir mi?
- Bölge 1 penceresi (T3 2–3 çevrim) ile CCVT güvenliğinin istediği gecikme çelişiyor (bkz. 2023 bölümündeki SIR 37 hesabı). Yardımcı sinyal bu çelişkiyi çözebilir mi?
- Δf kaynaklı dönen infeed hatası (5), küme tabanlı bir garantide zamanla büyüyen bir belirsizlik kümesi olarak modellenebilir mi?
- Zaman alanı R-L en küçük kareler tahmini aslında bir sistem tanılama problemidir. Yardımcı sinyal bu tahminin koşul sayısını, yani A·C − B² paydasını, iyileştirmek için tasarlanabilir mi?

---

## 3. Kasztenny & Chowdhury (2023) — Yüksek SIR ve CCVT'li sistemlerde Bölge 1 güvenlik kriteri

- **Künye:** Bogdan Kasztenny ve Ritwik Chowdhury (SEL), "Security Criterion for Distance Zone 1 Applications in High SIR Systems With CCVTs". 50th WPRC'de (Ekim 2023) sunuldu; ilk olarak 76th Georgia Tech PRC'de (Mayıs 2023). 17 numaralı sayfa ve kapak (PDF 18 sayfa).
- **Tek cümlede:** Yüksek SIR'de Bölge 1'in güvenli olup olmadığı, gerçek IZ–V sinyalinin (1−m1)/(SIR+1) bütün "sabit" hataları — CCVT geçicisi, VT ve rölenin mutlak hatası, GPR, kuplaj — aşması koşuluna indirgenir; makale bunun için elle hesaplanabilen kriterler veriyor.

### Ne öğretiyor

**a) Problem (s.1–2).** Bölge 1'in yön denetimi geri arızalara karşı korur. Bu yüzden Bölge 1 güvenliği yalnızca ileri yöndeki dış arızalarda **aşırı erişim** sorusudur. Aşırı erişimin iki türü vardır:
- **geçici aşırı erişim:** başlıca CCVT kaynaklıdır;
- **kalıcı (persistent) aşırı erişim:** VT/CT oran hataları, hat empedansı hataları, infeed, kuplaj ve GPR kaynaklıdır (s.1).

Üreticiler "SIR 30'a kadar ve her CCVT ile %5 TO" gibi beyanlar veriyor; bu beyanlar bazen belirsiz ve ara sıra yaşanan yanlış çalışma raporlarıyla çelişiyor (s.1–2). IEEE C37.113-2015'in kısa/orta/uzun hat sınıflaması pratik bir kriter olamayacak kadar basit (s.1).

**b) Ortak kriter (s.2–3).** Ölçülen sinyal (IZ − V)_ÖLÇ = (IZ − V)_GERÇEK + V_HATA (1) şeklindedir; eleman güvenli kalır, eğer |(IZ − V)_GERÇEK| > |V_HATA| (2). Polarize sinyal (hafıza ya da akım) gerilim hatalarından etkilenmez. Bu yüzden aynı kriter mho ve dörtgen için geçerlidir (s.2). Sinyal |m − m1|/(SIR + m) (3) olduğundan, uzak bara arızası (m = 1) için kriter şu hâle gelir (s.3):

  **(1 − m1)/(SIR + 1) > |V_HATA(pu)|   (5)**

- **SIR (s.3):** Röle geriliminin uzak bara arızasındaki değerine dayanan tanım artık yaygın kabul görüyor. SIR_LL faz elemanları, SIR_LG toprak elemanları içindir. Topraklama yolları nedeniyle SIR_LG genellikle daha düşüktür.
- **Oran hatası ile sabit hata ayrımı (s.3):**
  - *Oran hataları* ölçülen büyüklükle orantılıdır ve yüzdeleri toplanarak erişimden düşülür. **Örnek:** %2 V, %5 I ve %5 Z hataları %12 eder, yani Bölge 1 < %88.
  - *Sabit hatalar* ölçülen büyüklükten bağımsızdır: CCVT geçicisi gerilim *değişimiyle* orantılıdır, kuplaj gerilimi komşu hattın akımıyla orantılıdır. Bunlar oran hataları düşüldükten sonra (5) ile ayrıca ele alınır.

**c) Geçici (CCVT) kriteri (s.3–8).**
- CCVT geçicisi bir sayı değil, POW'a bağlı bir zaman serisidir. Röle bu geçiciyi filtreler; ayrıca CCVT'den CCVT'ye çok farklıdır ve etiket bilgisinden çıkarılamaz (s.4).
- **Anahtar fikir (s.4):** Bölge 1, erişim noktasının hemen ötesindeki bir dış arızada yanlış çalışacaksa, bunu yaklaşık olarak erişim noktasının hemen berisindeki bir iç arızada çalıştığı sürede (T_OP) yapar. Bu yüzden üreticinin yayımladığı çalışma süresi, elemanın iç gecikmesinin bir ölçüsü olarak kullanılabilir.
- Kullanıcının ek gecikmesi T_D ve filtre penceresi W ile birlikte: t > T_OP + T_D − W için (1−m1)/(SIR+1) > |E_CCVT(pu)|(t) koşulu aranır (6). W = 1 çevrim alınır, çünkü yanlış çalışma geç olur (1–1,5 çevrim sonra) (s.5). Yüksek SIR'de ve erişim noktasına yakın arızada Bölge 1 normalde 1,5 çevrimden hızlı çalışmaz. İlk yarım çevrimde gerilim zaten düşmektedir; bu yüzden t > max(0,5 çevrim, T_OP − 1 çevrim) + T_D (8) yazılır (s.5).
- **Standartlar (s.5–6):** IEC 61869-5 üç, Draft IEEE PC57.13.9 iki geçici sınıfı tanımlar ve bu sınıflar birbirinin aynısı değildir. İkisi de ilk 0,5 çevrim için şart koymaz. Zarf (envelope) yüzdesi arıza gerilimine değil, **arıza öncesi tepe gerilimine** göredir. Bu yüzden %10'luk bir zarf hatası "erişimi %10 kısaltarak" karşılanamaz (s.6). Sahadaki CCVT'ler muhtemelen hiçbir sınıfa uymaz. Üreticiden zarfı ya da sıfır geçişi ve tepe noktasında başlayan iki arıza için test eğrilerini isteyip ikisinin büyüğünden bir zarf çizin (s.6).
- **Uzak bara için ölçekleme (s.6):** Uzak bara arızasında gerilim değişimi ΔV = SIR/(SIR+1) (9) olduğundan |E_CCVT| = [SIR/(SIR+1)]·|E_ZARF| (10) ve 1 − m1 > SIR·|E_ZARF|(T0) (11) elde edilir.
- **Filtre zayıflatması (s.7):** Tam çevrimlik Fourier ve kosinüs filtreleriyle yapılan EMT simülasyonlarında, 1,5 çevrimden sonraki en kötü zayıflatma A = 2,5 bulundu; yani filtre zarfı %40'ın altına indirir. (Tek bir CCVT için örnek: ham geçici 0,2 pu, filtrelenmiş 0,05 pu ise A = 4.) A'nın evrensel olması bekleniyor, çünkü CCVT'ler iyi bilinen kurallarla tasarlanır ve az sayıda parametreyle tanımlanır.
- **Nihai kriter (13), s.7:**

  **1 − m1 > 0,4 · SIR · |E_ZARF|(T0)/100%,  T0 = max(0,5 çevrim, T_OP − 1 çevrim) + T_D**

  Bu kriteri sağlamak şu durumlarda kolaylaşır: erişim kısa, SIR düşük, zarf küçük, röle yavaş veya ek gecikme uzun (s.7–8).
- **Grafik form (14), s.8:** |E_ZARF|(T0) < 2,5·(1−m1)/SIR·%100. Zarf grafiğine bir yatay ve bir dikey çizgi çizilir; kesişim noktaları zarfın üstündeyse uygulama güvenlidir.
- **Adım adım prosedür (s.8):**
  1. Bütün olasılıklar için en yüksek SIR'i bulun.
  2. Üreticinin eğrisinden bu SIR'e ve yayımlanan en uzak arıza konumuna karşılık gelen T_OP'u okuyun.
  3. m1 ile başlayın (0,75 veya 0,80) ve T_D = 0 alın.
  4. Zarfın T0 anındaki değerini okuyun.
  5. Kriteri (13) kontrol edin.
  6. Sağlanıyorsa başka çalışma gerekmez.
  7. Sağlanmıyorsa seçenekler: üreticiye danışın; m1'i azaltın; T_D ekleyin (makaleye göre yüksek SIR'de gecikme eklemek, erişimi kısaltmaktan genellikle daha etkilidir); ikisini birlikte uygulayın; ya da yeni bir tesis için gereken CCVT zarfını bu koşuldan türetin.

**d) İşlenmiş örnekler (s.8–9).** Zarf IEC 61869-5 Class 3PT2 (Şekil 6). Figürden okunan yaklaşık basamaklar: 1 çevrime kadar %25, 1–2 çevrim %10, 2–3 çevrim %2, 3–4 çevrim %0,6, 4–5 çevrim %0,2. Uzak bara arızasında röle gerilimi 0,065 pu olduğundan SIR = 1/0,065 − 1 = 14,4; Bölge 1 ayarı m1 = 0,80.

| | Röle A (T_OP = 1,5 çevrim) | Röle B (T_OP = 3 çevrim) |
|---|---|---|
| T0 | max(0,5; 0,5) + 0 = 0,5 çevrim | max(0,5; 2) + 0 = 2 çevrim |
| Zarf değeri | < %25 | < %2 |
| Kriter: 0,2 > 0,4·14,4·E ? | 0,2 > 1,44 → **sağlanmıyor** | 0,2 > 0,115 → **güvenli** |
| Gecikmeyle çözüm | Zarfın 2,5·0,2/14,4 = %3,47'nin altına inmesi gerekir; bu 2 çevrimde olur. 1,5 − 1 + T_D = 2'den T_D = 1,5 çevrim. | — |
| Erişimle çözüm | m1 < 1 − 0,4·14,4·0,25 = −0,44 → **imkânsız** | — |

**e) Kalıcı (sabit hata) kriteri (s.10–15).**
- CT hataları ve rölenin akım girişi hataları (%2–5) oran hatasıdır ve normal marjın içinde kalır. Transpoze olmayan hatta %5'lik çevrim farkları ve k0 belirsizliği de olağan marjla karşılanmış varsayılır; faz Bölge 1'i üç faz çevriminin, toprak Bölge 1'i üç toprak çevriminin en küçük görünür empedansına göre ayarlanır (s.10).
- Geriye kalan hatalar ölçülen gerilimle orantılı **olmayan** gerilim hatalarıdır. Kriter: (1 − m1)/(SIR + 1) > E_SS (15). Buradan iki eşdeğer biçim çıkar: SIR < (1−m1)/E_SS − 1 (16) ve m1 < 1 − E_SS·(SIR+1) (17) (s.10–11). **Örnek:** E_SS = 0,025 pu ve SIR = 15 ise sabit hatalar için marj en az %40 olmalı, yani erişim < %60 (s.11).
- Hatalar en kötü durumda toplanır: E_SS = E_VT + E_REL + E_GPR + E_MC (18) (s.11).
- **VT ve rölenin büyüklük hatası (s.11–12):** Ölçüm aralığının altında mutlak hatanın sabit kaldığı varsayılır: E_VT_MAG = E%·V_MIN(pu) (19) ve E_REL_MAG = E_SEC/V_NOM (20).
  - Örnek 1: VT sınıfı %0,6, aralık %90–110 → 0,0054 pu. Bu, SIR 20'de (gerilim %4,8) ölçülen değerin %11'i, SIR 30'da (%3,2) %17'sidir.
  - Örnek 2: IEC Class 6P, aralık %5–100 → 0,0030 pu; ölçülenin %6,3'ü ve %9,4'ü.
  - Örnek 3: Röle, 66,4 V nominal, "±%0,25 ya da 0,1 V" spesifikasyonu → 0,1/66,4 = 0,0015 pu.
- **Açı hatası (s.12–13):** Doğrudan ölçülen gerilimlerde (toprak elemanları veya üçgen bağlı VT) açı hatası ihmal edilebilir. Ancak yıldız bağlı VT'den türetilen faz-faz geriliminde E_ANG = 2·sin(δ/2) ≈ sin δ (21) olur. Örnek 4: 1° + 0,5° → 0,0262 pu. Birleşik hata:
  - toprak elemanı veya üçgen VT için doğrudan toplam (22);
  - yıldız VT ile faz elemanı için karesel toplam √((E_VT_MAG+E_REL_MAG)² + E_ANG²) (23).

  Tipik birleşik hata yaklaşık 0,02 pu'dur (s.13).
- **GPR (s.13–14):** V_R = Z_L·I_R + R_GPR·3I0T + R_F·I_F (24). 3I0T ile I_R aynı fazdaysa bu bileşen görünür empedansı rezistif bir arızadaki gibi sağa kaydırır; Bölge 1 güvenliğini tehlikeye atmaz ama özellikle kısa hatlarda güvenilirliği azaltabilir. Makaleye göre GPR'nin tipik sonucu toprak elemanlarında eksik erişimdir (s.13). Şebeke homojen değilse kayma aşağı eğilebilir ve aşırı erişim olur; yüksek SIR'de genişleyen hafıza polarizeli mho ya da geniş rezistif erişimli dörtgen bu nedenle aşırı erişebilir (s.13). *(Dikkat: 2021 makalesi (s.16) GPR'nin VT'yi düşük okutup aşırı erişime yol açtığını söylüyor; bkz. sözlükteki GPR maddesi.)* Kural:
  - topraklama yolu yoksa E_GPR = 0;
  - endüktif topraklama yolu varsa (en kötü 30° homojensizlik) E_GPR = 0,5·V_GPR(pu);
  - ototransformatör akımı ters çevirebiliyorsa E_GPR = V_GPR(pu).

  GPR değeri, merkezi dış tesislere bağlayan haberleşme kablolarının dayanım değerlerinden tahmin edilebilir; makale 2 kV'u makul bir tahmin olarak öneriyor [ANSI/IEEE 487], ama varsa kurumun kendi topraklama tasarım verisinin kullanılmasını söylüyor (s.13). Örnek (s.14): 0,5·2 kV/(500 kV/√3) = 0,0035 pu; 69 kV'ta 0,0251 pu.
- **Kuplaj (s.14–15):** Pozitif ve negatif bileşen kuplajı kısa devre programlarında modellenmez, ama yüksek SIR'de aşırı erişime yol açabilir. Makalenin önerdiği en kötü durum katsayısı (60 Hz): **0,100 V/(A·mil)** ya da 0,062 V/(A·km); 50 Hz'de 0,083 ve 0,052 (s.14–15). Örnek: 230 kV'luk hatta 10 mil kuplaj ve 5 kA → 5 kV. Bu, faz elemanı için %2,17, toprak elemanı için %3,77 hata eder (s.14). Hesap (26)–(27) ile primer büyüklüklerde yapılır. Bu en kötü durumdur, çünkü transpozisyon olmadığı varsayılır (s.15).
- **İşlenmiş örnekler (s.15):**
  - *Faz elemanı:* 230 kV, SIR 4, E_VT+E_REL = 0,03, 10 mil kuplajlı hatta 4 kA. E_MC = 0,1·4000·10/230 kV = 0,0174 pu; toplam 0,0474 → m1 < 1 − 0,0474·5 = **0,76**. Kuplaj olmasaydı **0,85** olurdu.
  - *Toprak elemanı:* E_VT+E_REL = 0,015; endüktif topraklama için E_GPR = 0,5·2 kV/(230 kV/√3) = 0,0075; toplam 0,0225 → m1 < **0,89**.

**f) Hataları birleştirme (s.15–16).** Oran, CCVT ve sabit hata marjları toplanır: m1 = 1 − Σmarj (28), yani m1 = m1_ORAN + m1_CCVT + m1_SABİT − 2 (30). Örnek: 0,90 + 0,90 + 0,80 − 2 = **0,60**. Sonuç negatifse Bölge 1 devre dışı bırakılır (s.16). Bunun bir başka biçimi m1 < m1_ORAN − E_SS(SIR+1) (31)'dir (s.16).

**g) IEEE C37.113 ile bağlantı (s.16–17).** Kılavuzda SIR 0,5 güçlü sistemin ("uzun hat"), SIR 4 zayıf sistemin ("kısa hat") sınırıdır. Makale %20'lik toplam marjın yarısını oran ve sabit hatalara, yarısını CCVT'ye ayırarak bu sınırları açıklıyor:
- Zarfın hep %40'ın altında kaldığı varsayılırsa (çok kötü bir CCVT bile) SIR < **0,63** çıkar.
- Oran ve sabit hatalar toplam 0,025 pu ise SIR < **3** çıkar.

Bu değerler kılavuzdaki 0,5 ve 4'e yakındır (s.16). Yorum: SIR 0,5'te uzak bara arızasında gerilim nominalin 2/3'üdür; bu, CCVT'nin ihmal edilebileceği üst sınırdır. SIR 4'te gerilim nominalin 1/5'idir; bu da kalıcı hataların ihmal edilebileceği üst sınırdır (s.17).

### Ana bulgular / öneriler
- Basit iki kriter: **geçici** (13) ve **kalıcı** (15)/(17). İkisi de yalnızca şu verileri ister: SIR, m1, T_OP, T_D, CCVT zarfı ve hata spesifikasyonları (s.2, s.8, s.15).
- Yüksek SIR'de gecikme eklemek, erişimi kısaltmaktan genellikle daha etkilidir (s.8). Örnek 1'de erişimle çözüm imkânsızken 1,5 çevrimlik gecikme yetiyor (s.9).
- Tipik birleşik VT ve röle hatası yaklaşık 0,02 pu'dur (s.13); GPR için 2 kV tahmini (s.13); kuplaj katsayısı 0,1 V/(A·mil) (s.14).
- Makale üreticilere yeni bir spesifikasyon biçimi öneriyor: "Bölge 1 güvenlik çizelgesi". Bu çizelge CCVT sınıfına, faz ya da toprak elemanına ve CCVT mantığının açık ya da kapalı olmasına göre ayrı ayrı verilir; IEC 60255-121 ya da IEEE C37.113'e girebilir (s.10).

### İnvertörlü şebekeler için anlamı
- *(Benim hesabım; 2022'deki saha örneğinin SIR'i ≈ 37, s.18.)*
  - **Kalıcı kriter:** Tipik E_SS = 0,02 pu ile (17) m1 < 1 − 0,02·38 = **0,24** verir. İnvertör baskın bir uçta Bölge 1 en fazla hattın yaklaşık dörtte birini kapsayabilir. GPR eklenirse, örneğin 69 kV'ta 0,0251 pu, sonuç negatife düşer ve toprak Bölge 1'i kullanılamaz.
  - **Geçici kriter:** 3PT2 zarfında 0,4·37·E < 0,2 olması için E < %1,35 gerekir, yani T0 ≥ 3 çevrim (zarf %0,6). T_OP = 1,5 çevrimlik bir rölede bu T_D ≥ 2,5 çevrim demektir. Oysa 2022'deki Bölge 1 penceresi yalnızca 2–3 çevrimdir (2022, s.11–12). İki gereksinim aynı anda zor sağlanıyor.
- İnvertör arıza akımını sınırladığı için (2022, s.5) arızalı çevrim gerilimi daha da düşer; makalenin "yüksek SIR" senaryosu invertörlü şebekelerde olağan durum hâline gelir.

### Projeyle bağlantı
- **En yakın kavramsal akraba:** (2)'deki |gerçek sinyal| > |sınırlı hata| koşulu, en kötü durum sınırlarıyla verilmiş bir ayrıklık garantisidir. Taylor'ın küme tabanlı garantisinin konvansiyonel karşılığı budur. Adil bir karşılaştırma için baseline rölenin güvenli erişimi ve gecikmesi **aynı hata kümeleriyle** (E_VT, E_REL, E_GPR, E_MC, CCVT zarfı, A = 2,5) hesaplanmalıdır. Ardından yardımcı sinyal yönteminin aynı kümeler altında garanti ettiği kapsama (gecikmesiz koruma altındaki hat yüzdesi) ve karar süresi bununla kıyaslanmalıdır.
- **Tespit edilebilirlik ile müdahale etmeme arasındaki gerilim** *(benim çıkarımım)*:
  - Yardımcı sinyalin rölede yarattığı gerilim imzası, bu makalenin sabit hata tabanının (yaklaşık 0,02 pu, artı GPR ve kuplaj) ve T0 anındaki CCVT zarfının belirgin biçimde üstünde olmalıdır; yoksa tespit edilemez.
  - Aynı zamanda imza, konvansiyonel elemanların (32Q, 46) eşiklerini aşmamalıdır.
  - Bu iki koşul, enjeksiyon genliği için bir alt ve bir üst sınır tanımlıyor. Bu aralığın SIR'e göre nasıl değiştiği projede çizilebilir.
- **Zaman bütçesi:** T0 = max(0,5, T_OP − 1) + T_D ifadesi, gerilime dayalı her dedektör için ilk 1–2 çevrimin CCVT tarafından kirletildiğini hatırlatır. Bir öğrenilmiş dedektör veya yardımcı sinyal kararı ilk 2 çevrimde veriliyorsa, CCVT modeli olmayan bir simülasyonla yapılan karşılaştırma adil değildir.

### Açık sorular / fikirler
- A = 2,5 bir faz büyüklüğü filtresi için türetildi. Yardımcı sinyal dedektörünün kullandığı filtre (örneğin negatif bileşen için ayrı bir dar bant) için eşdeğer zayıflatma ne olur?
- "Bölge 1 güvenlik çizelgesi" fikri, yardımcı sinyal yöntemi için "garanti çizelgesi"ne dönüştürülebilir: eksenler SIR ile m, renkler garanti edilen karar süresi.
- Kuplaj katsayısı (0,1 V/(A·mil)) pozitif ve negatif bileşen kuplajını da kapsıyor. Komşu hattaki büyük akımlar, enjekte edilen I2'nin rölede ölçülen V2 imzasını bozabilir mi?

---

## 4. Hou & Roberts (1996) — CVT'ler: geçici aşırı erişim sorunu ve mesafe rölesi için çözümler

- **Künye:** Daqing Hou ve Jeff Roberts (SEL), "Capacitive Voltage Transformers: Transient Overreach Concerns and Solutions for Distance Relaying". İlk olarak 22nd WPRC'de (Ekim 1995) sunuldu; ayrıca 49th CPRE (Nisan 1996), 50th Georgia Tech PRC (Mayıs 1996) ve 1996 Canadian Conference on Electrical and Computer Engineering'de. Revize baskı Ekim 2010. 20 numaralı sayfa ve kapak (PDF 21 sayfa). PDF taranmış bir belge; metin çıkarımında s.14 eksikti ve PDF'ten okundu.
- **Tek cümlede:** CVT geçicisini oluşturan bileşenleri (kapasitans, aktif ya da pasif ferrorezonans bastırma, yük) modelleyip SIR arttıkça Bölge 1'in güvenli erişiminin nasıl çöktüğünü gösteriyor ve düşük gerilim, düşük akım ve "mesafe hesabının düzgünlüğü" bilgilerine dayanan, ayar gerektirmeyen bir CVT geçicisi algılama mantığı öneriyor.

### Ne öğretiyor
- **Tanım (s.1):** CVT geçicisinin süresi, CVT çıkışının oran gerilimiyle örtüşmediği süredir. Geçici, temel bileşen gerilimini düşürür; hesaplanan empedans da düşer ve Bölge 1 bölge dışındaki arızalarda çalışır. Bölge içindeki bir arızada bu düşüş zararsızdır.
- **Eski çözümler (s.2):** Erişimi kısaltmak bazen Bölge 1'i etkisiz kılacak kadar kısaltmayı gerektirir. Bütün Bölge 1 çalışmalarını geciktirmek ise yakın arızaları gereksiz yere cezalandırır.
- **Bileşenler (s.2):**
  - kuplaj kapasitörleri C1 ve C2: ara gerilim tipik olarak 5–15 kV;
  - kompanzasyon reaktörü L: şebeke frekansında kapasitif reaktansı iptal ederek faz kaymasını önler;
  - ara (step-down) transformatör: röle gerilimine indirir, tipik olarak 115/√3 V;
  - ferrorezonans bastırma devresi: zorunludur, ama geçiciyi kötüleştirebilir.
- **POW etkisi (s.3):** Gerilimin sıfırdan geçtiği anda başlayan arızada çıkış 1,75 çevrim boyunca ideal çıkışa uymaz; tepe noktasında başlayan arızada bu yaklaşık 1,25 çevrimdir. Ara transformatörün dönüştürme oranı yükselince yükün kapasitörler üzerindeki etkisi azalır (s.3).
- **Kapasitans (s.5):** İncelenen CVT'lerde C1+C2 ≈ 100 nF'tır. Kapasitansı 4 kat olan bir CVT çok daha küçük bir geçici verir ve buna bağlı aşırı erişim de çok daha küçük olur. Daha yüksek kapasitans maliyeti artırdığı için bir denge kurulması gerekir.
- **Ferrorezonans bastırma devresi (s.6–8):**
  - **AFSC (aktif):** Şebeke frekansına ayarlı paralel bir LC devresi ve orta uca bağlı bir yükleme direncinden oluşur. Bir bant geçiren filtre gibi davranır, ek gecikme ekler ve enerji depolayarak geçiciyi kötüleştirir.
  - **PFSC (pasif):** Kalıcı bağlı bir direnç (Rf), nominalin yaklaşık %150'sinde doyan bir endüktör (Lf) ve hava aralıklı bir yükleme direncinden oluşur. Ferrorezonans yokken devre büyük ölçüde ayrık kaldığı için geçiciye etkisi azdır. Dezavantajı daha büyük bir ara transformatör gerektirmesidir.
- **Model (s.8–10):** Tek fazlı radyal bir sistem kullanılıyor: hat sabit, kaynak empedansı değişken. Gerilim değişimini SIR, arıza konumu ve R_F belirler. Genel röle modelinde analog kenar yumuşatma (anti-aliasing) filtresi, A/D ve seyreltme (decimation), sayısal bant geçiren filtre ve empedans hesabı var; hiçbir CVT güvenlik önlemi yok (s.10). AFSC'li CVT'nin frekans yanıtı düz değil, PFSC'li olanınki çok daha düz (s.9–10).
- **Sonuç: Şekil 14 (s.11).** Hat sonu arızası, en kötü POW (gerilim sıfırı).
  - AFSC'li CVT ile Bölge 1 en fazla SIR 4'e kadar dayanır. Ek mantık olmadan SIR ≥ 20'de Bölge 1 tamamen kaldırılmalıdır.
  - PFSC ile Bölge 1 SIR 30'a kadar etkilidir.
  - *(Figürden kabaca okuma: AFSC'de en fazla güvenli erişim SIR 5'te yaklaşık 0,7, SIR 10'da yaklaşık 0,4, SIR 15'te yaklaşık 0,13, SIR 20'de 0. PFSC'de SIR 30'da bile yaklaşık 0,9.)*
- **Yük (burden), s.12:** ANSI C93.1-1990'a göre test yükü iki paralel koldan oluşur: Rp ve güç faktörü 0,5 olan Rs+jXs. Yük, en yüksek nominal VA'nın %100'ü veya %25'idir ve toplam güç faktörü 0,85'tir. Şekil 16'da (SIR 10, 200 VA, PFSC) ANSI yükü rezistif yüke göre daha fazla aşırı erişime yol açıyor. *(Figürden: %100 yükte en fazla erişim ANSI yükünde yaklaşık 0,75 pu'ya, rezistif yükte yaklaşık 0,91 pu'ya iniyor.)* Mikroişlemcili ve statik rölelerin yükü küçük ve neredeyse rezistiftir. CVT'ye bağlı toplam yük hesaplanmalı ve aşırı olmamalı, neredeyse rezistif olmalıdır.
- **Sorunun tanımı (s.13):** Sorun yüksek SIR ile AFSC birleşince ortaya çıkar. Düşük C değeri ve ağır endüktif yük sorunu daha da kötüleştirir.
- **Önceki algılama yöntemleri ve kusurları (s.13–14):**
  - erişimi kısaltmak;
  - sabit gecikme: CVT geçicisinin süresinden uzun olmalıdır ve SIR'den bağımsız olarak her zaman uygulanır;
  - V ve I eşikleriyle "SIR algılama": aşırı akım eşiğini seçmek zordur ve yüksek SIR'de yakın ve uzak arıza akımları birbirine çok yakındır.
- **Önerilen mantık (s.14–16; patent 5,703,745):**
  - Faz-nötr ve faz-faz düşük gerilim (27) elemanı çalışır ama ilgili aşırı akım (50) elemanı çalışmazsa "HSIR" (yüksek SIR) kararı verilir. Bu durumda Bölge 1 çıkışı bir TDDO süresi kadar geciktirilir (s.14).
  - Faz-faz arızada faz-nötr gerilimi pek düşmediği için ayrı bir faz-faz düşük gerilim elemanı gerekir (s.14).
  - Eşikler, önceden belirlenmiş bir SIR değeriyle kurulan radyal model ve hat sonu arızası üzerinden **otomatik** hesaplanır (s.14–16). Kullanıcı yalnızca replika hat empedansını girer:
    - V_faz = |V0+V1+V2| = V_nom/(SIR+1);
    - V_faz-faz = |(a²−a)(V1−V2)| = √3·V_nom/(SIR+1);
    - I_faz = |3V_nom/((SIR+1)(2Z_L1+Z_L0))|;
    - I_faz-faz = |√3·V_nom/((SIR+1)·Z_L1)|.
  - Yakın arıza akımının uzak arıza akımına oranı (SIR+1)/SIR'dir. Bu yüzden yüksek SIR'de akım eşiği yakın arızaları ayırt edemez (s.16).
  - **"m-düzgünlüğü" (s.16):** Yakın arızada mesafe hesabı hızla oturur; uzak arızada ancak CVT geçicisi sönünce oturur. Eşik, deneysel olarak belirlenmiş −a·m + b biçimindedir; yakın arızada daha fazla dalgalanmaya izin verir. Hesap düzgünse gecikme atlanır.

### Ana bulgular / öneriler (s.16–17)
- En kötü CVT geçicisi, gerilimin sıfırdan geçtiği anda başlayan arızada oluşur.
- PFSC, AFSC'den çok daha küçük geçici üretir.
- Düşük SIR'de aşırı erişim her iki tip için de sorun değildir.
- Yüksek kapasitanslı CVT ve daha küçük yük aşırı erişimi azaltır. Mikroişlemcili rölelerin rezistif yükü, elektromekanik rölelerin endüktif yükünden daha az geçiciye yol açar.
- Önerilen mantığın üstünlükleri: kullanıcı ya da fabrika ayarı gerektirmez, iç arızalarda gecikmeyi en aza indirir, eşikleri her uygulama için otomatik belirler ve m-düzgünlüğüyle yakın arızalardaki gereksiz gecikmeyi atlar.

### İnvertörlü şebekeler için anlamı
- *(Benim çıkarımım.)* HSIR mantığı "düşük gerilim ve düşük akım" koşuluna dayanır. İnvertör arıza akımını nominalin yaklaşık 2 katıyla sınırladığı için (2022, s.5), invertör baskın bir uçta "düşük akım" koşulu neredeyse her zaman sağlanır. Bu da Bölge 1'in her arızada gecikmeye girmesi demektir. Eşik formülleri ayrıca kaynağın sabit bir empedans (SIR·Z_L) olduğunu varsayar; invertör için bu varsayım geçersizdir (2022, s.5).
- Makale CVT kaynaklı sorunun **yüksek SIR'de** kritikleştiğini gösteriyor (s.11). İnvertörlü şebekelerde yüksek SIR olağan durum olduğu için (2022, s.13, s.18) CVT modeli test düzeneğinin zorunlu bir parçasıdır.

### Projeyle bağlantı
- **Tekrarlanabilir bir CCVT modeli:** Ek bölümde (s.18–19) iki CVT için tam parametre seti veriliyor.
  - *Aktif CVT:* ara gerilim 5 kV, Ce 100 nF, Lc 68 H, Rc 228 Ω, Cp 0,14 nF, Lp 2,8 H, Rp 400 Ω, Cf 9600 nF, Lf 0,7 H, Rf 37,5 Ω, orta uç 0,35.
  - *Pasif CVT:* 6 kV, Ce 69,5 nF, Lc 101,2 H, Lf 16,5 H, Rf 231 Ω.
  - *Sistem:* Zs 10 Ω∠87,5°, ZL 1 Ω∠87,5° (yani SIR 10), POW 270°, m = 1, Rf = 0, yük 200 Ω, CVT yükü 100 Ω rezistif.

  Bu parametrelerle baseline'ın ve yardımcı sinyal dedektörünün gerilim girişlerine gerçekçi bir CCVT filtresi eklenebilir.
- **Frekans yanıtı** *(benim çıkarımım)*: AFSC'li CVT'nin frekans yanıtı düz değildir (s.9–10). Yardımcı sinyalin şebeke frekansı dışında bileşenleri varsa, örneğin modüle edilmiş ya da çok frekanslı bir sinyal, CVT bunları hem genlik hem faz olarak bozar. Sinyal tasarımında CVT'nin transfer fonksiyonu bilinen bir dinamik olarak ya da bir belirsizlik bandı olarak hesaba katılmalıdır.
- **Kural tabanlı bir dedektör örneği:** HSIR ve m-düzgünlüğü mantığı, "kural tabanlı bir dedektör"ün güzel bir örneğidir. Öğrenilmiş dedektörle karşılaştırırken baseline'da CVT güvenlik mantığının açık olması gerekir; 2012 makalesi modern rölelerde bunun açılmasını öneriyor.
- **Negatif bileşen ölçümü** *(benim çıkarımım)*: CVT geçicisi her fazda POW'a göre farklıdır. Bu yüzden geçici, üç fazdan hesaplanan V2'ye sahte bir negatif bileşen gerilimi ekler; 2012'deki 32Q olayları bunu destekliyor. V2'ye dayalı bir yardımcı sinyal dedektörü ilk 1–2 çevrimde bu sahte V2'yle karşılaşacaktır.

### Açık sorular / fikirler
- CVT'nin bilinen doğrusal modeli (ek bölümdeki parametreler) ters çevrilerek bir "CVT kompanzasyon" ön katmanı kurulabilir; 2021 makalesinde (s.20) yaklaşım (e) olarak geçiyor. Yardımcı sinyal yöntemi kompanze edilmiş gerilimle mi çalışmalı?
- Şekil 14'teki erişim–SIR eğrisi, kendi simülasyonumuzda aynı parametrelerle yeniden üretilip CCVT modelimizi doğrulamak için kullanılabilir.

---

## 5. Costello & Zimmerman (2012) — CVT geçicilerine yeniden bakış

- **Künye:** David Costello ve Karl Zimmerman (SEL), "CVT Transients Revisited – Distance, Directional Overcurrent, and Communications-Assisted Tripping Concerns". İlk olarak 65th Annual Conference for Protective Relay Engineers'da (Nisan 2012, IEEE, doi:10.1109/CPRE.2012.6201222) sunuldu; ayrıca 15th Georgia Tech Fault and Disturbance Analysis Conf. (Nisan 2012), 39th WPRC (Ekim 2012) ve 49th Minnesota Power Systems Conf.'ta (Kasım 2013). 12 numaralı sayfa ve iki ön sayfa (PDF 14 sayfa).
- **Tek cümlede:** Saha kayıtlarıyla CVT geçicilerinin yalnızca Bölge 1 aşırı erişimine değil, negatif bileşen yön elemanlarının kısa süreli yanlış kararlarına, tekrar kapamada hafıza bozulmasına ve DCB koordinasyon sorunlarına da yol açabildiğini gösteriyor ve pratik önlemler sıralıyor.

### Ne öğretiyor
- **Yapı (s.1):** Gerilim çoğunlukla C1 üzerinde düşer. C2 üzerindeki gerilim tipik olarak 5–20 kV'tur; 400 kV'luk bir CVT'de C2 için tipik değer 2000 pF'tır. Nominal çıkış tipik olarak 66,4 V'tur. CVT'ler ayrıca güç hattı taşıyıcı sinyalini hatta bağlamak için kullanılır ve kesicinin geçici toparlanma gerilimini (TRV) azaltabilir.
- **Saha olayları (s.2):**
  - 2011: Geri yöndeki üç fazlı bir bara arızasında CT'ler doydu ve hat tarafındaki CVT'ler geçici üretti. Yön elemanı önce doğru olarak "geri" dedi, sonra kısa bir süre "ileri" dedi ve röle yanlış çalıştı. Temel neden CT doymasıydı: akımlar ciddi biçimde dengesizken V2 sıfıra yakındı ve bu, ileri yönde bir Z2 üretti. CT ve CVT hataları aynı anda olabilir.
  - 138 kV'luk bir hatta faz-toprak arızasında geçiciler arızanın başında ve temizlenmesinde görüldü; temizlemeden sonra sağlam fazlar nominalin üstüne çıktı.
  - 2008: Halka baralı bir merkezde hat ucu açıldıktan sonra CVT'de sönümlü salınım (ringdown) görüldü.
- **CVT geçicisini belirleyen altı etken (s.2):** POW; tap ve kolon kapasitansı; bastırma devresinin tipi (aktif veya pasif); yükün bileşimi; ara VT'nin dönüştürme oranı; ara transformatörün mıknatıslama akımı.
- **Zaman sabitleri, 230 kV'luk bir CVT (s.3):** τ_CE = n²Z_B·C_E = 30,644 ms ve τ_LC = L_C/(n²Z_B) = 0,189 ms. Parametreler: C_E = 276,9 nF, L_C = 20,954 H, n²Z_B = 110 kΩ. Kapasitördeki enerji sıfır geçişinde en büyüktür; bu yüzden en uzun geçici o anda başlayan arızada oluşur (s.3).
- **Kapasitans (s.3):** C_E büyürse kapasitör üzerindeki gerilim düşer ve deşarj geçicisi küçülür; ancak geçicinin **süresi uzar**. Bu, 1996'daki "yüksek kapasitans daha iyidir" önermesine bir nüans ekliyor.
- **Ferrorezonans ve yük (s.4–5):** AFSC bant geçiren filtre gibi davranır; PFSC'nin geçiciye etkisi azdır. Yük ne kadar büyükse depolanan enerji ve geçici de o kadar büyük olur. Endüktif yük geçiciyi kötüleştirir ve şebeke frekansının altında bir frekansta salınıma yol açar. Mikroişlemcili rölenin yükü VA cinsinden ANSI yükünden 2–3 mertebe küçüktür ve neredeyse tamamen rezistiftir (s.5).
- **Dönüştürme oranı ve mıknatıslama akımı (s.5):** Yüksek dönüştürme oranı (ör. 15–20 kV/66,4 V) geçicinin genliğini azaltır ama süresini uzatır. Ayrı olarak, primer akım birim olmayan güç faktöründe olduğunda şebeke frekansının altında salınımlar oluşabilir ve büyük primer akım geçiciyi büyütür; bu yüzden transformatörler mıknatıslama akımını en aza indirecek şekilde tasarlanır.
- **Bölge 1 aşırı erişimi (s.5–6):** Geçici, temel bileşeni düşürür ve hesaplanan empedansı bir spiral boyunca hareket ettirir.
  - 2002: 230 kV'luk bir hatta CG arızası gerilim tepesinde başladı ve Bölge 1 toprak elemanı, erişiminin ötesindeki bir arıza için açtırdı. CVT AFSC'liydi ve eleman 1 çevrimden kısa süre çalışık kaldı (s.5).
  - Önlemler: Bölge 1'i kapatmak (çoğu uygulamada uygun değil), erişimi kısaltmak ya da hafif bir gecikme (**1,5 çevrim**) eklemek (s.5).
  - Şekil 16: AFSC'li CVT'de %80 Bölge 1 en fazla **SIR 4**'e kadar dayanır; ek mantık olmadan **SIR ≥ 20**'de Bölge 1 kaldırılmalıdır. PFSC ile %80 Bölge 1 **SIR 30**'a kadar etkilidir (s.5–6).
- **Olay verisinden SIR (4), s.6:** SIR = (V1_ARIZA − V1_ÖNCESİ)/((I1_ARIZA − I1_ÖNCESİ)·Z1_HAT). Fazörler aynı örnekleme anlarından okunmalıdır; alternatif olarak arıza sırasındaki negatif bileşen büyüklükleri kullanılabilir.
  - **İşlenmiş örnek:** Z_S = 11 Ω ve Z_L = 0,59 Ω (sekonder) → SIR > 18. AFSC'de güvenli en fazla erişim hattın %7'si olur; bu da rölenin en küçük ayar değerinin (0,05 Ω sek.) altında kalır, bu yüzden Bölge 1 kapatıldı. *(Kontrol: 0,07·0,59 ≈ 0,041 Ω < 0,05 Ω.)*
- **Bölünmüş Bölge 1 (s.6):** Kısaltılmış erişimli bir ani bölüm ile normal erişimli ve **1,5 çevrim** gecikmeli bir bölüm kullanılır.
- **Modern CVT algılama mantığı (s.6–7):** Bir CVT geçicisi algılandığında, kullanıcı ayarıyla etkinleştirilmişse, SOTF (switch-onto-fault) ve kesici açık değilse Bölge 1'i **en fazla 1,5 çevrim** bloklar. Mesafe hesabı oturursa gecikme kısalır ya da kalkar. Özel ayar gerektirmez ve SIR'e uyum sağlar.
  - 2009: 7 mil uzunluğunda 161 kV'luk bir hatta Bölge 1 %90'a ayarlıydı ve uzak bara arızasında aşırı erişti. AB çevrimi 1 çevrimden kısa süre Bölge 1 içinde kaldı (s.6–7).
  - Kayıt laboratuvarda mantık açıkken tekrar oynatıldığında eleman güvenli kaldı. Öneri: modern rölede bu mantığı **açın** (s.7).
- **Yön elemanları (s.7–9):** 32Q'nun ölçtüğü Z2ölç = Re[V2·(1∠Z1ANG·I2)*]/|I2|² (5). Değer Z2F'den küçükse ileri, Z2R'den büyükse geri kararı verilir (s.7).
  - 345 kV'luk bir hatta, buz fırtınasında komşu hatta bir geri AG arızası oldu. 32QF önce yanlışlıkla ileri dedi, sonra 32QR doğru olarak geri dedi; sağlam faz gerilimleri yükselmiş, C fazı aşmıştı (s.8).
  - 161 kV'luk bir hatta geri bir CG arızasında da aynı şey oldu (s.8).
  - Olası nedenler: şebeke topraklaması (sağlam fazlar en fazla 1,732 kata çıkabilir; olayda geçiciden sonra yaklaşık %110), sekonder topraklama (incelendi, sorun bulunmadı) ya da düşük kapasitanslı AFSC'li bir CVT (s.8).
  - CVT'nin kılavuzu (1957) şunu öneriyor: yükü %100 ya da hafif ileri güç faktörüne kompanze edin ve paralel dirençle 150 W'lık tam yüke çıkarın; tam yükte 13 var fazlalık 5° ileri açı verir (s.9).
  - RTDS'te onlarca senaryo denendi: güçlü ve zayıf kaynak, seri kompanzasyonlu ve kompanzasyonsuz, farklı arıza tipleri, CVT'li ve CVT'siz. Yön elemanları genel olarak doğru çalıştı. Arıza temizlendikten sonra CVT'li hatlarda gerilimin sönmesi daha uzun sürüyor (s.9).
- **Tekrar kapama (s.9–10):** 2005'te 161 kV'luk bir hatta geçici bir BG arızası oldu. Yaklaşık 0,5 s sonra tekrar kapamada Bölge 1 hemen açtırdı. Nedenleri şunlardı: hafızanın zaman sabiti yaklaşık 1 s olduğu için hat tarafı CVT'nin sönümlü salınımı V1 hafızasını, açısını ve frekans takibini bozdu; buna dallanmış bir transformatörün kapama akımı (inrush) eklendi (s.9). Hafıza sıfırlanarak yapılan tekrar oynatmada açtırma olmadı (s.10). Öneriler (s.10):
  - tekrar kapama açık aralığını CVT'nin sönümü ve V1 hafızasını hesaba katarak belirleyin;
  - arıza dedektörlerini inrush akımının üstüne ayarlayın;
  - sönümlü salınım ya da hat ucunun açık olduğu algılanınca hafıza zaman sabitini sıfıra yaklaştırın veya hafıza filtresine sıfır besleyin.
- **Haberleşmeli şemalar (s.10–11):**
  - 345 kV DCB: Geri arızada uzak uçtan gelen blok sinyali gecikti, çünkü yönlü taşıyıcı başlatması gecikmişti ve kanal gecikmesiyle birlikte toplam, 1,5 çevrimlik koordinasyon gecikmesini aştı. Röle 67N2 ile fazladan açtırdı (s.10).
  - DCB: CVT kaynaklı mesafe aşırı erişimi DCB için risk değildir. Sorunlu AFSC'li CVT değiştirilemiyorsa taşıyıcı koordinasyon gecikmesini uzatın (s.11).
  - PUTT: Bölge 1 erişimini kısaltın ya da CVT mantığını kullanın. POTT: AFSC'li CVT varsa gönderilen izin sinyaline bir pickup gecikmesi ekleyin (s.11).
- **Yaşlanan CVT'ler (s.11):** Kapasitör elemanları arızalanıp patlayabilir. Taslak NERC PRC-005-2 standardı, izlenen ekipman için asgari test aralığını ve sürekli izlenen şeylere göre neyin test edilmesi gerektiğini tanımlıyor. Önerilen izleme yöntemi, senkrofazörlerle otomatik ölçüm karşılaştırmasıdır: halka bara ya da 1,5 kesicili düzende, bütün kesiciler kapalıyken hat CVT'lerinin hepsi aynı genlik ve açıyı göstermelidir.

### Ana bulgular / öneriler (s.11–12)
- CVT geçicisini büyüten koşullar: gerilim sıfırında başlayan arıza, düşük kapasitans, AFSC, yüksek SIR, düşük dönüştürme oranı, yüksek mıknatıslama akımı, endüktif ve büyük yük. Bunların tersi geçiciyi küçültür.
- Eski rölelerde Bölge 1 kapatılır, geciktirilir ya da kısaltılır. Yeni rölelerde **CVT geçicisi algılama mantığı açılmalıdır**.
- Yön elemanları genelde güvenlidir, ama iki istisna saha olayı belgelenmiştir.
- Hızlı tekrar kapama, hafıza polarizasyonu ve dallanmış yüklerin inrush akımıyla birleşince sorun çıkar: açık aralığını uzatın, dedektörleri doğru ayarlayın ve hafızayı sıfırlayın.
- DCB ve POTT genelde risk altında değildir. Eski AFSC'li CVT'lerde ise üreticinin yük önerilerine uyun, uzun taşıyıcı koordinasyonu ve gecikmeli izin sinyali kullanın.
- Yaşlanan CVT'ler senkrofazörlerle izlenmelidir.

### İnvertörlü şebekeler için anlamı
- *(Benim çıkarımım.)* Olay verisinden SIR hesabı (4), kaynağın sabit bir Z1 gibi davrandığını varsayar. İnvertörde ΔV1/ΔI1 oranı zamanla ve akım sınırlamasına göre değişir (2022, s.5). Bu yüzden "SIR" tek bir sayı değil, bir aralık ya da zaman serisi olarak raporlanmalıdır.
- Hafıza bozulması iki kaynaktan gelebilir: CVT'nin sönümlü salınımı (s.9) ve invertörün frekans ve açı kayması (2022, s.3). İkisi aynı anda olabilir; tekrar kapama senaryoları invertörlü şebekede daha da risklidir.
- 32Q'nun V2'nin çok küçük olduğu durumlardaki kırılganlığı (2011 olayı, s.2), invertörün düşük ve kontrolsüz I2'siyle birleşince daha da önem kazanır.

### Projeyle bağlantı
- **Negatif bileşen kararlarının kırılganlığı:** Saha olaylarında V2 ≈ 0 iken dengesiz akımlar (CT doyması) ya da CVT kaynaklı sahte V2, 32Q'yu kısa süreliğine ters yöne çevirmiştir (s.2, s.8). *(Benim çıkarımım:)* I2 enjeksiyonuna dayanan bir yöntemin V2 ölçümü de aynı sahte bileşenlerle kirlenecektir. Garanti kümesine CVT geçici zarfı ve CT doyması dahil edilmeli; test matrisine "geri arıza ve CVT geçicisi" ile "CT doyması ve küçük V2" vakaları konmalıdır.
- **SIR'in çevrim içi tahmini** *(benim çıkarımım)*: Makale SIR'in arıza sırasında negatif bileşen büyüklüklerinden de hesaplanabileceğini söylüyor (s.6). Bilinen bir ΔI2 enjeksiyonu ve ölçülen ΔV2, kaynak ve şebeke Z2'sinin sürekli tahmin edilmesine imkân verir. Bu, uyarlanır ayarlar ya da enjeksiyon genliğinin uyarlanması için kullanılabilir.
- **Baseline kuralı:** Modern bir röle baseline'ında CVT geçicisi algılama mantığı **açık** olmalı (en fazla 1,5 çevrim blok ve hesap oturursa erken bırakma). Kapalı bir mantıkla yapılan karşılaştırma haksızdır (s.7, s.11–12).
- **Senaryo listesine eklenecekler:** tekrar kapama sırasında sönümlü salınım ve inrush (s.9–10); DCB'de taşıyıcı koordinasyon gecikmesi (s.10); en kötü POW ile 1 çevrimden kısa aşırı erişim pencereleri (s.5–7).

### Açık sorular / fikirler
- RTDS çalışması "genelde doğru" sonucunu verdi, ama sahada iki istisna var. Bu istisnaların hangi CVT ve yük kombinasyonunda ortaya çıktığı, 1996'daki parametrelerle simülasyonda yeniden üretilebilir mi?
- Yaşlanan CVT'leri izlemek için kullanılan senkrofazör karşılaştırması, ölçüm zincirinin sağlığını izleyen veri tabanlı bir yöntemdir. Yardımcı sinyal de benzer biçimde "ölçüm zinciri öz-testi" için kullanılabilir mi?

---

## Sentez: adil bir konvansiyonel röle temel çizgisi (baseline) nasıl kurulur

**İlke:** Karşılaştırma, uygulamada en iyi sayılabilecek konvansiyonel röleye karşı yapılmalı, kolay yenilen bir "saman adam"a karşı değil. Bu röle bu makalelerdeki pratik kurallarla ayarlanmalı ve önerilen yöntemle **aynı ölçüm zincirini, aynı hata kümelerini ve aynı zaman bütçesini** kullanmalıdır.

**A. Sistem ve SIR**
- [ ] SIR_G ve SIR_P'yi 2021'deki tanımla (uzak barada metalik arıza, SIR = 1/V_PU − 1) **bütün makul olasılıklar** için hesaplayın ve tek bir değer yerine aralık olarak raporlayın (2021, s.14–15; 2023, s.8 adım 1). Kısa devre modeline invertörün arıza tepkisini (akım sınırı yaklaşık 2 pu, 2022, s.5) dahil edin (2021, s.15).
- [ ] Senaryoları SIR sınıflarına ayırın: < 0,5 (CCVT ihmal edilebilir), 0,5–4, > 4 (kalıcı hatalar önem kazanır), ≥ 20 (AFSC'li CVT'de ek mantık yoksa Bölge 1 olmaz) ve invertör baskın (≈ 37) (2023, s.16–17; 2012, s.5–6; 2022, s.18).

**B. Ölçüm zinciri: iki yöntem için de aynı**
- [ ] **CT:** %5–10 oran hatası ve doyma modeli. Doyma testleri, yedek korumanın temizleme süresi ya da 300–500 ms boyunca sürmeli (2021, s.5, s.15).
- [ ] **VT:** Oran hatası ve düşük gerilimde sabit mutlak hata: E_VT_MAG = E%·V_MIN, E_REL_MAG = E_SEC/V_NOM. Yıldız bağlı VT'den türetilen faz-faz geriliminde açı hatası da eklenmeli. Tipik birleşik değer yaklaşık 0,02 pu (2023, s.11–13).
- [ ] **CCVT:** AFSC ve PFSC modelleri (1996 ekindeki parametreler, s.18–19) ya da bir IEC 61869-5 sınıf zarfı (ör. 3PT2) (2023, s.6). Rezistif ve ANSI yükleri ayrı ayrı denenmeli (1996, s.12; 2012, s.5).
- [ ] **POW taraması:** En az gerilimin sıfır geçişi ve tepe noktası; tercihen tam tarama (1996, s.3, s.11; 2023, s.6).
- [ ] **Röle filtresi:** Kenar yumuşatma filtresi, örnekleme ve tam çevrimlik Fourier ya da kosinüs filtresi (1996, s.10; 2023, s.7).
- [ ] **Sabit gerilim hataları:** GPR (≈2 kV tahmini, topraklama türüne göre 0, 0,5 veya 1 katsayısıyla), kuplaj (0,1 V/(A·mil)) ve sekonder kabloya indüklenen gerilim (66,4 V'ta yüzde birin altı, yüzlerce mV) (2023, s.13–15; 2021, s.15–16).
- [ ] **Frekans sapması:** Hz başına yaklaşık %1,7 reaktans etkisi; düşük atalette Δf ≈ 0,25 Hz gibi değerler (2021, s.6; 2022, s.4).

**C. Geleneksel röle fonksiyonları**
- [ ] Altı çevrimli mesafe ölçümü, k0 = (Z0/Z1 − 1)/3 ile; Z0 belirsizliği için marj bırakın (2021, s.4, s.6).
- [ ] Hafıza polarizeli mho ve I2 (veya I0) polarizeli dörtgen; dörtgende aşağı eğim ve (19)'a göre sınırlı rezistif erişim (2021, s.8, s.11).
- [ ] **Bölge 1:** Faz %80, toprak %75 ile başlayın. Ardından 2023'ün kriterleriyle doğrulayın: geçici (13), kalıcı (17) ve birleşik (30). Kriter sağlanmazsa gecikme (T_D) ekleyin, erişimi kısaltın ya da "Bölge 1 yok" seçeneğini kullanın (2021, s.7, s.22; 2023, s.8–9, s.16).
- [ ] **Bölge 2:** Kısa devre programından alınan en büyük görünür empedans artı marj, en az %120; Bölge 2 için de bir eksik erişim hata bütçesi yapın (2021, s.9, s.14, s.22).
- [ ] **Bölge 3 / geri bölge:** DCB'de karşı ucun Bölge 2'sinin gördüğü her dış arızayı görmeli, yani ondan daha az hassas olmamalı (2021, s.22–23).
- [ ] **Infeed kuralı:** Bölge 1 ≤ elektriksel olarak en yakın uzak uç. Kuplaj olasılıkları: paralel hat servis dışı, topraklı veya topraksız; Bölge 1 için %25 marj (2021, s.9–10).
- [ ] **Yön denetimi:** 32Q ve 32G; üç fazlı arızalar için faz veya pozitif bileşen yön elemanı *(genel bilgi)*.
- [ ] **Çevrim seçimi ve aşırı akım denetimi:** Dahil edilmeli.
- [ ] **Yük tecavüzü:** Yük tecavüzü mantığı ya da yüklenebilirliğe göre ayarlanmış kör çizgi *(genel bilgi; 2022, s.8)*.
- [ ] **CCVT geçicisi güvenlik mantığı:** Açık olmalı (en fazla 1,5 çevrim blok ve "hesap oturursa erken bırakma"); SOTF ve kesici açık koşullarıyla birlikte (2012, s.6–7).
- [ ] **Çalışma süresi eğrileri:** T_OP'un SIR'e ve arıza konumuna göre değişimini kaydedin; 2023'ün kriterleri bu değere ihtiyaç duyar (2023, s.8; 2021, s.21).
- [ ] **Pilot şema (isteğe bağlı):** POTT ya da DCB, taşıyıcı koordinasyon gecikmesiyle birlikte (2012, s.10–11). Karşılaştırılan yöntem kanal kullanmıyorsa, baseline'da da kanalsız sonuçları ayrıca raporlayın.

**D. İnvertör farkındalığı olan konvansiyonel baseline (2022)**
- [ ] Ofset mho ve dörtgen; Bölge 1'de aşağı, Bölge 2'de yukarı eğim; geri erişim %10–30; sağ kör çizgi yüklenebilirliğe göre (s.7–8).
- [ ] Toprak elemanlarında 32G izin verici; faz elemanlarında 32WI, 1,25·I_FWD(MAX) < 50WI < 0,8·I_REV(MIN) ile (s.9–10).
- [ ] TD32: bloklama mantığında T1 = 1/8–1/4 çevrim, T2 > en kötü geri arıza temizleme süresi. Bölge 1 penceresi: T3 = 2–3 çevrim, T4 ≈ 1 s (s.11–12).
- [ ] Düşük gerilime dayalı çevrim seçimi (1,1 çarpanı) ve toprak elemanları için 3I0 denetimi (s.12–13).
- [ ] İsteğe bağlı: zaman alanı R-L en küçük kareler tahmincisi (s.16–18) ve Şekil 25'teki güçlü/zayıf anahtarlama (s.15).
- [ ] Rapor iki baseline'ı ayrı ayrı göstermeli: "geleneksel" ve "zayıf-besleme".

**E. Test matrisi**
- [ ] **Arıza tipleri:** 11 tipin hepsi (2023, s.14).
- [ ] **Konumlar:** 0 (yakın), 0,5, m1'in hemen berisi ve ötesi, m = 1 (uzak bara) ve komşu hat. Ayrıca yakın geri arızalar ve kesici arızası nedeniyle geç temizlenen dış arızalar.
- [ ] **Arıza direnci:** R_F aralığı; load-in ve load-out ön yükleri; iki dirençli BCG gibi karmaşık arızalar (2021, s.7–8, s.12).
- [ ] **Topoloji:** Kesici açık (infeed'in ortadan kalkması), paralel hat servis dışı veya topraklı (2021, s.9–10).
- [ ] **Düşük atalet:** Δf > 0 ile uzun süren arıza; dönen infeed hatası (2022, s.4–5).
- [ ] **Diğer:** CT doyması; CVT geçicisi ile geri arızanın birleşimi (32Q'nun sınanması); tekrar kapamada sönümlü salınım ve inrush (2012, s.2, s.8–10).
- [ ] **Arızasız durumlar:** Normal işletme, ağır yük, yük salınımı.

**F. Metrikler ve adalet**
- [ ] Güvenlik (dış ve geri arızada açtırma olmaması), güvenilirlik (iç arızada açtırma), karar süresi dağılımı ve gecikmesiz kapsanan hat yüzdesi.
- [ ] Karşılaştırma **eşit güvenlik düzeyinde** yapılmalı. Örneğin konvansiyonel rölenin 2023 kriterleriyle garanti edilen erişim ve gecikmesi, yardımcı sinyal yönteminin aynı hata kümeleriyle garanti ettiği kapsamayla kıyaslanmalı.
- [ ] "Bölge 1 kullanmamak ve pilot şema ya da 87L'ye güvenmek" de meşru bir konvansiyonel seçenektir ve raporlanmalıdır (2021, s.22, s.24).
- [ ] **Öğrenilmiş dedektörler için:** Aynı girişler (aynı CT/VT/CCVT modellerinden geçmiş V ve I) ve aynı karar zamanı kullanılmalı. Eğitim ve test verileri rastgele değil, sistem yapılandırmasına ve invertör kontrol sürümüne göre ayrılmalı, çünkü invertör davranışı zamanla değişiyor (2022, s.6).

**G. Negatif bileşen enjeksiyonunun etkileşim testleri** *(benim önerilerim)*
- [ ] **Normal işletmede enjeksiyon:** 32Q'nun Z2ölç değeri (2012 (5)) ve etkinleştirme eşikleri; DCB'de sürekli blok sinyali oluşup oluşmadığı; POTT izninin etkilenip etkilenmediği; 46/50Q/51Q elemanlarının çalışıp çalışmadığı.
- [ ] **Arızada enjeksiyon:** I2 polarizeli reaktans elemanındaki ek Θ hatası ve bunun rezistif erişime etkisi (2021 (18)); 32Q kararının kararlılığı; I2–I0 tabanlı çevrim seçimi; 50WI'nın I_FWD(MAX) değerine katkı; TD32'nin artımsal sinyalleri.
- [ ] **Görünür empedans:** Metalik arızada enjeksiyondan bağımsız kalmalı (2022, s.6–7 gereği). Rezistif arızada I_Y/I_X değişimi (2022 (3)) ölçülmeli.
- [ ] **Tespit edilebilirlik:** Enjeksiyonun rölede yarattığı gerilim imzası şu ikisinden büyük olmalı: sabit hata tabanı (≈0,02 pu, GPR ve kuplaj dahil) ve T0 anındaki CCVT zarfı (A = 2,5 ile zayıflatılmış). Aynı imza konvansiyonel elemanların eşiklerinden küçük kalmalı. Bu iki sınırın SIR'e göre çizilmesi önerilir.
