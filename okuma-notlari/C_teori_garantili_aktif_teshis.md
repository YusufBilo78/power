# C — Teori: Garantili (küme-tabanlı) aktif arıza teşhisi

**Okunan makaleler**

1. J. K. Scott, R. Findeisen, R. D. Braatz, D. M. Raimondo — *Input design for guaranteed fault diagnosis using zonotopes*, Automatica 2014.
2. D. M. Raimondo, G. R. Marseglia, R. D. Braatz, J. K. Scott — *Closed-loop input design for guaranteed fault diagnosis using set-valued observers*, Automatica 2016.

> **Okuma kuralları**
>
> - Sayfa numaraları dergi sayfalarıdır (Scott: s. 1580–1589; Raimondo: s. 107–117). Denklem, teorem, şekil ve tablo numaraları makalelerdekiyle aynıdır.
> - **[Yorum]** etiketli her şey makalede yazmıyor. Bunlar benim akıl yürütmem, türetimim ya da önerimdir; kullanmadan önce kontrol edilmeli.
> - **[Taylor özeti]** etiketli ifadeler Taylor & Domínguez-García (IEEE TAC 2025, *Active fault detection in static systems*) hakkında bu görevde bana verilen özete dayanır. O makaleyi bu notlar için ayrıca açmadım. Özellikle $\zeta$ ve $\chi$'nın kesin tanımları orijinalinden kontrol edilmeli.
> - Notasyon: tilde (~) zaman boyunca alt alta dizilmiş (stacked) vektör demektir: $\tilde u=(u_0,\dots,u_{N-1})\in\mathbb R^{Nn_u}$, $\tilde y=(y_0,\dots,y_N)\in\mathbb R^{(N+1)n_y}$.

---

## 0. Kısa sözlük (iki makalede ortak)

- **Zonotop (zonotope):** $Z=\{G\xi+c:\ \|\xi\|_\infty\le 1\}$, kısaca $Z=\{G,c\}$. $c$ merkezdir; $G=[g_1\ \cdots\ g_{n_g}]$ matrisinin sütunları **üreteçlerdir (generators)**. Geometrik olarak bir kutunun (küpün) doğrusal görüntüsüdür; doğru parçalarının Minkowski toplamı olarak da düşünülebilir. Merkezcil simetrik, konveks bir politoptur. 2-B'de 2 üreteç bir paralelkenar, 3 üreteç bir altıgen verir. **Mertebe (order)** $=n_g/n$ olarak tanımlanır; doğrusal bağımsız üreteçli birinci mertebe zonotop bir paralelotoptur (Scott s. 1581).
- **Minkowski toplamı:** $Z\oplus Y=\{z+y:z\in Z,y\in Y\}$. Zonotoplarda iki üreteç matrisini yan yana koymaktan ibarettir: $\{[G_z\ G_y],\,c_z+c_y\}$ (Scott (6)).
- **Pontryagin farkı:** $Z\ominus Y=\{x:\ x+Y\subset Z\}$ (Scott (5)).
- **Kısıtlı zonotop (constrained zonotope, CZ):** $\{G\xi+c:\ \|\xi\|_\infty\le1,\ A\xi=b\}$. Her sınırlı konveks politop bir CZ'dir (Raimondo s. 108, Scott ve diğ. 2016'ya atıfla).
- **Ayırıcı giriş (separating input):** Belirsizliklerin tüm olası değerleri için, ölçülen çıkışın en fazla bir modelle (ya da senaryoyla) tutarlı olmasını garanti eden giriştir.
- **Küme-değerli gözlemci (set-valued observer):** Ölçümlerle tutarlı bütün durumları içeren bir kümeyi zaman içinde yinelemeli olarak güncelleyen gözlemcidir.

---

## 1. Scott ve diğ. (2014): Zonotoplarla garantili teşhis için açık-çevrim giriş tasarımı

### Künye

Joseph K. Scott, Rolf Findeisen, Richard D. Braatz, Davide M. Raimondo. "Input design for guaranteed fault diagnosis using zonotopes." *Automatica*, 50(6):1580–1589, 2014. DOI: 10.1016/j.automatica.2014.03.016. Ön sonuçları ACC 2013'te sunulmuştur (s. 1580 dipnotu).

### Tek cümlede

Belirsizlikleri zonotoplarla sınırlı, sonlu sayıda doğrusal ayrık-zamanlı model (bir nominal, geri kalanı arızalı) arasında, $N$ adım sonunda çıkış yörüngesinin **en fazla bir** modelle tutarlı olacağını **garanti eden** ve diğer amaçlar açısından en az zararlı olan (ör. en küçük 2-normlu) açık-çevrim giriş dizisini bulur; problemi gevşetmeden, eşdeğer bir karma tamsayılı karesel programa (MIQP) dönüştürerek çözer.

### Sezgisel anlatım (bulut resmi)

1. **Bulutlar.** Bir model $i$ ve bir giriş dizisi $\tilde u$ sabitlensin. Başlangıç durumu $x_0\in X_0$, bozucular $w_k\in W$ ve ölçüm hataları $v_k\in V$ izin verilen bütün değerleri aldığında çıkış yörüngesi $\tilde y\in\mathbb R^{(N+1)n_y}$ bir küme tarar. Bu küme, modelin "bulutu" olan $\tilde\Psi_{0:N}(\tilde u,i)$'dir. Belirsizlikler kutu (zonotop) olduğu ve model doğrusal olduğu için bulut da bir zonotoptur.
2. **Sinyal bulutu yalnızca öteler.** Makalenin "kritik gözlemi" şudur (s. 1582): $\tilde u$, $\tilde\Psi(\tilde u,\tilde j)$'yi $\tilde\Psi(\tilde u,\tilde i)$'ye göre yalnızca **öteler (translates)**; kümelerin şeklini ya da göreli yönelimini değiştirmez. Bunun nedeni, girişin yalnızca bulutun merkezine girmesidir; üreteçler girişten bağımsızdır.
3. **Önemli olan göreli kaymadır.** İki bulutu aynı miktarda kaydırmak hiçbir şeyi değiştirmez. Önemli olan, $j$ bulutunun $i$ bulutuna göre ne kadar kaydığıdır. Bu göreli kayma $\tilde N(i,j)\,\tilde u$'dur ve $\tilde N(i,j)=\tilde C(j)\tilde B(j)-\tilde C(i)\tilde B(i)$, iki modelin giriş→çıkış haritalarının farkıdır.
4. **"Çarpışma kümesi"** (bu terim benim; makalede yok). $\tilde Z(i,j)$, göreli kaymanın hangi değerlerinde iki bulutun çakıştığını gösteren kümedir. İki bulut şeklinin Minkowski toplamıdır ve sıfır-girişteki merkez farkına yerleştirilmiştir. Sinyalin görevi göreli kaymayı bu kümenin dışına itmektir. Robotikteki konfigürasyon-uzayı engeline benzetilebilir **[Yorum]**.
5. **Problem neden konveks değil?** "Bir konveks kümenin dışında olmak" konveks bir kısıt değildir: ya sağa ya sola ya yukarı itebilirsiniz. Hangi yüzden çıkılacağı kombinatoryal bir seçimdir ve makale bu seçimi ikili değişkenlerle modeller.
6. **Neden zonotop?** Doğrusal dönüşüm ve Minkowski toplamı zonotoplarda tamdır (kesindir) ve ucuzdur: matris çarpımı ve sütun eklemekten ibarettir. Genel politoplarda (yarı-uzay gösterimi) aynı işlemler, yaklaşık 10 boyutun üzerinde aşırı pahalı ve sayısal olarak kararsız hale gelir (s. 1581). Önceki yöntem (Nikoukhah 1998) yüksek boyutlu politop izdüşümü gerektiriyordu ve $N(n_y+n_u)\gtrsim10$ olduğunda hesaplanamaz hale geliyordu (s. 1583).
7. **Şekil 1 (s. 1587).** 5 model ve $N=2$ için optimal ayırıcı girişle elde edilen 3-B $(y_0,y_1,y_2)$ bulutları birbirinden ayrıktır. Bu yüzden ölçülen yörünge en fazla bir modele uyar.

### Matematiksel kurulum

**(a) Model (s. 1581).** Her $[k,k+1]$ aralığında $n_m$ doğrusal modelden biri geçerlidir, $i\in\mathbb I=\{1,\dots,n_m\}$:
$$x_{k+1}=A(i_k)x_k+B(i_k)u_k+r(i_k)+B_w(i_k)w_k \quad (1)$$
$$y_k=C(i_k)x_k+s(i_k)+D_v(i_k)v_k \quad (2)$$

- $i=1$ nominal modeldir. $r(i)$ ve $s(i)$ toplamsal arızaları (aktüatör ve sensör ofseti) modeller.
- $x_0\in X_0$ ve $(w_k,v_k)\in W\times V$ olup $X_0$, $W$, $V$ zonotoptur.
- Arıza bir model geçişidir ($i_k\ne i_{k-1}$). **Arıza senaryosu** $\tilde i=(i_0,\dots,i_N)$ bir model dizisidir; $\tilde{\mathbb I}$ izin verilen senaryoların kümesidir.
- $\tilde{\mathbb I}$'da $s$ senaryo varsa $Q=\binom{s}{2}$ çift koşulu sağlanmalıdır. Makale, anlamsız (ör. kendiliğinden düzelen) ya da çok olasılıksız senaryoların elenmesini önerir; $\tilde{\mathbb I}$'nın verildiği varsayılır.
- **[Yorum]** (2)'de doğrudan besleme ($Du$) terimi yoktur; $u_k$ çıkışı ilk kez $y_{k+1}$'de etkiler.

**(b) Zonotop işlemleri ve iki lemma (s. 1581–1582).** $RZ=\{RG,Rc\}$ ve $Z\oplus Y=\{[G_z\ G_y],c_z+c_y\}$ (6). Mertebe büyümesini sınırlamak için daha düşük mertebeli dış yaklaşım (order reduction) kullanılır; makale Althoff ve diğ. (2010) Method C'yi kullanır.

