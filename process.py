import os
import json
import requests
from datetime import datetime

def hava_durumu_al():
    try:
        url = "https://wttr.in/Kas?format=%C+%t"
        cevap = requests.get(url, timeout=10)
        return cevap.text.strip()
    except:
        return "Hava durumu alınamadı"

def palemos_oku():
    yol = './data/palemos.txt'
    if os.path.exists(yol):
        with open(yol, 'r', encoding='utf-8') as f:
            metin = f.read()
            # Metnin başından bir parça alalım (ilk 1000 karakter)
            return {
                "ozet": metin[:1000] + "...",
                "uzunluk": len(metin),
                "durum": "Dosya okundu"
            }
    return {"ozet": "Henüz metin yüklenmemiş.", "uzunluk": 0, "durum": "Eksik"}

# Verileri topla
veriler = {
    "tarih": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "hava": hava_durumu_al(),
    "palemos": palemos_oku(),
    "liste": os.listdir('./data') if os.path.exists('./data') else []
}

# Kaydet
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(veriler, f, ensure_ascii=False, indent=4)
