import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('canecas2.jpg',0) #leitura da Imagem

hist,bins = np.histogram(img.flatten(),256,[0,256]) #calculando histograma

aculmulada = hist.cumsum()
aculmulada_normalized = aculmulada * hist.max()/ aculmulada.max()

#plt.plot(aculmulada_normalized, color = 'b')#linha  no grafico
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('Frequencia dos Pixels',''), loc = 'upper left')
plt.show()

'''
equ = cv2.equalizeHist(img) #equalizando a imagem
res = np.hstack((img,equ)) #colocando as imagens lado a lado
cv2.imshow('res.png',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''