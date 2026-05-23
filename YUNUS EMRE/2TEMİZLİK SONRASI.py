import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split #test ve train ayrımı için gerekli
from sklearn.impute import KNNImputer

#TEMİZ VERİ SETİ İLE DEVAM EDİLİR

df = pd.read_csv('brfss2024_temiz.csv')
#GERİYE KALAN İŞLEMLER
#1) Train/test split
#2) KNN imputasyonu. gereksiz değerleri NaN yapmıştık. Şimdi o değerleri elimizdeki verilere dayanarak ortalama bir şekilde dolduracağız.(KNN imputation)
#3) Ölçeklendirme: Veriler arasında orantısızlık varsa model yanlı olur. Bunu engellemek için ölçekleme yaparız.


BAGIMSIZ = [
    'CHCSCNC1', 'CHECKUP1', '_AGEG5YR', 'SMOKE100',
    'DIABETE4', 'EXERANY2', 'ASTHMA3', 'CHCKDNY2',
    'HAVARTH4', 'CVDINFR4', 'PERSDOC3', '_RFHLTH',
    'INCOME3', 'EDUCA', '_BMI5CAT',
]
#şuan ağırlıklarla yani hipotez fonksiyonundaki X'in önündeki teta'lar ile işimiz yok. Sadece veriyi ikiye böleceğiz o kadar.
X = df[BAGIMSIZ] #bağımsız değişkenler = X
y = df['CHCOCNC1'] #Hedef değişken = y = tahmin edilmeye çalışılan sonuç. "Bu kişi kanser midir?" Sorusuna yanıt verecek!!!!

X_train, X_test, y_train, y_test = train_test_split( #Burada ikisi de train ve test olarak ayrıldı.
    X, y,
    test_size=0.20, # %20 test %80 eğitim verisi olarak ayarlandı.
    random_state=42,
    stratify=y
)

print(f"Eğitim seti: {len(X_train):,} satır")
print(f"Test seti  : {len(X_test):,} satır")
print(f"Eğitimde kanser oranı: %{y_train.mean()*100:.1f}")
print(f"Testte kanser oranı  : %{y_test.mean()*100:.1f}")
# Ayırma işlemi burada biter.

#Şimdi sira NaN'ları doldurmak için KNN imputasyonunda.
#!!YUNUS EMRE'YE NOT: KNN benim bilgisayarımda çok uzun sürdüğü için devamını getirmedim. Yani aşağıdan sonrasını yapamadım malesef. Burdan sornasına bakabilirsin!!
#!!YUNUS EMRE'YE NOT: Burdan sonra kalan tek şey KNN imputation kullanarak NaN'ları doldurmak, Farklı boyutta veri varsa modelin yanlı olmasını engellemek için veri ölçekleme yapmak!!
imputer = KNNImputer(n_neighbors=5)

# Sadece eğitim verisine fit edilecek.
X_train = pd.DataFrame(
    imputer.fit_transform(X_train),
    columns=BAGIMSIZ
)

# Test verisine sadece transform uygulanacak.
X_test = pd.DataFrame(
    imputer.transform(X_test),
    columns=BAGIMSIZ
)

print("KNN tamamlandı.")
print(f"Train'de kalan NaN: {X_train.isna().sum().sum()}")
print(f"Test'te kalan NaN : {X_test.isna().sum().sum()}") 