import cv2 as cv
import matplotlib.pyplot as plt

tigre=cv.imread('tigre.jpg', cv.IMREAD_COLOR)
tigre2=cv.imread('tigre.jpg', cv.IMREAD_COLOR)

print(tigre.shape)

rows,cols,tres=tigre.shape

r=0
g=0
b=0
c=7

for x in range(rows):
    for y in range(cols):
        r=tigre.item(x,y,2)*c
        g=tigre.item(x,y,1)*c
        b=tigre.item(x,y,0)*c
        if r>255: r=255
        if g>255: g=255
        if b>255: b=255
        tigre2.itemset((x,y,2),r)
        tigre2.itemset((x,y,1),g)
        tigre2.itemset((x,y,0),b)

plt.subplot(1,2,1),plt.imshow(cv.cvtColor(tigre, cv.COLOR_BGR2RGB)),plt.title('Original')
plt.subplot(1,2,2),plt.imshow(cv.cvtColor(tigre2, cv.COLOR_BGR2RGB)),plt.title('C = 7')
plt.show()
