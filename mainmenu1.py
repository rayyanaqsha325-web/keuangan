# main.py
from transaksi import Transaksi, menu, format_rupiah

def main():
    catatan = Transaksi()

    while True:
        menu()
        pilihan = input("Pilih menu (1-7): ")

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

        else:
            print("Pilihan tidak valid, coba lagi!")


if __name__ == "__main__":
    main()
