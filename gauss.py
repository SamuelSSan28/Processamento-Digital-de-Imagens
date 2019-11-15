import cv2
from Histogram_Class import Histograma as hist

img_ruidosa = cv2.imread('blobs.tif',0) # Lendo imagem ruidosa
img_pintada = cv2.imread('blobs2.tif',0) # Lendo imagem pintada no Gimp
hist.exibe_histograma(hist,img_ruidosa,"Imagem com Ruído")

img_gaussBlur = cv2.medianBlur(img_ruidosa,5) # aplicando filtro gausiano na imagem
#cv2.imwrite("final_gaussBlur.png",img_gaussBlur,[16,0])#Salvando a imagem
hist.exibe_histograma(hist,img_gaussBlur,"Imagem sem Ruído (GaussianBlur)")

ret,img_limiarizada = cv2.threshold(img_gaussBlur,140,255,cv2.THRESH_BINARY) #limiarizando a imagem
#cv2.imwrite("final_limiarizada1.png",img_limiarizada,[16,0])#Salvando a imagem

result = img_pintada - img_limiarizada # subtraindo imagem pintada com o resultado da limiarização
cv2.imwrite("final_diferencaMedian.png",result,[16,0])#Salvando a imagem

x,y = result.shape[0],result.shape[1] #pegando largura e altura da imagem
cont = 0 #inicializando o contador

for i in range(x):
    for j in range(y):
        if result[i][j] != 0:
            cont += 1
            result[i][j] = 255

print("Pixels Errados:",cont)
print("Tamanho da Imagem",x*y)
print("Porcentagem de acerto",(1 - (cont/(x*y)))*100,"%")