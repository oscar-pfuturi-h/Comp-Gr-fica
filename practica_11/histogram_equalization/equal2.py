import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math

def sumatoria(mylist,n):
    P=0
    for j in range(n):
        P+=mylist[j]/npixels
    return P

img = cv.imread('equal3.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('equal3.jpg', cv.IMREAD_GRAYSCALE)

print(img.shape)

rows,cols=img.shape
L=256
mylist=[0]*L

startRow=int(rows*.4)
startCol=int(cols*.4)
endRow=int(rows*.6)
endCol=int(cols*.6)

croppedImage=img[startRow:endRow,startCol:endCol]
rows2,cols2=croppedImage.shape
npixels=rows2*cols2

# cv.imshow('Cropped Image', croppedImage)

for x in range(rows2):
    for y in range(cols2):
        i=croppedImage.item(x,y)
        mylist[i]=mylist[i]+1

for x in range(rows):
    for y in range(cols):
        s=math.floor((L-1)*sumatoria(mylist,img.item(x,y)))
        img.itemset((x,y),s)

hist = cv.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
plt.show()
