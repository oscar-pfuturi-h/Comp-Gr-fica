import cv2 
import numpy as np 
import matplotlib.pyplot as plt
camp = cv2.imread('camp.png') 
camp2 = cv2.imread('camp.png')
print(camp[50][50])
print(camp.shape)
for i in range ( len(camp) ):
	for j in range ( len(camp[i]) ):
		if( 
		(camp[i][j][2] < 240 and camp[i][j][2] > 190) and 
		(camp[i][j][1] < 200 and camp[i][j][1] > 160) and 
		(camp[i][j][0] < 180 and camp[i][j][0] > 140)):
			camp[i][j][0]=255
			camp[i][j][1]=255
			camp[i][j][2]=255
		else:
			camp[i][j][0]=0
			camp[i][j][1]=0
			camp[i][j][2]=0

plt.subplot(1,2,1),plt.imshow(cv2.cvtColor(camp2, cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2),plt.imshow(camp)
plt.show()