- **Lemma 1** (Pontryagin farkı): $Y=\{G,c\}$ ve $\mathcal Z=\{z:Hz\le k\}$ ise $\mathcal Z\ominus Y=\{z:Hz\le k'\}$, burada $k'_i=k_i-h_i^\top c-\|h_i^\top G\|_1$.
- Her zonotop simetriktir: $\{G,c\}=\{-G,c\}$.
- **Lemma 2** (kesişmeme testi): $Z=\{G_z,a_z+b_z\}$ ve $Y=\{G_y,a_y+b_y\}$ ise
$$Z\cap Y=\emptyset\iff a_y-a_z\notin\{G_z,b_z\}\oplus\{G_y,-b_y\}.$$
İki zonotopun kesişmemesi, tek bir noktanın tek bir zonotopa ait olmaması sorusuna iner. Bu da bir LP ile sınanabilir.

**(c) Erişilebilir kümeler (s. 1582).** Model doğrusal olduğundan yığınlanmış matrisler $\tilde A,\tilde B,\tilde C,\dots$ tanımlanabilir:
$$\tilde\Phi_{\ell:k}(\tilde u,\tilde i)=\tilde A(\tilde i)X_0\oplus\tilde B(\tilde i)\tilde u\oplus\tilde r(\tilde i)\oplus\tilde B_w(\tilde i)\tilde W \quad (7)$$
$$\tilde\Psi_{\ell:k}(\tilde u,\tilde i)=\tilde C(\tilde i)\tilde\Phi_{\ell:k}(\tilde u,\tilde i)\oplus\tilde s(\tilde i)\oplus\tilde D_v(\tilde i)\tilde V \quad (8)$$

- Bu kümeler zonotoptur: $\tilde\Psi_{\ell:k}(\tilde u,\tilde i)=\{G^\Psi_{\ell:k}(\tilde i),\ \bar\psi_{\ell:k}(\tilde u,\tilde i)\}$ (10).
- Üreteçler $G^\Phi=[\tilde A G_0\ \ \tilde B_wG_{\tilde W}]$ ve $G^\Psi=[\tilde C G^\Phi\ \ \tilde D_vG_{\tilde V}]$ olup **girişten bağımsızdır**.
- Merkezler, belirsizliklerin merkezlerinde değerlendirilen nominal yörüngelerdir ve girişe **doğrusal-afin** bağlıdır: $\bar\psi_{0:N}(\tilde u,\tilde i)=\tilde C(\tilde i)\tilde B(\tilde i)\tilde u+\bar\psi_{0:N}(0,\tilde i)$.
- Yalnızca uç zamandaki kümeler $\Phi_N,\Psi_N$ (11)–(13) ile özyinelemeli (recursive) hesaplanabilir.
- Tüm yörünge kümesi ise özyinelemeli hesaplanamaz ve yüksek boyutludur. Buna karşılık zamanlar arasındaki bağı korur: $\tilde\Psi_{0:N}\subset\Psi_0\times\dots\times\Psi_N$ (14). Yani tüm yörünge bulutu, her anın bulutlarının kartezyen çarpımından daha küçüktür ve dolayısıyla daha bilgilidir.

**(d) Ayrışma koşulu (s. 1582).** Çıktı $\tilde y$, senaryo $\tilde i$ ile ancak ve ancak $\tilde y\in\tilde\Psi_{0:N}(\tilde u,\tilde i)$ (15) ise tutarlıdır.

- **Tanım 1:** $\tilde u$, $\tilde i$ ile $\tilde j$'yi $[0,N]$ üzerinde **ayırır** ancak ve ancak
$$\tilde\Psi_{0:N}(\tilde u,\tilde i)\cap\tilde\Psi_{0:N}(\tilde u,\tilde j)=\emptyset. \quad (16)$$
Her çifti ayıran girişlerin kümesi $\mathscr S(\tilde{\mathbb I})$ ile gösterilir.
- Çevrimiçi testte (15) her senaryo için kontrol edilir. Ayırıcı girişle bu test ya teşhisi verir (nominal durum dahil) ya da "$\tilde{\mathbb I}$'daki hiçbir senaryo doğru değil" sonucunu verir (s. 1582).
- Ayırıcı olmayan bir giriş de, belirli çıkış değerleri gözlenirse teşhis sağlayabilir. Ayırıcı bir giriş bazen $M<N$ adımda teşhis verebilir (s. 1582).

**(e) Teorem 3: kilit sonuç (s. 1582).**
$$\tilde u\in\mathscr S(\tilde{\mathbb I})\iff \tilde N(\tilde i,\tilde j)\,\tilde u\notin\tilde Z(\tilde i,\tilde j)\quad\forall\,\tilde i\ne\tilde j, \quad (17)$$
$$\tilde N(\tilde i,\tilde j)\equiv\tilde C(\tilde j)\tilde B(\tilde j)-\tilde C(\tilde i)\tilde B(\tilde i),\qquad \tilde Z(\tilde i,\tilde j)\equiv\big\{[G^\Psi_{0:N}(\tilde i)\ \ G^\Psi_{0:N}(\tilde j)],\ \bar\psi_{0:N}(0,\tilde i)-\bar\psi_{0:N}(0,\tilde j)\big\}.$$

*İspat:* (16)'ya (10) ile Lemma 2 uygulanır; $a_z=\tilde C(\tilde i)\tilde B(\tilde i)\tilde u$ ve $a_y=\tilde C(\tilde j)\tilde B(\tilde j)\tilde u$ alınırsa $a_y-a_z=\tilde N\tilde u$ olur.

Doğrudan sonuçlar (s. 1583):

- $\tilde Z$ kompakt olduğundan, $\tilde N(\tilde i,\tilde j)\ne0$ ise bu çifti ayıran girişlerin kümesi boş değildir ve sınırsızdır. Yeterince büyük bir sinyal her zaman ayırır, ancak giriş kısıtları bu imkânı kaldırabilir **[Yorum]**.
- $\tilde N(\tilde i,\tilde j)=0$ ise iki durum vardır: $0\notin\tilde Z$ ise **her** giriş ayırır (çift pasif olarak ayırt edilebilir); $0\in\tilde Z$ ise **hiçbir** giriş ayırmaz.
- Ayıran girişler kümesi bir konveks kümenin tümleyenidir, dolayısıyla konveks değildir.

**(f) Optimal ayırıcı giriş ve MIQP'ye dönüşüm (s. 1583).** $J(\tilde u)=\sum_{k=0}^{N-1}u_k^\top Ru_k$ ($R\succeq0$) ve $\tilde U=U\times\dots\times U$ ($U$ konveks politop) olsun.
$$\inf\{J(\tilde u):\ \tilde u\in\tilde U\cap\mathscr S(\tilde{\mathbb I})\} \quad (18)\quad\Longleftrightarrow\quad \inf\{J(\tilde u):\ \tilde u\in\tilde U,\ \tilde N^{[q]}\tilde u\notin\tilde Z^{[q]},\ q=1..Q\} \quad (19)$$

- **Lemma 4.** $\tilde Z^{[q]}=\{G^{[q]},c^{[q]}\}$ ve $G^{[q]}$ tam satır ranklı olsun. Tanımlayalım:
$$\hat\delta^{[q]}(\tilde u)\equiv\min_{\delta,\xi}\ \delta\quad\text{s.t.}\quad \tilde N^{[q]}\tilde u=G^{[q]}\xi+c^{[q]},\ \ \|\xi\|_\infty\le1+\delta. \quad (20)$$
O zaman $\tilde N^{[q]}\tilde u\notin\tilde Z^{[q]}\iff\hat\delta^{[q]}(\tilde u)>0$. Burada $1+\hat\delta$, noktanın zonotopun kaç "katı" dışarıda olduğunu ölçen bir gösterge (gauge) gibidir.
- Olurlu küme kapalı olmadığından $\hat\delta\ge\varepsilon$ kullanılır (küçük bir muhafazakârlık getirir). Big-M için bir üst sınır $\hat\delta_m$ de gerekir. Böylece iki seviyeli (bilevel) program elde edilir:
$$\min\{J(\tilde u):\ \tilde u\in\tilde U,\ \varepsilon\le\hat\delta^{[q]}(\tilde u)\le\hat\delta^{[q]}_m\}. \quad (21)$$
- İç LP, gerek ve yeter optimallik (KKT) koşullarıyla değiştirilir:
  - (22) $\tilde N^{[q]}\tilde u=G^{[q]}\xi^{[q]}+c^{[q]}$
  - (23) $\|\xi^{[q]}\|_\infty\le1+\delta^{[q]}$
  - (24) $(G^{[q]})^\top\lambda^{[q]}=\mu_1^{[q]}-\mu_2^{[q]}$
  - (25) $1=(\mu_1^{[q]}+\mu_2^{[q]})^\top\mathbf 1$
  - (26) $\mu_1^{[q]},\mu_2^{[q]}\ge0$
  - (27)–(28) tamamlayıcılık (complementarity): $\mu_{1,k}(\xi_k-1-\delta)=0$ ve $\mu_{2,k}(\xi_k+1+\delta)=0$.
- **Neden KKT?** Yalnızca "$\exists\xi$ öyle ki $\|\xi\|_\infty\le1+\delta$" yazılsaydı, optimizasyon $\delta$'yı keyfi büyük seçerdi. $\delta$'nın gerçekten iç problemin *minimumu* olduğunu KKT koşulları garanti eder **[Yorum: açıklama benim]**.
- Tamamlayıcılık koşulları konveks değildir. Bu yüzden ikili $p_1,p_2\in\{0,1\}^{n_g}$ değişkenleri ve Fortuny-Amat & McCarl (1981) yöntemi kullanılır (29). Bu ima ilişkileri şu doğrusal kısıtlarla uygulanır: (30) $\mu_{1,k}\le p_{1,k}$ ve $\mu_{2,k}\le p_{2,k}$; (31) $\xi_k-1-\delta\in[-2(1+\hat\delta_m)(1-p_{1,k}),0]$; (32) $\xi_k+1+\delta\in[0,2(1+\hat\delta_m)(1-p_{2,k})]$.
- Sonuç **(33)** bir MIQP'dir: $J(\tilde u)$ minimize edilir; kısıtlar $\tilde u\in\tilde U$, $\varepsilon\le\delta^{[q]}\le\hat\delta_m^{[q]}$, (22)–(26), (30)–(32) ve $p\in\{0,1\}$'dir, her $q$ için. Problem (21) ile **eşdeğerdir**, yani gevşetme değildir. Makale CPLEX ile çözmüştür.
- **Remark 1:** $G^{[q]}$ tam satır ranklı değilse eksik yönler $H^{[q]}\gamma^{[q]}$ ile tamamlanır ve benzer bir program elde edilir.

> **[Yorum] Dual yorumu ve Taylor'la köprü.** LP (20)'nin duali, (24)–(26)'dan okunabilir:
> $$\hat\delta(\tilde u)=\max_\lambda\{\lambda^\top(\tilde N\tilde u-c)-1:\ \|G^\top\lambda\|_1\le1\}.$$
> (Gerekçe: $\mu_1-\mu_2=G^\top\lambda$, $\mathbf 1^\top(\mu_1+\mu_2)=1$ ve $\mu\ge0$ birlikte $\|G^\top\lambda\|_1\le1$ demektir.) Dolayısıyla
> $$\hat\delta(\tilde u)>0\iff\exists\lambda:\ \lambda^\top\tilde N\tilde u>\lambda^\top c+\|G^\top\lambda\|_1=h_Z(\lambda).$$
> Burada $h_Z$, $Z$'nin destek fonksiyonudur (support function). Bu bir **ayırıcı hiperdüzlem / Farkas sertifikasıdır**: $\lambda$, iki bulutu ayıran düzlemin normalidir. Bu "∃λ" formu doğrudan kullanılsaydı kısıt $\lambda$ ile $\tilde u$ arasında **bilineer** olurdu ($\lambda^\top\tilde N\tilde u$). Taylor'ın bilineer SDP'sindeki yapı da muhtemelen budur. Scott bilineerlikten kaçmak için primal+dual (KKT) yazıp tamamlayıcılığı ikili değişkenlerle doğrusallaştırıyor. Sonuç, dal-sınır (branch-and-bound) ile **global** çözülebilen bir MIQP'dir.

**(g) Yardımcı adımlar (s. 1584).**

- *$\hat\delta_m$ hesabı (5.1):* $\hat\delta$ parametrik bir LP'nin değeri olduğu için $\tilde U$ üzerinde konvekstir. Maksimumu $\tilde U$'nun köşelerindedir. Köşe sayısı çoksa (34) "tahmin et ve doğrula" MILP'i kullanılır; Lemma 5 tahminin geçerliliğini karakterize eder.
- *Durum kısıtları (5.2):* Doğru senaryo hangisi olursa olsun durumun $\mathscr X=\{z:Hz\le k\}$ politopunda kalması istenebilir: $\Phi_k(\tilde u_{0:k-1},\tilde i_{0:k})\subset\mathscr X$ (35). Lemma 1 ile bu, nominal durum üzerinde $H\bar\phi_k\le k'$ doğrusal kısıtına dönüşür; yani dayanıklı (robust) kısıt ucuzdur.

**(h) Karmaşıklık ve indirgeme (Bölüm 6, s. 1584–1585).**

- İkili değişken sayısı $B=\sum_q 2n_g^{[q]}$'dur. Mertebe $\ell=n_g/((N+1)n_y)$ ile yazılırsa $B=Q\cdot2(N+1)n_y\ell$ olur.
- **Çift eleme (6.1):** Her çift için şu QP çözülür:
$$\min\{J(\tilde u):\tilde u\in\tilde U,\ \tilde N\tilde u=G\xi+c,\ \|\xi\|_\infty\le1\} \quad (36)$$
  - QP olursuzsa hiçbir izinli giriş bu çifti çakıştıramaz, yani kısıt atılır.
  - Olurluysa ve optimum değer $J_*>0$ ise (yani $0\notin Z$), kısıt tek bir doğrusal kısıtla değiştirilir: $(\lambda^{[q]})^\top\tilde u\le(1-\gamma)J_*^{[q]}$ ve $(\lambda^{[q]})^\top=(\tilde u_*^{[q]})^\top\tilde R$ (37). Bu, ayırıcı kümenin içinde kalan, orijini içeren bir yarı-uzaydır.
  - **Lemma 6:** Ayırmayan her $\tilde u$ (37)'yi ihlal eder. (37)'yi ihlal eden her $\tilde u$ için $J\ge(1-\gamma)^2J_*$'dır. Dolayısıyla elde edilen program bir kısıtlamadır (restriction). Optimum değer tüm $q$'lar için $(1-\gamma)^2J_*^{[q]}$'dan küçükse orijinal programa eşdeğerdir. Uygulamada $\gamma=10^{-6}$ kullanılmıştır.
  - Makalenin yorumu: "Muhtemelen ayırt edilmesi zor birkaç kilit çift vardır ($0\in Z$); geri kalanlar kolaydır."
- **Zonotop mertebe indirgeme (6.2):** $\tilde Z^{[q]}$ dıştan daha düşük mertebeli bir zonotopla değiştirilir. Bu muhafazakârdır ama hâlâ garantili ayırıcıdır (Teorem 3). Mertebeyi bir azaltmak ikili değişken sayısını $Q\cdot2(N+1)n_y$ kadar düşürür. Makale bunu "by a factor of" diye ifade ediyor; $B$ formülüne göre doğru okuma "kadar azalma"dır **[Yorum]**.

**(i) Gözlemci tabanlı yöntem (Bölüm 7, s. 1585–1586).** Amaç ikili değişken sayısının $N$'ye bağımlılığını kaldırmaktır.

- Her senaryo için Luenberger tipi bir gözlemci kurulur, $\hat x_0=c_0$:
$$\hat x_{k+1}=A\hat x_k+Bu_k+r+L(y_k-\hat y_k) \quad (41)$$
$$\hat y_k=C\hat x_k+s \quad (42)$$
  Hatalar girişten bağımsızdır ((43)–(44)); hata sınırları $\hat E_k,\hat F_k$ özyinelemeli zonotoplardır ((45)–(46)).
- Gerçek senaryo için $\tilde y\in\tilde\Psi_{0:N}\Rightarrow y_N\in\hat\Psi_N(\tilde u,\tilde i,\tilde y_{0:N-1})$ (47) sağlanır. Gözlemci tam değildir: (47)'nin tersi geçmez.
- Çevrimiçi test (48): $y_N\in\hat\Psi_N(\cdot,\tilde i,\cdot)$, $n_y$ boyutlu ve özyinelemeli olarak kontrol edilir.
- **Tanım 2 ($\mathscr L$-ayırma):** $\tilde i$ verildiğinde, $\tilde i$'nin üretebileceği her geçmiş $\tilde y_{0:N-1}$ için $\hat\Psi_N(\tilde u,\tilde i,\cdot)\cap\hat\Psi_N(\tilde u,\tilde j,\cdot)=\emptyset$ olmalıdır ((49)–(50)).
- **Tanım 3 ($\mathscr L^*$):** "$\tilde i$ verildiğinde **veya** $\tilde j$ verildiğinde" ayırma yeterlidir. Ek bir mantık adımıyla teşhis yine garantilidir.
- $\mathscr L^*$-ayırıcı her giriş, Tanım 1 anlamında da ayırıcıdır; tersi doğru değildir (s. 1585–1586). Bu yüzden tam yöntem en az bu kadar iyi sonuç verir, gözlemci yöntemi ise çok daha ucuzdur.
- Aynı form, şimdi $n_y$ boyutunda, yeniden elde edilir: $\{\tilde u:N^{[q]}\tilde u\notin Z^{[q]}\}$ (51), $N^{[q]}\in\mathbb R^{n_y\times Nn_u}$. Türetme şöyledir: $q_k=(\hat x_k(\tilde i),\hat x_k(\tilde j),x_k)$ artırılmış sistemi ((53)–(54)) ve $\Gamma_N(\tilde u)=\{G^\Gamma_N,\bar{\mathscr B}^\Gamma_N\tilde u+\bar\gamma_N\}$ ile
$$[I\ -I\ 0]\bar{\mathscr B}^\Gamma_N\tilde u\notin\hat F_N(\tilde i)\oplus\hat F_N(\tilde j)\oplus[I\ -I\ 0]\Gamma_N(0). \quad (55)$$
- İkili değişken sayısı $\mathscr L^*$ için $Q(2n_y\ell)$, $\mathscr L$ için $(2Q)(2n_y\ell)$'dir; $N$'den bağımsızdır.
- **$L(i)=0$ (7.2):** Koşul yalnızca uç zaman kümelerinin ayrıklığına iner: $\Psi_N(\tilde u,\tilde i)\cap\Psi_N(\tilde u,\tilde j)=\emptyset$ (56). Bu "terminal-ölçüm yöntemi"dir; ölçümlerden bağımsız ve simetriktir. Makaleye göre özellikle $\mathrm{rank}\,C(i)=n_x$ olduğunda iyi çalışır.
- Kararlı $A_L(i)$ veren kazançlar (Kalman, kutup yerleştirme) "çoğu durumda iyi çalışıyor" ama sonuç kullanıcının seçimine çok bağlıdır. Optimal $L$ seçimi açık bir problem olarak bırakılmıştır.

### Ana sonuçlar ve örnekler

**Örnek 1: 2 durumlu sistem, 5 model (Bölüm 8, s. 1586–1587).**

- Model: $A(1)=\begin{bmatrix}0.6&0.2\\-0.4&-0.2\end{bmatrix}$, $B(1)=I_2$, $C=[1\ 0]$ (yani $n_y=1$), $B_w(1)=\mathrm{diag}(1,0)$, $D_v=1$.
- Arızalar: modeller 2 ve 3 aktüatör arızasıdır, $B(2)=\mathrm{diag}(1,0)$ ve $B(3)=\mathrm{diag}(0,1)$. Modeller 4 ve 5 sistem arızasıdır, $A(4)=\begin{bmatrix}1.2&0.2\\-0.4&-0.2\end{bmatrix}$ ve $A(5)=\begin{bmatrix}2.0&0.2\\-0.4&-0.7\end{bmatrix}$.
- Belirsizlik kümeleri: $X_0=\{0.2I,(-3,-3)\}$, $W=\{0.5I,0\}$, $V=\{0.2,0\}$. Amaç ve kısıt: $R=I$, $U=\{\|u\|_\infty\le9\}$.
- Her senaryoda tek bir model tüm ufukta aktiftir; 5 senaryo ve $Q=10$ çift vardır.

Tam-ölçüm yöntemi (Bölüm 5):

| Ayar | Sonuç |
|---|---|
| Olurluluk | Yalnızca $N\ge2$ için olurlu |
| $\ell=1$, $N=2$ | $\lVert\tilde u\rVert_2=8.6143$, 0.02 s |
| $\ell=2$, $N=2$ | $8.6081$, 3.58 s |
| $\ell=2$, çift eleme ile | Aynı optimum 8.6081, 0.36 s (bir mertebe hızlanma) |

- Çift elemenin ayrıntısı: 3 çift (36) olursuz çıktığı için atıldı. $\ell=1$'de 1 çift doğrusal kısıta dönüştü ve $Q'=6$ kaldı; $\ell=2$'de 4 çift dönüştü ve $Q'=3$ kaldı.
- Makaledeki ikili değişken sayısı ifadesi tutarsız görünüyor. Makale "$2Q(N+1)n_y\ell=10(N+1)$ veya $20(N+1)$" yazıyor; oysa $Q=10$, $n_y=1$ ile formül $20(N+1)\ell$ verir **[Yorum]**.

Gözlemci tabanlı yöntem:

| Kazanç | Olurluluk | En iyi sonuç |
|---|---|---|
| (a) $L=0$ ("terminal-ölçüm") | $N\ge3$ | $N=3$, $\ell=1$: $\lVert\tilde u\rVert_2=11.5203$, 0.01 s (Şekil 2) |
| (b) Kalman kazancı ($Q'=1000I$, $R'=I$) | $N\ge2$ | $N=2$, $\ell=1$: $9.2144$, 0.01 s (Şekil 3) |

- Neden (a) daha zayıf? Şekil 1'deki 3-B bulutlar ayrık olsa da $y_2$ eksenine izdüşümleri çakışıyor. Bu yüzden tam yöntemin optimal girişi (a) için $\mathscr L^*$-ayırıcı değildir (s. 1587).
- Bu örnekte $\ell$'yi artırmak gözlemci yöntemlerine fayda sağlamamış.

> **[Yorum] Neden en az $N=2$ gerekiyor? $\tilde N(i,j)$'nin rolüne güzel bir örnek.** İlk Markov parametreleri $CB(i)$ şöyledir:
>
> | Model | $CB(i)$ |
> |---|---|
> | 1 | $[1,0]$ |
> | 2 | $[1,0]$ |
> | 3 | $[0,0]$ |
> | 4 | $[1,0]$ |
> | 5 | $[1,0]$ |
>
> $N=1$ ufkunda $y_1$ girişi yalnızca $CB$ üzerinden görür ($y_0$ girişten bağımsızdır). Bu yüzden (1,2), (1,4), (1,5), (2,4), (2,5) ve (4,5) çiftleri için $\tilde N=0$ olur: sinyal bu bulutları **aynı** miktarda kaydırır. Bu çiftlerden en az biri sıfır girişte çakışıyorsa hiçbir sinyal yardım edemez. $N=1$'deki olursuzluğun olası açıklaması budur; makale bu açıklamayı vermiyor.
>
> $N=2$'de ikinci Markov parametreleri $CA(i)B(i)$ devreye girer:
>
> | Model | $CA(i)B(i)$ |
> |---|---|
> | 1 | $[0.6,0.2]$ |
> | 2 | $[0.6,0]$ |
> | 3 | $[0,0.2]$ |
> | 4 | $[1.2,0.2]$ |
> | 5 | $[2.0,0.2]$ |
>
> Artık bütün çiftler ayrışır, ama farklı yönlerden. (1,2) çifti $y_2$'de yalnızca $u_0$'ın 2. bileşenine duyarlıdır (fark $[0,0.2]$). (4,5) çifti ise yalnızca $u_0$'ın 1. bileşenine duyarlıdır (fark $[0.8,0]$). Sonuç: optimal sinyal, her çiftin "baktığı" giriş yönünü uyarmak zorundadır. "Sinyal iki bulutu farklı kaydırmalı" sezgisinin tam karşılığı budur.

**Rastgele büyük sistemler (s. 1587–1588).** $n_x=50$, $n_y=n_u=n_w=n_v=10$, MATLAB `drss`; $U=\{\|u\|_\infty\le20\}$, $N=10$, $\ell=1$, 100 test. Gözlemci yöntemi $L=0$ ile çalıştırılmıştır.

| Durum | Tam yöntem: süre | Gözlemci: süre | Tam yöntem: norm | Gözlemci: norm |
|---|---|---|---|---|
| 2 model | 1.13 s | 0.04 s | 19.01 | 41.70 |
| 3 model | 50.30 s | 1.04 s | 247.10 | 573.99 |

- $N=100$'de yalnızca gözlemci yöntemi çalışabilmiştir (ortalama 20.42 s).
- $\ell=2$ ve 2 modelle ortalama süreler: $N=10$'da 6.0358 s, $N=100$'de 18.4609 s.

**DC motor (Bölüm 8.1, s. 1588–1589).**

- Model: 2 durum (akım $i$, hız $n$), iki çıkış (her ikisi de ölçülüyor). 6 model (Tablo 1): arızasız; armatür direnci +0.5 Ω; armatür direnci +1.14 Ω; fırça aşınması; iki komütatör çubuğunun kısa devresi; bobinin komütatörden kopması. Parametreler deneysel verilerden alınmıştır (Tablo 2).
- Ayrıklaştırma: ileri Euler, 5 ms.
- Giriş: nominal $u_c=6$ V, $r(i)=B(i)u_c$ ile modellenmiş. Aktif sinyal $u_s$ buna eklenir, $|u_s|\le6$ V.
- Parametrik belirsizlik: %5'lik belirsizlik, akım $[-2,2]$ A ve hız $[-150,150]$ rad/s sınırlı varsayılarak en kötü durum toplamsal hatası olarak $B_w(i)w_k$'ya gömülmüştür.

Sonuçlar:

| Ayar | $N$ | $\lVert\tilde u\rVert$ | Süre |
|---|---|---|---|
| 6 model, gözlemci $L=0$, $\ell=3$ | 9 (en küçük olurlu) | 15.92 | 58.47 s (Şekil 4) |
| 6 model, aynı ayar + çift eleme (15 → 10 çift; optimum korunmadı) | 10 | 16.0095 | 0.065 s |
| 3 senaryo (2, 4, 6), tam-ölçüm yöntemi, $\ell=1$ | 2 (en küçük olurlu) | 6.5762 | 0.035 s |

3 senaryo (2, 4, 6) için gözlemci yöntemi, Tablo 3:

| $\ell$ | $L=0$: $N$ | $L=0$: $\lVert\tilde u\rVert$ | $L=0$: süre | Kutup yerleştirme: $N$ | Kutup yerleştirme: $\lVert\tilde u\rVert$ | Kutup yerleştirme: süre |
|---|---|---|---|---|---|---|
| 1 | 7 | 13.571 | 0.02 s | 2 | 7.182 | 0.01 s |
| 2 | 7 | 13.571 | 0.02 s | 2 | 7.182 | 0.01 s |
| 3 | 7 | 13.571 | 0.07 s | 2 | 7.182 | 0.03 s |
| 4 | 7 | 13.559 | 0.28 s | 2 | 6.846 | 0.71 s |
| 5 | 3 | 8.433 | 4.41 s | 2 | 6.846 | 4.33 s |
| 6 | 3 | 8.230 | 36.71 s | 2 | 6.846 | 22.35 s |

- Kutup yerleştirmede $A_L(i)$ özdeğerleri sıfıra konmuştur. Kalman kazancı bu örnekte tatmin edici sonuç vermemiştir.
- İyi bir $L(i)$ tasarımı performansı ciddi biçimde artırıyor.
- Tam-ölçüm satırı için bir not: makale "this example" diyor ve cümle 3 senaryo paragrafının hemen ardından geliyor. 6 model için mi, 3 senaryo için mi geçerli olduğu metinden kesin değil **[Yorum]**.

### Varsayımlar ve sınırlamalar

1. Modeller doğrusal, ayrık-zamanlı ve matrisleri bilinir. Arızalar sonlu bir model kümesi arasında anahtarlama olarak modellenir. Senaryo kümesi $\tilde{\mathbb I}$ verilidir ve seçimi kullanıcıya bırakılmıştır (s. 1581).
2. Belirsizlikler **noktasal (pointwise)** zonotoplarla sınırlıdır; stokastik değildir. Garanti, ancak bu kümeler gerçeği kapsıyorsa geçerlidir.
3. Enerji sınırlı belirsizlik bu makalenin konusu değildir; Campbell & Nikoukhah çizgisi enerji sınırlarını ele alır (s. 1580–1581).
4. Noktasal elipsoidal sınırlar ancak dış zonotop yaklaşımıyla işlenebilir ve bu muhafazakârdır (Remark 2). Elipsoid sınırları altında erişilebilir kümeler elipsoid değil, zonoid'dir.
5. Giriş **açık çevrimdir**; $N$ sabittir ve 1'den başlayarak artırılır.
6. $G^{[q]}$'nun tam satır ranklı olduğu varsayılır (Remark 1 bunu genelleştirir). Olurlu küme kapalı değildir, bu yüzden $\varepsilon$ eşiği kullanılır. Big-M için $\hat\delta_m$ hesaplanmalıdır.
7. Karmaşıklık: ikili değişken sayısı $Q\cdot2(N+1)n_y\ell$'dir. $Q$, senaryo sayısının karesiyle büyür. MIQP en kötü durumda üsteldir. Mertebe indirgeme ve çift eleme muhafazakârlık ekleyebilir; DC motor örneğinde çift eleme optimumu korumamıştır.
8. Parametrik (girişle çarpılan) belirsizlik ancak toplamsal bozucuya "en kötü durum" olarak gömülerek ele alınabilir (DC motor örneği). Bu da durum sınırlarının varsayılmasını gerektirir.
9. Gözlemci kazancı seçimi açık bir problemdir (7.2).

### Taylor TAC 2025 ile karşılaştırma

| Boyut | Scott 2014 | Taylor & Domínguez-García 2025 **[Taylor özeti]** |
|---|---|---|
| Model | Ayrık-zamanlı doğrusal **dinamik**, $N$ adımlık ufuk | **Statik** doğrusal: $\Theta_k\theta+X_kx=h_k+H_k\lambda_k$, $k=0..M$ |
| Belirsizlik | $\lVert\xi\rVert_\infty\le1$ → zonotop, noktasal | $\lVert\lambda_k\rVert<1$ (2-norm ise elipsoid) |
| Bulutun gösterimi | Açık (explicit), üreteçlerle: $y=G\xi+c$ | Örtük (implicit): $X_kx\in\dots$; $X_k\ne I$ olabilir |
| Ek kısıtlar | Girişte politop $U$, durumda dayanıklı politop $\mathscr X$ | $x$ üzerinde isteğe bağlı karesel kısıtlar |
| Ayrışma testi | Lemma 2: nokta–zonotop üyeliği, bir LP | Farkas/dualite ve SDP gevşetmesi |
| Tasarım problemi | MIQP; **gevşetme yok**, dal-sınır ile global optimum | Bilineer SDP; gevşetmeye dayanır ve konveks değildir |
| Amaç | $\sum u^\top Ru$ (karesel), istenirse MPC içinde | En küçük $\lVert\theta\rVert$ |
| Alt sınır | Makalede yok | $\lVert\theta\rVert\ge(1-\zeta)/\chi$ (toplamsal, kısıtsız durum) |
| Çevrim | Açık çevrim | Açık çevrim, tek atış |
| Arızanın zamanlaması | Ufuk içinde model geçişleri (senaryolar) mümkün | Statik: her hipotez tek bir model |

**1) Dinamik ile statik aslında aynı geometri [Yorum].** Scott'un dinamik problemi, yığınlama sonrasında **statik** bir problemdir: $\tilde y=\tilde C\tilde B(i)\,\tilde u+(\text{belirsizliğe bağlı terim})$. Teorem 3'ün ispatı tamamen statiktir; zamanın tek katkısı $\tilde C\tilde B$ ve $G^\Psi$ matrislerini kurmaktır.

