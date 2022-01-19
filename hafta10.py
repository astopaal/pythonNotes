#this app controls if some values in idx1 and idx5 json files are within safe limits given in ayar.json file

#after it creates plot with matplotlib
#if value is safe, plot color is green, else red

#temp ics
#humidity icn
#data co2
import matplotlib.pyplot as plt
import json
import numpy as np


def guvenliMi(deger,alt,ust):
    if alt <= deger <= ust:
        print("Güvenli")
        return True
    else:
        print("Güvenli değil")

with open('idx1.json', "r") as idx1dosya:
    idx1data = json.load(idx1dosya)

temp = idx1data['result'][0]["Temp"]

humidity = idx1data['result'][0]["Humidity"]

with open('ayar.json', "r") as ayardosya:
    ayardata = json.load(ayardosya)

#####################################################

with open('idx5.json', "r") as idx5dosya:
    idx5data = json.load(idx5dosya)

dataString = idx5data['result'][0]["Data"]

data = int(dataString[:2])

degerler = []

icsAlt = ayardata["icsAlt"]
icsUst = ayardata["icsUst"]
icnAlt = ayardata["icnAlt"]
icnUst = ayardata["icnUst"]
co2Alt = ayardata["co2Alt"]
co2Ust = ayardata["co2Ust"]


guvenliMi(temp, icsAlt, icsUst)
guvenliMi(humidity, icnAlt, icnUst)
guvenliMi(data, co2Alt, co2Ust)

veriler = [temp, humidity, data]

height = [temp, humidity, data]
bars = ('Sıcaklık', 'İç nem', 'Hava Kalitesi')

x_pos = np.arange(len(bars))

# Create bars
barlist = plt.bar(x_pos, height)

if guvenliMi(temp, icsAlt, icsUst):
    barlist[0].set_color('green')
else:
    barlist[0].set_color('red')

if guvenliMi(humidity, icnAlt, icnUst):
    barlist[1].set_color('green')
else:
    barlist[1].set_color('red')
    
if guvenliMi(data, co2Alt, co2Ust):
    barlist[2].set_color('green')
else:
    barlist[2].set_color('red')

# Create names on the x-axis
plt.xticks(x_pos, bars)
plt.show()
