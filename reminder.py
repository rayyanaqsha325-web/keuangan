# reminder.py
import json
import os
import datetime  # pastikan ini ada (menggunakan modul datetime)

class Reminder:
    def __init__(self, file_name="data_tagihan.json"):
        self.file_name = file_name
        self.tagihan = self.load_tagihan()

    def load_tagihan(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    # file korup / kosong → reset jadi list kosong
                    return []
        return []  # default kosong

    def simpan_tagihan(self):
        with open(self.file_name, "w") as f:
            json.dump(self.tagihan, f, indent=4)

    # 1. Tambah Tagihan
    def tambah_tagihan(self, nama, jatuh_tempo, jumlah):
        """
        jatuh_tempo: string format 'DD-MM-YYYY'
        jumlah: int
        """
        # Validasi format tanggal sebelum simpan
        try:
            _ = datetime.datetime.strptime(jatuh_tempo, "%d-%m-%Y").date()
        except ValueError:
            print("Format tanggal tidak valid. Gunakan DD-MM-YYYY (contoh: 31-10-2025).")
            return

        try:
            jumlah = int(jumlah)
            if jumlah < 0:
                print("Jumlah harus positif.")
                return
        except (ValueError, TypeError):
            print("Jumlah harus berupa angka bulat (contoh: 250000).")
            return

        self.tagihan.append({
            "nama": nama,
            "jatuh_tempo": jatuh_tempo,
            "jumlah": jumlah
        })
        self.simpan_tagihan()
        print(f"✅ Tagihan {nama} berhasil ditambahkan!")

    # 2. Tampilkan Tagihan yang Akan Jatuh Tempo
    def tampilkan_tagihan(self):
        hari_ini = datetime.date.today()
        if not self.tagihan:
            print("Belum ada data tagihan.")
            return

        print("\n=== Pengingat Tagihan ===")
        ada_tagihan = False
        for t in self.tagihan:
            try:
                due_date = datetime.datetime.strptime(t["jatuh_tempo"], "%d-%m-%Y").date()
            except (ValueError, KeyError):
                # Lewati entri yang tidak valid formatnya
                print(f"⚠️ Format tanggal tidak valid untuk tagihan: {t}. Lewati.")
                continue

            selisih = (due_date - hari_ini).days
            if selisih < 0:
                # Sudah lewat jatuh tempo
                print(f"⚠️ Tagihan {t['nama']} sudah lewat jatuh tempo ({abs(selisih)} hari yang lalu). Jumlah: Rp{t['jumlah']:,}".replace(",", "."))
                ada_tagihan = True
            elif selisih <= 3:
                # Dalam 3 hari ke depan
                print(f"⚠️ Tagihan {t['nama']} akan jatuh tempo dalam {selisih} hari. Jumlah: Rp{t['jumlah']:,}".replace(",", "."))
                ada_tagihan = True

        if not ada_tagihan:
            print("✅ Tidak ada tagihan yang mendekati jatuh tempo.")

    # 3. Hapus Tagihan
    def hapus_tagihan(self):
        if not self.tagihan:
            print("Belum ada data tagihan yang bisa dihapus.")
            return

        print("\n=== Daftar Tagihan ===")
        for i, t in enumerate(self.tagihan, start=1):
            print(f"{i}. {t.get('nama','-')} - Jatuh tempo: {t.get('jatuh_tempo','-')} - Jumlah: Rp{t.get('jumlah',0):,}".replace(",", "."))

        try:
            pilihan = int(input("Masukkan nomor tagihan yang ingin dihapus: "))
            if 1 <= pilihan <= len(self.tagihan):
                tagihan_dihapus = self.tagihan.pop(pilihan - 1)
                self.simpan_tagihan()
                print(f"✅ Tagihan {tagihan_dihapus.get('nama','-')} berhasil dihapus.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid!")
