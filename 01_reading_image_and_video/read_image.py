import cv2 as cv

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('Naruto', img)
#wait for a specific delay (time in ms)
cv.waitKey(0)
