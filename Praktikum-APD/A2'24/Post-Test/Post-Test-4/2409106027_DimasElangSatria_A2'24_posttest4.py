
username_terdaftar = "dimas"
password_terdaftar = "27"

percobaan = 0
jumlah_max_percobaan = 3

while percobaan < jumlah_max_percobaan:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username == username_terdaftar and password == password_terdaftar:
        print("Login berhasil!")
        break 
    else:
        percobaan += 1
        print(f"Login gagal. Sisa percobaan: {jumlah_max_percobaan - percobaan}")
        if percobaan == jumlah_max_percobaan:
            print("Anda telah mencoba 3 kali. login diblokir.")
            exit()

while True:
    nama = input("Masukkan Nama Lengkap: ")
    nim = input("Masukkan NIM: ")
    pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
    lama = int(input("Masukkan Lama Cicilan (tahun): "))
    
    if lama == 1: 
        BungaTahunan = 0.07
        JumlahBulan = 12 
    elif lama == 2: 
        BungaTahunan = 0.13
        JumlahBulan = 24 
    elif lama == 3: 
        BungaTahunan = 0.19
        JumlahBulan = 36 
    else:
        print("Maaf", nama, "Opsi lama cicilan hanya tersedia untuk 1 tahun, 2 tahun, dan 3 tahun.")
        while True:
            ulang = input("Ingin mencoba lagi? (ya/tidak): ")
            if ulang == "tidak":
                print("Terimakasih, sampai jumpa")
                exit()
            elif ulang == "ya":
                break
            else:
                print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")

    BungaPerBulan = (BungaTahunan / 12) * pinjaman
    TotalBunga = BungaPerBulan * JumlahBulan
    CicilanPerBulan = (pinjaman + TotalBunga) / JumlahBulan

    print(f"{nama}, NIM: {nim}, memiliki total pinjaman Rp. {pinjaman} dengan lama cicilan {lama} tahun, sehingga jumlah cicilan per bulan: Rp. {CicilanPerBulan}")


    while True:
        ulang = input("Ingin mencoba lagi? (ya/tidak): ")
        if ulang == "tidak":
            print("Terimakasih, sampai jumpa")
            exit()
        elif ulang == "ya":
            break
        else:
            print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")
