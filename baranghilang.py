import tkinter as tk
from tkinter import messagebox

class BarangHilang:
    def __init__(self, nama_pelapor, jenis_barang, lokasi_terakhir):
        self.nama_pelapor = nama_pelapor
        self.jenis_barang = jenis_barang
        self.lokasi_terakhir = lokasi_terakhir
        self.status = "Hilang"
        self.diterima_oleh = "Belum Ditentukan"

class PetugasKeamanan:
    def __init__(self, nama_petugas):
        self.nama_petugas = nama_petugas

class SistemMonitoring:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Monitoring Barang Hilang")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        self.laporan = []
        self.setup_ui()

    def setup_ui(self):
        judul = tk.Label(self.root, text="Form Laporan Barang Hilang", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
        judul.pack(pady=10)

        frame_form = tk.Frame(self.root, bg="#f0f0f0")
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Nama Pelapor", font=("Helvetica", 11), bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_pelapor = tk.Entry(frame_form, width=40)
        self.entry_pelapor.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Jenis Barang", font=("Helvetica", 11), bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_jenis = tk.Entry(frame_form, width=40)
        self.entry_jenis.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Lokasi Terakhir", font=("Helvetica", 11), bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_lokasi = tk.Entry(frame_form, width=40)
        self.entry_lokasi.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Nama Petugas", font=("Helvetica", 11), bg="#f0f0f0").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_petugas = tk.Entry(frame_form, width=40)
        self.entry_petugas.grid(row=3, column=1, padx=5, pady=5)

        self.btn_lapor = tk.Button(self.root, text="Lapor Barang Hilang", command=self.lapor_barang, bg="#007acc", fg="white", font=("Helvetica", 11), padx=10, pady=5)
        self.btn_lapor.pack(pady=5)

        self.btn_tampilkan = tk.Button(self.root, text="Tampilkan Laporan", command=self.tampilkan_laporan, bg="#28a745", fg="white", font=("Helvetica", 11), padx=10, pady=5)
        self.btn_tampilkan.pack(pady=5)


        self.list_laporan = tk.Listbox(self.root, width=60, height=12, font=("Courier", 10))
        self.list_laporan.pack(pady=10)
        
        self.btn_ditemukan = tk.Button(self.root, text="Tandai Ditemukan", command=self.tandai_ditemukan, bg="#ffc107", fg="black", font=("Helvetica", 11), padx=10, pady=5)
        self.btn_ditemukan.pack(pady=5)
        
    def lapor_barang(self):
        nama = self.entry_pelapor.get()
        jenis = self.entry_jenis.get()
        lokasi = self.entry_lokasi.get()
        nama_petugas = self.entry_petugas.get()

        if nama and jenis and lokasi and nama_petugas:
            barang = BarangHilang(nama, jenis, lokasi)
            petugas = PetugasKeamanan(nama_petugas)
            barang.diterima_oleh = petugas.nama_petugas
            self.laporan.append(barang)
            messagebox.showinfo("Sukses", "Laporan berhasil ditambahkan!")
            self.entry_pelapor.delete(0, tk.END)
            self.entry_jenis.delete(0, tk.END)
            self.entry_lokasi.delete(0, tk.END)
            self.entry_petugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Gagal", "Lengkapi semua data!")

    def tampilkan_laporan(self):
        self.list_laporan.delete(0, tk.END)
        for i, barang in enumerate(self.laporan):
            self.list_laporan.insert(
                tk.END,
                f"{i+1}. {barang.nama_pelapor} - {barang.jenis_barang} - {barang.lokasi_terakhir} - {barang.status} (Petugas: {barang.diterima_oleh})"
            )

    def tandai_ditemukan(self):
        selected_index = self.list_laporan.curselection()
        if not selected_index:
            messagebox.showwarning("Peringatan", "Pilih laporan yang ingin ditandai sebagai ditemukan.")
            return

        index = selected_index[0]
        barang = self.laporan[index]
        if barang.status == "Ditemukan":
            messagebox.showinfo("Info", "Barang ini sudah ditandai sebagai ditemukan.")
        else:
            barang.status = "Ditemukan"
            messagebox.showinfo("Sukses", "Status barang diperbarui menjadi 'Ditemukan'.")
            self.tampilkan_laporan()

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemMonitoring(root)
    root.mainloop()
