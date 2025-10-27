import matplotlib.pyplot as plt
from transaksi import Transaksi
import json, os

class LaporanBulanan:
    def __init__(self, file_name="data_laporan.json"):
        self.file_name = file_name
        self.transaksi = Transaksi()

    def tampilkan_ringkasan(self):
        data = self.transaksi.data
        if not data:
            print("Belum ada data transaksi.")
            return

        total_masuk = sum(t["jumlah"] for t in data if t["jenis"] == "pemasukan")
        total_keluar = sum(t["jumlah"] for t in data if t["jenis"] == "pengeluaran")
        saldo = total_masuk - total_keluar

        ringkasan = {
            "total_pemasukan": total_masuk,
            "total_pengeluaran": total_keluar,
            "saldo": saldo
        }
        self.simpan_ringkasan(ringkasan)

        print("\n=== Laporan Bulanan ===")
        print(f"Pemasukan: Rp{total_masuk:,}".replace(",", "."))
        print(f"Pengeluaran: Rp{total_keluar:,}".replace(",", "."))
        print(f"Saldo Akhir: Rp{saldo:,}".replace(",", "."))

        plt.bar(["Pemasukan", "Pengeluaran", "Saldo"], [total_masuk, total_keluar, saldo],
                color=["green", "red", "blue"])
        plt.title("Laporan Keuangan Bulanan")
        plt.show()

    def simpan_ringkasan(self, data):
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)
