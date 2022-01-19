#bu uygulama ip tablosunda verilen değerlerin içinde bir ip arar
#eşleşen ip değerlerinin olduğu satırları html dosyasına yazar
#ve bu ip değerlerinin yazı rengini ve arka plan rengini değiştirir

logfile = open("ipTables.log", "r+")

line = logfile.readline()
htmlfile = open("iplog.html", "a+")

ip = "192.168.2.89"


htmlfile.write("<html>")
htmlfile.write("<body>")

while line:
    if ip in line:
        htmlfile.write(line)
        htmlfile.write("</br>")
    line = logfile.readline()

htmlfile.write("</body>")
htmlfile.write("</html>")

htmlfile.close()

with open('iplog.html', 'r') as html:
    htmldata = html.read()

htmldata = htmldata.replace('192.168.2.89', '<span style="background-color:yellow; color:red;"> 192.168.2.89 </span>')

with open('iplog.html', 'w') as file:
  file.write(htmldata)