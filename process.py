import os
import json
import requests # İnternetten bilgi çekmek için
from datetime import datetime

# 1. Hava Durumu Bilgisi Alalım (Kaş için)
def hava_durumu_al():
    # Bu adres Kaş'ın hava durumunu veren ücretsiz bir servis
    url = "https://wttr.in/Kas?format=j1"
    try:
        cevap = requests.get(url)
        veri = cevap.json()
        derece = veri['current_condition'][0]['temp_C']
        durum = veri['current_condition'][0]['lang_tr'][0]['value']
        return f"{derece}°C, {durum}"
    except:
        return "Hava durumu bilgisi alınamadı."

# 2. Dosyalarımızı listeleyelim
dosyalar = os.listdir('./data')

# 3. Her şeyi birleştirelim
rapor = {
    "guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "kas_hava_durumu": hava_durumu_al(),
    "dosya_listesi": dosyalar
}

# 4. Kaydedelim
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(rapor, f, ensure_ascii=False, indent=4)

print("İşlem tamam: Hava durumu ve dosyalar kaydedildi!")
