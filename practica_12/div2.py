import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('foto1.jpg')
img2=cv.imread('foto2.jpg')

a=max(len(img),len(img2))
b=max(len(img[0]),len(img2[0]))
img=cv.resize(img,(b,a))
img2=cv.resize(img2,(b,a))

C=100
A=0
B=255

c1=255
d1=0
c2=255
d2=0
c3=255
d3=0
for x in range(a):
    for y in range(b):
        p=(img.item(x,y,0)/img2.item(x,y,0))
        img.itemset((x,y,0),p*C)
        if c1>img.item(x,y,0):
            c1=img.item(x,y,0)
        if d1<img.item(x,y,0):
            d1=img.item(x,y,0)
        p=(img.item(x,y,1)/img2.item(x,y,1))
        img.itemset((x,y,1),p*C)
        if c2>img.item(x,y,1):
            c2=img.item(x,y,1)
        if d2<img.item(x,y,1):
            d2=img.item(x,y,1)
        p=(img.item(x,y,2)/img2.item(x,y,2))
        img.itemset((x,y,2),p*C)
        if c3>img.item(x,y,2):
            c3=img.item(x,y,2)
        if d3<img.item(x,y,2):
            d3=img.item(x,y,2)

# I eq
for x in range(a):
    for y in range(b):
        t=(img.item(x,y,0)-c1)*((B-A)/(d1-c1))+A
        img.itemset((x,y,0),t)
        t=(img.item(x,y,1)-c2)*((B-A)/(d2-c2))+A
        img.itemset((x,y,1),t)
        t=(img.item(x,y,2)-c3)*((B-A)/(d3-c3))+A
        img.itemset((x,y,2),t)


plt.subplot(1,1,1),plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
#plt.subplot(1,2,2),plt.imshow(cv.cvtColor(hoja, cv.COLOR_BGR2RGB)),plt.title('Thresholding = 170')
plt.show()