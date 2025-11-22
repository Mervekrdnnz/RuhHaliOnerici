import pandas as pd
import os
import shutil
from datetime import datetime

# Excel dosya adı
excel_dosya = "gecmis_log.xlsx"

# Eğer eski log varsa yedekle ve temiz bir log oluştur
if os.path.exists(excel_dosya):
    # yedek dosya adı: gecmis_log_backup_YYYYMMDD_HHMMSS.xlsx
    yedek_adi = f"gecmis_log_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    try:
        shutil.move(excel_dosya, yedek_adi)
        print(f"Eski log dosyası yedeklendi -> {yedek_adi}")
    except Exception as e:
        print(f"Uyarı: eski log dosyası yedeklenirken hata: {e}")
else:
    print("Eski log dosyası bulunamadı — yeni temiz log oluşturulacak.")

# Şimdi temiz DataFrame oluştur (boş log)
df = pd.DataFrame(columns=["tarih", "ruh_hali", "müzik", "aktivite", "mesaj"])

# (Aşağıya mevcut programının geri kalanını ekle)
# Örneğin: ruh halı sözlükleri, kullanıcı etkileşimi ve kayıt kodu...
# Buraya mevcut kodunu yapıştırabilirsin; örnek devam aşağıdaki gibidir:

# örnek basit veri (kendi mevcut kodunu buraya taşı)
ruh_emoji = {
    "mutlu": "😊",
    "üzgün": "😢",
    "stresli": "😰",
    "yorgun": "😴",
    "heyecanlı": "🤩",
    "sakin": "🧘",
    "motivasyonlu": "💪",
    "kızgın": "😡",
    "endişeli": "😟"
}

oneri_muzik = {
    "mutlu": "Happy - Pharrell Williams",
    "üzgün": "Fix You - Coldplay",
    "stresli": "Weightless - Marconi Union",
    "yorgun": "Lovely - Billie Eilish",
    "heyecanlı": "Can't Hold Us - Macklemore",
    "sakin": "Weightless - Marconi Union",
    "motivasyonlu": "Stronger - Kanye West",
    "kızgın": "Let It Be - Beatles",
    "endişeli": "Breathe Me - Sia"
}

oneri_aktivite = {
    "mutlu": "Müzik aç ve dans et",
    "üzgün": "Yürüyüş yapmak",
    "stresli": "Nefes egzersizi",
    "yorgun": "Biraz dinlenmek",
    "heyecanlı": "Hedeflerini yazmak",
    "sakin": "Meditasyon yapmak",
    "motivasyonlu": "Hedeflerini gözden geçirmek",
    "kızgın": "Derin nefes egzersizi",
    "endişeli": "Günlük yazmak"
}

motivasyon_mesaji = {
    "mutlu": "Bu enerjiyle her şey daha güzel olacak! ✨",
    "üzgün": "Her şey daha iyi olacak, biraz sabret 💪",
    "stresli": "Derin bir nefes al, her şey kontrol altında 🌿",
    "yorgun": "Kendine zaman ver, dinlenmeyi hak ediyorsun 🛌",
    "heyecanlı": "Bu heyecan seni ileri taşıyacak! ⚡",
    "sakin": "Ruhunu dinlendir, huzur seninle 🌿",
    "motivasyonlu": "Şimdi harekete geçme zamanı! 💥",
    "kızgın": "Sakin ol, nefes al ve devam et 😤",
    "endişeli": "Her şey yoluna girecek, güven 😊"
}

# Basit etkileşim döngüsü (kendi detaylarını buraya geri taşı)
while True:
    kullanici_ruh = input("Ruh halinizi girin (Mutlu, Üzgün, Stresli, Yorgun, Heyecanlı, Sakin, Motivasyonlu, Kızgın, Endişeli): ").lower()
    if kullanici_ruh not in oneri_muzik:
        print("Geçersiz ruh hali! Lütfen doğru bir ruh hali yazın.")
        continue

    muzik = oneri_muzik[kullanici_ruh]
    aktivite = oneri_aktivite[kullanici_ruh]
    mesaj = motivasyon_mesaji[kullanici_ruh]

    print(f"\nRuh Haliniz: {kullanici_ruh.capitalize()} {ruh_emoji[kullanici_ruh]}")
    print(f"Önerilen Müzik: {muzik}")
    print(f"Önerilen Aktivite: {aktivite}")
    print(f"Motivasyon Mesajı: {mesaj}\n")

    # Excel'e ekle
    yeni_satir = pd.DataFrame({
        "tarih": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "ruh_hali": [kullanici_ruh],
        "müzik": [muzik],
        "aktivite": [aktivite],
        "mesaj": [mesaj]
    })
    df = pd.concat([df, yeni_satir], ignore_index=True)
    df.to_excel(excel_dosya, index=False)

    print("✔ Öneri kaydedildi (yeni temiz gecmis_log.xlsx).\n")

    devam = input("Başka bir ruh hali denemek ister misiniz? (E/H): ").lower()
    if devam != "e":
        print("Programdan çıkılıyor. Hoşça kal!")
        break