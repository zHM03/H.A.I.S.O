from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os

def kapatma_popup_ac(parent_widget):
    layout = BoxLayout(orientation='vertical', spacing=10, padding=15)

    bilgi_label = Label(text="Enter the time until shutdown:")
    saat_input = TextInput(hint_text="Hours", multiline=False, input_filter='int')
    dakika_input = TextInput(hint_text="Minutes", multiline=False, input_filter='int')

    butonlar = BoxLayout(size_hint_y=None, height="40dp", spacing=10)
    kapat_buton = Button(text="Shutdown", background_color=(1, 0, 0, 1))
    iptal_buton = Button(text="Cancel")

    popup = Popup(title="Scheduled Shutdown",
                  content=layout,
                  size_hint=(None, None), size=("400dp", "300dp"),
                  auto_dismiss=False)

    def kapat_callback(instance):
        try:
            saat = int(saat_input.text or 0)
            dakika = int(dakika_input.text or 0)
            toplam_saniye = saat * 3600 + dakika * 60

            if toplam_saniye <= 0:
                parent_widget.cevap = "Please enter a valid time."
                return

            os.system(f"shutdown /s /t {toplam_saniye}")
            parent_widget.cevap = f"The computer will shut down in {saat} hour(s) and {dakika} minute(s)."
            popup.dismiss()
        except Exception as e:
            parent_widget.cevap = f"An error occurred: {e}"
            popup.dismiss()

    def iptal_callback(instance):
        popup.dismiss()

    kapat_buton.bind(on_release=kapat_callback)
    iptal_buton.bind(on_release=iptal_callback)

    butonlar.add_widget(kapat_buton)
    butonlar.add_widget(iptal_buton)

    layout.add_widget(bilgi_label)
    layout.add_widget(saat_input)
    layout.add_widget(dakika_input)
    layout.add_widget(butonlar)

    popup.open()
