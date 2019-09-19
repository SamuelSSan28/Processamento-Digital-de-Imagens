import cv2
import math
from Histogram_Class import Histograma as hist
import numpy as np

def calculaDiferenca(img1, img2):
  h,l = img1.shape[0],img1.shape[1]
  gray11 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  gray22 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  gray1 = hist.retorna_acumlada(hist,gray11)
  gray2 = hist.retorna_acumlada(hist,gray22)

  dif_pix = cv2.absdiff(gray22,gray11)

  for i in range(h):
    for j in range(l):
      #print(gray1[gray22[i][j]],gray2[gray22[i][j]],"-----")
      if gray1[gray22[i][j]] > 0:
        dif = gray1[gray22[i][j]] - gray2[gray22[i][j]]
        if dif < 0: dif=dif*-1

        if  dif > 290 and dif_pix[i][j] > 7:
          img2[i][j] = [0,0,255]


  return img2



img = cv2.imread('caneca10.jpeg',1) #leitura da Imagem
img2 = cv2.imread('caneca11.jpeg',1) #leitura da Imagem

#hist.exibe_histograma(hist,img)
#hist.exibe_histograma(hist,img2)

movimento= calculaDiferenca(img,img2)

cv2.imshow("oii", movimento)
cv2.waitKey(0)
cv2.destroyAllWindows()


