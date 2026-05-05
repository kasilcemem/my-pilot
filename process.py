import os
import json
import re
from datetime import datetime

def calistir():
    yol = os.path.join('data', 'palemos.txt')
    icerik = ""
    sayfalar = []
    
    if os.path.exists(yol):
        with open(yol, 'r', encoding='utf-8', errors='ignore') as f:
            icerik = f.read()
            
        # Metni [SAYFA X] ibarelerine göre böler
        ham_sayfalar = re.split(r'\[SAYFA \d+\]', icerik)
        # Boş sayfaları temizle ve listeye ekle
        sayfalar = [s.strip() for s in ham_sayfalar if s.strip()]
    
    if not sayfalar:
        sayfalar = [icerik if icerik else "Metin bulunamadı."]

    sonuc = {
        "guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "palemos": {
            "baslik": "Palemos Belgesi",
            "sayfalar": sayfalar,
            "toplam_sayfa": len(sayfalar)
        }
    }

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    calistir()
