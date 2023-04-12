from PIL import Image
from pyzbar.pyzbar import decode

img = Image.open('./qr_code.png')

result = decode(img)

print(result)
