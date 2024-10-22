# Variabel Global
users = {}  
pendaftar = {}  
turnamen_aktif = "TURNAMEN MLBB IT 2024"

# Menampilkan Menu Utama
def menu_awal(): # Prosedur
    while True:
        print(f"\n=== Program {turnamen_aktif} ===")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            register()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Terima kasih telah berpartisipasi dalam turnamen ini.")
            exit()  # Keluar dari program
        else:
            print("Input tidak valid. Silakan pilih 1, 2, atau 3.")

# Fungsi Register: Membuat Akun Baru
def register():
    username = input("Masukkan username baru: ")
    if username in users:
        hasil = print("Username sudah terdaftar!")
        return hasil
    else:
        password = input("Masukkan password: ")
        role = input("Pilih role (admin/pendaftar): ").lower()

        if role not in ["admin", "pendaftar"]:
            hasil = print("Role tidak valid. Pilih 'admin' atau 'pendaftar'.")
            return hasil
        else:
            users[username] = {"password": password, "role": role}
            hasil = print(f"Akun {role} dengan username '{username}' berhasil dibuat!")
            return hasil

# Fungsi Login: Masuk ke Sistem
def login_user():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        print(f"\nLogin berhasil sebagai {role}!")
        if role == "admin":
            admin_menu()
        elif role == "pendaftar":
            pendaftar_menu(username)
    else:
        a = print("Username atau password salah.")
        return a

# Menu Admin
def admin_menu(): # Prosedur
    while True:
        print("\n=== Menu Admin ===")
        print("1. Lihat Pendaftar")
        print("2. Tambah Pendaftar")
        print("3. Ubah Data Pendaftar")
        print("4. Hapus Pendaftar")
        print("5. Logout")
        admin_choice = input("Pilih menu: ")

        if admin_choice == "1":
            lihat_pendaftar()
        elif admin_choice == "2":
            tambah_pendaftar()
        elif admin_choice == "3":
            ubah_pendaftar()
        elif admin_choice == "4":
            hapus_pendaftar()
        elif admin_choice == "5":
            print("Logout berhasil.")
            menu_awal()
        else:
            print("Pilihan tidak valid.")

# Fungsi untuk Melihat Daftar Pendaftar
def lihat_pendaftar():# fungsi tanpa paarameter
    global a
    a = True
    if not pendaftar:
        print("Belum ada pendaftar yang terdaftar.")
        a = False

    else:
        print("=== Daftar Pendaftar ===")
        for i, (key, value) in enumerate(pendaftar.items(), start=1):
            print(f"{i}. Nama: {value['nama']}, Usia: {value['usia']}, Rank: {value['rank']}")
        return 

# Fungsi untuk Menambah Pendaftar 
def tambah_pendaftar():
    nama = input("Masukkan nama pendaftar: ")
    try:
        usia = int(input("Masukkan usia: "))
    except ValueError:
        print("Usia harus berupa angka.")
        return
    
    rank = input("Masukkan rank (Warrior, Elite, Master, Grandmaster, Epic, Legend, Mythic): ").capitalize()
    if usia < 17:
        print("Pendaftar harus berusia minimal 17 tahun.")
    elif rank not in ["Epic", "Legend", "Mythic"]:
        print("Rank minimal yang diizinkan adalah Epic.")
    else:
        pendaftar[nama] = {"nama": nama, "usia": usia, "rank": rank}
        print(f"Pendaftar {nama} berhasil ditambahkan!")

# Fungsi untuk Mengubah Data Pendaftar
def ubah_pendaftar():
    lihat_pendaftar()
    while a == True :
        i = int(input("Masukkan nomor pendaftar yang ingin diubah: "))
        if i <= 0 or i > len(pendaftar):
            print("Nomor pendaftar tidak valid.")
        else:
            nama = list(pendaftar.keys())[i - 1]
            pendaftar[nama]["nama"] = input("Masukkan nama baru: ")

            # Validasi usia
            while True:
                try:
                    usia_baru = int(input("Masukkan usia baru: "))
                    if usia_baru >= 17:
                        pendaftar[nama]["usia"] = usia_baru
                        break
                    else:
                        print("Usia harus minimal 17 tahun.")
                except ValueError:
                    print("Usia harus berupa angka.")
                    return

        # Validasi rank
        while True:
            rank_baru = input("Masukkan rank baru (Warrior, Elite, Master, Grandmaster, Epic, Legend, Mythic): ").capitalize()
            if rank_baru in ["Epic", "Legend", "Mythic"]:
                pendaftar[nama]["rank"] = rank_baru
                break
            else:
                print("Rank minimal yang diizinkan adalah Epic.")

        print(f"Data pendaftar {nama} berhasil diubah.")
        break

# Fungsi untuk Menghapus Pendaftar
def hapus_pendaftar():
    lihat_pendaftar()
    while a == True:
        i = int(input("Masukkan nomor pendaftar yang ingin dihapus: "))
        if i <= 0 or i > len(pendaftar):
            print("Nomor pendaftar tidak valid.")
        else:
            nama = list(pendaftar.keys())[i - 1]
            del pendaftar[nama]
            print(f"Data pendaftar {nama} berhasil dihapus.")
            return

# Menu Pendaftar
def pendaftar_menu(username): #fungsi paramaeter
    while True:
        print("\n=== Menu Pendaftar ===")
        print("1. Mendaftar Turnamen")
        print("2. Cek Pendaftaran Saya")
        print("3. Logout")
        pendaftar_choice = input("Pilih menu: ")

        if pendaftar_choice == "1":
            mendaftar_turnamen(username)
        elif pendaftar_choice == "2":
            lihat_data_saya(username)
        elif pendaftar_choice == "3":
            print("Logout berhasil.")
            menu_awal()
        else:
            print("Pilihan tidak valid.")

# Fungsi untuk Mendaftar Turnamen
def mendaftar_turnamen(username):#fungsi parameter
    if username in pendaftar:
        print("Anda sudah terdaftar dalam turnamen.")
    else:
        nama = input("Masukkan nama: ")
        try:
            usia = int(input("Masukkan usia: "))
        except ValueError:
            print("Usia harus berupa angka.")
            return
        
        rank = input("Masukkan rank (Warrior, Elite, Master, Grandmaster, Epic, Legend, Mythic): ").capitalize()
        if usia < 17:
            print("Anda harus berusia minimal 17 tahun untuk mendaftar.")
        elif rank not in ["Epic", "Legend", "Mythic"]:
            print("Rank minimal yang diizinkan adalah Epic.")
        else:
            pendaftar[username] = {"nama": nama, "usia": usia, "rank": rank}
            print("Anda berhasil mendaftar dalam turnamen!")

# Fungsi untuk Melihat Data Sendiri
def lihat_data_saya(username):
    if username in pendaftar:
        data = pendaftar[username]
        print(f"Nama: {data['nama']}, Usia: {data['usia']}, Rank: {data['rank']}")
    else:
        print("Anda belum mendaftar ke turnamen.")
        return

menu_awal()
