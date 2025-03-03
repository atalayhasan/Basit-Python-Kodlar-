import tkinter as tk
from tkinter import messagebox

# Görevleri saklamak için bir liste
tasks = []

# Görevleri dosyaya kaydet
def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Görevleri dosyadan yükle
def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

# Görevi ekle
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Uyarı", "Görev girin!")

# Görevi sil
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        tasks.remove(task)
        update_task_list()
        save_tasks()

# Görev listesini güncelle
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Ana pencereyi oluştur
window = tk.Tk()
window.title("Görev Listesi")

# Görev giriş kutusu
task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=10)

# Görev ekleme butonu
add_button = tk.Button(window, text="Görev Ekle", command=add_task)
add_button.pack(pady=5)

# Görev listesi
task_listbox = tk.Listbox(window, width=50, height=10)
task_listbox.pack(pady=10)

# Görev silme butonu
delete_button = tk.Button(window, text="Görev Sil", command=delete_task)
delete_button.pack(pady=5)

# Yüklenen görevleri listeye ekle
tasks = load_tasks()
update_task_list()

# Pencereyi başlat
window.mainloop()
