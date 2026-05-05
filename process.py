import os
import json
from datetime import datetime

# 1. Metin Okuma ve Düzenleme (Editör)
def metni_isle():
    dosya_yolu = './data/palemos.txt' # Dosyanın adını buraya yaz
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            metin = f.read()
            # Metnin ilk 500 karakterini özet olarak alalım
            ozet = metin[:500] + "..."
            karakter_sayisi = len(metin)
            return {"ozet": ozet, "uzunluk": karakter_sayisi}
    return {"ozet": "Dosya bulunamadı.", "uzunluk": 0}

# 2. Genel Bilgiler
dosyalar = os.listdir('./data')
palemos_verisi = metni_isle()

rapor = {
    "guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "toplam_dosya": len(dosyalar),
    "palemos_detay": palemos_verisi,
    "dosya_listesi": dosyalar
}

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(rapor, f, ensure_ascii=False, indent=4)
