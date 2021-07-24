import cv2 as cv
import matplotlib.pyplot as plt
import math

img=cv.imread('plaza.jpg')
img2=cv.imread('tigre.jpg')

a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv.resize(img,(b,a))
img2=cv.resize(img2,(b,a))

C=0.75

for x in range(a):
    for y in range(b):
        x1=abs(math.floor(img.item(x,y,0)*(C)) + math.floor(img2.item(x,y,0)*(1-C)))
        img.itemset((x,y,0),x1)
        x1=abs(math.floor(img.item(x,y,1)*(C)) + math.floor(img2.item(x,y,1)*(1-C)))
        img.itemset((x,y,1),x1)
        x1=abs(math.floor(img.item(x,y,2)*(C)) + math.floor(img2.item(x,y,2)*(1-C)))
        img.itemset((x,y,2),x1)

plt.subplot(1,1,1),plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)),plt.title('C = 0.25')
#plt.subplot(1,2,2),plt.imshow(cv.cvtColor(hoja, cv.COLOR_BGR2RGB)),plt.title('Thresholding = 170')
plt.show()