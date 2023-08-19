import cv2 as cv

def rescaleFrame(img, scale= 0.5):
    width= int(img.shape[1] * scale)
    height= int(img.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
img = cv.imread('images/simba_plays.jpg')#Path of file
cv.imshow('simba', img)
img_resized= rescaleFrame(img)
cv.imshow('simba resized', img_resized) #Window title 
cv.waitKey(0)
