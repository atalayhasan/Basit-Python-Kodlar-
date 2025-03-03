sayi = int(input("Bir sayı giriniz:"))

if sayi < 2:
    print(f"{sayi} sayısı asal değildir.")
elif sayi == 2:
    print(f"{sayi} sayısı asaldır.")
else:
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            print(f"{sayi} sayısı asal değildir.")
            break
    else:
        print(f"{sayi} sayısı asaldır.")
