import unittest

from toko.validasi import cek_angka, cek_baris
from toko.processing import Barang, Toko, hitung_total, buat_record
from toko.fileio import baca_barang

class TestToko(unittest.TestCase):
    def setUp(self):
        # data contoh, dibuat ulang sebelum tiap tes
        self.toko = Toko()
        self.toko.tambah(Barang("B001", "Pensil", 2000, 50))
        self.toko.tambah(Barang("B002", "Buku", 5000, 3))
        self.toko.tambah(Barang("B003", "Penggaris", 3000, 10))

    def test_angka_benar(self):
        self.assertEqual(cek_angka("7"), 7)

    def test_angka_negatif(self):
        with self.assertRaises(ValueError):
            cek_angka("-5")

    def test_baris_rusak(self):
        with self.assertRaises(ValueError):
            cek_baris("B009;Buku;abc;10")

    def test_total_nilai(self):
        # 2000x50 + 5000x3 + 3000x10 = 145000
        self.assertEqual(self.toko.total_nilai(), 145000)

    def test_stok_menipis(self):
        self.assertEqual(len(self.toko.stok_menipis()), 1)

    def test_urutkan_harga(self):
        self.assertEqual(self.toko.urutkan_harga()[0].nama, "Pensil")

    def test_cari(self):
        self.assertEqual(self.toko.cari("B002").nama, "Buku")
        self.assertIsNone(self.toko.cari("XXXX"))

    def test_args_dan_kwargs(self):
        self.assertEqual(hitung_total(1, 2, 3), 6)
        self.assertEqual(buat_record("A", merek="Faber")["merek"], "Faber")

    def test_file_tidak_ada(self):
        self.assertEqual(baca_barang("file_tidak_ada.txt"), [])

def jalankan():
    unittest.main(module="toko.testing", argv=["tes"], verbosity=2, exit=False)

if __name__ == "__main__":
    jalankan()
