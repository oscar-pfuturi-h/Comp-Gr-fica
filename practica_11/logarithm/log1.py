import cv2 as cv
import matplotlib.pyplot as plt
import math

img = cv.imread('log1.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('log1.jpg', cv.IMREAD_GRAYSCALE)

print(img.shape)

rows,cols=img.shape
c=60

for x in range(rows):
    for y in range(cols):
        img2.itemset((x,y),c*math.log10(1+img.item(x,y)))

hist = cv.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
plt.show()
