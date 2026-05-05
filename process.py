import os
import json
import re
from datetime import datetime

def imla_duzelt(metin):
    if not metin: return ""
    
    # 1. Gereksiz çift boşlukları ve satır başı/sonu boşluklarını temizle
    metin = re.sub(r' +', ' ', metin).strip()
    
    # 2. Nokta, soru işareti ve ünlemden sonra büyük harf kontrolü
    # Bu regex, işaretlerden sonra gelen ilk harfi bulur ve büyük yapar
    metin = re.compile(r'([.!?]\s+)([a-zğüşıöç])').sub(lambda m: m.group(1) + m.group(2).upper(), metin)
    
    # 3. Metnin en başındaki ilk harfi büyük yap
    if len(metin) > 0:
        metin = metin[0].upper() + metin[1:]
    
    # 4. Sık yapılan işaretleme hatalarını düzelt (noktadan önce boşluk varsa siler)
    metin = re.sub(r'\s+([.!?])', r'\1', metin)
    
    return metin

def calistir():
    yol = os.path.join('data', 'palemos.txt')
    icerik = ""
    
    if os.path.exists(yol):
        with open(yol, 'r', encoding='utf-8', errors='ignore') as f:
            ham_metin = f.read()
            # Otomatik İmla Düzeltme Burada Çalışıyor
            icerik = imla_duzelt(ham_metin)
    
    # Metni yaklaşık 2000 karakterlik sayfalara böl (Kitap formatı için)
    # Kelime bütünlüğünü bozmamak için boşluktan böler
    sayfalar = re.findall(r'[\s\S]{1,2000}(?=\s|$)', icerik) if icerik else ["Metin bulunamadı."]
    
    sonuc = {
        "guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "palemos": {
            "baslik": "Palemos Belgesi - 1600'ler Arşivi",
            "icerik": icerik, # Arama için tam metin
            "sayfalar": sayfalar,
            "toplam_sayfa": len(sayfalar),
            "karakter": len(icerik)
        }
    }

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    calistir()
