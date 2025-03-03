import random

# Rastgele sayı seç
sayi = random.randint(1, 100)

print("1 ile 100 arasında bir sayı tahmin edin! 5 tahmin hakkınız var.")

tahmin_hakki = 5  # Maksimum tahmin hakkı

for deneme in range(1, tahmin_hakki + 1):
    tahmin = int(input(f"\n{deneme}. tahmininizi girin: "))

    if tahmin == sayi:
        print(f"TEKRİKLER! {deneme}. denemede doğru tahmini buldunuz!")
        break
    elif tahmin > sayi:
        print(" Daha küçük bir sayı girin!")
    else:
        print("Daha büyük bir sayı girin!")

    kalan_hak = tahmin_hakki - deneme
    if kalan_hak > 0:
        print(f" Kalan hakkınız: {kalan_hak}")
    else:
        print(f"Üzgünüm, hakkınız bitti! Doğru sayı: {sayi}")
