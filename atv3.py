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
for i in range(h):
    for j in range(l):
        if dilatacao[i][j] == 0:
            dilatacao[i][j] = 255
        else:
            dilatacao[i][j] = 0

kernel = kernel = np.ones((11,11), np.uint8)
h,l = dilatacao.shape

for i in range(h):
    for j in range(l):
        if dilatacao[i][j] == 0:
            dilatacao[i][j] = 255
        else:
            dilatacao[i][j] = 0
output_image = cv2.morphologyEx(dilatacao, cv2.MORPH_HITMISS, kernel)


rate = 50
kernel = (kernel + 1) * 127
kernel = np.uint8(kernel)
kernel = cv2.resize(kernel, None, fx = rate, fy = rate, interpolation = cv2.INTER_NEAREST)

cv2.imshow("kernel", kernel)
cv2.moveWindow("kernel", 0, 0)

cv2.imshow("Hit or Miss", output_image)
cv2.moveWindow("Hit or Miss", 500, 200)

cv2.imshow("Origem", dilatacao)
cv2.waitKey(0)
cv2.destroyAllWindows()
