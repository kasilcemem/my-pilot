import os
import json
from datetime import datetime

# 1. Adım: Data klasöründeki dosyaları oku
dosyalar = os.listdir('./data')

# 2. Adım: Bilgileri birleştir (İndeksleme)
sonuc_verisi = {
    "guncelleme_tarihi": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "toplam_dosya": len(dosyalar),
    "dosya_listesi": dosyalar
}

# 3. Adım: Sonucu 'result.json' olarak kaydet
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(sonuc_verisi, f, ensure_ascii=False, indent=4)

print("Aşçı işini bitirdi: result.json hazır!")
