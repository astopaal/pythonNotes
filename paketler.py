#paketler içinde modüller barındırır
#modülleri hiyerarşik bir yapıda organize ederekpaketler oluşturmak ve bu paketleri nokta notasyonu ile kullanmak mümkündür

import paketler.module1 #paketler içindeki module1 dosyasını çağırır

from paketler.module1 import x #paketler/module1 içindeki x nesnesini import eder

#eğer paket içinde __init__.py dosyası varsa, paket import edildiğinde direkt olarak bu dosya çalışır

#init doyası içinde modüllerin importu varsa, paket import edildiğinde bu modüller de otomatik olarak import edilir

#pip kullanımı

# pip install ..... - bir paketi kurar
# pip download .... - paketi indirir
# pip uninstall ... - paketi kaldırır
# pip list          - yüklü paketleri listeler
# pip search ...... - paket deposunda bir paketi arar
# pip show ........ - yüklü bir paket hakkında bilgi verir