Tersine, Taylor'ın modelinde $X_k=I$ ve $\infty$-norm alınırsa, model $k$'nın bulutu $\{H_k,\ h_k-\Theta_k\theta\}$ olur. Lemma 2 doğrudan şunu verir:
$$\text{ayrık}\iff(\Theta_i-\Theta_j)\,\theta\notin\{[H_i\ H_j],\ h_i-h_j\}.$$
Bu, tek zaman adımlı bir Teorem 3'tür ve $N_{\text{Taylor}}(i,j)=\Theta_i-\Theta_j$ karşılığını verir. (Taylor'da $\|\lambda\|<1$ açık top olduğu için sınır durumları biraz farklıdır.)

**2) $\tilde N(i,j)$'nin rolü: "sinyal iki bulutu farklı kaydırmalı".** $\tilde N(i,j)=\tilde C(j)\tilde B(j)-\tilde C(i)\tilde B(i)$, iki modelin giriş→çıkış haritalarının (Markov parametrelerinden oluşan alt-üçgen bloklu matrislerin) farkıdır; Raimondo bunlara "output controllability matrices" der. Bulut merkezi $\tilde C\tilde B(i)\tilde u$ kadar kayar, dolayısıyla $\tilde N\tilde u$ **göreli kaymanın kendisidir**. Sonuçları:

