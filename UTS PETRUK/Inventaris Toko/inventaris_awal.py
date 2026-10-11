# VERSI AWAL (sebelum refactoring): semua kode dalam satu file, nama variabel singkat,
# pengecekan angka ditulis dua kali, batas stok 5 ditulis langsung, file dibuka-tutup manual.
f = open("inventaris.txt", "r")
for b in f:
    x = b.strip().split(";")
    h = int(x[2])
    s = int(x[3])
    if h < 0 or s < 0:
        print("data salah")
    elif s <= 5:
        print(x[1], "stok menipis:", s)
    else:
        print(x[1], h, s)
f.close()

k = input("Kode: ")
n = input("Nama: ")
h = int(input("Harga: "))
s = int(input("Stok: "))
if h < 0 or s < 0:
    print("data salah")
else:
    f = open("inventaris.txt", "a")
    f.write(k + ";" + n + ";" + str(h) + ";" + str(s) + "\n")
    f.close()
