import cv2 as cv
img = cv.imread('images/butterfly.jpg')#Path of file
cv.imshow('butterfly', img) #Window title 
cv.waitKey(0)