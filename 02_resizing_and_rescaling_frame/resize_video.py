import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

"""read video"""
capture = cv.VideoCapture('../video/music.mp4')
while True:
    #read video frame by frame
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame)
    #show video
    cv.imshow('original', frame)
    cv.imshow('resize', frame_resize)
    if(cv.waitKey(20) and 0xFF==ord('d')):
       break
capture.release()
cv.detroyAllWindows()
