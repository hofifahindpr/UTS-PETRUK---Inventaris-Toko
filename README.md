# Program Inventaris Toko

## Deskripsi
Program inventaris toko ini dibuat menggunakan Python untuk memenuhi tugas UTS Pemrograman Terstruktur. Program dapat membaca data barang dari file teks, memvalidasi data, menampilkan daftar barang, menambahkan barang baru, menampilkan stok menipis, membuat laporan inventaris, dan menjalankan unit test.

## Struktur Program
- `main.py`: menu utama program.
- `inventaris.txt`: menyimpan data barang.
- `laporan_inventaris.txt`: menyimpan hasil laporan.
- `inventaris_awal.py`: contoh kode sebelum refactoring.
- `toko/fileio.py`: menangani pembacaan dan penulisan file.
- `toko/processing.py`: berisi class dan fungsi pengolahan data.
- `toko/validasi.py`: memeriksa validitas data.
- `toko/testing.py`: berisi unit test.
- `toko/__init__.py`: menandai folder sebagai package Python.

## Cara Menjalankan
Pastikan Python sudah terpasang, kemudian buka terminal pada folder proyek.

Jalankan program:
```bash
python main.py
```

Jalankan unit test secara terpisah:
```bash
python -m unittest toko.testing -v
```

## Format Data
Data barang disimpan dengan format:
`kode;nama;harga;stok`

## Fitur
1. Melihat daftar barang.
2. Menambahkan barang.
3. Melihat barang dengan stok 5 atau kurang.
4. Membuat laporan inventaris.
5. Menjalankan unit test.
