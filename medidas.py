import cv2
import numpy as np
from scipy import stats

#leitura das imagens
img1 = cv2.imread('WashingtonDC_01.tif',0)
img2 = cv2.imread('WashingtonDC_02.tif',0)

#desvio padrão
dp1 = img1.std()
dp2 = img2.std()
print("Desvio Padrão:\n Img1:{:.2f} Img2:{:.2f}\n".format(dp1,dp2))

#Variancia
var1 = (dp1)**2
var2 = (dp2)**2
print("Variancia:\n Img1:{:.2f} Img2:{:.2f}\n".format(var1,var2))

#media
media1 = img1.mean()
media2 = img2.mean()
print("Media: \n Img1:{:.2f} Img2:{:.2f}\n".format(media1,media2))

#moda
moda1 = stats.mode(img1,axis=None).mode[0]
moda2 = stats.mode(img2,axis=None).mode[0]
print("Moda: \n Img1:{:.2f} Img2:{:.2f}\n".format(moda1,moda2))

#mediana
mediana1 = np.median(img1)
mediana2 = np.median(img2)
print("Mediana:\n Img1:{:.2f} Img2:{:.2f}\n".format(mediana1,mediana2))

#covariancia
x =  img1.flatten() #transforma em uma matriz 1-D
y =  img2.flatten() #transforma em uma matriz 1-D
cov = np.cov(x,y)
print("Covariância:\n",cov)

#correlacao
corr = np.corrcoef(x,y)

print("\nCorrelação: {:.2f}".format(corr[0][1]))

