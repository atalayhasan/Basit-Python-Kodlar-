ders_sayi = int(input("Kaç dersin notunu gireceksiniz? "))

toplam_not = 0
for i in range(ders_sayi):
    not_degeri = float(input(f"{i + 1}. dersin notunu girin: "))
    toplam_not += not_degeri

# Ortalamayı hesapla
ortalama = toplam_not / ders_sayi

# Geçip geçmediğini kontrol et
gecme_notu = 60  # Geçme notu belirliyoruz (örneğin 60)
if ortalama >= gecme_notu:
    print(f"Tebrikler! Ortalamanız {ortalama:.2f}. Geçtiniz.")
else:
    print(f"Maalesef ortalamanız {ortalama:.2f}. Kaldınız.")
