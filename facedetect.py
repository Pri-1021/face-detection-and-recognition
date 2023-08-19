import cv2 as cv

img= cv.imread('images/lena.jpg')
cv.imshow('face' , img)
haar_cascade = cv.CascadeClassifier('haarface.xml')
faces_rect=haar_cascade.detectMultiScale(img, scaleFactor = 1.1, minNeighbors=2)
for(x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w,y+h),(0,255,0), thickness= 2)
        cv.putText(img, 'Face', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv.imshow('facedetect', img)


cv.waitKey(0)