import cv2 as cv
import numpy as np

"""translation"""
#-x -> left
#-y -> up
#x -> right
#y -> down
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

"""rotation"""
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    #cv.getRotationMatrix2D(<center>, <angle>, <scale>)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('Naruto', img)

#translate
translate_up = translate(img, 0, -100)
translate_down = translate(img, 0, 100)
translate_left = translate(img, -100, 0)
translate_right = translate(img, 100, 0)
translate_upright = translate(img, 400, -200)
translate_leftdown = translate(img, -50, 300)

cv.imshow('translate_up', translate_up)
cv.imshow('translate_down', translate_down)
cv.imshow('translate_left', translate_left)
cv.imshow('translate_right', translate_right)
cv.imshow('translate_upright', translate_upright)
cv.imshow('translate_leftdown', translate_leftdown)

#rotate
rotated = rotate(img, 45)
cv.imshow('rotated', rotated)
rotated_rotated = rotate(rotated, -45)
cv.imshow('rotated_rotated', rotated_rotated)

#resize
resized = cv.resize(img, (300,300), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#flipping
flip = cv.flip(img, -1)
#0->horizontal
#1->vertical
#-1->both
cv.imshow('flip', flip)

#crop
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

#wait for a specific delay (time in ms)
cv.waitKey(0)
