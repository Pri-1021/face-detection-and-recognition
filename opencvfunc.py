import cv2 as cv
img = cv.imread('images/butterfly.jpg')
cv.imshow('butterfly' , img)


#Converting to GrayScale- 
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('lena_gray' , gray)
# cv.waitKey(0)

#blurring an image 
# blur= cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blurred ela', blur)
# cv.waitKey(0)

#Creating Edge Cascade

canny = cv.Canny(img, 150,150)
cv.imshow('canny', canny)
cv.waitKey(0)