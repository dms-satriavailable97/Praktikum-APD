users = [["dimas", "27", "admin"]]  # Data pengguna (username, password, role)
pendaftar = []  # Data pendaftar yang menggunakan nested list

# Program Utama
while True:
    print("\n=== Program Turnamen MLBB ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    choice = input("Pilih menu: ")

    # Error handling untuk menu
    if choice not in ["1", "2", "3"]:
        print("Input tidak valid. Silakan pilih 1, 2, atau 3.")
        continue

    if choice == "1":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        
        # Error handling role
        while True:
            role = input("Masukkan role (admin/pendaftar): ").lower()
            if role in ["admin", "pendaftar"]:
                break
            else:
                print("Role tidak valid. Harus admin atau pendaftar.")

        users.append([username, password, role])
        print(f"Pengguna {username} berhasil didaftarkan.")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        user = None
        
        # Proses login
        for i in users:
            if i[0] == username and i[1] == password:
                user = i
                break
        
        if user is None:
            print("Login gagal, username atau password salah.")
        else:
            print(f"Selamat datang, {username}!")
            while True:
                if user[2] == "admin":
                    # Menu Admin
                    print("\n=== Menu Admin ===")
                    print("1. Lihat Pendaftar")
                    print("2. Tambah Pendaftar")
                    print("3. Ubah Pendaftar")
                    print("4. Hapus Pendaftar")
                    print("5. Logout")
                    admin_choice = input("Pilih menu: ")

                    # Error handling untuk menu admin
                    if admin_choice not in ["1", "2", "3", "4", "5"]:
                        print("Input tidak valid. Silakan pilih menu yang ada.")
                        continue

                    if admin_choice == "1":
                        if not pendaftar:
                            print("Belum ada pendaftar.")
                        else:
                            for i, player in enumerate(pendaftar):
                                print(f"\nPlayer ke-{i+1}\nNAMA : {player[0]}\nUSIA : {player[1]}\nRANK : {player[2]}")

                    elif admin_choice == "2":
                        nama = input("Masukkan nama: ")

                        # Error handling untuk usia (input angka)
                        while True:
                            try:
                                usia = int(input("Masukkan usia: "))
                                break
                            except ValueError:
                                print("Usia harus berupa angka. Silakan coba lagi.")

                        # Validasi rank dan usia
                        while True:
                            rank = input("Masukkan rank (Warrior, Elite, Master, Grandmaster, Epic, Legend, Mythic): ").capitalize()
                            if rank in ["Warrior", "Elite", "Master", "Grandmaster", "Epic", "Legend", "Mythic"]:
                                break
                            else:
                                print("Rank tidak valid. Silakan coba lagi.")

                        if usia < 17:
                            print("Pendaftar di bawah 17 tahun tidak diizinkan.")
                        elif rank not in ["Epic", "Legend", "Mythic"]:
                            print("Rank di bawah Epic tidak diizinkan mendaftar.")
                        else:
                            pendaftar.append([nama, usia, rank])  
                            print(f"Pendaftar {nama} berhasil ditambahkan.")

                    elif admin_choice == "3":
                        if not pendaftar:
                            print("Belum ada pendaftar untuk diubah.")
                        else:
                            print (
                            """
                            Pilih data player ke-x untuk diubah
                            """
                            )
                            for i in range(len(pendaftar)):
                                print(f"\n Player ke-{i+1}\nNAMA : {pendaftar[i][0]}\nUSIA : {pendaftar[i][1]}\nRANK : {pendaftar[i][2]}")

                            while True :
                                try:
                                    idx = int(input("Pilih player ke-berapa yang ingin diubah (ketik 0 jika tidak ada): ")) - 1
                                    if 0 <= idx < len(pendaftar):  
                                        print(f"Mengubah data pendaftar: {pendaftar[idx][0]}")

                                        while True :    
                                            pendaftar[idx][0] = input("Masukkan nama baru: ")
                                            usia_baru = input("Masukkan usia : ")
                                            if usia_baru.isdigit():
                                                usia_baru = int(usia_baru)
                                                if usia_baru >= 17:
                                                    pendaftar[idx][1] = usia_baru
                                                    rank_baru = input("Masukkan rank baru (Warrior, Elite, Master, Grandmaster, Epic, Legend, Mythic): ").capitalize()
                                                    if rank_baru in ["Epic", "Legend", "Mythic"]:
                                                        pendaftar[idx][2] = rank_baru
                                                        print("Data pendaftar berhasil diubah.")
                                                        break
                                                    else :
                                                        print("Rank dibawah epic tidak boleh mendaftar atau Masukkan pilihan yang sesuai.")
                                                else :
                                                    print("player dibawah 17 tahun tidak boleh mendaftar")
                                            else :
                                                print("Usia harus berupa angka")
                                    elif idx == -1 :
                                        break
                                    else:
                                        print("Pendaftar tidak ditemukan.")
                                except ValueError:
                                    print("Input tidak valid.")

                    elif admin_choice == "4":
                        if not pendaftar:
                            print("Belum ada pendaftar.")
                        else:
                            for i, data in enumerate(pendaftar, 1):
                                print(f"{i}. Nama: {data[0]}, Usia: {data[1]}, Rank: {data[2]}")
                            try:
                                idx = int(input("Pilih nomor pendaftar yang ingin dihapus: ")) - 1
                                if 0 <= idx < len(pendaftar):
                                    del pendaftar[idx]  
                                    print("Pendaftar berhasil dihapus.")
                                else:
                                    print("Pendaftar tidak ditemukan.")
                            except ValueError:
                                print("Input tidak valid.")
                                
                    elif admin_choice == "5":
                        break

                else:
                    # Menu Pendaftar
                    print("\n=== Menu Pendaftar ===")
                    print("1. Daftar Turnamen")
                    print("2. Lihat Pendaftaran Saya")
                    print("3. Logout")
                    pendaftar_choice = input("Pilih menu: ")
                    
                    if pendaftar_choice == "1" :
                        nama = input("Masukkan nama: ")

                        # Error handling untuk usia (input angka)
                        while True:
                            try:
                                usia = int(input("Masukkan usia: "))
                                break
                            except ValueError:
                                print("Usia harus berupa angka. Silakan coba lagi.")

                        # Validasi rank dan usia
                        while True:
                            rank = input("Masukkan rank (Warrior, Elite, Master, Grandmaster, Epic, Legend, Mythic): ").capitalize()
                            if rank in ["Warrior", "Elite", "Master", "Grandmaster", "Epic", "Legend", "Mythic"]:
                                break
                            else:
                                print("Rank tidak valid. Silakan coba lagi.")

                        if usia < 17:
                            print("Pendaftar di bawah 17 tahun tidak diizinkan.")
                        elif rank not in ["Epic", "Legend", "Mythic"]:
                            print("Rank di bawah Epic tidak diizinkan mendaftar.")
                        else:
                            pendaftar.append([nama, usia, rank])  
                            print(f"Pendaftar {nama} berhasil ditambahkan.")

                    elif pendaftar_choice == "2":
                        found = False
                        for player in pendaftar:
                            if player[0] == username:
                                print(f"\nNAMA : {player[0]}\nUSIA : {player[1]}\nRANK : {player[2]}")
                                found = True
                        if not found:
                            print("Anda belum mendaftar turnamen.")
                    elif pendaftar_choice == "3":
                        break

    elif choice == "3":
        print("Terimakasih telah berpartisipasi dalam Turnamen kami")
        exit()
