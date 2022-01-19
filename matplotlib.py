#matplotlib python için geliştirilmiş grafik çizme paketidir
#çoğu matplotlib aracı pyplot alt modülünde bulunur

import matplotlib.pyplot as plt #pyplot alt modülünü plt kısa adı ile import eder
import numpy as np

xpoints = np.array([1,8]) #x eksenine 1-8 arası sayılar yazar
ypoints = np.array([3,10]) #y eksenine 3-10 arası sayılar yazar

plt.plot(xpoints,ypoints) #.plot fonksiyonu eksenleri parametre alır ve bu parametrelere göre grafiği çizer

plt.show() #grafiği bir pencerede görüntüler

#PLOTTING - ÇİZİM YAPMA

#varsayılan olarak plot() fonksiyonu bir noktadan başka bir noktaya çizgi çizer
#plot düzlemi aslında koordinat eksenleridir
#ilk parametre x ekseni üzerindeki noktaları içeren bir dizidir
#ikinci parametre y ekseni üzerindeki noktaları içeren bir dizidir
# **** üstteki fonksiyonda x ekseninde 1'e y eksenindeki 3 karşılık gelir, x eksenindeki 8'e ise y ekseninde 10 gelir.
#bu değerlere göre diğer sayıları da yazarak grafiği çizer

#TÜM PLOT PARAMETRELERİ AŞAĞIDA LİSTELİ

plt.plot(xpoints,ypoints, "o") #çizgi yerine, eşleşen (1,3) ve (8,10) noktalarına nokta koyarak gösterir

xpoints = np.array([1,3,5,7])
ypoints = np.array([2,4,6,8])

#üstteki gibi bir çok referans noktası belirleyebiliriz (1,2) (3,4) (5,6) (7,8) noktaları eşleşir

plt.plot(ypoints) #eğer x ekseni verilmezse varsayılan değerler atar

plt.plot(ypoints, marker = 'o') #marker parametresi ile işaretçi şeklini belirleyebiliriz
#markerlar grafik üzerindeki eşleşme noktalarında bulunur

# o * . , x h v < > 1 2 3 4 | _ p P d D s + X tüm parametre çeşitleri bunlardır

plt.plot(ypoints, 'o:r:c') #fmt parametresi biçimlendiricidir

#fmt kullanımı

#fmt parametresi marker:line:color şeklindedir

#line seçenekleri - : -- -. şeklindedir. bunlar sırasıyla solid dotted dashed ve dashed-dotted line'dır

#colorlar r-g-b-c-m-y-k ve w-white'dır

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r') #marker şekillendirme

#marker şekillendirmede marker türü, büyüklüğü, dış rengi ve iç rengi ayarlanabilir
#ms ya da markersize parametresi ile büyüklüğü
#mec ya da markeredgecolor parametresi ile dış çizgi rengini
#mfc ya da markerfacecolor parametresi ile ise iç rengini belirleyebiliriz
#markıt biçimlendirmede hexadecimal renk kodları ya da html renk kodları kullanılabilir

#ÇİZGİ BİÇİMLENDİRME

plt.plot(ypoints, lw='5.5', c = '#ff0011', ls='dashed')

#line bicimlendirmede linestyle ya da ls ile çizgi stili
#color ya da c ile rengi
#linewidth ya da lw ile de çizginin kalınlığını belirleyebiliriz


ypoints1 = np.array([3,8,1,10])
ypoints2 = np.array([6,2,7,11])

plt.plot(ypoints1)
plt.plot(ypoints2)

#üstteli gibi farklı y eksenleri için peşpeşe plot oluşturarak grafik üstünde 2 çizgi oluşturabiliriz


#### TEK BİR PENCEREDE BİRDEN ÇOK ÇİZİM OLUŞTURMA - SUBPLOTS ####

#birinci plot
x = np.array([0,1,2,3])
y = np.array([4,5,6,7])

plt.subplot(1,2,1) #subplot parametreleri satır, sütun, sıralama şeklindedir
plt.plot(x,y)
#üstteki plot 1 satır 2 sütun ve 1.sıradaki çizimdir


#ikinci plot
x = np.array([0,1,2,3])
y = np.array([4,5,6,7])

plt.subplot(1,2,2)
plt.plot(x,y)
#üstteki plot ise 1 satır 2 sütunlu 2.sıradaki çizimdir

plt.suptitle("subtitle") #subtitle ya da supertitle ile tüm pencerenin başlığını belirleriz

plt.title("title") #title ile plotların başlığını belirleriz

#SCATTER - DAĞILIM GÖSTERİMİ

#scatterlar iki veri arasındaki ilişkileri tespit etmek ve yorumlamak amacıyla kullanılır
#plt.scatter() ile oluşturulur. bu method her gözlem için bir nokta oluşturur
#scatter çizimi için aynı uzunlukta 2 adet dizi gereklidir

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,87,94,78,103,77,85,86])

plt.scatter(x,y)

plt.show()

#FARKLI DAĞILIMLARI BİRLEŞTİRME
#aynı plot çizimde olduğu gibi peşpeşe yapılan scatter çizimlerinde de iki dağılım birleşecektir


#MATPLOTLIB BARS - ÇUBUKLAR

#cubuk grafikler olusturmak icin bar() fonksiyonu kullanilir

x = np.array(['a', 'b', 'c', 'd'])
y = np.array([3,8,1,10])

plt.bar(x,y)
plt.show

plt.barh(x,y) #barh (barhorizontal) ile çubuklar yatay olarak çizilir. 

#çubuk biçimlendirme

plt.bar(x, y, width = 0.1, color = 'red') #color ile rengi width ile kalınlığı belirlenebilir

### matplotlib histogram ###

#histogramlar frekans dağılımlarını gösterir
#verilen aralıktaki gözlem sayısını gösterir
#mesela 250 kişinin boy verisini histogramlar il gösterebiliriz

#plt.hist() ile oluşturulur

x = np.random.normal(80,20,250)

plt.hist(x, color = 'r')
plt.show()

#üstteki kod bloğur x dizisini parametre alarak kırmızı renk bir histogram oluşturur

# MATPLOTLIB PIE - PASTA GRAFIKLER

y = np.array([35,45,20,15])
plt.pie(y) #varsayılan olarak x ekseninden başlayarak saat yönünün tersine doğru döner

#pie grafikler 360 dereceye göre verilen verileri oranlayarak farklı renklerle gösterim sağlar

#label parametresi ile verilere etiket yazılabilir

mylabels = ["x", "y", "z", "a"]
plt.pie(y, label = mylabels) #mylabels içindeki stringleri sırasıyla verilere atar
plt.show

#dilim ayırma

myexplode = [0.2, 0, 0, 0] #bu değerler pastanın parçalarının merkeze olan uzaklığıdır

#0.2 değerini alacak olan y listesinin ilk elemanı diğer parçalardan ayrılır

#explode parametresi ile verilir

plt.pie(y, label = mylabels, explode = myexplode)

#RENK GÖSTERGESİ EKLEME

plt.legend() #bu fonksiyon verdiğimiz label değerlerini pencerede renk gösttergesi olarak ekler





