import cv2 as cv

"""read image"""
img = cv.imread('../image/bird.jpg')
cv.imshow('original', img)

#averaging blur
avg = cv.blur(img, (7,7))
cv.imshow('blur_avg', avg)

#gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('blur_gaussian', gauss)

#median blur
median = cv.medianBlur(img, 7)
cv.imshow('blur_median', median)

#bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

#wait for a specific delay (time in ms)
cv.waitKey(0)
