from toko.validasi import cek_baris

def buat_file(nama_file):
    try:
        with open(nama_file, "x") as file:
            file.write("")
        print("File", nama_file, "berhasil dibuat")
    except FileExistsError:
        print("File", nama_file, "sudah ada, tidak dibuat ulang")

def tambah_barang(nama_file, baris):
    with open(nama_file, "a") as file:
        file.write(baris + "\n")

def baca_barang(nama_file):
    daftar = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                if baris.strip() == "":
                    continue
                try:
                    daftar.append(cek_baris(baris))
                except ValueError as e:
                    print("Baris dilewati:", baris.strip(), "->", e)
    except FileNotFoundError:
        print("File", nama_file, "belum ada, buat dulu filenya")
    return daftar

def tulis_laporan(nama_file, teks):
    with open(nama_file, "w") as file:
        file.write(teks)
