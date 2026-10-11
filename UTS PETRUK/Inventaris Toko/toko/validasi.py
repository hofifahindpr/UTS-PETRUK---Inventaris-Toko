"""validasi.py - mengecek input dan data barang."""

def cek_kosong(**data):
    # **kwargs: jumlah isian bebas, tidak boleh kosong
    for nama, isi in data.items():
        if isi.strip() == "":
            raise ValueError(nama + " tidak boleh kosong") 

def cek_angka(teks):
    try:
        angka = int(teks)
    except ValueError:
        # pesan error dibuat supaya lebih jelas
        raise ValueError("'" + teks + "' bukan angka")
    if angka < 0:
        raise ValueError("Angka tidak boleh negatif")
    return angka

def cek_baris(baris):
    # satu baris file: kode;nama;harga;stok
    bagian = baris.strip().split(";")
    if len(bagian) != 4:
        raise ValueError("Kolom harus ada 4")
    kode, nama, harga, stok = bagian
    cek_kosong(kode=kode, nama=nama, harga=harga, stok=stok)
    return kode, nama, cek_angka(harga), cek_angka(stok)

if __name__ == "__main__":
    print(cek_baris("B001;Pensil;2000;50"))
    try:
        cek_baris("B002;Buku;kosong;10")
    except ValueError as e:
        print("Ditolak:", e)
