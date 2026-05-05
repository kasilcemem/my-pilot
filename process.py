import os
import json
from datetime import datetime

def calistir():
    # Dosya yollarını tanımla
    yol = os.path.join('data', 'palemos.txt')
    
    # Varsayılan içerik
    icerik = "Metin okunamadı."
    karakter = 0
    
    # Dosyayı oku
    if os.path.exists(yol):
        try:
            with open(yol, 'r', encoding='utf-8') as f:
                icerik = f.read()
                karakter = len(icerik)
        except Exception as e:
            icerik = f"Okuma hatası: {str(e)}"
    else:
        icerik = "Hata: data/palemos.txt bulunamadı!"

    # Sonuçları hazırla
    sonuc = {
        "guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "palemos": {
            "baslik": "Palemos Belgesi",
            "icerik": icerik,
            "karakter": karakter
        }
    }

    # result.json dosyasına yaz
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    calistir()
