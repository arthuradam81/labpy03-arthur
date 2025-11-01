saldo = 1000000

while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        tarik = int(input("Masukkan jumlah penarikan: "))
        
        if tarik <= saldo:
            saldo -= tarik
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak cukup!")
        
        if saldo == 0:
            print("Saldo Anda habis. Terima kasih telah menggunakan ATM!")
            break
    
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    
    else:
        print("Pilihan tidak valid, coba lagi.")
