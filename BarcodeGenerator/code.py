from qrcode import qrcode
img = qrcode.make("I love coding!")
img.save("youtubeQR.png")
