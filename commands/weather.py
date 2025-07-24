from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import requests

def hava_durumu_getir(sehir, callback):
    api_key = "7f1df4d02ef267fb2359c2305d0634e7"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric&lang=en"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            sicaklik = data['main']['temp']
            aciklama = data['weather'][0]['description']
            mesaj = f"The current temperature in {sehir.title()} is \n{sicaklik}°C, {aciklama}."
        else:
            mesaj = f"Weather information for {sehir.title()} could not be retrieved: {data.get('message', '')}"
    except Exception as e:
        mesaj = f"An error occurred while retrieving weather information: {e}"
    
    if callback:
        Clock.schedule_once(lambda dt: callback(mesaj))

def weather_popup_ac(root_widget):
    layout = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
    layout.bind(minimum_height=layout.setter('height'))

    input_sehir = TextInput(
        multiline=False,
        size_hint_y=None,
        height=40,
        hint_text="Please enter a city name.",
        font_size=16,
        padding=[10, 10, 10, 10],
        background_color=(0.95, 0.95, 0.95, 1),
        foreground_color=(0, 0, 0, 1),
        cursor_color=(0.2, 0.4, 0.7, 1),
        halign="left"
    )
    btn_gonder = Button(
        text="Get Weather",
        size_hint_y=None,
        height=45,
        background_color=(0.2, 0.5, 0.8, 1),
        color=(1, 1, 1, 1),
        font_size=16,
        bold=True
    )
    btn_iptal = Button(
        text="Cancel",
        size_hint_y=None,
        height=45,
        background_color=(0.8, 0.2, 0.2, 1),
        color=(1, 1, 1, 1),
        font_size=16,
        bold=True
    )
    btn_kutu = BoxLayout(size_hint_y=None, height=45, spacing=15)
    btn_kutu.add_widget(btn_gonder)
    btn_kutu.add_widget(btn_iptal)
    
    layout.add_widget(input_sehir)
    layout.add_widget(btn_kutu)
    
    popup = Popup(
        title="Weather Inquiry",
        content=layout,
        size_hint=(0.7, None),
        height=220,
        auto_dismiss=False,
        background_color=(0.9, 0.9, 1, 1)
    )
    
    def update_result(mesaj):
        root_widget.cevap = mesaj
    
    def gonder_callback(instance):
        sehir = input_sehir.text.strip()
        if not sehir:
            root_widget.cevap = "Please enter a city name."
            return
        popup.dismiss()
        hava_durumu_getir(sehir, callback=update_result)
    
    def iptal_callback(instance):
        popup.dismiss()
    
    btn_gonder.bind(on_release=gonder_callback)
    btn_iptal.bind(on_release=iptal_callback)
    
    popup.open()
