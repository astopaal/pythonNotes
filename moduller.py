#pythonda modüller 3 şekilde bulunur

#python ile yazılan modüller
#c ile yazılıp çalışma zamanında dinamik oalrak yüklenebilir
#yorumlayıcı içinde dahili olarak bulunur

#herhangi bir python dosyası içindeki tüm değerlere bu dosyayı import ederek başka bir dosya içerisinden erişebiliriz

import hafta3 #hafta3 modülünü import eder

hafta3.columnCount
hafta3.coupon
hafta3.i #for içindeki dğeişkenlere bile erişilebilir

import hafta10

hafta10.guvenliMi() #fonksiyonlara da aynı şekilde erişilebilir

from hafta10 import guvenliMi #hafta 10 içinden sadece güvenliMi fonksiyonunu çeker

from hafta3 import * #tüm nesneleri çeker



