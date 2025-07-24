from kivy.clock import Clock
import threading
import time

def _geri_sayim(mesaj, sure, callback):
    for i in range(sure, -1, -1):
        if callback:
            Clock.schedule_once(lambda dt, m=mesaj, s=i: callback(f"{m} {s}"))
        time.sleep(1)

def _nefes_egzersizi_thread(callback):
    adimlar = [
        ("Take a deep breath", 4),
        ("Hold your breath", 7),
        ("Exhale slowly", 8),
        ("Take a deep breath again", 4)
    ]

    time.sleep(2) 

    for mesaj, sure in adimlar:
        _geri_sayim(mesaj, sure, callback)

    if callback:
        Clock.schedule_once(lambda dt: callback("Do you feel better now?"))

def breath(metin: str, callback=None) -> str:
    lowered = metin.lower()
    if "nefes" in lowered or "breath" in lowered or "breathing" in lowered:
        threading.Thread(target=_nefes_egzersizi_thread, args=(callback,), daemon=True).start()
        return "Adjust your posture..."
    return None
