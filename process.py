import os
import json
import requests
from datetime import datetime

def hava_durumu_al():
    # Kaş hava durumu (En basit servis)
    try:
        url = "https://wttr.in/Kas?format=%C+%t"
        cevap = requests.get(url, timeout=10)
        return cevap.text.strip()
    except:
        return "Hava durumu su an alinamadi"

# 1. Dosyalari listele
try:
    dosyalar = os.listdir('./data')
except:
    dosyalar = ["data klasoru bulunamadi"]

# 2. Verileri paketle
veriler = {
    "tarih": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "hava": hava_durumu_al(),
    "liste": dosyalar
}

# 3. Kaydet
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(veriler, f, ensure_ascii=False, indent=4)

print("Mutfak hazir, veriler result.json'a yazildi!")
