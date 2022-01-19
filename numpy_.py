#numpy dizilerle çalışmak için kullanılan bir python kütüphanesidir
#pip install numpy ile kurulur
#lineer cebir, matrisler, fourier dönüşümü gibi alanlarda çalışak için hazır br çok methoda sahiptir
#ndarray adı veriler python dizilerine göre 50 kat daha hızlı bir dizi sistemi vardır

#numpy en son cpu mimarileriyle çalışmaya meyillidir
#normal listelerin aksine numpy memoryde tek bir sürekli alanda ndarray'leri tutarak çok daha hızlı işlem yapar
#buna ***referans yerelliği*** denir (locality of reference)
#numpy python ile yazılmıştır ancak hızlı hesaplama gerektiren parçaların çocu c ve c++ ile yazılmıştır

import numpy as np #numpy import etme

arr = np.array([1,2,3,4,5]) #numpy ile ndarray nesnesi oluşturma

arr2 = np.array(42) # [42], 0 boyutlu bir ndarray nesnesi

arr3 = np.array([1,2,3,4,5]) #1 boyutlu bir ndarray

arr4 = np.array([[1,2], [5,6]]) #1 boyutlu elemanlara sahip 2 boyutlu ndarray

arr5 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [0,0,0]]]) #2 boyutlu elemanlara sahip 3 boyutlu bir ndarray

arr5.ndim # arr5 nesnesinin boyut sayısı

arr[0] + arr[3] #arr nesnesinin 0 ve 3 indexlerinin toplamı

arr5[1,0] #arr5 nesnesinin 1.boyutunun 0. elemanı

arr5[0,1,2] #arr5 nesnesinin 0.boyutunun 1. elemanının 2.elemanı

# arr4[0, -1] #ilk boyutun son elemanı

dilimleme = np.array([1,2,3,4,5,6,7])

#dilimleme [start: end: step] seklinde yapilir
#start verilmezse 0dır
#end belirtilmezse dizi lengthidir
#step belirtilmezse 1'dir
dilimleme[1:6:2] # [2,4,6]

arr5[1, 0:1] #2d dilimleme

arr5.dtype # verinin tipini yazdırır

#numpy veri tipleri

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type (void)

###  NUMPY COPY VE VIEW
#numpyda listeler kopyalanabilir
#copy ile kopyalandığında listenin o hali alınır sonra yapılan değişiklikler kopyaya aktarılmaz

copyarr = arr5.copy()

#view ile kopyalamada ise o listenin bir görünümü elde edilir

viewarr = arr5.view() #listedeki değişiklikler bu değişkeni de değiştirir

#SHAPE OZELLIGI

arr5.shape() #her boyuttaki eleman sayısını gösterir 

# örn : [1,3,2] 1.boyutta 1, 2.boyutta 3 3.boyutta 2  gibi.

#RESHAPE METHODU

liste__ = np.array([1,2,3,4,5,6])

liste__.reshape(2,3) # listeyi tekrardan boyutlandırır [[[1,2], [3,4], [5,6]]] çıktısını verir

#numpyda bilinmeyen boyut
#reshape içinde 2 boyutu yazınca 3.boyut yerine -1 yazarsak numpy bunu bizim için hesaplar

bilinmeyen = np.array([1,2,3,4,5,6,7,8])

newarr = bilinmeyen.reshape(2,2,-1)

#numpy dizileri iterable'dir

for i in bilinmeyen:
    print(i)

#multidimensional arraylarde iç içe for ile iterate edilebilir

for i in arr5:
    for j in i:
        for x in j:
            print(x)

#bunun yerine nditer methodu kullanabiliriz

for x in np.nditer(arr5):
    print(x)

#numpyde diziler belirtilen eksen boyunca birleştirilebilir eksen belirtilmezse 0'dır

liste111 = [1,2,3]
liste222 = [4,5,6]

birlesik = np.concatenate((liste111, liste222))  # [1,2,3,4,5,6]

#concatenate tam tersi oalrak array_split kullanılır

liste333 = np.array([1,2,3,4,5,6])

bolunmus = np.array_split(liste333,2) # [array([1,2,3]), array([4,5,6])]

#numpy ile dizide bir değer ve ya işlem aranabilir

tekSayilar = np.where(liste333%2 == 1)

#FİLTRELEME
#bir boolean true false listesi ndarray içine atılırsa sonuç olarak sadece true değerlere karşılık gelen elemanların olduğu bir liste döner

liste444 = np.array([1,2,3,4,5,6])

filter_list = []

for element in liste444:
    if element%2 == 1: 
        filter_list.append(True) 
    else:
        filter_list.append(False)

filtered_list = liste444[filter_list]

#burada filter_list = [True, False, True, False, True, False] olur
#filtered_list = [1,3,5] olur

filter_list > liste444 < 3 #bu kullanım ile hızlıca filter list oluşturulabilir 

## NUMPY İLE RASTGELE LİSTELER OLUŞTURMAK İÇİN NUMPY'IN KENDİ RANDOM MODÜLÜ KULANILIR

from numpy import random

x = random.randint(100) #0-100 arası int değer
y = random.rand(100) #0-100 arası float değer

randlist = random.randint(100, size=(5)) #0-100 arası 5 elementli rastgele dizi oluşturur

randnum = random.choice([1,2,3,4,5]) #bu listeden bir sayı çeker 

#shuffle() methodu elemanları rastgele karıştırır
#permutation() methodu elemanlarının rastgele bir permütasyonunu döndürür ancak listeyi değiştirmez