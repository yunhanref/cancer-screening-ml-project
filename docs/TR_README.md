<div align="center">
  <img width="2197" height="704" alt="CBU KOU HITU" src="https://github.com/user-attachments/assets/79f15f90-16a5-49cf-bae5-0252bfb0d502" />
</div>

  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=26&pause=1000&color=007ACC&center=true&vCenter=true&width=800&lines=Cancer+Screening+ML+Project;Erken+Teşhis+İçin+Makine+Öğrenmesi;MCBÜ+%7C+KOÜ+%7C+HİTÜ" alt="Proje Başlığı Animasyonu" />
  
  <p><b>Kocaeli Üniversitesi, Manisa Celal Bayar Üniversitesi ve Hitit Üniversitesi öğrencileri işbirliği ile geliştirilmiştir.</b></p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Machine_Learning-FF9900?style=for-the-badge" alt="Machine Learning" />
  <img src="https://img.shields.io/badge/CDC_BRFSS_Data-007ACC?style=for-the-badge" alt="Data" />
  <img src="https://img.shields.io/badge/Academic_Research-4CAF50?style=for-the-badge" alt="Academic Research" />
</p>

---
## Proje Hakkında

Bu proje, kanser taraması, risk faktörlerinin tespiti ve erken teşhis süreçlerini optimize etmek amacıyla geliştirilmiş bir makine öğrenmesi araştırmasıdır. Hastaların demografik bilgileri, yaşam tarzı alışkanlıkları ve genel sağlık durumlarına ilişkin veriler analiz edilerek, bireylerin kanser riski taşıyıp taşımadığı veya kanser tarama programlarına uyum gösterip göstermeyeceği tahmin edilmektedir.

Üç farklı üniversitenin bilgi birikimi ve işbirliği ile disiplinlerarası bir akademik çalışma olarak hayata geçirilen bu proje, koruyucu hekimlik politikaları için veri odaklı bir karar destek mekanizması sunmayı hedeflemektedir.

---
## 👤 Rolüm ve Katkılarım

Çoklu üniversite işbirliğine dayanan bu projede, Proje Grup Lideri ve Makine Öğrenmesi Geliştiricisi olarak görev aldım. Temel odak noktam proje altyapısını kurmak, temel verileri hazırlamak ve ana tahmine dayalı sınıflandırma modellerini geliştirmekti.

Kanser Tarama ML Projesine yaptığım spesifik teknik katkılar şunlardır:

**Proje Liderliği:**
* Tüm ekip için versiyon kontrol iş akışını ve branch (dal) politikalarını belirleyerek GitHub repository mimarisini tasarladım.
* Manisa Celal Bayar, Kocaeli ve Hitit Üniversitelerindeki öğrenci takım arkadaşları arasında görev dağılımını ve kod incelemelerini (code review) koordine ettim.

**Veri Ön İşleme ve Öznitelik Mühendisliği (Feature Engineering):**
* İstatistiksel uygunluğa dayanarak kritik klinik değişkenleri izole etmek amacıyla, özellik seçimi (feature selection) için keşifsel Codebook analizi yürüttüm.
* Eksik verileri gidermek, aykırı değerleri (outliers) ele almak ve ham veri setini modelin işleyebileceği formata getirmek için veri temizleme pipeline'larını yürüttüm.
* Tarafsız bir değerlendirme sağlamak adına katmanlı (stratified) train/test veri ayrımını uyguladım ve kendi iş akışımı veri mühendisliği ekibinin pipeline'ı ile entegre ettim.

**Makine Öğrenmesi Modeli Geliştirme (Lojistik Regresyon):**
* Bu çalışmada değerlendirilen üç temel tahmin modelinden biri olan Lojistik Regresyon sınıflandırıcısını geliştirdim ve modelin ince ayarlarını (fine-tuning) yaptım.
* Modeli klinik tespit senaryoları için optimize edecek şekilde hiperparametreleri ve eşik (threshold) değerlerini yapılandırdım.
## Veri Seti: 2024 BRFSS (SAS Transport Format)

