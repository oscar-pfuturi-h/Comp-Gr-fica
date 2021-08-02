import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('gato.jpg', cv.IMREAD_UNCHANGED)
 
print('Dimensión original: ',img.shape)
 
scale_percent = 150 # Porcentaje
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized1 = cv.resize(img, dim, interpolation = cv.INTER_LINEAR)

resized2 = cv.resize(img, dim, interpolation = cv.INTER_NEAREST)

plt.title('Scores by group and gender')
plt.subplot(1,2,1),plt.imshow(cv.cvtColor(resized1,cv.COLOR_BGR2RGB)),plt.title('Interpolación de píxeles')
plt.subplot(1,2,2),plt.imshow(cv.cvtColor(resized2,cv.COLOR_BGR2RGB)),plt.title('Pixel replication shape: ')
plt.show()

 