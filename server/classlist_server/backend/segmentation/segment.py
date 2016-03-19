import cv2
import os
import time
from PIL import Image

def detect_faces(imagePath, cascPath='haarcascade_frontalface_default.xml', scaleFactor=1.02):
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier('backend/segmentation/' + cascPath)
    print os.getcwd()
    print '/home/tommalla/Programowanie/Python/BrainCode/BRAINCODE2016/server/classlist_server/backend/segmentation/' + cascPath
    print faceCascade.empty()

    # Read the image
    image = cv2.imread(imagePath)
    height, width, channels = image.shape

    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=scaleFactor,
        minNeighbors=10,
        minSize=(45, 45),
        maxSize=(500,500)
    )

    print "Found {0} faces".format(len(faces))

    i = 0
    change = 20

    for (x, y, w, h) in faces:
        i += 1
        im = Image.open(imagePath)
        crop_tuple = (max(x - change, 0), max(y - change, 0), min(x + w + change, width), min(y + h + change, height))
        im = im.crop(crop_tuple)
        current_time = int(time.time())
        faceImagePath = 'photos/%d-%d.png' % (current_time, i)
        im.save(faceImagePath)

    return faces, height, width
