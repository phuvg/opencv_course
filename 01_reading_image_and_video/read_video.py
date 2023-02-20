import cv2 as cv

"""read video"""
capture = cv.VideoCapture('../video/music.mp4')
while True:
    #read video frame by frame
    isTrue, frame = capture.read()
    #show video
    cv.imshow('music', frame)
    if(cv.waitKey(20) and 0xFF==ord('d')):
       break
capture.release()
cv.detroyAllWindows()
