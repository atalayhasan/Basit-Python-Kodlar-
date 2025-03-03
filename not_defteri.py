def not_defteri():
    print("📒 Not Defteri Uygulaması")
    
    with open("notlar.txt", "a") as dosya:
        while True:
            not_icerik = input("Notunuzu girin (Çıkmak için 'q' tuşuna basın): ")
            if not_icerik.lower() == "q":
                print("Not defteri kapatıldı.")
                break
            dosya.write(not_icerik + "\n")
            print("✅ Not kaydedildi.")

not_defteri()
