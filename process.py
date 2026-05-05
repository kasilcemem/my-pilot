import os
import json
import requests
from datetime import datetime

def hava_durumu_al():
    try:
        r = requests.get("https://wttr.in/Kas?format=%C+%t", timeout=10)
        return r.text.strip()
    except:
        return "Hava durumu alınamadı"

def metin_oku():
    # Klasör ismini kontrol edelim (Büyük/Küçük harf duyarlıdır!)
    klasor = 'data'
    dosya_adi = 'palemos.txt'
    yol = os.path.join(klasor, dosya_adi)
    
    if os.path.exists(yol):
        try:
            with open(yol, 'r', encoding='utf-8') as f:
                icerik = f.read()
                return {"ozet": icerik[:1500] + "...", "uzunluk": len(icerik), "hata": "Yok"}
        except Exception as e:
            return {"ozet": f"Dosya okuma hatası: {str(e)}", "uzunluk": 0, "hata": "Okuma Hatası"}
    else:
        # Klasördeki gerçek dosyaları listeleyelim ki hatayı anlayalım
        mevcut_dosyalar = os.listdir(klasor) if os.path.exists(klasor) else "Klasör yok"
        return {
            "ozet": f"Hata: {dosya_adi} bulunamadı. Mevcut dosyalar: {mevcut_dosyalar}",
            "uzunluk": 0, 
            "hata": "Dosya Yok"
        }

# Raporu oluştur
rapor = {
    "tarih": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "hava": hava_durumu_al(),
    "palemos": metin_oku()
}

# Kaydet
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(rapor, f, ensure_ascii=False, indent=4)

print("İşlem başarıyla tamamlandı (Hatalar yakalandı).")
