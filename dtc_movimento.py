import cv2import mathfrom Histogram_Class import Histograma as histimport numpy as npdef calculaDiferencaG(img1, img2):  h,l = img1.shape[0],img1.shape[1]  gray11 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  gray22 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  gray1 = hist.retorna_acumlada(hist,gray11)  gray2 = hist.retorna_acumlada(hist,gray22)  dif_pix = cv2.absdiff(gray22,gray11)  for i in range(h):    for j in range(l):      dif = gray1[gray22[i][j]] - gray2[gray22[i][j]]      if dif < 0: dif = dif*-1      if  dif > 75 and dif_pix[i][j] > 10:        img2[i][j] = [0,0,255]  cv2.imshow("oii", img2)  cv2.waitKey(0)  cv2.destroyAllWindows()  return img2def verifica_novo_px(hist,rgb):  r,g,b = rgb[0],rgb[1],rgb[2]  r = hist[0][r] > 0  g = hist[1][g] > 0  b = hist[2][b] > 0  return r or g or bdef calculaDiferencaC(img1, img2):  h,l = img1.shape[0],img1.shape[1]  acc1 = hist.retorna_acumladaC(hist,img1)  acc2 = hist.retorna_acumladaC(hist,img2)  dif_freq = []  dif_pixel = []  for i in range(h):    for j in range(l):      rgb1 = img2[i][j]      rgb2 = img1[i][j]      #print((acc1[2][int(rgb2[2])]  - acc2[2][int(rgb2[2])]))      if (int(rgb1[2]) - int(rgb2[2])) > 45 and acc2[2][int(rgb1[2])]  - acc1[2][int(rgb2[2])] < 15:       img2[i][j] = [0, 0, 255]      if (int(rgb1[0]) - int(rgb2[0])) > 80 and (acc1[0][int(rgb1[0])] - acc2[0][int(rgb2[0])]) < 83:       img2[i][j] = [0, 0, 255]      #if (int(rgb1[1]) - int(rgb2[1])) < 1 and (acc2[1][int(rgb2[1])] - acc1[1][int(rgb1[1])]) >0:       img2[i][j] = [0, 0, 255]  cv2.imshow("oii", img2)  cv2.waitKey(0)  cv2.destroyAllWindows()  return img2img = cv2.imread('caneca101.jpg',1) #leitura da Imagemimg2 = cv2.imread('caneca102.jpg',1) #leitura da Imagemimg2 = calculaDiferencaC(img,img2)#hist.exibe_histogramaC(hist,img)#hist.exibe_histogramaC(hist,img2)