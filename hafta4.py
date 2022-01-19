#bu uygulama çok boyutlu dizilerin elemanlarını tek boyutluymuş gibi yazdırır.
#this app prints all elements of multidimensional arrays as if they were one dimensional

liste = [0,[1,2,['a','b']],3,[4,5,6]]

def yaz(a):

    for i in a:
        if isinstance(i, list):
            yaz(i)
        else:
            print(i)
yaz(liste)

