import os
import sys
from kivy.config import Config
from kivy.lang import Builder
from kivy.app import App

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '600')

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # PyInstaller'dan paketlendiğinde _MEIPASS klasörü içinde olur
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

kv_path = resource_path("ui.kv")
Builder.load_file(kv_path)

from ui import AsistanEkrani

class AsistanApp(App):
    def build(self):
        self.icon = resource_path("assets/icon.ico")
        return AsistanEkrani()

if __name__ == "__main__":
    try:
        AsistanApp().run()
    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()
