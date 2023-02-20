import cv2 as cv
import numpy as np

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#method 1
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

#method 2
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours1, hierarchies1 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours1)} contour(s)1 found!')

#draw contours
blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow('blank', blank)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('draw contours', blank)

blank1 = np.zeros(img.shape, dtype='uint8')
#cv.imshow('blank1', blank1)

cv.drawContours(blank1, contours1, -1, (255,0,0), 1)
cv.imshow('draw contours1', blank1)


#wait for a specific delay (time in ms)
cv.waitKey(0)
