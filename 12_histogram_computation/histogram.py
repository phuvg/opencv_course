import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

"""read image"""
img = cv.imread('../image/bird.jpg')
cv.imshow('original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//3), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('mask', mask)

#grayscale histogram
#cv.calcHist(<list_image>, <list_channel>, <mask>, <histSize>, <list_range>)
#gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
#gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
#plt.figure()
#plt.title('grayscale_histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

#color histogram
plt.figure()
plt.title('color_histogram')
plt.ylabel('# of pixels')
plt.xlabel('Bins')

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0,256])
plt.show()

#wait for a specific delay (time in ms)
cv.waitKey(0)
