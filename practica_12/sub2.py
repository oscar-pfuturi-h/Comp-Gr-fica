import cv2 as cv
import matplotlib.pyplot as plt

foto1=cv.imread('foto1.jpg')
foto2=cv.imread('foto2.jpg')
subs=cv.imread('foto1.jpg')

a=max(len(foto1),len(foto2))
b=max(len(foto1[0]),len(foto2[0]))
foto1=cv.resize(foto1,(b,a))
foto2=cv.resize(foto2,(b,a))

print(foto1.shape,foto2.shape)

rows,cols,tres=foto1.shape

for x in range(rows):
    for y in range(cols):
        s=abs(foto1.item(x,y,2)-foto2.item(x,y,2))
        subs.itemset((x,y,2),s)
        s=abs(foto1.item(x,y,1)-foto2.item(x,y,1))
        subs.itemset((x,y,1),s)
        s=abs(foto1.item(x,y,0)-foto2.item(x,y,0))
        subs.itemset((x,y,0),s)

plt.subplot(1,1,1),plt.imshow(subs)
plt.show()
