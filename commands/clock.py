from datetime import datetime

def saat(metin: str) -> str:
    metin = metin.lower()

    if "saat" in metin or "time" in metin:
        simdi = datetime.now()
        gunler = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        aylar = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
        tarih_str = f"{simdi.day} {aylar[simdi.month - 1]} {simdi.year}, {gunler[simdi.weekday()]}"
        return f"               Time {simdi.hour}:{simdi.minute:02d}\n{tarih_str}"
    
    elif ("tarih" in metin or "hangi gündeyiz" in metin or "kaçıncı gün" in metin or "ayın kaçı" in metin
          or "date" in metin or "day is it" in metin or "what day" in metin or "what's the date" in metin):
        simdi = datetime.now()
        gunler = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        aylar = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
        tarih_str = f"{simdi.day} {aylar[simdi.month - 1]} {simdi.year}, {gunler[simdi.weekday()]}"
        return f"Today:\n{tarih_str}"
    
    return None
