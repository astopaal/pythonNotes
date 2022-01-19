#open fonksiyonu kullanılarak dosya oluşturma/açma işlemleri yapılır

# r: read w: write a:add x:create

dosya = open("dosya.txt", "r")

dosya.closed() #dosya kapalı mı?
dosya.mode() #erişim modunu verir
dosya.name() #dosyanın ismini verir
dosya.close() #dosyayı kapatır
dosya.write("something")  #dosyaya yazar
dosya.readline() #bir satır okur
dosya.readlines() #tüm satırları sırayla okuyup bir listeye atar
dosya.writelines() #bir listeyi dosyaya satır satır yazar
dosya.tell() #imlecin nerede olduğunu söyler
dosya.seek #imlecin yerini değiştirir

#with ile dosya işlemleri
#alttaki iki blok da aynı işlemi yapar
#with kulannımı otomatik olarak gerek işlem yapıldığında dosyayı kapatır

dosya2 = open("dosya2.txt")
data = dosya2.read()
print(data)
dosya.close()


with open("dosya2.txt") as dosya2:
    data = dosya.read()
    print(data)


    