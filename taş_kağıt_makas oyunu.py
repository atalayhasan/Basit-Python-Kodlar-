import random

def bilgisayar_secimi():
    secimler = ["taş", "kağıt", "makas"]
    return random.choice(secimler)

def kazanan_belirle(kullanici, bilgisayar):
    if kullanici == bilgisayar:
        return "Berabere!"
    elif (kullanici == "taş" and bilgisayar == "makas") or \
         (kullanici == "kağıt" and bilgisayar == "taş") or \
         (kullanici == "makas" and bilgisayar == "kağıt"):
        return "Kullanıcı kazandı!"
    else:
        return "Bilgisayar kazandı!"

def oyun():
    while True:
        kullanici_secimi = input("Taş, Kağıt, Makas? (Çıkmak için 'q' ya basın): ").lower()
        if kullanici_secimi == 'q':
            print("Oyun bitti!")
            break
        if kullanici_secimi not in ["taş", "kağıt", "makas"]:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
            continue
        
        bilgisayar_sec = bilgisayar_secimi()
        print(f"Bilgisayarın seçimi: {bilgisayar_sec}")
        
        sonuc = kazanan_belirle(kullanici_secimi, bilgisayar_sec)
        print(sonuc)

oyun()
