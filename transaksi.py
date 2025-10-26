# transaksi.py
import json
import os

# Fungsi utilitas untuk format uang
def format_rupiah(angka):
    """Mengubah angka menjadi format Rupiah, misal 1500000 -> Rp1.500.000"""
    return f"Rp{angka:,}".replace(",", ".")


class Transaksi:
    def __init__(self, nama_file="data_keuangan.json"):
        self.nama_file = nama_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.nama_file):
            with open(self.nama_file, "r") as file:
                return json.load(file)
        return []

    def simpan_data(self):
        with open(self.nama_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def tambah_transaksi(self, jenis, jumlah, keterangan):
        # if statement → validasi input
        if jenis not in ["pemasukan", "pengeluaran"]:
            print("Jenis transaksi tidak valid! Gunakan 'pemasukan' atau 'pengeluaran'.")
            return
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return

        transaksi_baru = {
            "jenis": jenis,
            "jumlah": jumlah,
            "keterangan": keterangan
        }
        self.data.append(transaksi_baru)
        self.simpan_data()
        print(f"Transaksi {jenis} sebesar {format_rupiah(jumlah)} berhasil ditambahkan.")

    def tampilkan_semua(self):
        if not self.data:
            print("Belum ada transaksi yang tercatat.")
            return
        print("\n=== Daftar Transaksi ===")
        for i, t in enumerate(self.data, start=1):  # for loop
            print(f"{i}. [{t['jenis']}] {format_rupiah(t['jumlah'])} - {t['keterangan']}")

    def hitung_saldo(self):
        saldo = 0
        for t in self.data:
            if t['jenis'] == 'pemasukan':
                saldo += t['jumlah']
            elif t['jenis'] == 'pengeluaran':
                saldo -= t['jumlah']
        return saldo

    def cari_transaksi(self, keyword):
        hasil = []
        for t in self.data:  # for loop + if
            if keyword.lower() in t['keterangan'].lower():
                hasil.append(t)

        if not hasil:
            print(f"Tidak ditemukan transaksi dengan kata '{keyword}'.")
        else:
            print(f"\n=== Hasil Pencarian untuk '{keyword}' ===")
            for i, t in enumerate(hasil, start=1):
                print(f"{i}. [{t['jenis']}] {format_rupiah(t['jumlah'])} - {t['keterangan']}")

    def filter_berdasarkan_jenis(self, jenis):
        hasil = [t for t in self.data if t['jenis'] == jenis]  # list comprehension + if
        if not hasil:
            print(f"Tidak ada transaksi dengan jenis '{jenis}'.")
        else:
            print(f"\n=== Transaksi {jenis.capitalize()} ===")
            for i, t in enumerate(hasil, start=1):
                print(f"{i}. {format_rupiah(t['jumlah'])} - {t['keterangan']}")


# Fungsi menu di luar class
def menu():
    print("\n===== Menu Catatan Keuangan =====")
    print("1. Tambah Transaksi")
    print("2. Lihat Semua Transaksi")
    print("3. Lihat Total Saldo")
    print("4. Hapus Semua Data")
    print("5. Keluar")
    print("6. Cari Transaksi Berdasarkan Keterangan")
    print("7. Lihat Transaksi Berdasarkan Jenis")
    print("8. Lihat Pengingat Tagihan")
    print("9. Lihat Anggaran Bulanan")
    print("10. Lihat Laporan Bulanan")
