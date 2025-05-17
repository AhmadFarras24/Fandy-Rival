import tkinter as tk
from tkinter import messagebox

# Kelas untuk menyimpan data komplain
class Komplain:
    def __init__(self, nama, komplain):
        self.nama = nama
        self.komplain = komplain

# Kelas utama sistem
class SistemMonitoring:
    def __init__(self, root):
        self.root = root
        self.root.title("Komplain Karyawan")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        self.laporan = []  # List untuk menyimpan laporan
        self.setup_ui()

    def setup_ui(self):
        judul = tk.Label(self.root, text="Form Komplain", font=("Helvetica", 16, "bold"),
                         bg="#eed4d4", fg="#333")
        judul.pack(pady=10)

        frame_form = tk.Frame(self.root, bg="#f0f0f0")
        frame_form.pack(pady=10)

        # Input Nama
        tk.Label(frame_form, text="Nama", font=("Helvetica", 11),
                 bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_nama = tk.Entry(frame_form, width=40)
        self.entry_nama.grid(row=0, column=1, padx=5, pady=5)

        # Input Komplain
        tk.Label(frame_form, text="Komplain", font=("Helvetica", 11),
                 bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_komplain = tk.Entry(frame_form, width=40)
        self.entry_komplain.grid(row=1, column=1, padx=5, pady=5)

        # Tombol Lapor
        self.btn_lapor = tk.Button(self.root, text="Lapor Komplain", command=self.lapor_komplain,
                                   bg="#007acc", fg="white", font=("Helvetica", 11), padx=10, pady=5)
        self.btn_lapor.pack(pady=5)

        # Tombol Tampilkan
        self.btn_tampilkan = tk.Button(self.root, text="Tampilkan Komplain", command=self.tampilkan_laporan,
                                       bg="#28a745", fg="white", font=("Helvetica", 11), padx=10, pady=5)
        self.btn_tampilkan.pack(pady=5)

        # Listbox untuk menampilkan laporan
        self.list_laporan = tk.Listbox(self.root, width=60, height=15, font=("Courier", 10))
        self.list_laporan.pack(pady=10)

    def lapor_komplain(self):
        nama = self.entry_nama.get().strip()
        komplain = self.entry_komplain.get().strip()

        if nama and komplain:
            laporan_baru = Komplain(nama, komplain)
            self.laporan.append(laporan_baru)
            messagebox.showinfo("Sukses", "Laporan berhasil ditambahkan!")
            self.entry_nama.delete(0, tk.END)
            self.entry_komplain.delete(0, tk.END)
        else:
            messagebox.showwarning("Gagal", "Lengkapi semua data!")

    def tampilkan_laporan(self):
        self.list_laporan.delete(0, tk.END)
        for i, laporan in enumerate(self.laporan, 1):
            self.list_laporan.insert(tk.END, f"{i}. {laporan.nama} - {laporan.komplain}")

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemMonitoring(root)
    root.mainloop()
