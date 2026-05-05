import json

# Örnek sinyal verileri
data = [10, 25, 15, 40, 35, 60]

def analiz_et(liste):
    sonuclar = []
    for i in range(1, len(liste)):
        fark = liste[i] - liste[i-1]
        sonuclar.append({"nokta": i, "deger": liste[i], "fark": fark})
    return sonuclar

if __name__ == "__main__":
    analiz = analiz_et(data)
    with open("results.json", "w") as f:
        json.dump(analiz, f)
