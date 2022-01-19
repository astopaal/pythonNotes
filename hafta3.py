from random import randint

#bu uygulama kullanıcı için kullanıcının istediği sayıda rastgele süper loto kolonları oluşturur
#kullanıcı isterse her kolonda mutlak bulunması gereken bir banko sayı belirleyeiblir

#this application generates lotto coupons containing random numbers for the user as many times as they want
#the user can specify a number that they want to be on all coupons



columnCount = int(input("kolon sayısı girin"))

bankoIste = input("banko sayı istermisiniz? e/h")

if bankoIste=="e":

    banko = int(input("banko sayınızı girin"))

coupon = []

for i in range(columnCount):

    if bankoIste == "e":

        temp = []
        temp.append(banko)

        for j in range(5):
            temp.append(randint(1,90))

        coupon.append(temp)
    
    else:
        temp = []

        for j in range(6):
            temp.append(randint(1,90))

        coupon.append(temp)

print(coupon)
