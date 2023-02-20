import cv2 as cv

"""read image"""
img = cv.imread('../image/naruto.png')
cv.imshow('original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#simple thresholding
#cv.threshold(<image>, <thresh>, <maxval>, <type>)
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv', thresh_inv)

#adaptive thresholding
#cv.adaptiveThreshold(<image>, <maxValue>, <adaptiveMethod>, <thresholdType>, <blockSize>, <C>)
#adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive_thresh', adaptive_thresh)

#wait for a specific delay (time in ms)
cv.waitKey(0)
