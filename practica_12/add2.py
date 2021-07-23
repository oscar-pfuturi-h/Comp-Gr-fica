import cv2 as cv
import matplotlib.pyplot as plt

plaza=cv.imread('plaza.jpg', cv.IMREAD_COLOR)
leon=cv.imread('leon.jpg', cv.IMREAD_COLOR)

plaza=cv.resize(plaza,(840,550),interpolation=cv.INTER_LINEAR)
leon=cv.resize(leon,(840,550),interpolation=cv.INTER_LINEAR)

print(plaza.shape,leon.shape)

rows,cols,tres=plaza.shape

r=0
g=0
b=0

for x in range(rows):
    for y in range(cols):
        r=int(plaza.item(x,y,2)/2)+int(leon.item(x,y,2)/2)
        g=int(plaza.item(x,y,1)/2)+int(leon.item(x,y,1)/2)
        b=int(plaza.item(x,y,0)/2)+int(leon.item(x,y,0)/2)
        plaza.itemset((x,y,2),r)
        plaza.itemset((x,y,1),g)
        plaza.itemset((x,y,0),b)


#hist = cv.calcHist([plaza],[0],None,[256],[0,256])
plt.subplot(1,1,1),plt.imshow(cv.cvtColor(plaza, cv.COLOR_BGR2RGB))
#plt.subplot(1,2,2).hist(plaza.ravel(),256,[0,256])
plt.show()
