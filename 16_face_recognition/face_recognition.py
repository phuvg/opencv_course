import cv2 as cv
import numpy as np

#config
people = ['Bach Loc', 'Chuc Tu Dan', 'Cuc Tinh Y', 'Tran Ngoc Ky', 'Trieu Le Dinh']

#create CascadeClassifier
haar_cascade = cv.CascadeClassifier('../15_face_detection/haar_face_alt.xml')

#read features model and labels model
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

#face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

#read image
img = cv.imread(r'../image/test/test_trieuledinh_01.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#detect the face in image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 6)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (x-10,y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
cv.imshow('detected face', img)

#wait
cv.waitKey(0)
