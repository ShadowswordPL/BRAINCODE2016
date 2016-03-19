import cv2
import sys

from PIL import Image

from segment import detect_faces

def main():
    # Get user supplied values
    imagePath = sys.argv[1]

    faces, _, _ = detect_faces(imagePath, "haarcascade_frontalface_default.xml", 1.02)
    print "Found {0} faces!".format(len(faces))

    # Draw a rectangle around the faces
    image = cv2.imread(imagePath)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