- $\tilde N\tilde u=0$, yani $\tilde u\in\ker\tilde N$ ise iki bulut aynı miktarda kayar. Bu sinyal o çift için tamamen boşa harcanmıştır. Çekirdekteki (null space) bileşenler "boşa enerji"dir **[Yorum]**.
- $\tilde N=0$ ise sinyal hiçbir zaman yardım etmez. Sonuç yalnızca sıfır girişte bulutların çakışıp çakışmadığına bağlıdır. Öğrencinin "aynı kaydırırsa hiçbir sinyal yardım etmez" sezgisinin kesin ifadesi budur (s. 1583).
- $\tilde Z$ yalnızca belirsizlik kümelerine bağlıdır, $\tilde N$ ise yalnızca model matrislerine. Bu ayrışma sayesinde "ne kadar itmek gerekiyor" (çarpışma kümesinin genişliği) ile "sinyal ne kadar kaldıraç sağlıyor" ($\tilde N$'nin kazancı) ayrı ayrı okunabilir **[Yorum]**.
- Çok çift varsa sinyal aynı anda bütün $\ker\tilde N^{[q]}$'lardan uzak durmalı ve bütün $\tilde Z^{[q]}$'lardan çıkmalıdır **[Yorum]**.

**3) Alt sınırın Scott dilindeki karşılığı [Yorum: kendi türetimim].** Dual sertifikadan: $\tilde u$ ayırıyorsa bir $\lambda$ vardır ($\|G^\top\lambda\|_1=1$ olarak normalize edilir) ve $\lambda^\top\tilde N\tilde u>1+\lambda^\top c$ sağlanır. Cauchy–Schwarz ile
$$\|\tilde u\|_2>\frac{1+\lambda^\top c}{\|\tilde N^\top\lambda\|_2}=\frac{1-\zeta(\lambda)}{\chi(\lambda)},\qquad \zeta(\lambda):=-\lambda^\top c,\ \ \chi(\lambda):=\|\tilde N^\top\lambda\|_2 .$$

- Tek bir çift için ve giriş kısıtı yoksa bu ifade sıkıdır:
$$\inf\{\|\tilde u\|_2:\tilde u\text{ ayırır}\}=\min_{\lambda}\frac{h_Z(\lambda)}{\|\tilde N^\top\lambda\|_2}\qquad(0\in Z\text{ iken}).$$
  Gerekçe: ayırıcı küme, açık yarı-uzaylar $\{\tilde u:\lambda^\top\tilde N\tilde u>h_Z(\lambda)\}$'nin birleşimidir.
- Taylor'ın $(1-\zeta)/\chi$ sınırı yapı olarak buna çok benziyor: pay "sıfır sinyalde bulutlar ne kadar iç içe" ölçüsü, payda "sinyalin bulutları ayırma kaldıracı". Ancak Taylor'daki $\zeta$ ve $\chi$'nın tanımlarının bununla örtüşüp örtüşmediğini kontrol etmek gerekir.
- Formül her konveks bulut şekli için geçerlidir. Elipsoidlerde destek fonksiyonu $h(\lambda)=\lambda^\top c+\|H_i^\top\lambda\|_2+\|H_j^\top\lambda\|_2$ olur.

**4) Set sınıfının sonuçları.**

