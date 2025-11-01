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

#Latihan-3
Penjelasan:
saldo = 1000000
→ Inisialisasi saldo awal sebesar Rp 1.000.000.
while True:
→ Program akan terus berjalan (loop) sampai pengguna memilih keluar (break).
Menampilkan menu:
print("1. Tarik Uang")
print("2. Keluar")
→ Ditampilkan setiap kali loop berjalan.
Input pilihan pengguna:
pilihan = input("Pilih menu (1/2): ")
→ Pengguna memasukkan angka 1 atau 2.
Jika pilih 1 → tarik uang:
Program meminta jumlah uang yang ingin ditarik.
Mengecek apakah saldo cukup (if tarik <= saldo:).
Jika cukup → saldo dikurangi (saldo -= tarik).
Jika tidak → tampilkan “Saldo tidak cukup!”.
Jika saldo habis:
→ Program akan otomatis keluar dan menampilkan pesan:
Saldo Anda habis. Terima kasih telah menggunakan ATM!
Jika pilih 2 → keluar manual:
→ Program berhenti dengan pesan:
Terima kasih telah menggunakan ATM!
Jika input tidak valid:
→ Program akan menampilkan:
Pilihan tidak valid, coba lagi.
