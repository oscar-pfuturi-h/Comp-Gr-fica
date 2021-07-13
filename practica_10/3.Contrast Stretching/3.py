import cv2
import random
import numpy as np
import math
from matplotlib import pyplot as plt

img=cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
img2=cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
#hist = cv2.calcHist([img],[0],None,[256],[0,256])

a=0
b=255
fils,cols=img.shape

lista=[0]*256
cont=fils*cols

for x in range(fils):
    for y in range(cols):
        lista[img.item(x,y)]=lista[img.item(x,y)]+1

lista2=[]
for i in range(len(lista)):
    lista2=lista2+[i]*lista[i]
print(len(lista2),cont)
x=5*cont/100
y=95*cont/100
print(x,y)
c=lista2[round(x)]
d=lista2[round(y)]
print(c,d)
for x in range(fils):
    for y in range(cols):
        t=(img.item(x,y)-c)*((b-a)/(d-c))+a
        if t<0:
            t=0
        if t>255:
            t=255
        img2.itemset((x, y), t)
hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(2,2,2).hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3),plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.subplot(2,2,4).hist(img2.ravel(),256,[0,256])
cv2.imwrite('2.jpg',img2)
plt.show()