- Zonotoplar doğrusal dönüşüm ve Minkowski toplamı altında kapalıdır. Kutu bir çarpım kümesi olduğundan $\|(\xi_i,\xi_j)\|_\infty\le1\iff\|\xi_i\|_\infty\le1,\|\xi_j\|_\infty\le1$ sağlanır. Bu sayede iki bulutun Minkowski toplamı, üreteçleri yan yana koyarak tek bir zonotop olur.
- Elipsoidlerin Minkowski toplamı elipsoid değildir (Remark 2'deki "zonoid" notu bunun dinamik halidir). Taylor'ın ayrı $\lambda_i$, $\lambda_j$ topları tek bir topa birleştirilemez **[Yorum]**. Bu, Taylor'ın neden çarpanlı bir Farkas/S-lemma/SDP yaklaşımına ihtiyaç duyduğunu kısmen açıklıyor olabilir. Taylor'daki karesel kısıtlar ise zonotop çerçevesinde hiç ifade edilemez.
- Scott'un ifade edebildikleri: zaman korelasyonu (ortak $x_0$ ve bozucular), ufuk içinde arıza geçişi, dayanıklı durum kısıtları, giriş genlik kısıtları, kesin global optimum.
- Scott'un ifade edemedikleri: 2-norm ve enerji tipi belirsizlik (yalnızca muhafazakâr yaklaşık), ölçüm üzerinde karesel kısıtlar, girişle çarpılan belirsiz parametreler, örtük $X_k$ (bu sonuncusu kısıtlı zonotoplarla mümkün; aşağıya bakın).

**5) Konvekslik dışılık kaçınılmaz [Yorum].** Her iki çerçevede de olurlu sinyal kümesi bir konveks kümenin tümleyenidir. Herhangi bir kesin yöntem ya kombinatoryal (Scott: ikili değişkenler) ya da bilineer (Taylor: çarpan × sinyal) olmak zorunda görünüyor. İki makale aynı ters-konveks (reverse-convex) kısıtı iki farklı yoldan yönetiyor.

### Projeyle bağlantı ve araştırma fikirleri

Bu bölümdeki her şey **[Yorum]**dur.

**Fikir A (bence en umut verici): 2-B sinyal durumu için gevşetmesiz "kesin çözücü" ve SDP gevşetmesinin ölçülmesi.**

Mesafe korumasında sinyal $\theta\in\mathbb R^2$ ise (ör. enjekte edilen ek akım fazörünün iki bileşeni) Scott'un yapısı çok ucuz ve kesin bir yöntem verir.

1. *Kutu veya politop belirsizlikte kesin çözüm.* Belirsizlik kutuyla ifade edilebiliyorsa (kanal başına ölçüm hatası, $R_f$ gibi parametreler için aralık sınırları), her çift $q$ için yasak bölge şudur:
$$K_q=\{\theta\in\mathbb R^2:\ N_q\theta\in Z_q\}.$$
   Bu, 2-B bir **konveks çokgendir**; $N_q$ rank 1 ise bir şerit, $N_q=0$ ise boş ya da tüm düzlemdir. $K_q$, $\{(\theta,\xi):N_q\theta=G_q\xi+c_q,\|\xi\|_\infty\le1\}$ kümesinin $\theta$'ya izdüşümüdür. Nikoukhah'ın yüksek boyutta işlenemeyen izdüşümü 2-B'de birkaç LP ile tam hesaplanır.
2. Ayırıcı sinyaller $\mathbb R^2\setminus\bigcup_qK_q$'dur. En küçük normlu nokta birleşimin sınırındadır. Aday noktalar sonlu sayıdadır: orijinin her kenar doğrusuna dik izdüşümü, çokgen köşeleri ve farklı çokgenlerin kenar kesişimleri. Başka bir çokgenin içine düşmeyen en küçük normlu aday cevaptır. Bu **kesin ve global** bir yöntemdir.
3. Alternatif olarak doğrudan Scott'un (33) MIQP'si kullanılabilir. Amaç $\|\theta\|_\infty$ veya $\|\theta\|_1$ seçilirse problem bir MILP olur ve ücretsiz çözücülerle çözülebilir (ör. HiGHS, CBC, GLPK_MI; CVXPY'deki güncel destek kontrol edilmeli). $\|\theta\|_2$ için MIQP gerekir (SCIP, Gurobi vb.).
4. *Elipsoidal (2-norm) belirsizlik.*
   - **Sandviç yöntemi.** Elipsoid dıştan bir zonotopla yaklaşıklanırsa, bulunan sinyal kesin olarak ayırır ve gerçek minimum için bir **üst sınır** verir. İçten yaklaşıklanırsa gerçek minimum için bir **alt sınır** elde edilir. Mertebe arttıkça iki sınır birbirine yaklaşır.
   - **Doğrudan 2-B yöntem.** Her açı $\varphi$ için ışın $t\,d(\varphi)$ üzerinde $K_q\cap\text{ışın}$ bir aralıktır ve küçük bir SOCP ile bulunur. Sonra en küçük olurlu $t(\varphi)$ hesaplanır ve $\varphi$ üzerinde 1-B arama yapılır. Bu yöntem açısal çözünürlük dışında kesindir.
5. **Kullanım:**
   - (i) Taylor'ın bilineer SDP'sinin bulduğu $\theta$'nın kesin optimuma ne kadar uzak olduğunu (gevşetme açığını) ölçmek.
   - (ii) $(1-\zeta)/\chi$ alt sınırının ne kadar sıkı olduğunu, yukarıdaki tek çift formülü $\min_\lambda h_Z(\lambda)/\|N^\top\lambda\|$ ile karşılaştırmak.
   - (iii) Ayrıca *yönü* görselleştirmek: hangi fazör yönü hangi çifti ayırıyor?
6. *Uyarı.* Bu yöntem, sinyalin bulutları **yalnızca ötelediği** yapıya dayanır. Belirsiz bir parametre sinyalle çarpılıyorsa (ör. enjekte akımın gerilime etkisi bilinmeyen bir empedansa bağlıysa), bulutun şekli $\theta$ ile değişir ve Teorem 3 geçerli olmaz. Çözüm yolu, parametre aralığını alt aralıklara bölüp her birini ayrı bir model saymaktır; bu $Q$'yu büyütür.

**Fikir B: çift tanılaması ($\tilde N$ haritası).** Koruma hipotezlerinin her çifti için $N_q$ ve "$0\in Z_q$ mı?" hesaplanır. Çiftler üç sınıfa ayrılır:

- **pasif ayrılabilir:** $0\notin Z$
- **asla ayrılamaz:** $N=0$ ve $0\in Z$
- **aktif ayrılabilir:** diğerleri

Scott'un çift eleme fikri (Lemma 6) bunu sistematik hale getirir. Beklentim, zor çiftlerin bölge sınırına (reach) yakın arıza konumları olmasıdır. Asla ayrılamayan çiftler, sinyalin fiziksel olarak hangi bilgiyi taşıyamadığını gösterir.

**Fikir C: yalnızca sınıflar arası ayrışma.** Scott bütün çiftlerin ayrılmasını ister. Korumada ise yalnızca "aç" (bölge içi) ile "açma" (bölge dışı) hipotezlerinin ayrılması yeterlidir. Kısıtlar yalnızca sınıflar arası çiftlere uygulanırsa $Q$ küçülür ve sinyal küçülür. Bölge sınırında bir ölü bant (ör. %80 ile %100 arası) tanımlamak ise "asla ayrılamaz" çiftleri ortadan kaldırmanın doğal yoludur.

**Fikir D: çok periyotlu (dinamik) sürüm.** Birkaç şebeke periyodu boyunca enjeksiyon yapılıp ölçümler yığınlanırsa problem Scott'un dinamik çerçevesine girer. "En küçük ayrışma ufku", gereken en az periyot sayısı olarak yorumlanabilir. Ortak belirsizlikler (aynı $R_f$, aynı kaynak empedansı) zaman boyunca korelasyon olarak gelir; (14)'teki bağ korunduğu için bu bilgi kullanılır. Uzun ufuklarda gözlemci tabanlı yöntem (Bölüm 7) kullanılabilir.

**Fikir E: inverter akım sınırları.** Dayanıklı durum kısıtı (35) ve politop giriş kısıtı $U$, inverterin akım ve gerilim limitlerini her hipotez altında **sert** kısıt olarak koymaya izin verir. Bu MIQP'de doğrusal kısıttır ve ucuzdur.

---

## 2. Raimondo ve diğ. (2016): Küme-değerli gözlemcilerle kapalı-çevrim giriş tasarımı

### Künye

Davide M. Raimondo, Giuseppe Roberto Marseglia, Richard D. Braatz, Joseph K. Scott. "Closed-loop input design for guaranteed fault diagnosis using set-valued observers." *Automatica*, 74:107–117, 2016. DOI: 10.1016/j.automatica.2016.07.033. İlgili ön çalışma 12th European Control Conference'ta (2013, Zürih) sunulmuştur (s. 107 dipnotu).

### Tek cümlede

Scott 2014'ün MIQP tabanlı açık-çevrim tasarımını üç yönde genişletir. Kısıtlı zonotoplarla **genel politop** belirsizliklere taşır. Bunu küme-değerli gözlemcilerle bir **kayan ufuk (moving horizon)** döngüsüne koyar: her adımda ölçümle bulutları daraltıp sinyali yeniden tasarlar ve teşhis garantisini korurken ortalama sinyal boyunu ve normunu düşürür. Çevrimiçi hesabı azaltmak için de geçmiş ölçümlere göre önceden hesaplanmış **açık (explicit) bir kontrol yasası** (bakma tablosu, lookup table) önerir.

### Sezgisel anlatım

1. **Açık çevrimin israfı.** Açık çevrimde sinyal baştan tasarlanır ve sonuna kadar körlemesine uygulanır. Ölçümler gelir ama sinyal değişmez. Oysa her ölçüm, her model için "hâlâ mümkün olan durumlar" kümesini **daraltır**: bulutlar küçülür, bazı modeller tamamen elenir. Küçülmüş bulutları ayırmak için daha küçük ya da daha kısa bir sinyal yeterli olabilir.
2. **Kapalı çevrim fikri.** Her adımda her model için bir küme-değerli gözlemci ölçümü işler ve "şu an olası durumlar" kümesini $\hat X_{k+1|k}(i)$ günceller. Kalan süre için bu kümeleri *yeni başlangıç kümeleri* sayarak Scott'un MIQP'si yeniden çözülür. Yeni sinyal eskisinden iyiyse onunla devam edilir.
3. **Garantinin kaynağı.** Gözlemciler muhafazakâr olduğu için yeni tasarım bazen eskisinden kötü çıkabilir. Algoritma bu yüzden eski planın kaydırılmış halini (shifted sequence) hep yedek olarak tutar ve yeni planı **yalnızca daha iyiyse** kabul eder (Adım 9). Böylece kapalı çevrim, açık çevrimden asla daha geç teşhis koymaz (Teorem 5).
4. **Neden kısıtlı zonotop?** Ölçümle güncelleme bir **kesişim** işlemidir: "tahmin kümesi ∩ ölçümle uyumlu durumlar". Zonotopların kesişimi zonotop değildir ve iyi yaklaşıklanması zordur. Kısıtlı zonotoplarda ise kesişim tam ve ucuzdur; sadece bir eşitlik kısıtı eklenir. Ayrıca belirsizlik kümeleri artık herhangi bir politop olabilir (ör. bir gözlemcinin çıktısı veya modellenmemiş dinamik sınırı).
5. **Açık (explicit) yöntem.** Her adımda MIQP çözmek pahalıdır. Bunun yerine olası ölçüm ve giriş değerleri hücrelere bölünür, her hücre için sinyal çevrimdışı hesaplanır ve çevrimiçi yalnızca tabloya bakılır.

### Matematiksel kurulum

**(a) Model (s. 108).** Model Scott'la aynıdır ((1)–(2)) ancak iki fark vardır:

- Test aralığı $[0,N]$ boyunca **tek bir model $i^*$ aktiftir**; ufuk içinde arıza geçişi yoktur.
- Başlangıç kümesi $X_0(i)$ modele bağlı olabilir (ör. önceki ölçümlerden üretilmiş olabilir). $W$, $V$, $X_0(i)$ sınırlı konveks politoplardır. Giriş kısıtı $u_k\in U$ ve amaç karesel bir maliyettir.

Makalenin önerdiği kullanım: "Periyodik uygulanan kısa test sinyalleri ya da bir arıza **tespit edilmiş ama teşhis edilmemişken**" (s. 108).

**(b) Kısıtlı zonotoplar (s. 108–109).**

- **Tanım 1:** $Z=\{G\xi+c:\|\xi\|_\infty\le1,\ A\xi=b\}$, kısaca $\{G,c,A,b\}$ (3). $Z$ bir CZ'dir ancak ve ancak konveks politoptur (Scott ve diğ. 2016).
- İşlemler:
  - $RZ=\{RG_z,Rc_z,A_z,b_z\}$ (7)
  - $Z\oplus W=\big\{[G_z\ G_w],\ c_z+c_w,\ \mathrm{diag}(A_z,A_w),\ (b_z,b_w)\big\}$ (8)
  - Genelleştirilmiş kesişim: $Z\cap_RY\equiv\{z\in Z:Rz\in Y\}$ (6) için
$$Z\cap_RY=\Big\{[G_z\ 0],\ c_z,\ \begin{bmatrix}A_z&0\\0&A_y\\RG_z&-G_y\end{bmatrix},\ \begin{bmatrix}b_z\\b_y\\c_y-Rc_z\end{bmatrix}\Big\}. \quad (9)$$
- Zonotoplarda (4)–(5) hâlâ kolaydır, ama (6) bir zonotop değildir. CZ'ler için üreteç ve kısıt sayısını azaltan etkili indirgeme yöntemleri vardır (Scott ve diğ. 2016).

**(c) Erişilebilir kümeler (s. 109).** (10)–(13) Scott'unkilerle aynıdır; tek fark kısıtların blok-diyagonal olarak taşınmasıdır.

- $\tilde\Psi_{\ell:k}(\tilde u,i)=\{G^\Psi(i),\bar\psi(\tilde u,i),A^\Psi(i),b^\Psi(i)\}$.
- Girişe tek bağımlılık merkezler üzerindendir ve merkezler $\tilde u$'da doğrusaldır (s. 109). Bu "yalnızca öteleme" gözleminin CZ halidir.

**(d) Açık-çevrim tasarım (Bölüm 3, s. 109–110).**

- Test (14): $\tilde y\in\tilde\Psi_{0:N}(\tilde u,i,X_0(i))$. Bu test başarısız olursa $i$ aktif değildir.
- Gereken özellik, her $i\ne j$ için $\tilde\Psi(\tilde u,j,X_0(j))\cap\tilde\Psi(\tilde u,i,X_0(i))=\emptyset$ (15) koşuludur.
- **Tanım 2:** Bu özelliği sağlayan $\tilde u$, $(\mathbb I,X_0^{\mathbb I})$'yi $N$ adımda ayırır; bu girişlerin kümesi $\mathscr S_N$'dir.
- Girişler önce **uzunluğa**, sonra amaç fonksiyonuna göre sıralanır. Olurlu en küçük $N$'ye **en küçük ayrışma ufku (minimum separation horizon)** $\bar N$ denir.
- Optimizasyon problemi:
$$\inf\{J_N(\tilde u):\tilde u\in\tilde U_N\cap\mathscr S_N(\mathbb I,X_0^{\mathbb I})\} \quad (16)$$
  Makalede $J_N=\sum_{\ell=1}^{N-1}u_\ell^\top Ru_\ell$ yazılmış; toplam $\ell=1$'den başlıyor, Scott'ta ise $k=0$'dan. Bu muhtemelen bir dizgi hatası **[Yorum]**.
- Dipnot 1: $\mathscr S_N$ açık bir kümedir, bu yüzden "ε-çözüm"lerden söz edilmelidir.
- Scott'un formu hatırlatılır: $\mathscr S_N=\{\tilde u:N(i,j)\tilde u\notin Z(i,j)\}$ (17), burada $N(i,j)=\tilde C(j)\tilde B(j)-\tilde C(i)\tilde B(i)$ ve $Z(i,j)=\{[G^\Psi(i)\ -G^\Psi(j)],\bar\psi(0,i)-\bar\psi(0,j)\}$ (18).
- **Teorem 1 (s. 110):** $\tilde u\in\mathscr S_N\iff N(i,j)\tilde u\notin\mathscr Z(i,j)$ (19), burada
$$\mathscr Z(i,j)=\Big\{[G^\Psi(i)\ -G^\Psi(j)],\ \bar\psi(0,i)-\bar\psi(0,j),\ \mathrm{diag}(A^\Psi(i),A^\Psi(j)),\ (b^\Psi(i),b^\Psi(j))\Big\}. \quad (20)$$
  *İspat (Ek, s. 115):* (9) $R=I$ ile uygulanır. Kesişim (41)'deki kısıtlara sahip bir CZ'dir; bu kısıtların çözümsüz olması (42)'deki CZ'ye üyeliğin olmaması demektir. Son adımda $\bar\psi(\tilde u,i)=\tilde C\tilde B(i)\tilde u+\bar\psi(0,i)$ kullanılır.
  **[Yorum]** Zonotoplarda $-G^\Psi(j)$'deki eksi işareti simetri nedeniyle önemsizdir (Scott'ta yoktur). CZ'ler simetrik olmadığı için burada işaret önemlidir.
