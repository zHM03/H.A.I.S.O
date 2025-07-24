from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
from datetime import datetime

from commands.clock import saat
from commands.calculator import hesap_makinesi_popup_ac
from commands.reminder import hatirlatici_popup_ac
from commands.weather import weather_popup_ac
from commands.breath import breath
from commands.cleaner import clean
from commands.shutdown import kapatma_popup_ac

class AsistanEkrani(BoxLayout):
    kullanici_metni = StringProperty("")
    cevap = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kullanici_metni = self.saat_bazli_selamlama()
        
    def hatirlatici_popup_ac(self):
        print("Reminder popup opened")
        hatirlatici_popup_ac(self)

    def hesap_makinesi_popup_ac(self):
        print("Calculator popup opened")
        hesap_makinesi_popup_ac(self)

    def kapatma_popup_ac(self):
        print("Shutdown popup opened")
        kapatma_popup_ac(self)
        
    def weather_popup_ac(self):
        print("Weather popup opened")
        weather_popup_ac(self)

    def saat_bazli_selamlama(self):
        saat_ = datetime.now().hour
        if saat_ < 6:
            return "Good night!"
        elif saat_ < 12:
            return "Good morning!"
        elif saat_ < 18:
            return "Good day!"
        else:
            return "Good evening!"

    def yazili_girdi_isle(self, metin):
        metin = metin.strip()
        self.kullanici_metni = metin
        self.cevap = ""

        cevap = self.komut_calistir(metin, callback=self.guncelle_cevap)

        if not cevap:
            self.cevap = "I didn't understand."
        elif cevap != "Nefes egzersizi başladı...":  # Eğer nefes egzersizi mesajı varsa orijinal bırakılmış
            self.cevap = cevap

    def guncelle_cevap(self, mesaj):
        Clock.schedule_once(lambda dt: setattr(self, 'cevap', mesaj))

    def komut_calistir(self, metin, callback=None):
        # Metinle çalışan fonksiyonlar (cevap döndürürler)
        cevap_komutlar = [
            lambda m: breath(m, callback=callback) if callback else None,
            saat,
            clean,
            # Hesap makinesi komutu özel çünkü popup açıyor ama koşul var
            lambda m: hesap_makinesi_popup_ac(self) or "Calculator opened" if "hesap makinesi" in m.lower() else None,
        ]

        for komut in cevap_komutlar:
            sonuc = komut(metin)
            if sonuc:
                return sonuc

        # Popup açan komutları metin bazlı tetikle
        if "hava" in metin.lower() or "weather" in metin.lower():
            self.weather_popup_ac()
            return "Weather popup opened"
        
        if "hatırlatıcı" in metin.lower() or "reminder" in metin.lower():
            self.hatirlatici_popup_ac()
            return "Reminder popup opened"
        
        if "kapat" in metin.lower() or "shutdown" in metin.lower():
            self.kapatma_popup_ac()
            return "Shutdown popup opened"

        return None
