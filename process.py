import os
import json
import requests
from datetime import datetime

# 1. Hava Durumu (Hata vermemesi için korumalı)
def hava_durumu_al():
    try:
        r = requests.get("https://wttr.in/Kas?format=%C+%t", timeout=10)
        return r.text.strip()
    except:
        return "Hava durumu su an alinamadi"

# 2. Palemos Metnini Oku (Klasör kontrolü ile)
def metin_oku():
    # Klasör ismini ve dosya ismini senin dediğin gibi kontrol ediyoruz
    dosya_yolu = os.path.join('data', 'palemos.txt')
    
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, 'r', encoding='utf-8') as f:
            icerik = f.read()
            return {
                "ozet": icerik[:1500] + "...", # İlk 1500 karakter
                "uzunluk": len(icerik)
            }
    else:
        # Eğer dosya ismi farklıysa (örneğin palemos.txt değil de palemos ise)
        return {"ozet": "Hata: data/palemos.txt dosyasi bulunamadi. Lutfen dosya adini kontrol edin.", "uzunluk": 0}

# 3. Raporu Hazırla
sonuc = {
    "tarih": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "hava": hava_durumu_al(),
    "palemos": metin_oku(),
    "liste": os.listdir('data') if os.path.exists('data') else []
}

# 4. Kaydet
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(sonuc, f, ensure_ascii=False, indent=4)

print("Islem basariyla tamamlandi.")
