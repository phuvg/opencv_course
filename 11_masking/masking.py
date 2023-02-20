import cv2 as cv
import numpy as np

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

#circle mask
mask_circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//8), 100, 255, -1)
cv.imshow('mask_circle', mask_circle)

masked_circle = cv.bitwise_and(img, img, mask=mask_circle)
cv.imshow('masked_circle', masked_circle)

#rectangle mask
mask_rectangle = cv.rectangle(blank.copy(), (250, 50), (400, 150), 255, -1)
cv.imshow('mask_rectangle', mask_rectangle)

masked_rectangle = cv.bitwise_and(img, img, mask=mask_rectangle)
cv.imshow('masked_rectangle', masked_rectangle)

#wait for a specific delay (time in ms)
cv.waitKey(0)
