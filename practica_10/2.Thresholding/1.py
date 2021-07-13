import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
fils,cols=img.shape
print(fils,cols)
print(img.item(35,166))
for x in range(fils):
    for y in range(cols):
        if img.item(x,y)<=255 and 180<=img.item(x,y):
            img2.itemset((x, y), 255)
        else:
            img2.itemset((x, y), 0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow('hist',hist)
plt.subplot(1,3,1),plt.imshow(img,'gray')
plt.subplot(1,3,2),plt.imshow(img2,'gray')
plt.subplot(1,3,3).hist(img.ravel(),256,[0,256])
plt.show()
