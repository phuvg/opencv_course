import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('original', img)
    
cv.imshow('resize', rescaleFrame(img, 1.5))

#wait for a specific delay (time in ms)
cv.waitKey(0)
