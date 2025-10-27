import json, os
from transaksi import format_rupiah

class BudgetPlanner:
    def __init__(self, file_name="data_anggaran.json"):
        self.file_name = file_name
        self.data = self.load_data()

    # Muat atau buat data awal
    def load_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as f:
                    data = json.load(f)
                    if "anggaran" not in data:
                        data["anggaran"] = {}
                    if "pengeluaran" not in data:
                        data["pengeluaran"] = {}
                    return data
            except json.JSONDecodeError:
                pass
        # Data awal jika file kosong / rusak
        return {
            "anggaran": {"Makan": 1000000, "Transport": 500000, "Hiburan": 400000},
            "pengeluaran": {"Makan": 850000, "Transport": 200000, "Hiburan": 300000}
        }

    def simpan_data(self):
        with open(self.file_name, "w") as f:
            json.dump(self.data, f, indent=4)

    # Lihat status anggaran
    def tampilkan_status_anggaran(self):
        anggaran = self.data["anggaran"]
        pengeluaran = self.data["pengeluaran"]

        print("\n=== Status Anggaran Bulanan ===")
        if not anggaran:
            print("Belum ada kategori anggaran.")
            return

        for kategori, batas in anggaran.items():
            terpakai = pengeluaran.get(kategori, 0)
            sisa = batas - terpakai
            if sisa <= batas * 0.1:
                print(f"⚠️ {kategori} hampir mencapai batas! Sisa: {format_rupiah(sisa)}")
            else:
                print(f"✅ {kategori}: Sisa {format_rupiah(sisa)} dari {format_rupiah(batas)}")

    #  Ubah jumlah anggaran kategori
    def update_anggaran(self, kategori, jumlah):
        self.data["anggaran"][kategori] = jumlah
        self.simpan_data()
        print(f"Anggaran kategori {kategori} diperbarui menjadi {format_rupiah(jumlah)}.")

    #  Edit kategori anggaran
    def edit_anggaran(self):
        anggaran = self.data["anggaran"]

        print("\n=== Edit Anggaran Bulanan ===")
        if not anggaran:
            print("Belum ada kategori anggaran.")
            return

        for i, (kategori, batas) in enumerate(anggaran.items(), start=1):
            print(f"{i}. {kategori} - Saat ini: {format_rupiah(batas)}")

        try:
            pilihan = int(input("Pilih nomor kategori yang ingin diubah: "))
            if 1 <= pilihan <= len(anggaran):
                kategori_dipilih = list(anggaran.keys())[pilihan - 1]
                jumlah_baru = int(input("Masukkan jumlah anggaran baru (Rp): ").replace(".", "").strip())
                self.update_anggaran(kategori_dipilih, jumlah_baru)
            else:
                print("Nomor kategori tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid!")

    #  Tambah kategori baru (FIXED)
    def tambah_kategori(self):
        print("\n=== Tambah Kategori Anggaran Baru ===")
        kategori_baru = input("Masukkan nama kategori baru: ").capitalize()

        # Pastikan struktur data aman
        if not isinstance(self.data, dict):
            self.data = {"anggaran": {}, "pengeluaran": {}}
        if "anggaran" not in self.data:
            self.data["anggaran"] = {}
        if "pengeluaran" not in self.data:
            self.data["pengeluaran"] = {}

        # Cek duplikasi
        if kategori_baru in self.data["anggaran"]:
            print(f"⚠️ Kategori '{kategori_baru}' sudah ada!")
            return

        try:
            jumlah_awal = int(input("Masukkan jumlah anggaran awal (Rp): ").replace(".", "").strip())
        except ValueError:
            print("Jumlah harus berupa angka!")
            return

        # 🔸 Tambahkan ke data
        self.data["anggaran"][kategori_baru] = jumlah_awal
        self.data["pengeluaran"][kategori_baru] = 0
        self.simpan_data()

        print(f"✅ Kategori '{kategori_baru}' berhasil ditambahkan dengan anggaran {format_rupiah(jumlah_awal)}.")

    #  Hapus kategori
    def hapus_kategori(self):
        anggaran = self.data["anggaran"]

        print("\n=== Hapus Kategori Anggaran ===")
        if not anggaran:
            print("Belum ada kategori yang bisa dihapus.")
            return

        for i, kategori in enumerate(anggaran.keys(), start=1):
            print(f"{i}. {kategori}")

        try:
            pilihan = int(input("Masukkan nomor kategori yang ingin dihapus: "))
            if 1 <= pilihan <= len(anggaran):
                kategori_dihapus = list(anggaran.keys())[pilihan - 1]
                konfirmasi = input(f"Yakin ingin menghapus kategori '{kategori_dihapus}'? (yes/no): ").lower()
                if konfirmasi == "yes":
                    self.data["anggaran"].pop(kategori_dihapus, None)
                    self.data["pengeluaran"].pop(kategori_dihapus, None)
                    self.simpan_data()
                    print(f"✅ Kategori '{kategori_dihapus}' berhasil dihapus.")
                else:
                    print("Dibatalkan.")
            else:
                print("Nomor kategori tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid!")
