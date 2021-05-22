import qrcode
import image

qr = qrcode.QRCode(
    version=15,  # means version of qr code. higher the number, more large and complicated picture
    box_size=10,  # size of QR code box
    border=5  # border of the image with white color
)
data = 'https://www.instagram.com/akarishiraj'
# any link qr code you want. Past it in the colons

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save('test.png')
