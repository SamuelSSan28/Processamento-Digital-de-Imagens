import numpy as np
import cv2

# leitura das imagens
img = cv2.imread('morfologia.png', 0)

median = cv2.medianBlur(img, 5)

ret, binaria = cv2.threshold(median, 200, 255, cv2.THRESH_BINARY)

# kernelD = np.ones((3,3), np.uint8)
kernel = np.ones((3, 3), np.uint8)

print(kernel)
erosao = cv2.erode(binaria, kernel, iterations=6)  # destaca partes pretas
dilatacao = cv2.dilate(erosao, kernel, iterations=5)


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
    # draw contours
    cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
    # draw convex hull
    cv2.drawContours(drawing, hull, i, color, 2, 8)

cv2.imshow("Output", drawing)

cv2.waitKey(0)
cv2.destroyAllWindows()

size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

ret, img = cv2.threshold(img, 127, 255, 0)
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

cv2.imshow("skel", skel)
cv2.waitKey(0)
cv2.destroyAllWindows()