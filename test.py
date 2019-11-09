import cv2 as cv
import numpy as np

img = cv.imread("Image1.png",0)


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         if img[i][j] == 255:
             img[i][j] = 0
         else:
            img[i][j] = 255

kernel = cv.getStructuringElement(cv.MORPH_RECT,(29,31))


output_image = cv.morphologyEx(img, cv.MORPH_HITMISS, kernel)

cv.imshow("Hit or Miss", output_image)
cv.waitKey(0)
cv.destroyAllWindows()