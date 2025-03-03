from collections import Counter

def kelime_sayaci(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        metin = dosya.read().lower()

    kelimeler = metin.split()
    sayac = Counter(kelimeler)

    print(" En Çok Kullanılan Kelimeler:")
    for kelime, adet in sayac.most_common(10):
        print(f"{kelime}: {adet} kez")

# Kullanım
dosya = input("Analiz edilecek dosya adını girin (örneğin: metin.txt): ")
kelime_sayaci(dosya)
