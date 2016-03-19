import cv2

def detect_faces(imagePath, cascPath='haarcascade_frontalface_default.xml', scaleFactor=1.02):
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

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
    return faces, height, width
