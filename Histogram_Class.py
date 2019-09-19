import numpy as np
from matplotlib import pyplot as plt

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

    def retorna_acumlada(self,img):
        h = np.histogram(img.flatten(), 256, [0, 256])  # calculando histograma
        return h[0]
