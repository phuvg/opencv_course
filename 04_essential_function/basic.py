import cv2 as cv

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('original', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade
#cv.Canny(<img>, <threshold1>, <threshold2>)
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

#dilate the image
dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow('dilated', dilated)

#erode
eroded = cv.erode(dilated, (3,3), iterations=5)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (300,300), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#crop
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

#wait for a specific delay (time in ms)
cv.waitKey(0)
