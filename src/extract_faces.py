"""
Extract faces from the images using Open CV.
"""
import cv2
import sys
import os

RAW_IMAGE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/images/raw/'
PROCESSED_IMAGE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/data/images/processed/'
HAAR_CASCADE_FILE = 'haarcascade_frontalface_default.xml'

# create caascade
face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_FILE)

for filename in os.listdir(RAW_IMAGE_DIRECTORY):
    if filename == '.DS_Store':
        continue

    print(filename)

    # read image
    image = cv2.imread(RAW_IMAGE_DIRECTORY + filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for i, (x, y, w, h) in enumerate(faces):
        cv2.imwrite(PROCESSED_IMAGE_DIRECTORY+filename+'_'+str(i)+'.jpeg', image[y:y+h, x:x+w])
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imwrite(PROCESSED_IMAGE_DIRECTORY+filename+'.jpeg', image)
