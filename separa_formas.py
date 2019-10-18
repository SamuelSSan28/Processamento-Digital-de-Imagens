import numpy as np
import cv2

# leitura das imagens
img = cv2.imread('morfologia.png', 0)

median = cv2.medianBlur(img, 5)

ret, binaria = cv2.threshold(median, 200, 255, cv2.THRESH_BINARY)

# kernelD = np.ones((3,3), np.uint8)
kernel = np.ones((3, 3), np.uint8)

erosao = cv2.erode(binaria, kernel, iterations=6)  # destaca partes pretas
dilatacao = cv2.dilate(erosao, kernel, iterations=5)

blue = np.ones((img.shape[0], img.shape[0]), np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if dilatacao[i][j] == 0 and median[i][j] > 150:
            median[i][j] = median[i-100][j-100]


cv2.imshow("Output", dilatacao)
cv2.imshow("Original", median)
cv2.waitKey(0)
cv2.destroyAllWindows()