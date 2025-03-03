import tkinter as tk
from tkinter import messagebox
import requests

api_key = "5c87f6b8de4788b9a13d3c65"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

def döviz_dönüşüm():
    bozulan_doviz = bozulan_var.get()
    alinan_doviz = alinan_var.get()
    try:
        miktar = float(miktar_entry.get())
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir miktar girin.")
        return
    
    try:
        sonuc = requests.get(api_url + bozulan_doviz)
        sonuc.raise_for_status()
        sonuc_json = sonuc.json()
        
        if 'conversion_rates' in sonuc_json and alinan_doviz in sonuc_json['conversion_rates']:
            doviz_kuru = sonuc_json["conversion_rates"][alinan_doviz]
            sonuc_miktar = miktar * doviz_kuru
            sonuc_label.config(text=f"{miktar} {bozulan_doviz} = {sonuc_miktar:.2f} {alinan_doviz}")
        else:
            messagebox.showerror("Hata", f"{alinan_doviz} döviz türü bulunamadı.")
    except requests.RequestException as e:
        messagebox.showerror("Hata", f"API isteği başarısız oldu: {e}")


root = tk.Tk()
root.title("Döviz Dönüşüm Uygulaması")


tk.Label(root, text="Bozulan döviz türü:").grid(row=0, column=0, padx=10, pady=5)
bozulan_var = tk.StringVar(value="USD")
dovizler = ["USD", "EUR", "GBP", "JPY", "TRY"]
for idx, doviz in enumerate(dovizler):
    tk.Radiobutton(root, text=doviz, variable=bozulan_var, value=doviz).grid(row=1+idx, column=0, padx=10, pady=5, sticky="w")

tk.Label(root, text="Alınan döviz türü:").grid(row=0, column=1, padx=10, pady=5)
alinan_var = tk.StringVar(value="EUR")
for idx, doviz in enumerate(dovizler):
    tk.Radiobutton(root, text=doviz, variable=alinan_var, value=doviz).grid(row=1+idx, column=1, padx=10, pady=5, sticky="w")

# Miktar için etiket ve giriş alanı
tk.Label(root, text="Miktar:").grid(row=5, column=0, padx=10, pady=5)
miktar_entry = tk.Entry(root)
miktar_entry.grid(row=5, column=1, padx=10, pady=5)

# Hesapla butonu
hesapla_button = tk.Button(root, text="Hesapla", command=döviz_dönüşüm)
hesapla_button.grid(row=6, column=0, columnspan=2, pady=10)

# Sonuç etiketi
sonuc_label = tk.Label(root, text="")
sonuc_label.grid(row=7, column=0, columnspan=2, pady=10)

# Uygulama döngüsü
root.mainloop()
