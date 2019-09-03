from kivy.app import App
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
import cv2
import numpy as np
import gc


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    file = ''
    imagem = None

    def dismiss_popup(self):
        self._popup.dismiss()


    def gaussianBlur(self):
        if self.file == '':
            pass
        else:
            image = cv2.imread(self.file)
            gaussianBlur = cv2.GaussianBlur(image, (5, 5), 0)
            cv2.imshow('Gay Scale', gaussianBlur)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def gray_scale(self):
        if self.file == '':
            pass
        else:
            image = cv2.imread(self.file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Gay Scale', gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    def show_load(self): #mostrar explorador de arquivo
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        if self.imagem != None:
            self.ids.imagem.remove_widget(self.imagem)
        self.file = filename[0]
        self.imagem = im = Image(source=filename[0])
        cv2.imread(im.source)
        self.ids.imagem.add_widget(im)
        self.dismiss_popup()


class GUI(App):
    def build(self):
        return Root()


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
GUI().run()