- **Sonuç 2 (Corollary 2):** CZ'ye üyelik, daha yüksek boyutlu sıradan bir zonotopa üyeliğe dönüştürülür:
$$\begin{bmatrix}N(i,j)\\0\end{bmatrix}\tilde u\notin\mathscr Z^+(i,j)\equiv\Big\{\begin{bmatrix}G^{\mathscr Z}\\A^{\mathscr Z}\end{bmatrix},\begin{bmatrix}c^{\mathscr Z}\\-b^{\mathscr Z}\end{bmatrix}\Big\}. \quad (21)$$
  Yani "$p=G\xi+c$ ve $A\xi=b$" ile "$(p,0)=[G;A]\xi+[c;-b]$" aynı şeydir. Böylece Scott'un MIQP algoritması **değiştirilmeden** kullanılabilir.
- Makale, $\mathscr Z^+$ kompakt olduğundan "$N(i,j)\ne0$, yani modellerin çıkış kontrol edilebilirlik matrisleri özdeş değil" koşulunun ayırıcı bir girişin varlığı için yeterli olduğunu not eder (s. 110). **[Yorum]** Bu tek bir çift ve kısıtsız giriş için geçerlidir; $U$ sınırlıysa varlık garanti değildir. Ufkun 1'den başlayarak artırılmasının nedeni budur.
- **Karmaşıklık (s. 110):**
  - İkili değişken sayısı toplam üreteç sayısıyla orantılıdır.
  - Zonotoplarda $Z(i,j)$ indirgenir. Doğrudan $\mathscr Z^+$'yı indirgemek ise birinci mertebede bile $(N+1)n_y+2n_c$ üreteç bırakır.
  - Daha esnek yol, önce $\mathscr Z(i,j)$'yi CZ teknikleriyle indirgemek, sonra $\mathscr Z^+$'yı kurmaktır. En agresif indirgemede karmaşıklık $n_w$, $n_v$ ve $n_x$'ten bağımsız hale gelir.

**(e) Küme-değerli gözlemci ve çevrimiçi güncelleme (Bölüm 4, s. 110–111).**

- Kapalı-çevrim varsayımı: $u_{K+1}$, $[K,K+1]$ aralığında $\tilde y_{0:K}$ bilinerek sentezlenebilir. Kapalı çevrimde (15) gereğinden güçlüdür, çünkü ölçümler ek bilgi taşır.
- Her model için gözlemci, $\hat X_{0|-1}=X_0(i)$ ile başlar:
$$\hat X_{k|k}\supset\hat X_{k|k-1}\cap\{x_k:Cx_k\in(y_k-s)\oplus(-D_v)V\}, \quad (22)$$
$$\hat X_{k+1|k}\supset A\hat X_{k|k}\oplus Bu_k\oplus r\oplus B_wW. \quad (23)$$
- (22) tam olarak (9)'dur ($R=C$ ile), dolayısıyla prensipte **tam (exact)** bir gözlemcidir. Uygulamada karmaşıklık hızla büyüdüğü için her adımda hedef üreteç ve kısıt sayısına indirgenir; bu da gözlemciyi muhafazakâr yapar.
- **Lemma 3:** Geçmiş $\tilde y_-$ ile tutarlı her tam yörüngenin geleceği, gözlemci kümesinden başlayan bir yörüngedir:
$$\tilde y\in\tilde\Psi_{0:N}(\tilde u,i,X_0(i))\Rightarrow\tilde y_+\in\tilde\Psi_{0:N-K-1}(\tilde u_+,i,\hat X_{K+1|K}(i)).$$
  Tersi tam gözlemci için geçerlidir. İspat, Ek'teki Lemma 6'nın tümevarımıyla yapılır (s. 115).
- **Teorem 4:**
$$\tilde u_+\in\mathscr S_{N-K-1}(\mathbb I,\hat X^{\mathbb I}_{K+1|K})\Rightarrow\tilde y\in\tilde\Psi_{0:N}(\tilde u,i,X_0(i))\text{ en fazla bir }i\text{ için}. \quad (24)$$
  Tersi tam gözlemci için geçerlidir. Kısacası: kalan sinyal, gözlemci kümelerini başlangıç kümesi sayarak modelleri ayırıyorsa teşhis garantilidir.

**(f) Algoritma 1, "doğrudan yöntem" (s. 111).** Girdiler: $\mathbb I,W,V,X_0^{\mathbb I}$.

1. En küçük ufuk $\bar N$ ve optimal $\tilde u_{0:N-1|-1}$ hesaplanır.
2. $k=0$, $L=-1$ atanır.
3. $u^{CL}_k:=u_{k|L}$ uygulanır.
4. $y_k$ ölçülür.
5. Şu koşulu sağlayan modeller $\mathbb I$'dan çıkarılır:
$$\tilde y_{L+1:k}\notin\tilde\Psi_{L+1:k}(\tilde u^{CL}_{L+1:k-1},i,\hat X_{L+1|L}(i)). \quad (25)$$
6. $k=L+1+N$ ise $\mathbb I_{\text{out}}:=\mathbb I$ ile sonlandırılır.
7. Her model için $\hat X_{k+1|k}(i)$ (22)–(23) ile hesaplanır.
8. Yeni en küçük ufuk $N^*$ ve optimal giriş $\tilde u_{k+1:k+N^*|k}$ hesaplanır.
9. Yeni dizi kaydırılmış eski diziden **kısaysa**, ya da aynı uzunlukta olup **daha küçük amaç değerine** sahipse $N:=N^*$ ve $L:=k$ atanır.
10. $k:=k+1$ atanır ve 3. adıma dönülür.

- **Teorem 5:** $\bar N<\infty$ ise Algoritma 1 en fazla $\beta\le\bar N$ adımda $|\mathbb I_{\text{out}}|=1$ ile sonlanır. Elenen her $i$ için $\tilde y_{0:\beta}\notin\tilde\Psi_{0:\beta}(\tilde u^{CL}_{0:\beta-1},i,X_0(i))$ (26) sağlanır, yani elemeler doğrudur.
  *İspat fikri (s. 116):* $T_k=L+1+N$ hiç artmaz, çünkü güncelleme yalnızca $k+N^*\le L+N$ iken yapılır. Bu yüzden sonlanma en geç $\bar N$'de olur.
  **[Yorum]** Ayırma tanımı "en fazla bir model" garanti eder. $|\mathbb I_{\text{out}}|=1$ olması, makalenin "bir $i^*$ aktif" varsayımına dayanır.
- **Remark 1:** Algoritmada $u_{k+1}$, $[k,k+1]$ aralığında, yani $y_{k+1}$ gelmeden hesaplanır. Önceki sürümde (Raimondo, Braatz, Scott 2013) $u_{k+1}$, $y_{k+1}$'e bağlıydı. Makaleye göre bu ancak çevrimiçi hesap örnekleme süresinden çok daha kısa sürerse anlamlıdır; burada bu olası değildir, ama açık (explicit) yöntem için mümkün olabilir.

**(g) Açık (explicit) yöntem (Bölüm 5, s. 112–113).**

