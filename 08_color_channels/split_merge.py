import cv2 as cv
import numpy as np

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('original', img)

b,g,r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)
print(merged.shape)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('blank_blue', blue)
cv.imshow('blank_green', green)
cv.imshow('blank_red', red)

#wait for a specific delay (time in ms)
cv.waitKey(0)
