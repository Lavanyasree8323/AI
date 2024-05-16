import cv2
import imutils


## image read resize show
img = cv2.imread('org.JPG')
rsi = imutils.resize(img, width=100)
cv2.imshow('org.png', img)
cv2.imshow('new.png', rsi)
cv2.imwrite('new.png', rsi)

## GaussianBlur -  Smoothening
img =cv2.imread('org.JPG')
gaus = cv2.GaussianBlur(img, (41, 41), 50)
gaus1 = cv2.GaussianBlur(img, (21, 21), 0)
cv2.imshow("org", img)
cv2.imshow("bt", gaus)
cv2.imshow("ch", gaus1)

## convert to grey

img = cv2.imread("org.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('bori', img)
cv2.imshow('grayimg', gray)
cv2.imwrite('grayimg.png', gray)
print(img.shape)
print(img.size)


## Threshold - white& black
img = cv2.imread("org.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thrs = cv2.threshold(gray,180,255,cv2.THRESH_BINARY)[1]
cv2.imshow("original",img)
cv2.imshow("thrs",thrs)
