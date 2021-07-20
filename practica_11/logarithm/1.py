import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

img=cv2.imread('exp_5.jpg', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('exp_5.jpg', cv2.IMREAD_GRAYSCALE)

fils,cols=img.shape
cont=fils*cols


p=[0]*256
c=50
for x in range(fils):
    for y in range(cols):
        p=c*math.log(1+img.item(x,y),10)
        if p>255:
            p=255
        if p<0:
            p=0
        img2.itemset((x,y),int(p))
hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(img,'gray')
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(img2,'gray')
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
cv2.imwrite('h2.jpg',img2)
plt.show()


