import cv2
import sys

from PIL import Image

def main():
    # Get user supplied values
    imagePath = sys.argv[1]
    cascPath = sys.argv[2]

    faces, height, width = detect_faces(imagePath, "haarcascade_frontalface_default.xml", 1.02)
    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    i = 0
    change = 20

    image = cv2.imread(imagePath)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    for (x, y, w, h) in faces:
        i += 1
        im = Image.open(imagePath)
        crop_tuple = (max(x - change, 0), max(y - change, 0), min(x + w + change, width), min(y + h + change, height))
        im = im.crop(crop_tuple)
        faceImagePath = 'photos/%d.png' % i
        im.save(faceImagePath)

        #image2 = cv2.imread(faceImagePath)
        #faces2, height2, width2 = detect_faces(faceImagePath, "haarcascade_frontalface_default.xml", 1.01)

        faceImagePath2 = 'photos_results/%d.png' % i

        #if len(faces2) > 0:
        im.save(faceImagePath2)

        #for (x, y, w, h) in faces2:
        #    cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.imshow("Faces found", image2)
        #cv2.waitKey(0)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
