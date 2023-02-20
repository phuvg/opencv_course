import cv2 as cv
import numpy as np

#0 paint the blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank', blank)

#1 paint the image a certain colour
blank[100:400, 200:300] = 0,255,0
cv.imshow('green', blank)

#2 draw a rectangle
#cv.rectangle(<img>, <start_point>, <end_point>, <color>, <thickness>)
cv.rectangle(blank, (100,400), (400,100), (0,0,255), thickness=5)
cv.rectangle(blank, (0,0), (blank.shape[1]//4, blank.shape[0]//4), (255,0,255), thickness=cv.FILLED)
cv.rectangle(blank, (400,400), (500,500), (255,0,0), thickness=-1)
cv.imshow('rectangle', blank)

#3 draw a circle
#cv.circle(<img>, <center_circle>, <radius>), <color>, <thickness>)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (100,100,0), thickness=2)
cv.imshow('circle', blank)
cv.circle(blank, (400,100), 100, (200,200,0), thickness=-1)
cv.imshow('circle', blank)

#4 draw a line
#cv.line(<img>, <start_point>, <end_point>, <color>, <thickness>)
cv.line(blank, (0,blank.shape[0]//2), (blank.shape[1],blank.shape[0]//2), (0,200,200), thickness=3)
cv.line(blank, (100,300), (500,500), (255,255,255), thickness=10)
cv.imshow('line', blank)

#write text
#cv.putText(<img>, <text>, <start_point>, <font>, <font_scale>, <color>, <thickness>)
cv.putText(blank, 'Hi there! How are you?', (0,250), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)

#wait key
cv.waitKey(0)
