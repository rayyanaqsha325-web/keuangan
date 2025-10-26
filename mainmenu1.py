# main.py
from transaksi import Transaksi, menu, format_rupiah
from reminder import Reminder
from budget import BudgetPlanner
from laporan import LaporanBulanan


def main():
    catatan = Transaksi()
    reminder = Reminder()
    planner = BudgetPlanner()
    laporan = LaporanBulanan()

    while True:
        menu()
        pilihan = input("Pilih menu (1-10): ")

        if pilihan == "1":
            jenis = input("Masukkan jenis (pemasukan/pengeluaran): ").lower()
            try:
                jumlah = int(input("Masukkan jumlah: "))
            except ValueError:
                print("Jumlah harus berupa angka!")
                continue
            keterangan = input("Masukkan keterangan: ")
            catatan.tambah_transaksi(jenis, jumlah, keterangan)

        elif pilihan == "2":
            catatan.tampilkan_semua()

        elif pilihan == "3":
            saldo = catatan.hitung_saldo()
            print(f"Total saldo Anda saat ini adalah: {format_rupiah(saldo)}")

        elif pilihan == "4":
            konfirmasi = input("Yakin ingin menghapus semua data? (ya/tidak): ").lower()
            if konfirmasi == "ya":
                catatan.data = []
                catatan.simpan_data()
                print("Semua data berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")

        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break

        elif pilihan == "6":
            keyword = input("Masukkan kata keterangan yang ingin dicari: ")
            catatan.cari_transaksi(keyword)

        elif pilihan == "7":
            jenis = input("Pilih jenis (pemasukan/pengeluaran): ").lower()
            if jenis in ["pemasukan", "pengeluaran"]:
                catatan.filter_berdasarkan_jenis(jenis)
            else:
                print("Jenis tidak valid, pilih 'pemasukan' atau 'pengeluaran'.")

        elif pilihan == "8":
            print("\n=== Menu Pengingat Tagihan ===")
            print("1. Tambah Tagihan Baru")
            print("2. Lihat Tagihan yang Akan Jatuh Tempo")
            print("3. Hapus Tagihan")
            sub = input("Pilih opsi (1/2/3): ")

            if sub == "1":
                nama = input("Masukkan nama tagihan (misal: Listrik, Internet): ")
                jatuh_tempo = input("Masukkan tanggal jatuh tempo (format: DD-MM-YYYY): ")
                try:
                    jumlah = int(input("Masukkan jumlah tagihan (Rp): "))
                except ValueError:
                    print("Jumlah harus berupa angka!")
                else:
                    reminder.tambah_tagihan(nama, jatuh_tempo, jumlah)

            elif sub == "2":
                reminder.tampilkan_tagihan()

            elif sub == "3":
                reminder.hapus_tagihan()

            else:
                print("Pilihan tidak valid di menu Tagihan!")


        elif pilihan == "9":
            print("\n=== Menu Anggaran Bulanan ===")
            print("1. Lihat Status Anggaran")
            print("2. Edit Anggaran")
            print("3. Tambah Kategori Baru")
            print("4. Hapus Kategori")
            sub = input("Pilih opsi (1/2/3/4): ")

            if sub == "1":
                planner.tampilkan_status_anggaran()
            elif sub == "2":
                planner.edit_anggaran()
            elif sub == "3":
                planner.tambah_kategori()
            elif sub == "4":
                planner.hapus_kategori()
            else:
                print("Pilihan tidak valid di menu Anggaran!")


        elif pilihan == "10":
            laporan.tampilkan_ringkasan()

        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()
