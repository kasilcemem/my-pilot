import os
import json
import re
from datetime import datetime

def imla_ve_ozel_duzeltme(metin):
    if not metin: return ""
    
    # 1. "Dil Yazısı" ibaresini "ÖNSÖZ" olarak değiştir
    # (Büyük/küçük harf duyarlılığını ortadan kaldırmak için re.IGNORECASE kullanıyoruz)
    metin = re.sub(r'dil yazısı', 'ÖNSÖZ', metin, flags=re.IGNORECASE)
    
    # 2. Gereksiz çift boşlukları temizle
    metin = re.sub(r' +', ' ', metin).strip()
    
    # 3. Nokta, soru işareti ve ünlemden sonra büyük harf kontrolü
    metin = re.compile(r'([.!?]\s+)([a-zğüşıöç])').sub(lambda m: m.group(1) + m.group(2).upper(), metin)
    
    # 4. Metnin en başındaki ilk harfi büyük yap
    if len(metin) > 0:
        metin = metin[0].upper() + metin[1:]
    
    # 5. İşaretlerden önceki boşlukları sil
    metin = re.sub(r'\s+([.!?])', r'\1', metin)
    
    return metin

def calistir():
    yol = os.path.join('data', 'palemos.txt')
    icerik = ""
    
    if os.path.exists(yol):
        with open(yol, 'r', encoding='utf-8', errors='ignore') as f:
            ham_metin = f.read()
            # Hem imla düzelir hem de "Dil Yazısı" -> "ÖNSÖZ" olur
            icerik = imla_ve_ozel_duzeltme(ham_metin)
    
    # 2000 karakterde bir sayfalandır
    sayfalar = re.findall(r'[\s\S]{1,2000}(?=\s|$)', icerik) if icerik else ["Metin yüklenirken bir hata oluştu."]
    
    sonuc = {
        "guncelleme": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "palemos": {
            "baslik": "Palemos Arşivi",
            "icerik": icerik,
            "sayfalar": sayfalar,
            "toplam_sayfa": len(sayfalar)
        }
    }

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    calistir()
