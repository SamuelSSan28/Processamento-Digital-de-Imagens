import numpy as np
from matplotlib import pyplot as plt
import cv2

class Histograma:
    def __init__(self):
        pass

    def exibe_histograma(self,img):
        hist, bins = np.histogram(img.flatten(), 256, [0, 256])  # calculando histograma

        aculmulada = hist.cumsum()
        aculmulada_normalized = aculmulada * hist.max() / aculmulada.max()

        # plt.plot(aculmulada_normalized, color = 'b')#linha  no grafico
        plt.hist(img.flatten(), 256, [0, 256], color='r')
        plt.xlim([0, 256])
        plt.legend(('Frequencia dos Pixels', ''), loc='upper left')
        plt.show()

    def exibe_histogramaC(self,img):
        #bgr
        blue = cv2.calcHist(img, [0], None, [256], [0, 256])
        plt.plot(blue, color='b')
        plt.xlim([0, 256])

        green = cv2.calcHist(img,[1],None,[256],[0,256])
        plt.plot(green, color='g')
        plt.xlim([0, 256])

        red = cv2.calcHist(img,[2],None,[256],[0,256])
        plt.plot(red, color='r')
        plt.xlim([0, 256])

        plt.title('Histogram for color scale picture')
        plt.show()

    def retorna_acumlada(self,img):
        h = np.histogram(img.flatten(), 256, [0, 256])  # calculando histograma
        return h[0]

    def retorna_frequenciaC(self,img):
        blue = cv2.calcHist(img, [0], None, [256], [0, 256])
        green = cv2.calcHist(img, [1], None, [256], [0, 256])
        red = cv2.calcHist(img, [2], None, [256], [0, 256])
        return [red,green,blue]