import os
import json
from datetime import datetime

# Klasördeki dosyaları bulalım
dosyalar = os.listdir('./data')

# Bilgileri paketleyelim
indeks = {
    "son_guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "dosyalarim": dosyalar
}

# Sonucu 'result.json' dosyasına yazalım
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(indeks, f, ensure_ascii=False, indent=4)
