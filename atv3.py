import numpy as np
import cv2
from Compressao_Class import Compressao

# leitura da imagem
img = cv2.imread('morfologia.png', 0)

median = cv2.medianBlur(img, 5)
#cv2.imwrite("frames_video\sem_pontos.png", median,[16,0])

ret, binaria = cv2.threshold(median, 200, 255, cv2.THRESH_BINARY)

# kernelD = np.ones((3,3), np.uint8)
kernel = np.ones((3, 3), np.uint8)

print(kernel)
erosao = cv2.erode(binaria, kernel, iterations=6)  # destaca partes pretas
dilatacao = cv2.dilate(erosao, kernel, iterations=5)

#cv2.imwrite("frames_video\sem_Buracos.png", dilatacao,[16,0])
'''
# find contours
contours, hierarchy = cv2.findContours(dilatacao, cv2.RETR_TREE, \
                                            cv2.CHAIN_APPROX_SIMPLE)
# create hull array for convexHull points
hull = []
# calculate points for each contour
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))

# create an empty black image
drawing = np.zeros((dilatacao.shape[0], dilatacao.shape[1], 3), np.uint8)

# draw contours and hull points
for i in range(len(contours)):
    color_contours = (100, 255, 45)  # color for contours
    color = (255, 255, 255)  # color for convex hull
    # draw contours das formas da imagem
    cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
    # draw convex hull
    cv2.drawContours(drawing, hull, i, color, 2, 8)

#cv2.imwrite("frames_video\com_Fecho_Convexo.png", drawing,[16,0])

imgc =  cv2.imread('morfologia.png', 1)

for i in range(imgc.shape[0]):
    for j in range(imgc.shape[1]):
        rgb = drawing[i][j]
        if  rgb[0] == 255 and rgb[1] == 255 and rgb[2] == 255:
          imgc[i][j] = [0,50,48]

#cv2.imwrite("frames_video\com_Fecho_Convexo_na_Original.png", imgc,[16,0])
'''
img = img[0:102, 80:200]
img =  cv2.medianBlur(img, 5)
size = np.size(img)

#cv2.imwrite("frames_video\ vermelho.png", img,[16,0])
skel = np.zeros(img.shape, np.uint8)

ret, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
done = False

while (not done):
    eroded = cv2.erode(img, element)
    temp = cv2.dilate(eroded, element)
    temp = cv2.subtract(img, temp)
    skel = cv2.bitwise_or(skel, temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros == size:
        done = True


cv2.imwrite("frames_video\esqueleto_vermelho.png",skel,[16,0])
cv2.imshow("skel", skel)
cv2.waitKey(0)
cv2.destroyAllWindows()
