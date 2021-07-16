import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('arith.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('arith.jpg', cv.IMREAD_GRAYSCALE)

print(img.shape)

rows,cols=img.shape

startCol2=int(cols*.333)
endCol1=int(cols*.333)
endCol2=int(cols*.666)

marks_img=img[0:rows,0:endCol1]
photographer=img[0:rows,startCol2:endCol2]

cv.imwrite('marks_img.jpg',marks_img)
cv.imwrite('photgrapher.jpg',photographer)

print(marks_img.shape,photographer.shape)

rows2,cols2=marks_img.shape

for x in range(rows2):
    for y in range(cols2):
        add=(marks_img.item(x,y)+photographer.item(x,y))/2
        marks_img.itemset((x,y),add)

hist = cv.calcHist([marks_img],[0],None,[256],[0,256])
plt.subplot(2,2,1),plt.imshow(cv.cvtColor(marks_img, cv.COLOR_BGR2RGB))
plt.subplot(2,2,2).hist(marks_img.ravel(),256,[0,256])
plt.show()
