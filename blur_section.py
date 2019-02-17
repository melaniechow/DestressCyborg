# blur section of image

from PIL import Image, ImageFilter, ImageOps
import os

directory = "vid5"

for filename in os.listdir(directory):
    if os.path.splitext(filename)[1] == ".jpg":
        rawname = os.path.splitext(filename)[0]
        im = Image.open("%s/%s" % (directory, filename)).convert("RGBA")
    else:
        continue

    width, height = im.size

    with open("%s/%s.txt" % (directory, rawname)) as textFile:
        lines = [line.split() for line in textFile]


    def labels2box(width, height, line):
        b1 = width * (float(line[1]) - 0.5 * float(line[3]))
        b2 = height * (float(line[2]) - 0.5 * float(line[4]))
        b3 = width * (float(line[1]) + 0.5 * float(line[3]))
        b4 = height * (float(line[2]) + 0.5 * float(line[4]))
        #print(int(b1), int(b2), int(b3), int(b4))
        return (int(b1), int(b2), int(b3), int(b4))


    boxes = []

    for line in lines:
        boxes.append(labels2box(width, height, line))

    trigger = [0]

    for i in range(len(boxes)):
        if (int(lines[i][0]) in trigger):
            img = Image.open("Arthur.jpg", "r")
            box = boxes[i]
            box_width = box[2] - box[0]
            box_height = box[3] - box[1]
            print(box_width)
            print(box_height)
            #img.resize((box_width, box_height), Image.ANTIALIAS)
            img = ImageOps.fit(img, (box_width, box_height))
            ic = im.crop(box).convert("RGBA")
            print(img.mode)
            print(im.mode)
            print(ic.mode)
            ic.paste(img, (box[0],box[1]))
            im.paste(ic, box)
#            im.paste(ic, Image.open("sponge.png"))
#            ic = ic.filter(ImageFilter.GaussianBlur(10))
#            ic = ic.filter(ImageFilter.BLUR)
#            ic = ic.filter(ImageFilter.BLUR)
#            im.paste(ic, box)

    im.save("%s/%s_blur.png" % (directory, rawname))
