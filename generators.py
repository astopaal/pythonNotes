#generator fonksiyonlar normal fonksiyonlar gibi tanımlanır
#ancak bir değer döndürmek için return yerine yield kullanılır
#bu durumda fonksiyon bitirilmez, tekrar çağrılmak için bekler
#tekrar çağrıldığında ise kaldıkları yerden bir sonraki yield işlemine kadar devam ederler

#generator functions are defined like normal functions
#but use yield instead of return to return a value
#in this case the function does not finish, it waits to be called again
#when is called again, they continue from where they left off until the next yield operation.

def simpleGenerator():
    yield 1
    yield 2
    yield 3


for value in simpleGenerator:
    print(value)

#you can create generator object on generator function type
#you can iterate generator function with object.__next__()
#bu fonksiyon üzerinde bir generator nesne türetilebilir
#bu nesne nesne.__next__() fonksiyonu ile kullanılaiblir

nesne = simpleGenerator()

print(nesne.__next__())