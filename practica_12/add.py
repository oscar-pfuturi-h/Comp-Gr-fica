import cv2 as cv
import matplotlib.pyplot as plt

"""
img = cv.imread('arith.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('arith.jpg', cv.IMREAD_GRAYSCALE)

print(img.shape)

rows,cols=img.shape

startCol2=int(cols*.333)
endCol1=int(cols*.333)
endCol2=int(cols*.666)

marks_img=img[0:rows,0:endCol1]
photographer=img[0:rows,startCol2:endCol2]

cv.imwrite('marks.jpg',marks_img)
cv.imwrite('photographer.jpg',photographer)
"""

marks=cv.imread('marks.jpg',cv.IMREAD_GRAYSCALE)
photographer=cv.imread('photographer.jpg',cv.IMREAD_GRAYSCALE)
addition=cv.imread('marks.jpg',cv.IMREAD_GRAYSCALE)

print(marks.shape,photographer.shape)

rows2,cols2=marks.shape

c=0

for x in range(rows2):
    for y in range(cols2):
        add=int(marks.item(x,y)/2)+int(photographer.item(x,y)/2)+c
        if add>255: add=255
        addition.itemset((x,y),int(add))

#hist = cv.calcHist([marks],[0],None,[256],[0,256])
plt.subplot(1,3,1),plt.imshow(marks,'gray')
plt.subplot(1,3,2),plt.imshow(photographer,'gray')
plt.subplot(1,3,3),plt.imshow(addition,'gray')
#plt.subplot(1,2,2).hist(marks.ravel(),256,[0,256])
plt.show()
