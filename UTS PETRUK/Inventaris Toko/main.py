from toko import fileio, processing, validasi, testing

FILE_DATA = "inventaris.txt"
FILE_LAPORAN = "laporan_inventaris.txt"

def muat_toko():
    # baca file lalu masukkan datanya ke objek Toko
    toko = processing.Toko()
    for kode, nama, harga, stok in fileio.baca_barang(FILE_DATA):
        toko.tambah(processing.Barang(kode, nama, harga, stok))
    return toko

def lihat_barang():
    toko = muat_toko()
    for b in toko.urutkan_harga():
        b.tampil()

def tambah_barang():
    kode = input("Kode barang : ")
    nama = input("Nama barang : ")
    harga = input("Harga       : ")
    stok = input("Stok        : ")
    try:
        # cek dulu, kalau salah langsung loncat ke except
        kode, nama, harga, stok = validasi.cek_baris(f"{kode};{nama};{harga};{stok}")
        if muat_toko().cari(kode) is not None:
            raise ValueError("Kode " + kode + " sudah dipakai")
        barang = processing.Barang(kode, nama, harga, stok)
        fileio.tambah_barang(FILE_DATA, barang.ke_baris())
        print("Barang berhasil ditambahkan")
    except ValueError as e:
        print("Gagal:", e)

def lihat_stok_menipis():
    toko = muat_toko()
    menipis = toko.stok_menipis(batas=5)
    if len(menipis) == 0:
        print("Tidak ada barang yang stoknya menipis")
    for b in menipis:
        b.tampil()

def buat_laporan():
    toko = muat_toko()
    if len(toko.barang) == 0:
        print("Belum ada data barang")
        return
    teks = processing.buat_laporan(toko)
    fileio.tulis_laporan(FILE_LAPORAN, teks)
    print(teks)

def menu():
    fileio.buat_file(FILE_DATA)
    while True:
        print("\n=== INVENTARIS TOKO ===")
        print("1. Lihat barang")
        print("2. Tambah barang")
        print("3. Stok menipis")
        print("4. Buat laporan")
        print("5. Jalankan unit test")
        print("0. Keluar")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            lihat_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            lihat_stok_menipis()
        elif pilihan == "4":
            buat_laporan()
        elif pilihan == "5":
            testing.jalankan()
        elif pilihan == "0":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak ada")

menu()
