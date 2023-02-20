import cv2 as cv
import numpy as np
import os

#config
people = ['Bach Loc', 'Chuc Tu Dan', 'Cuc Tinh Y', 'Tran Ngoc Ky', 'Trieu Le Dinh']
DIR = r'D:\DATA\proj\py\opencv\opencv_course\image\train'

#global variable
features = []
labels = []

#report
counters = []

#create CascadeClassifier
haar_cascade = cv.CascadeClassifier('../15_face_detection/haar_face_alt.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        cnt = 0
        print(f'-------------------------------')
        print(f'training face: {person}')
        for img in os.listdir(path):
            #get image path
            img_path = os.path.join(path, img)
            #read image
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            #face detection
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
            if(len(faces_rect) == 1):
                cnt += 1
                for (x,y,w,h) in faces_rect:
                    faces_roi = gray[y:y+h, x:x+w]
                    features.append(faces_roi)
                    labels.append(label)
                print(f'{img} has {len(faces_rect)} face(s) --> train')
            else:
                print(f'{img} has {len(faces_rect)} face(s) --> not train')
        counters.append(cnt)

#prepare data train
create_train()
print(">> report...")
for i, person in enumerate(people):
    print(f'>> train face {person} with {counters[i]} image')
print(">> training done...")

#face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train the regconizer on the features list and the labels list
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer.train(features, labels)
#save trained yml and features and labels
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
print(">> creating done...")
