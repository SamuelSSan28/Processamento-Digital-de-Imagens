import numpy as np
import cv2

# leitura da imagem
img = cv2.imread('morfologia.png', 0)

median = cv2.medianBlur(img, 5)
ret, binaria = cv2.threshold(median, 200, 255, cv2.THRESH_BINARY)

# kernelD = np.ones((3,3), np.uint8)
kernel = np.ones((3, 3), np.uint8)

print(kernel)
erosao = cv2.erode(binaria, kernel, iterations=6)  # destaca partes pretas
dilatacao = cv2.dilate(erosao, kernel, iterations=5)

#encontrando os contornos
contours, hierarchy = cv2.findContours(dilatacao, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# crinado hull_array para os pontos do fecho convexo
hull = []
# calculando pontos para cada ponto de contorno
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))

# criando uma imagem preta
drawing = np.zeros((dilatacao.shape[0], dilatacao.shape[1], 3), np.uint8)

# # desenhando na imagem preta os contornos e hull points
for i in range(len(contours)):
    color = (255, 255, 255)  # cor pro fecho convexo
    # desenhando o fecho convexo na imagem preta
    cv2.drawContours(drawing, hull, i, color, 2, 8)

cv2.imwrite("Imagem3.png",drawing)

imgc =  cv2.imread('morfologia.png', 1)

for i in range(imgc.shape[0]):
    for j in range(imgc.shape[1]):
        rgb = drawing[i][j]
        if (i+5) < imgc.shape[0] and j+5 < imgc.shape[1]:
            rgb2 = imgc[i+5][j+5]
            if (rgb2[0] == 164):
                continue
        if (i - 10) < imgc.shape[0] and j - 10 < imgc.shape[1]:
            rgb2 = imgc[i - 5][j -5]
            if (rgb2[0] == 164):
                continue
        if (i + 10) < imgc.shape[0] and j - 10 < imgc.shape[1]:
            rgb2 = imgc[i + 5][j -5]
            if (rgb2[0] == 164):
                continue
        if (i - 10) < imgc.shape[0] and j + 10 < imgc.shape[1]:
            rgb2 = imgc[i - 5][j + 5]
            if (rgb2[0] == 164):
                continue
        if  rgb[0] == 255 and rgb[1] == 255 and rgb[2] == 255  and (i != 0 and i != 1 and j!=0 and j != 1
            and i!= (imgc.shape[0]-1) and j != (imgc.shape[1]-1) and i!= (imgc.shape[0]-2) and j != (imgc.shape[1]-2))  :
          imgc[i][j] = [0,50,48]

cv2.imwrite("frames_video\com_Fecho_Convexo_na_Original.png",imgc,[16,0])
cv2.imshow("skel", imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()