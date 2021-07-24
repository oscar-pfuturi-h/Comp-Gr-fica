import cv2 as cv
import matplotlib.pyplot as plt

hoja=cv.imread('hoja_texto.jpg')
hoja2=cv.imread('hoja_blanco.jpg')

a=max(len(hoja),len(hoja2))
b=max(len(hoja[0]),len(hoja2[0]))
hoja=cv.resize(hoja,(b,a))
hoja2=cv.resize(hoja2,(b,a))

max = 0
min = 255
nMax = 255
nMin = 0
c=100

for x in range(a):
    for y in range(b):
        p=(hoja.item(x,y,0)/hoja2.item(x,y,0))
        hoja.itemset((x,y,0),p*c)
        if p <= min:
            min = p
        if p >= max:
            max = p
        p=(hoja.item(x,y,1)/hoja2.item(x,y,1))
        hoja.itemset((x,y,1),p*c)
        if p <= min:
            min = p
        if p >= max:
            max = p
        p=(hoja.item(x,y,2)/hoja2.item(x,y,2))
        hoja.itemset((x,y,2),p*c)
        if p <= min:
            min = p
        if p >= max:
            max = p
            
min=min*c
max=max*c
print(min)
print(max)
print(int((((hoja.item(x,y,0)-min)*((nMax-nMin)/(max-min)))+nMin)))

for x in range(a):
    for y in range(b):
        p=int((((hoja.item(x,y,0)-min)*((nMax-nMin)/(max-min)))+nMin))
        if p >= 255:
            p=255
        if p <= 0:
            p=0
        hoja.itemset((x,y,0),p)
        p=int((((hoja.item(x,y,1)-min)*((nMax-nMin)/(max-min)))+nMin))
        if p >= 255:
            p=255
        if p <= 0:
            p=0
        hoja.itemset((x,y,1),p)
        p=int((((hoja.item(x,y,2)-min)*((nMax-nMin)/(max-min)))+nMin))
        if p >= 255:
            p=255
        if p <= 0:
            p=0
        hoja.itemset((x,y,2),p)

for x in range(0,a):
    for y in range(0,b):
        if (hoja.item(x,y,0)+hoja.item(x,y,1)+hoja.item(x,y,2))/3<=170 and 0<=(hoja.item(x,y,0)+hoja.item(x,y,1)+hoja.item(x,y,2)):
             hoja.itemset((x,y,0),0)
             hoja.itemset((x,y,1),0)
             hoja.itemset((x,y,2),0)
        else:
             hoja.itemset((x,y,0),255)
             hoja.itemset((x,y,1),255)
             hoja.itemset((x,y,2),255)

plt.subplot(1,2,1),plt.imshow(cv.cvtColor(hoja, cv.COLOR_BGR2RGB)),plt.title('Texto dividido (Thresholding 170)')
plt.show()
