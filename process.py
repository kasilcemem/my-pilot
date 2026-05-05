import os
import json
from datetime import datetime

def calistir():
    yol = os.path.join('data', 'palemos.txt')
    icerik = "Metin okunamadı."
    karakter = 0
    
    if os.path.exists(yol):
        # Farklı dil kodlamalarını sırayla dene (UTF-8, Latin-1, Windows-1254)
        for kodlama in ['utf-8', 'latin-1', 'iso-8859-9', 'cp1254']:
            try:
                with open(yol, 'r', encoding=kodlama) as f:
                    icerik = f.read()
                    karakter = len(icerik)
                    break # Başarılı olursa döngüden çık
            except:
                continue
    else:
        icerik = "Hata: data/palemos.txt bulunamadı!"

    sonuc = {
        "guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "palemos": {
            "baslik": "Palemos Belgesi",
            "icerik": icerik,
            "karakter": karakter
        }
    }

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    calistir()
