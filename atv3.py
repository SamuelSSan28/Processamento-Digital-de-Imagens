import numpy as np
import cv2

#leitura das imagens
img = cv2.imread('morfologia.png',0)

median = cv2.medianBlur(img,5)

ret,binaria = cv2.threshold(median,200,255,cv2.THRESH_BINARY)

#kernelD = np.ones((3,3), np.uint8)
kernel = np.ones((3,3), np.uint8)

print(kernel)
dilatacao = cv2.erode(binaria, kernel , iterations=6)#destaca partes pretas
dilatacao = cv2.dilate(dilatacao,kernel, iterations=5)

kernel = np.ones((21,21), np.uint8)

for i in range(kernel.shape[0]):
    for j in range(kernel.shape[1]):
        if i + j == i or i+j == j or i == 20 or j == 20 or i == 1 or j ==1 or i == 19 or j == 19 or i == 18 or j == 18:
                kernel[i][j] = 1
        else:
            kernel[i][j] = -1

for i in range(dilatacao.shape[0]):
    for j in range(dilatacao.shape[1]):
        if dilatacao[i][j] == 0:
                dilatacao[i][j] = 255
        else:
            dilatacao[i][j] = 0

output_image = cv2.morphologyEx(dilatacao, cv2.MORPH_HITMISS, kernel)

cv2.imshow("Kernel", kernel)

cv2.imshow("Hit or Miss", output_image)
cv2.moveWindow("Hit or Miss", 500, 200)

cv2.imshow("Origem", dilatacao)
cv2.waitKey(0)
cv2.destroyAllWindows()







