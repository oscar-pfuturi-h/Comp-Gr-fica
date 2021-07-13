import cv2
from matplotlib import pyplot as plt

img=cv2.imread('contr2_1.jpg', cv2.IMREAD_GRAYSCALE)

for x in range(15):
    for y in range(15):
        img.itemset((x, y), 0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow('hist',hist)
plt.subplot(1,2,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2).hist(img.ravel(),256,[0,256])
plt.show()

cv2.imwrite('outlayer.jpg',img)
