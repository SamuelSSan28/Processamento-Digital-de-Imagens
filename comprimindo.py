import cv2

#Lista com o endereco das imagens para leitura
imagens = ["frames_video\com_Fecho_Convexo.png",
           "frames_video\com_Fecho_Convexo_na_Original.png",
           "frames_video\Esqueleto do fecho convexo.png",
           "frames_video\esqueleto_vermelho.png",
           "frames_video\sem_Buracos.png",
           "frames_video\sem_pontos.png",
           "frames_video\ fecho_vermelho.png",
           "frames_video\ vermelho.png"]

j = 1 #contador para salvar as imagens
for i in imagens:
    nome = "frames_video\Img" + str(j) + ".png" #variavel que guarda nome da imagem comrimida

    img = cv2.imread(i,1) #lendo a imagem original

    cv2.imwrite(nome,img,[16,3]) #salvando a imagem no formato png com a compressão RLE
    j+=1