- **Varsayım 1:** Her model gözlemlenebilirdir; $\Omega+1$, modeller arasındaki en büyük gözlemlenebilirlik indeksidir. İzinli tüm girişleri ve olası tüm çıkışları içeren $\bar U$ ve $\bar Y$ kümeleri bilinir.
- **Sonlu bellekli gözlemci (5.1):** $J\in[\Omega,K]$ seçilir. $x_{K+1}$ yalnızca son $J+1$ giriş ve ölçümden kestirilir; $X_0$'a hiç bağlı değildir.
  - Matris formu: $P\begin{bmatrix}x_{K+1}\\x_{K-J}\end{bmatrix}=Q\begin{bmatrix}\tilde u\\\tilde y\end{bmatrix}+R\begin{bmatrix}\tilde w\\\tilde v\end{bmatrix}+d$ (29), $P=\begin{bmatrix}I&-A^{J+1}\\0&-\tilde C\tilde A\end{bmatrix}$.
  - Gözlemlenebilirlik $\tilde C\tilde A$'nın tam sütun ranklı olmasını sağlar. Gauss eliminasyonu ile indirgenmiş satır eşelon forma geçilir ve (30) elde edilir. 1. blok satır $x_{K+1}$'i verir; 3. blok satır gürültüler üzerinde ek **tutarlılık kısıtlarıdır**. Bunlar CZ'nin kısıtı olarak eklenir.
  - Ölçümler tam bilinmek yerine bir hiperdikdörtgen hücre $U_\sigma\times Y_\sigma$ içinde biliniyorsa (31) kullanılır. Sonuç bir CZ'dir: $x_{K+1}\in\hat X^\sigma_{K+1|K}=\{G_1^\sigma,c_1^\sigma,[A^\sigma;G_2^\sigma],[b^\sigma;-c_2^\sigma]\}$ (32).
  - Bellek $J+1\ge\Omega+1$ olmalıdır. Bellek büyüdükçe gözlemci doğrulaşır, ama ilk tahmin ancak $k=J$'de hazır olur; o zamana kadar $u_k=0$ uygulanır.
- **Remark 2:** $X_0(i)$ bilinmiyorsa $0\le k\le\Omega$ boyunca $u=0$ uygulanır. Sonra $\hat X_{\Omega+1|\Omega}$ verilerden hesaplanır ve Algoritma 1 bununla başlatılır.
- **Açık yöntem (5.2):** $\bar U\times\bar Y$ hiperdikdörtgenlere bölünür. Her pencere-hücresi $\sigma\in S^{J+1}$ için gözlemci kümeleri ve optimal ayırıcı giriş **çevrimdışı** hesaplanır. Çevrimiçi: 3–5. adımlar aynen uygulanır; 7–8. adımlar yerine yalnızca hücre tabloda aranır.
  - Bedeli: gözlemci daha zayıftır, bu yüzden 9. adımda güncellemeler daha seyrek kabul edilir. Ayrıca $J$ ölçüm birikmeden sinyal başlayamaz. Model elemenin avantajını kullanmak için her hücre ve **her model alt kümesi** için ayrı girişler gerekir.

### Ana sonuçlar ve örnekler

| Örnek | Kurulum | Sonuç |
|---|---|---|
| **1** (s. 113, Şekil 1) | 3 model, 2 durum ($A(2)$: $a_{12}=0$, $A(3)$: $a_{21}=0$). $C=D_v=I$; $V=\{0.2I,0\}$. $W$ ve $X_0(i)$ tek eşitlik kısıtlı CZ'ler ((33)–(34)). $\lVert u_k\rVert_\infty\le3$. Zonotop yöntemi için kısıtlar atılıp dış zonotop kullanılmış. | **Z:** $N=7$, $\lVert u\rVert_2=9.4914$. **CZ:** $N=3$, $\lVert u\rVert_2=5.629$. Süre: CZ 0.01 s, Z 0.13 s. |
| **2** (s. 113–114, Şekil 2) | 10 durum; $B=0.5I$, $B_w=0.05I$, $C=D_v=I$. $A(2)$ ve $A(3)$, $A(1)$'den yalnızca birkaç elemanda farklı ("zor" ayrışma). | **Z:** $N=5$, $10.4596$. **CZ:** $N=4$, $10.3516$. Süre: 129 s'den **5.92 s**'ye. |
| **3** (s. 114, Şekil 3) | Kapalı çevrim, DC motor; 3 model (nominal; armatür direnci artışı; bobin kopması). Önceki zonotopik gözlemcili yöntem (Raimondo, Braatz, Scott 2013) ile CZ gözlemcili yöntem karşılaştırılmış. | Ortalama $N$ ve $\lVert u\rVert_2$: **Z** 6.7133 / 10.6961; **CZ** 5.6267 / 9.2031. |
| **4** (s. 114–115, Şekil 4) | 3 durum, 2 çıkış ($C=\begin{bmatrix}1&0&0\\0&1&0.2\end{bmatrix}$; **eksik durum ölçümü**); $\lVert u\rVert_\infty\le1$. Açık-çevrim, doğrudan ve açık kapalı-çevrim yöntemleri karşılaştırılmış. | Ortalama $\lVert u\rVert_2$ / $N$: **doğrudan CL** 1.7696 / 4.2533; **açık (explicit) CL** 2.5513 / 6.5067; **açık çevrim** 3.1098 / 8.2867. |

- **Örnek 1 notları:**
  - CZ daha hızlı çıkmış. Makalenin açıklaması: "sezgiye aykırı" bu sonuç CZ'nin çok daha kısa ufukla teşhis koymasından kaynaklanıyor; aynı ufukta zonotop daha hızlı olurdu.
  - İndirgeme: zonotopik $Z(i,j)$ → $(N+1)n_y$ üreteç; CZ $\mathscr Z(i,j)$ → 2 kısıt ve $(N+1)n_y+2$ üreteç.
  - Makalenin yorumu (s. 113): $X_0(i)$ çoğu zaman bir gözlemcinin çıktısıdır ve zonotop olmayabilir. $W$ da modellenmemiş doğrusal olmayan dinamiği sınırlamak için kullanıldığında çoğu zaman bir politoptur.
- **Örnek 2 notu:** Süredeki büyük düşüş, ufkun 5'ten 4'e inmesinden kaynaklanıyor.
- **Örnek 3 notları:**
  - $\Delta t=5$ ms; $u_c=6$ V, $|u_s|\le6$ V. $X_0(i)=\{\mathrm{diag}(0.3,3),(0.6,70)\}$, $V=\{\mathrm{diag}(0.3,3),0\}$; $W$ iki kısıtlı bir CZ.
  - $X_0(i)$ tasarım için **bilinmiyor**; gözlemciler $u_0=u_1=0$ iken $(y_0,y_1)$ ile başlatılıyor (Remark 2).
  - Ortalamanın kaç simülasyon üzerinden alındığını metinde bulamadım **[Yorum]**.
- **Örnek 4 notları:**
  - $X_0(i)$ bilinmiyor; tüm yöntemler $u_0=0$ uyguluyor ve $\hat X_{1|1}$, $(y_0,y_1)$'den hesaplanıyor.
  - Doğrudan yöntem hesaplama gecikmesi yüzünden $u_1=0$ da uygulamak zorunda; ilk sıfırdan farklı girişi $k=2$'de. Açık yöntemde hesap hızlı varsayıldığı için ilk sıfırdan farklı giriş $u_1$.
  - Açık yöntem için ızgara $(y_0,y_1,u_0)$ uzayında (6-B): giriş $[-1,1]$ aralığı 4 alt aralığa, çıkış $[-1.5,1.5]$ aralığı 6 alt aralığa bölünmüş. Toplam $6^4\cdot4^2=20\,736$ hücre.
  - Önceden hesaplama: 3 modeli ayırma ve her model çiftini ayırma için toplam **7.6 saat** (tek çekirdek). Bir hücrede 3 modeli ayıran girişin hesabı ortalama 0.97 s.
  - Makalenin özeti: açık yöntem açık çevrimden iyi; doğrudan yöntem, $u_{k+1}$'i $y_{k+1}$'i bilmeden hesaplamasına rağmen en iyisi.

### Varsayımlar ve sınırlamalar

