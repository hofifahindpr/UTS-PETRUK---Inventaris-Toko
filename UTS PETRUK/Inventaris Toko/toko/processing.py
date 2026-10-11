class Barang:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def nilai(self):
        # nilai barang di gudang = harga x stok
        return self.harga * self.stok

    def ke_baris(self):
        # ubah jadi satu baris teks untuk disimpan ke file
        return f"{self.kode};{self.nama};{self.harga};{self.stok}"

    def tampil(self):
        print(f"{self.kode} | {self.nama} | Rp{self.harga} | stok {self.stok}")

class Toko:
    def __init__(self):
        self.barang = []  # isinya objek Barang

    def tambah(self, barang):
        self.barang.append(barang)

    def cari(self, kode):
        # cari barang berdasarkan kode, kalau tidak ketemu hasilnya None
        for b in self.barang:
            if b.kode == kode:
                return b
        return None

    def total_nilai(self):
        semua = []
        for b in self.barang:
            semua.append(b.nilai())
        return hitung_total(*semua)

    def rata_rata_harga(self):
        assert len(self.barang) > 0, "Data barang kosong"
        return sum(b.harga for b in self.barang) / len(self.barang)

    def stok_menipis(self, batas=5):
        # lambda: ambil barang yang stoknya sama dengan atau di bawah batas
        return list(filter(lambda b: b.stok <= batas, self.barang))

    def urutkan_harga(self, terbalik=False):
        # lambda: urutkan barang berdasarkan harga
        return sorted(self.barang, key=lambda b: b.harga, reverse=terbalik)

def hitung_total(*angka):
    # *args: boleh kirim angka sebanyak apa pun
    return sum(angka)

def buat_record(kode, **kwargs):
    # **kwargs: atribut tambahan bebas, misal merek="Faber"
    record = {"kode": kode}
    record.update(kwargs)
    return record

def buat_laporan(toko):
    teks = "LAPORAN INVENTARIS TOKO\n"
    teks += "-" * 30 + "\n"
    teks += f"Jumlah jenis barang : {len(toko.barang)}\n"
    teks += f"Total nilai stok    : Rp{toko.total_nilai()}\n"
    teks += f"Rata-rata harga     : Rp{toko.rata_rata_harga():.0f}\n"
    termahal = toko.urutkan_harga(terbalik=True)[0]  # keyword argument
    teks += f"Barang termahal     : {termahal.nama} (Rp{termahal.harga})\n"
    teks += "Stok menipis (<= 5):\n"
    menipis = toko.stok_menipis(batas=5)  # keyword argument
    if len(menipis) == 0:
        teks += "  (tidak ada)\n"
    for b in menipis:
        teks += f"  - {b.nama}: sisa {b.stok}\n"
    return teks

if __name__ == "__main__":
    t = Toko()
    t.tambah(Barang("B001", "Pensil", 2000, 50))
    t.tambah(Barang("B002", "Buku", 5000, 3))
    print(buat_laporan(t))
    print(buat_record("B001", merek="Faber", warna="hitam"))
