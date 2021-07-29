import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

def Translation(X,Y):
    N=np.array([[1.,0.,X],[0.,1.,Y]])
    return N

def Scale(X,Y):
    N=np.array([[X,0.,0],[0.,Y,0]])
    return N

def Rotate(angulo,rows,cols):
    N=np.array([[math.cos(angulo), math.sin(angulo), (1-math.cos(angulo))*cols/2 - math.sin(angulo)*rows/2],
                [-math.sin(angulo), math.cos(angulo), math.sin(angulo)*cols/2 + (1-math.cos(angulo))*rows/2]])
    return N

def Shear(X1,X2,Y1,Y2):
    N=np.array([[X1,Y1,0],
                [X2,Y2,0]])
    return N

img=cv.imread('tigre.jpg',cv.IMREAD_COLOR)
rows,cols,ch=img.shape

#M = Translation(75,150)
#M = Scale(0.5,0.8)
#M = Rotate(math.pi/3,rows,cols)
M = Shear(0.2,0.9,0.5,0.5)
img2=cv.warpAffine(img, M, (cols, rows))

plt.subplot(1,2,1),plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB)),plt.title('Original')
plt.subplot(1,2,2),plt.imshow(cv.cvtColor(img2,cv.COLOR_BGR2RGB)),plt.title('Modified')
plt.show()
