import json #json modülü pythonda hazır olarak gelir

json.loads() #json türünde yazılmış string değer python dictionary şeklinde okunur
json.load() #json dosyasını python dictionary'e atar

json.dumps() #python ensnesini json tipinde stringe çevirir
json.dump() #dictionary yapılı bir değişkeni json olarak dosyaya yazar

x = '{ "name" : "Samet", "age" : "25" }' #json tipinde yazılmış string

y = json.loads(x) #x stringini dictionary yapar

#json içindeki tek veya çok boyutlu verilere dizilerdeki boyut ve indis mantığı ile erişilir


