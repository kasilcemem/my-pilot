import os
import json
import re
from datetime import datetime

def imla_duzelt(metin):
    if not metin: return ""
    metin = re.sub(r' +', ' ', metin).strip()
    metin = re.compile(r'([.!?]\s+)([a-zğüşıöç])').sub(lambda m: m.group(1) + m.group(2).upper(), metin)
    if len(metin) > 0:
        metin = metin[0].upper() + metin[1:]
    metin = re.sub(r'\s+([.!?])', r'\1', metin)
    return metin

def calistir():
    data_klasoru = 'data'
    ana_metin_yolu = os.path.join(data_klasoru, 'palemos.txt')
    onsoz_yolu = os.path.join(data_klasoru, 'onsoz.txt')
    
    tam_icerik = ""

    # 1. Önce Önsözü Oku ve Düzenle
    if os.path.exists(onsoz_yolu):
        with open(onsoz_yolu, 'r', encoding='utf-8', errors='ignore') as f:
            onsoz_ham = f.read()
            # "Dil" başlığını temizleyip "ÖNSÖZ" yapalım
            onsoz_temiz = re.sub(r'^dil\b', '', onsoz_ham, flags=re.IGNORECASE).strip()
            tam_icerik += "ÖNSÖZ\n\n" + imla_duzelt(onsoz_temiz) + "\n\n---\n\n"

    # 2. Sonra Ana Metni Oku ve Ekle
    if os.path.exists(ana_metin_yolu):
        with open(ana_metin_yolu, 'r', encoding='utf-8', errors='ignore') as f:
            ana_ham = f.read()
            tam_icerik += imla_duzelt(ana_ham)

    # Sayfalandırma (2000 karakterlik bloklar)
    sayfalar = re.findall(r'[\s\S]{1,2000}(?=\s|$)', tam_icerik) if tam_icerik else ["Metin bulunamadı."]
    
    sonuc = {
        "guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "palemos": {
            "baslik": "Palemos Arşivi (1600)",
            "sayfalar": sayfalar,
            "toplam_sayfa": len(sayfalar)
        }
    }

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    calistir()
