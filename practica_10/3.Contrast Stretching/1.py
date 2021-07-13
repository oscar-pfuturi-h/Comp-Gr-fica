import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('contr2_1.jpg', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('contr2_1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)


a=0
b=255
c=255
d=0
fils,cols=img.shape
for x in range(fils):
    for y in range(cols):
        if c>img.item(x,y):
            c=img.item(x,y)
        if d<img.item(x,y):
            d=img.item(x,y)
print(c,d)


for x in range(fils):
    for y in range(cols):
        t=(img.item(x,y)-c)*((b-a)/(d-c))+a
        img2.itemset((x, y), t)

hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
cv2.imwrite('contr3_2.jpg',img2)
plt.show()


