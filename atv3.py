import cv2
import numpy as np
from skimage import  morphology

#leitura das imagens
img = cv2.imread('morfologia.png',0)

median = cv2.medianBlur(img,5)

ret,binaria = cv2.threshold(median,200,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((3,3), np.uint8)
kernel[1][1] = 0

print(kernel)
dilatacao = cv2.dilate(binaria, kernel, iterations=5)#destaca partes pretas

#img_dilation = cv2.dilate(img_erosion, kernel, iterations=1) #DESTACAR PARTES BRANCAS



cv2.imshow('test', dilatacao)

# Aguarda tecla para finalizar
cv2.waitKey(0)