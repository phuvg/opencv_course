import cv2 as cv
import matplotlib.pyplot as plt

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('original', img)

#BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#HSV to BGR
hsv_gbr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_gbr', hsv_gbr)

#L*a*b to RGB
lab_rgb = cv.cvtColor(hsv, cv.COLOR_LAB2RGB)
cv.imshow('lab_rgb', lab_rgb)

#matplot
plt.imshow(img)
#plt.imshow(rgb)
plt.show()


#wait for a specific delay (time in ms)
cv.waitKey(0)
