import os

from PIL import Image

INROW = 4

def main():
    path1 = '../gunwo'
    listing = os.listdir(path1)
    listing = [file for file in listing if file != '.directory']
    images = [Image.open(path1 + '/' + file) for file in listing]
    maxW = max([im.width for im in images])
    maxH = max([im.height for im in images])
    row = 0
    col = -1
    res = Image.new('RGB', (INROW * maxW, maxH * (len(images) / INROW)))
    for im in images:
        im = im.resize((maxW, maxH), Image.BILINEAR)
        col += 1
        if col >= INROW:
            col = 0
            row += 1
        res.paste(im, box=(col * maxW, row * maxH))

    res.save("beka.png")

if __name__ == "__main__":
    main()
