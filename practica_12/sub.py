import cv2 as cv
import matplotlib.pyplot as plt

hoja1=cv.imread('hoja_texto.jpg')
hoja2=cv.imread('hoja_blanco.jpg')
subs=cv.imread('hoja_texto.jpg')

a=max(len(hoja1),len(hoja2))
b=max(len(hoja1[0]),len(hoja2[0]))
hoja1=cv.resize(hoja1,(b,a))
hoja2=cv.resize(hoja2,(b,a))

print(hoja1.shape,hoja2.shape)

rows2,cols2,tres=hoja1.shape

c=55

for x in range(rows2):
    for y in range(cols2):
        s=abs(hoja1.item(x,y,2)-hoja2.item(x,y,2)-c)
        subs.itemset((x,y,2),s)
        s=abs(hoja1.item(x,y,1)-hoja2.item(x,y,1)-c)
        subs.itemset((x,y,1),s)
        s=abs(hoja1.item(x,y,0)-hoja2.item(x,y,0)-c)
        subs.itemset((x,y,0),s)

for x in range(0,a):
    for y in range(0,b):
        g=subs.item(x,y,0)+subs.item(x,y,1)+subs.item(x,y,2)
        if g/3<=80 and 0<=g/3:
             subs.itemset((x,y,0),0)
             subs.itemset((x,y,1),0)
             subs.itemset((x,y,2),0)
        else:
             subs.itemset((x,y,0),255)
             subs.itemset((x,y,1),255)
             subs.itemset((x,y,2),255)

plt.subplot(1,2,1),plt.imshow(hoja1)
plt.subplot(1,2,2),plt.imshow(subs)
plt.show()
