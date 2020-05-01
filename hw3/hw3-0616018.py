img = open('face.bmp', 'rb').read()
new_img = bytearray(img)
for i in range(54, len(new_img), 3):
    new_img[i] = (new_img[i] - 50) % 256

open('face2.bmp', 'wb').write(new_img)