Çalışmamızda **CDC (Centers for Disease Control and Prevention)** tarafından yayınlanan [2024 BRFSS (Behavioral Risk Factor Surveillance System](https://www.cdc.gov/brfss/index.html) veri seti kullanılmıştır. 

* **İçerik:** 7. grubun konusu olan kanser araştırmaya göre başından sonuna kadar temizlenmiş veri setinde genel olarak pek çok kanser türleri, sigara/alkol tüketimi, fiziksel aktivite, kronik hastalık geçmişi ve sosyodemografik anket cevapları bulunmaktadır.
* **Veri Boyutu:** Hem işlenmiş hem de orjinal veri setleri oldukça büyük hacimli olduğundan GitHub reposunda değil, grubumuzun drive adresinde barındırılmaktadır (Bkz. *data/drive.txt*).

---

## Metodoloji

Tabular anket verilerinden anlamlı sonuçlar üretebilmek için aşağıdaki veri bilimi boru hattı (pipeline) izlenmiştir:

1.  **Veri Hazırlığı:**  CDC BRFSS 2024 veri setinin [Codebook'u](https://www.cdc.gov/brfss/annual_data/2024/zip/codebook24_llcp-v2-508.zip), veri mimarlarınca detaylıca incelenmiş olup, proje konusu kapsamında ana ve bağımsız değişkenler üzerinde tartışılmıştır.
<div align="center">
  <img width="885" height="488" alt="CHCOCNC1" src="https://github.com/user-attachments/assets/37263639-0a21-426e-8a13-092f0d1d697a" />
  <p><small>resim 1.0 - Ana Değişken CHCOCNC1</small></p>
  <img width="885" height="489" alt="SMOKE100" src="https://github.com/user-attachments/assets/5b574605-cd30-45c4-aadc-d14a90f1b7a6" />
  <p><small>resim 2.0 - Yan Değişken Örn. SMOKE100</small></p>
</div> 

2. **Veri Ön İşleme (Data Preprocessing):**
   * **Ana değişkenin belirlenmesi:** Konumuz olan kanser taramaya yönelik değişken seçimimiz için veri setinde geniş kitleye hitap eden ve potansiyel yan değişken verilerinin en çok korelasyon gösterebileceği verinin "CHCOCNC1" olduğuna kanaat getirdik.
   * **Özellik Mühendisliği (Feature Engineering):** Genel kanser teşhisi ile en çok korelasyon gösteren demografik ve davranışsal özelliklerin (Örn: `_AGEG5YR`, `SMOKE100`, `CHCSCNCR`) seçilmesi.
   * **Seçilen Ana ve Bağımlı Değişkenler:**
   ```
   Ana Değişkenler:
   CHCOCNC1: Melanom veya herhangi bir kanser teşhisi konuldu mu? (30 kategori)

   Bağımsız Değişkenler:
   CHCSCNC1: Cilt kanseri veya melanom teşhisi konuldu mu?
   CHECKUP1: Rutin kontrolünüz için en son ne zaman doktora gittiniz?
   _AGEG5YR: Kaç yaşınızdasınız? (14 kategori)
   SMOKE100: Hayatınız boyunca en az 100 sigara içtniz mi?
   DIABETE4: Daha önce diyabet teşhisi konuldu mu?
   EXERANY2: Geçtiğimiz ay boyunca, işiniz hariç, fiziksel aktivite veya egzersiz yaptınız mı?
   ASTHMA3:  Daha önce astım teşhisi konuldu mu?
   CHCKDNY2: Size hiç Böbrek taşı, mesane enfeksiyonu veya idrar kaçırmak hariç böbrek hastalığı teşhisi konuldu mu?
   HAVARTH4: Size hiç artrit, romatoid artrit, gut, lupus veya fibromiyalji gibi bir rahatsızlığınız olduğu söylendi mi?
   CVDINFR4: Daha önce kalp krizi (miyokard enfarktüsü) geçirdiniz mi?
   PERSDOC3: Bir veya bir grup doktorun kişisel sağlık sağlayıcınız olduğunu düşünüyor musunuz?
   _RFHLTH:  Sağlık durum sorusu
   INCOME3:  Tüm gelir kaynaklarınızdan gelen yllık geliriniz ne kadar? (11 kategori)
   EDUCA:    Tamamladığınız en yüksek eğitim durumunuz nedir?
   _BMI5CAT: Vücut Kitle Endeksiniz nedir? (4 categories of BMI)
   ```
   
3. **Veri Okuma ve Dönüştürme:**
   * `.xpt` formatındaki verilerin Python ortamına aktarılması ve Pandas DataFrame formatına dönüştürülmesi.
   * BRFSS özelindeki "Bilmiyorum/Reddedildi" (bkz. resim 1.0 7, 9. değerler) yanıtlarının eksik veri (NaN) olarak ele alınması.
   * İkili yanıtlara sahip değişken değerlerinin, öğrenme performansı açısından 1 ve 0'lar şeklinde yeniden değiştirilmesi.
   * Hedef değişkenin (kanser tanısı / tarama durumu) belirlenmesi ve sınıf dengesizliklerinin (Cost-Sensitive Learning, ) giderilmesi.
4. **Modelleme:** Tabular verilerde yüksek performans gösteren Lojistik Regresyon, Bayesyen Yaklaşım ve Yapay Sinir Ağları kullanılarak oluşturulan modellerin eğitilmesi:
5. **Değerlendirme (Evaluation):** Modeller; Doğruluk (Accuracy), Hassasiyet (Precision), Duyarlılık (Recall), F1-Skoru ve ROC-AUC metrikleri ile istatistiksel olarak ölçülmüş ve birbirleriyle kıyaslanmıştır.
---

## Mimari
```
cancer-screening-ml-project/
│
├── data/               # CDC BRFSS ham ve düzenlenmiş (.csv) veri setleri
├── notebooks/          # Veri Analiz Bulguları (EDA) ve prototip modelleme Jupyter Notebook'ları
├── src/                # Model pipeline, veri ön işleme, eğitim ve tahmin Python betikleri
├── docs/               # Araştırma raporu, proje yönergeleri, CDC Codebook
├── variables_codebook/ # Veri mimarlarınca Codebook'dan ekran görüntüsü alınmış anket verileri
├── .gitignore          # Git takibinden dışlanacak gereksiz ve büyük dosyalar
├── .gitkeep            # Boş klasör yapılarının korunması için komut
├── README.md           # Proje tanıtımı
├── requirements.txt    # Python betikleri için gerekli kütüphanele
└── extras              # Proje hakkında ekstra bilgilendirmeler
```
---
## Kurulum ve Kullanım
1. **Repoyu Klonlayın ve Kütüphaneleri Yükleyin:**
  ```
  git clone [https://github.com/KULLANICI_ADI/cancer-screening-ml-project.git](https://github.com/KULLANICI_ADI/cancer-screening-ml-project.git)
  cd cancer-screening-ml-project
  pip install -r requirements.txt
  ```
2. **Veri Setini Ekleyin:**
  Dosya boyutu kısıtlamaları nedeniyle veri seti GitHub'da yoktur. data/drive.txt içindeki bağlantıdan X_train, X_test, y_train ve y_test dosyalarını indirip data/ klasörüne koyun.
  
3. **Modelleri Çalıştırın:**
  Modelleri baştan eğitmek için src/ klasöründeki betikleri kullanabilirsiniz:
  ```
  python src/logistic_regression.py
  python src/naive_bayes.py
  python src/ann_model_training.py
  (Not: Hazır sonuçları ve grafikleri görmek için notebooks/ klasöründeki Jupyter dosyalarını inceleyebilirsiniz.)
  ```


<div align="center">
  <img width="480" height="320" alt="Flag_of_Turkey svg" src="https://github.com/user-attachments/assets/3eabddf6-0791-4fdf-a1a2-1241124a0aa3" />
</div>  
