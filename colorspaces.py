import cv2 as cv
img = cv.imread('images/squirrel.jpg')
cv.imshow('city', img)



#BGR to HSV
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('city_HSV' , hsv)



#BGR to L*a*b
lab=  cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('city_lab' , lab)



#BGR to RGB
rgb=  cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('city_RGB', rgb)
cv.waitKey(0)