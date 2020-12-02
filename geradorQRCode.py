import pyqrcode
QRstr = "https://github.com/pedro-emidio"
url = pyqrcode.create(QRstr)
url.png(r'C:\teste.png', scale=8)
