import os
import json
from datetime import datetime

# 1. Klasör ve Dosya Kontrolü
klasor = 'data'
dosya_adi = 'palemos.txt'
yol = os.path.join(klasor, dosya_adi)

# Eğer data klasörü yoksa oluştur
if not os.path.exists(klasor):
    os.makedirs(klasor)
    print(f"'{klasor}' klasörü oluşturuldu.")

# 2. Metni Oku
if os.path.exists(yol):
    with open(yol, 'r', encoding='utf-8') as f:
        icerik = f.read()
        durum = "Dosya başarıyla okundu"
else:
    icerik = "Henüz metin yüklenmedi. Lütfen data/palemos.txt dosyasını oluşturun."
    durum = "Dosya bulunamadı"

# 3. Sonucu Hazırla
data = {
    "guncelleme": datetime.now().strftime("%H:%M - %d/%m/%Y"),
    "palemos": {
        "baslik": "Palemos Belgesi",
        "icerik": icerik,
        "karakter": len(icerik),
        "durum": durum
    }
}

# 4. Kaydet
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("İşlem tamamlandı: result.json güncellendi.")
