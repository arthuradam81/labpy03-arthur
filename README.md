# labpy03-arthur

#Penjelasan-pertemuan-ke-7

#Latihan-1
Penjelasan:
from random import random
→ Mengambil fungsi random() dari modul random, untuk menghasilkan angka acak antara 0.0 dan 1.0.
n = int(input("Masukkan nilai N: "))
→ Pengguna memasukkan jumlah bilangan acak yang ingin ditampilkan.
while i < n:
→ Loop akan terus berjalan sampai jumlah data yang dihasilkan = n.
a = random()
→ Menghasilkan angka acak (contohnya 0.17, 0.92, dst).
if a < 0.5:
→ Hanya menampilkan angka yang lebih kecil dari 0.5.
i += 1
→ Dijalankan hanya jika angka memenuhi syarat (a < 0.5), supaya hanya hitung angka valid.

#Latihan2
Penjelasan:
modal = 100000000
→ Uang awal 100 juta.
for bulan in range(1, 9):
→ Mengulang dari bulan ke-1 sampai ke-8.
Gunakan percabangan (if):
Bulan 1–2 → belum ada laba (0)
Bulan 3–4 → laba = 1% × modal
Bulan 5–7 → laba = 5% × modal
Bulan 8 → laba = 3% × modal
total += laba
→ Menjumlahkan seluruh laba ke total akhir.
Output menampilkan laba tiap bulan dan totalnya.