1. Test aralığı boyunca **tek bir model aktiftir**; Scott'taki ufuk-içi geçiş senaryoları kullanılmamıştır. Belirsizlikler sınırlı konveks politoplardır ve doğrusal model yapısı Scott'la aynıdır.
2. Garanti, **açık-çevrim olurluluğuna** dayanır. Algoritma 1, 1. adımda $\bar N<\infty$ olmasını ister. Kapalı çevrim ortalama performansı iyileştirir, ancak açık çevrimin hiç ayıramadığı bir durumda garanti üretmez (Teorem 5'in hipotezi).
3. Gözlemciler indirgeme yüzünden muhafazakârdır. Bu yüzden yeni plan eskisinden kötü olabilir ve Adım 9'daki yedekleme mekanizması zorunludur.
4. Doğrudan yöntem her adımda bir MIQP çözer. Makale bunun bir örnekleme süresinden kısa olmasının "olası değil" olduğunu söyler (Remark 1); giriş bir adım önceden hesaplanır.
5. Açık yöntemde boyutların laneti vardır: $|S|^{J+1}$ hücre gerekir (Örnek 4'te 20 736 hücre, 7.6 saat). Sonlu bellekli gözlemci daha zayıftır. İlk $J$ adımda sinyal sıfırdır. Gözlemlenebilirlik (Varsayım 1) ve $\bar U$, $\bar Y$ sınırları gerekir.
6. Amaç fonksiyonunda toplam $\ell=1$'den başlıyor; bu bir dizgi hatası olabilir **[Yorum]**.

### Taylor TAC 2025 ile karşılaştırma

| Boyut | Raimondo 2016 | Taylor 2025 **[Taylor özeti]** |
|---|---|---|
| Model | Dinamik, tek model aktif | Statik |
| Belirsizlik kümesi | **Herhangi bir politop** (CZ) | Norm topları ve $x$ üzerinde karesel kısıtlar |
| Ölçümle güncelleme | Var: kesişim CZ'de tam | Yok (tek atış) |
| Çevrim | **Kapalı** (kayan ufuk) ve açık yasa | Açık, tek atış |
| Hesaplama | Her adımda MIQP ya da çevrimdışı tablo | Tek bir bilineer SDP |
| Garanti | Açık-çevrim olurluluğundan miras (Teorem 5) | Tek atışta, gevşetmenin sertifikasından |

- **$N(i,j)$'nin rolü, Raimondo'da [Yorum].** $N(i,j)$ Scott'takiyle aynıdır. Makale $N\ne0$ koşulunu "çıkış kontrol edilebilirlik matrisleri özdeş değil" diye ifade eder (s. 110); "sinyal bulutları farklı kaydırmalı" sezgisinin dinamik karşılığı budur. Kapalı çevrimde ise $K$ anında geçerli olan, **kalan ufkun** matrisi $N_{N-K-1}(i,j)$'dir: kalan girişlerin kalan çıkışlar üzerindeki kaldıracı. Ufkun sonuna yaklaştıkça bu kaldıraç küçülür, ölçümler ise çarpışma kümesini küçültür. Kapalı çevrimin kazancı, bilgi kazancının kaldıraç kaybını geçmesinden gelir.
- **Kapalı çevrim, açık çevrim ayıramazken yardımcı olur mu? [Yorum: kendi argümanım]** İki durumu ayırmak gerekir:
  1. *Yapısal olarak ayrılamaz:* tüm ufuk için $N(i,j)=0$ ve sıfır girişte bulutlar çakışık. Bu durumda **hiçbir nedensel geri besleme yardımcı olmaz**. Gerekçe: $\tilde y=\tilde C\tilde B\,\tilde u(\tilde y)+e$ yazılsın; $e$ belirsizlik kısmıdır ve iki modelde de aynı $\tilde C\tilde B$ kullanılır. Ortak bölgeden bir $e\in\tilde\Psi(0,i)\cap\tilde\Psi(0,j)$ seçilirse, $\tilde u$ kesin nedensel olduğu için bu $e$'den adım adım bir $\tilde y$ kurulur ve bu $\tilde y$ iki modelle de tutarlıdır.
  2. *Kaynak yetersizliği:* $N\ne0$ ama giriş sınırları ya da ufuk açık çevrimin ayırmasına izin vermiyor. Burada gerçek bir geri besleme politikası prensipte açık çevrimden daha güçlü olabilir. Örneğin $y_0$'ın değerine göre sinyal yukarı ya da aşağı itilebilir; açık çevrim tek yönü bütün $y_0$'lar için seçmek zorundadır. Ancak Raimondo'nun algoritması bunu **sertifikalayamaz**: her güncelleme yine "kalan ufukta açık çevrim"dir (açık-çevrim-geri beslemeli, MPC tarzı) ve başlangıçta $\bar N<\infty$ ister. En kötü durum garantisi için min-max (dinamik programlama) bir tasarım gerekir. Bu açık bir araştırma sorusu.
- **Taylor'ın statik modelinde kapalı çevrim [Yorum].** Tek bir anlık görüntüde (snapshot) kapalı çevrim anlamsızdır. Ama birden fazla ölçüm periyodu varsa ve bazı belirsizlikler **kalıcıysa** (aynı $\lambda$ bileşeni periyotlar boyunca sabitse), ilk ölçüm $\lambda$ kümesini daraltır ve ikinci sinyal daha küçük olabilir.
  - Elipsoid/top belirsizlikte "top ∩ afin altuzay" yine bir toptur (daha düşük boyutlu). Fakat ölçüm gürültüsü de bir topta ise iki elipsoidin kesişimi elipsoid değildir ve dış yaklaşım gerekir.
  - CZ'de bu güncelleme tamdır.
- **CZ'ler Taylor'ın örtük modelini kısmen ifade edebilir [Yorum].** $\{x\in\text{kutu}:X_kx=h_k-\Theta_k\theta+H_k\lambda,\ \|\lambda\|_\infty\le1\}$ eşitlik kısıtlı bir CZ'dir. Dolayısıyla $\infty$-norm ve sınırlı $x$ altında Taylor'ın $X_k\ne I$ durumu Teorem 1 ve Sonuç 2 ile **kesin** ele alınabilir. Karesel kısıtlar ise yine ifade edilemez.

### Projeyle bağlantı ve araştırma fikirleri

Bu bölümdeki her şey **[Yorum]**dur.

**Fikir F (bu makale için en umut verici): iki adımlı (sıralı) yoklama ile mesafe koruması.**

1. *Periyot 1:* Küçük bir yoklama sinyali $\theta_1$ uygulanır ve ölçülür. Tutarsız hipotezler elenir ve kalıcı belirsizliklerin kümesi daraltılır (ör. $R_f$ aralığı, kaynak empedansı).
2. *Periyot 2:* Kalan hipotezler ve daralmış bulutlar için $\theta_2$, Scott veya Taylor yöntemiyle yeniden tasarlanır.
3. *Garanti için:* Algoritma 1'deki gibi, baştan tasarlanmış iki periyotluk açık-çevrim plan yedekte tutulur. Böylece toplam süre hiçbir zaman açık-çevrim planından uzun olmaz (Teorem 5'in analoğu).
4. *Önkoşullar:* (i) Belirsizliğin önemli bir kısmı periyotlar arasında kalıcı olmalı. Her periyot bağımsız gürültüyse ölçüm yalnızca hipotez eleme sağlar. (ii) İnverter enjeksiyonu periyot ölçeğinde değiştirebilmeli. (iii) Hesaplama süresi koruma gecikme bütçesine sığmalı. Bu nedenle 2-B sinyal ve az sayıda hipotez için önceden hesaplanmış bir tablo (açık yöntem) doğal bir adaydır.
5. *Ne öğreniriz?* Pasif tespitten sonra devreye giren aktif teşhis mimarisi ("arıza tespit edildi ama teşhis edilemedi", s. 108) koruma rölesindeki "start/pickup → bölge kararı" akışına birebir oturuyor.

**Fikir G: açık çevrimin başarısız olduğu durumları sınıflandırmak.** Önce $N_q$ hesaplanır.

- "Yapısal olarak ayrılamaz" çiftler ($N=0$ ve $0\in Z$) için kapalı çevrimle uğraşmak boşunadır. Bu çiftler için ya ölçüm seti değiştirilmeli (yeni sensör ya da kanal), ya sinyalin modelleri farklı etkilediği yeni bir fiziksel kanal bulunmalı (Taylor dilinde farklı $\Theta_k$), ya da sınıf tanımı değiştirilmeli (ölü bant).
- "Kaynak sınırlı" çiftler için kapalı çevrim ve çok periyotlu tasarım denenmelidir.

**Fikir H: rölede bakma tablosu.** Raimondo'nun açık yöntemi, koruma rölesi yazılımına uygun bir yapı sunuyor: çevrimiçi optimizasyon yok, yalnızca hücre arama var. 2-B sinyal ve birkaç ölçüm kanalı için hücre sayısı yönetilebilir olabilir. Öncelikle ölçüm uzayının boyutu ve hücre çözünürlüğü kestirilmelidir; Örnek 4'te 6 boyut ve 20 736 hücre 7.6 saat sürmüştür.

**Fikir I: CZ ile fiziksel kısıtlar.** $R_f\ge0$, parametreler arası doğrusal ilişkiler ya da ölçüm kanalları arasında bağlı hata bütçeleri gibi politop bilgiler CZ ile **tam** temsil edilebilir. Örnek 1'deki etki dikkat çekicidir: yalnızca kümeleri daha doğru temsil etmek ufku 7'den 3'e, normu 9.49'dan 5.63'e indirdi. Kutu yaklaşımının sinyal boyutunu ne kadar şişirdiği proje modelinde ölçülmeye değer.

---

## Sentez

**1. Ortak çekirdek: üç makale aynı geometriyi kullanıyor.**

- Her hipotezin ölçüm "bulutu" vardır. Sinyal bulutları **yalnızca öteler**; şekilleri belirsizlik kümelerinden gelir ve sinyalden bağımsızdır.
- Ayrışmanın tek ölçütü göreli kaymadır: Scott ve Raimondo'da $N(i,j)\tilde u$, Taylor'da $X=I$ iken $(\Theta_i-\Theta_j)\theta$ **[Yorum]**. Bu göreli kayma, iki bulut şeklinin Minkowski toplamı olan "çarpışma kümesinin" dışına çıkmalıdır.
- $N=0$ ise sinyal işe yaramaz (Scott s. 1583). $N\ne0$ ise yeterince büyük sinyal her zaman ayırır (Raimondo s. 110), giriş kısıtları hariç.
- Ayırıcı sinyal kümesi bir konveks kümenin tümleyenidir. Bu yüzden kesin tasarım ya kombinatoryaldir (Scott ve Raimondo: MIQP) ya da bilineerdir (Taylor: çarpan × sinyal) **[Yorum]**.
- Scott'un LP dual değişkeni $\lambda$, Taylor'ın Farkas sertifikasıyla aynı rolü oynar: iki bulutu ayıran hiperdüzlemin normali **[Yorum]**.

**2. Küme sınıfı her şeyi belirliyor.**

| Küme sınıfı | Doğrusal dönüşüm | Minkowski toplamı | Kesişim (ölçüm güncellemesi) | Tasarım problemi |
|---|---|---|---|---|
| Zonotop (Scott) | Tam | Tam | Tam değil | MIQP, kesin |
| Kısıtlı zonotop (Raimondo) | Tam | Tam | **Tam** | MIQP, kesin; her politop |
| Elipsoid / norm topu (Taylor) | Tam | Tam değil **[Yorum]** | Tam değil (genelde) **[Yorum]** | SDP gevşetmesi, bilineer **[Taylor özeti]** |

Sonuç: politop belirsizlik kabul edilebiliyorsa zonotop veya CZ yöntemi **gevşetmesiz** global optimum verir (ε eşiği ve indirgeme muhafazakârlığı dışında). 2-norm ve karesel kısıtlar gerekiyorsa Taylor'ın yolu daha ifade gücü yüksek ama gevşetmelidir. İkisi birbirini **doğrulamak** için birlikte kullanılabilir **[Yorum]**.

**3. Zamanın rolü [Yorum].**

- Dinamik problem, yığınlama sonrasında statiktir. Ufuk uzadıkça iki şey olur: (a) yeni Markov parametreleri $N$'ye girer ve sinyalin kaldıracı artar (Scott Örnek 1'de $N=1$'de bazı çiftler için $N=0$, $N=2$'de hepsi $\neq0$); (b) çıkış boyutu artar, ama bulutlar da büyür.
- Kapalı çevrim bulutları ölçümle daraltır. Ortalama performansı iyileştirir (Raimondo Örnek 4: açık çevrim 8.29 adım / 3.11 norm; doğrudan kapalı çevrim 4.25 adım / 1.77 norm). Fakat yapısal ayrılamazlığı çözmez ve Raimondo'nun yöntemi açık-çevrim olurluluğu olmadan garanti üretmez.

**4. Projeye somut yol haritası [Yorum].**

1. **$N$ haritası (Fikir B).** Mesafe koruması hipotezlerinin (bölge içi/dışı, konum ve direnç alt aralıkları) her çifti için $N_q$ ve "$0\in Z_q$?" hesaplanır. Çiftler pasif, aktif ve asla ayrılamaz olarak sınıflandırılır. Bu, sinyal tasarımına girmeden "hangi bilgi hiç taşınamıyor"u gösterir.
2. **EN UMUT VERİCİ FİKİR: 2-B kesin çözücü (Fikir A).**
   - Kutu veya politop belirsizlikli bir proje modelinde, $K_q$ çokgenleri ve aday nokta taraması ya da Scott'un MILP/MIQP'si ile **kesin** en küçük sinyal bulunur.
   - Aynı problem için Taylor'ın bilineer SDP'si ve $(1-\zeta)/\chi$ sınırı hesaplanır. Böylece gevşetme açığı ve sınırın sıkılığı sayısal olarak ölçülür.
   - Elipsoidal belirsizlikte iç ve dış zonotop sandviçi ya da 1-B açı taraması kullanılır.
   - Neden en umut verici: küçük boyutlu (öğrencinin uygulayabileceği), kesin cevap üretiyor (referans ve "ground truth"), doğrudan Taylor çizgisinin açık sorusuna, gevşetme ne kadar iyi sorusuna, değiyor ve sinyal yönünü görselleştirerek sezgi kazandırıyor.
3. **Sınıflar arası ayrışma (Fikir C).** Yalnızca "aç" ile "açma" hipotezleri arasındaki çiftler kısıtlanır. Sinyalin ne kadar küçüldüğü ölçülür.
4. **İki periyotlu yoklama (Fikir F).** Kalıcı belirsizlik varsayımı altında $\theta_1\to$ ölçüm $\to\theta_2$ tasarlanır, açık-çevrim plan yedekte tutulur. Kazanç, tek atışlık sinyalle ortalama ve en kötü durum normu üzerinden karşılaştırılır.

**5. Açık sorular [Yorum].**

- Taylor'ın SDP gevşetmesi, kutu belirsizliğe uyarlandığında Scott'un kesin MIQP sonucuyla ne zaman çakışır?
- Tek çift için $\min_\lambda h_Z(\lambda)/\|N^\top\lambda\|$ formülü Taylor'ın $(1-\zeta)/\chi$'sıyla aynı mı, yoksa onun bir gevşetmesi mi?
- Girişle çarpılan belirsiz parametreler (bulut şeklinin sinyalle değişmesi) durumunda "yalnızca öteleme" yapısı bozulur. Bu durumda hangi parçalama veya yaklaşım en az muhafazakârdır?
- Gerçek geri besleme politikaları (min-max) açık-çevrim olursuzken garanti verebilir mi ve bunun hesap maliyeti ne olur?
