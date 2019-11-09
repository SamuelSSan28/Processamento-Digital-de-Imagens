import numpy as np
import cv2

huul = cv2.imread('Imagem4.png', 0)
red2 = huul[10:99, 87:180]
red2 = cv2.medianBlur(red2,5)

cv2.imwrite("pb.png",red2)

for i in range(red2.shape[0]):
    for j in range(red2.shape[1]):
        if i+5 < red2.shape[0] and j+5 < red2.shape[0]:
            if red2[i][j] == 91 and red2[i+2][j+2] == 255 and red2[i+1][j+1] != 0  :
                red2[i+2][j+2] = 91


red2 = cv2.medianBlur(red2,5)
red2 = cv2.medianBlur(red2,5)

cv2.imwrite("Fecho preechido.png",red2)

img = red2
#binrizando o inverso
for i in range(red2.shape[0]):
    for j in range(red2.shape[1]):
         if img[i][j] == 255:
             img[i][j] = 0
         else:
            img[i][j] = 255

cv2.imwrite("frames_video\ fecho_vermelho.png",red2,[16,0])
size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

cv2.imshow("ll", img)
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

cv2.imwrite("frames_video\Esqueleto do fecho convexo.png",skel,[16,0])
cv2.imshow("skel", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



