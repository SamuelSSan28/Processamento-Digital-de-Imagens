import numpy as np
import cv2

# leitura das imagens
img = cv2.imread('morfologia.png', 1)
red = img[0:100, 80:200]

for i in range(red.shape[0]):
    for j in range(red.shape[1]):
        rgb = red[i][j]
        if not (rgb[0] == 36 and rgb[1] == 28 and rgb[2] == 237):
            red[i][j] = [255, 255, 255]

red_gray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
size = np.size(red_gray)
skel = np.zeros(red_gray.shape, np.uint8)

ret, img = cv2.threshold(red_gray, 127, 255, cv2.THRESH_BINARY_INV)
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


cv2.imwrite("skel.png", skel)
cv2.imshow("kkkk",skel)
cv2.waitKey(0)
cv2.destroyAllWindows()

