import cv2 as cv
import matplotlib.pyplot as plt
import math

def sumatoria(mylist,n):
    P=0
    for j in range(n):
        P+=mylist[j]/npixels
    return P

img = cv.imread('equal1.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('equal1.jpg', cv.IMREAD_GRAYSCALE)

print(img.shape)

rows,cols=img.shape
npixels=rows*cols
L=256
mylist=[0]*256

for x in range(rows):
    for y in range(cols):
        i=img.item(x,y)
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
