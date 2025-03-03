import random
import string

def sifre_olustur(uzunluk=12):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

print("🔒 Rastgele Şifre Oluşturucu")
uzunluk = int(input("Şifre uzunluğunu girin: "))
print(f"Oluşturulan Şifre: {sifre_olustur(uzunluk)}")
