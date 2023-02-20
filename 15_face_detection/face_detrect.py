import cv2 as cv

#create CascadeClassifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

"""image ronaldo"""
img_ronaldo = cv.imread('../image/ronaldo.jpg')
#cv.imshow('ronaldo', img_ronaldo)

gray_ronaldo = cv.cvtColor(img_ronaldo, cv.COLOR_BGR2GRAY)
#cv.imshow('gray_ronaldo', gray_ronaldo)

faces_rect_ronaldo = haar_cascade.detectMultiScale(gray_ronaldo, scaleFactor=1.1, minNeighbors=3)
print(f'Number of faces found = {len(faces_rect_ronaldo)}')

for (x,y,w,h) in faces_rect_ronaldo:
    cv.rectangle(img_ronaldo, (x,y), (x+w, y+h), (0,255,0), thickness=3)

cv.imshow('ronaldo_face', img_ronaldo)

"""image brazil"""
img_brazil = cv.imread('../image/brazil2002.jpg')
#cv.imshow('brazil', img_brazil)

gray_brazil = cv.cvtColor(img_brazil, cv.COLOR_BGR2GRAY)
#cv.imshow('gray_brazil', gray_brazil)

faces_rect_brazil = haar_cascade.detectMultiScale(gray_brazil, scaleFactor=1.1, minNeighbors=8)
print(f'Number of faces found = {len(faces_rect_brazil)}')

for (x,y,w,h) in faces_rect_brazil:
    cv.rectangle(img_brazil, (x,y), (x+w, y+h), (0,255,0), thickness=3)

cv.imshow('brazil_face', img_brazil)

#wait for a specific delay (time in ms)
cv.waitKey(0)
