import os
import json
from datetime import datetime

def palemos_islem():
    yol = os.path.join('data', 'palemos.txt')
    
    if os.path.exists(yol):
        with open(yol, 'r', encoding='utf-8') as f:
            tam_metin = f.read()
            return {
                "baslik": "Palemos Belgesi",
                "icerik": tam_metin, # Tüm metni çekiyoruz
                "karakter": len(tam_metin),
                "durum": "Hazır"
            }
    return {"baslik": "Hata", "icerik": "Metin dosyası bulunamadı!", "durum": "Eksik"}

# Veriyi paketle
data = {
    "guncelleme": datetime.now().strftime("%H:%M - %d/%m/%Y"),
    "palemos": palemos_islem()
}

# Kaydet
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
