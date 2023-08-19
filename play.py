import cv2 as cv
capture = cv.VideoCapture('images/Megamind.avi')
while True:
    isTrue, Frame= capture.read()
    cv.imshow('Video', Frame)
    if cv.waitKey(25) & 0xFF==ord('c'):
     break
capture.release()
cv.destroyAllWindows()

