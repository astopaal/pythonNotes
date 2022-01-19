#pythonda tek satırdan oluşan ve bir işlem yapan fonksiyonlar tanımlanabilir
#you can define one row functions in python

def sumOfNumbers(x,y):
    return x+y

sumOfNumbers_ = lambda x,y : x+y

#bir dizinin içindeki tüm elemanlar için fonksiyon çalıştırmak için map fonksiyonu kullanılabilir
#map function runs the function for each element of the array

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

x = list(map(lambda i,j: i+j, list1, list2))

#filter fonksiyonu da map gibi bir dizi ve fonksiyon olarak iki parametre alır
#dizinin her elemanı için işlem gerçekleştirir ve true dönen sonuçları döndürür

#filter function, like the map function, takes an array and a function parameter.
#performs an operation on each element of the array and returns true results

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
tekSayilar = list(filter(lambda x: x%2==0, fibonacci))

