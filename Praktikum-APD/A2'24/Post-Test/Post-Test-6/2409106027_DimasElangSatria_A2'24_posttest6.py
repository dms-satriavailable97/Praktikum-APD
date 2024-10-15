users = {} 
pendaftar = {}  

while True:
    print("\n=== Program Turnamen MLBB ===")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    choice = input("Pilih menu: ")

    if choice not in ["1", "2", "3"]:
        print("Input tidak valid. Silakan pilih 1, 2, atau 3.")
        continue

    if choice == "1":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")

        if username in users:
            print("Username sudah terdaftar!")
        else:
            role = input("Pilih peran (admin/pendaftar): ").lower()
            if role not in ["admin", "pendaftar"]:
                print("Peran tidak valid, pilih 'admin' atau 'pendaftar'.")
            else:
                users[username] = {"password": password, "role": role}
                print(f"Registrasi berhasil sebagai {role}!")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nLogin berhasil sebagai {role.capitalize()}!")

            if role == "admin":
                print(f"Selamat datang, {username}!")
                while True:
                    print("\n=== Menu Admin ===")
                    print("1. Lihat Pendaftar")
                    print("2. Tambah Pendaftar")
                    print("3. Ubah Pendaftar")
                    print("4. Hapus Pendaftar")
                    print("5. Logout")
                    admin_choice = input("Pilih menu: ")

                    if admin_choice == "1":
                        if not pendaftar:
                            print("Belum ada pendaftar.")
                        else:
                            print("Daftar Pendaftar:")
                            for i, (id_peserta, data_peserta) in enumerate(pendaftar.items()):
                                print(f"{i+1}. Nama: {data_peserta['nama']}, Usia: {data_peserta['usia']}, Rank: {data_peserta['rank']}")

                    elif admin_choice == "2": 
                        nama = input("Masukkan nama: ")
                        while True:
                            try:
                                usia = int(input("Masukkan usia: "))
                                if usia >= 17:
                                    break
                                else:
                                    print("Usia harus minimal 17 tahun.")
                            except ValueError:
                                print("Usia harus berupa angka. Silakan coba lagi.")

                        while True:
                            rank = input("Masukkan rank (Warrior, Elite, Master, Grandmaster, Epic, Legend, Mythic): ").capitalize()
                            if rank in ["Warrior", "Elite", "Master", "Grandmaster", "Epic", "Legend", "Mythic"]:
                                if rank in ["Epic", "Legend", "Mythic"]:
                                    break
                                else:
                                    print("Rank di bawah Epic tidak diizinkan.")
                            else:
                                print("Rank tidak valid. Silakan coba lagi.")

                        id_pendaftar = len(pendaftar) + 1
                        pendaftar[id_pendaftar] = {"nama": nama, "usia": usia, "rank": rank}
                        print(f"Pendaftar {nama} berhasil ditambahkan.")

                    elif admin_choice == "3":  
                        if not pendaftar:
                            print("Belum ada pendaftar.")
                        else:
                            print("Daftar Pendaftar:")
                            for i, (id_peserta, data_peserta) in enumerate(pendaftar.items()):
                                print(f"{i+1}. Nama: {data_peserta['nama']}, Usia: {data_peserta['usia']}, Rank: {data_peserta['rank']}")

                            try:
                                pilihan = int(input("Pilih nomor peserta yang akan diubah: ")) - 1
                                if 0 <= pilihan < len(pendaftar):
                                    id_peserta = list(pendaftar.keys())[pilihan]
                                    peserta = pendaftar[id_peserta]

                                    nama_baru = input(f"Masukkan nama baru ({peserta['nama']}): ") or peserta['nama']

                                    while True:
                                        usia_baru = input(f"Masukkan usia baru ({peserta['usia']}): ")
                                        if usia_baru:
                                            try:
                                                usia_baru = int(usia_baru)
                                                if usia_baru >= 17:
                                                    break
                                                else:
                                                    print("Usia harus minimal 17 tahun.")
                                            except ValueError:
                                                print("Usia harus berupa angka.")
                                        else:
                                            usia_baru = peserta['usia']
                                            break

                                    while True:
                                        rank_baru = input(f"Masukkan rank baru ({peserta['rank']}): ").capitalize()
                                        if rank_baru:
                                            if rank_baru in ["Warrior", "Elite", "Master", "Grandmaster", "Epic", "Legend", "Mythic"]:
                                                if rank_baru in ["Epic", "Legend", "Mythic"]:
                                                    break
                                                else:
                                                    print("Rank di bawah Epic tidak diizinkan.")
                                            else:
                                                print("Rank tidak valid. Silakan coba lagi.")
                                        else:
                                            rank_baru = peserta['rank']
                                            break

                                    pendaftar[id_peserta]['nama'] = nama_baru
                                    pendaftar[id_peserta]['usia'] = usia_baru
                                    pendaftar[id_peserta]['rank'] = rank_baru

                                    print(f"Data pendaftar {nama_baru} berhasil diubah.")
                                else:
                                    print("Pilihan tidak valid.")
                            except ValueError:
                                print("Input harus berupa angka.")

                    elif admin_choice == "4":
                        if not pendaftar:
                            print("Belum ada pendaftar.")
                        else:
                            print("Daftar Pendaftar:")
                            for i, (id_peserta, data_peserta) in enumerate(pendaftar.items()):
                                print(f"{i+1}. Nama: {data_peserta['nama']}, Usia: {data_peserta['usia']}, Rank: {data_peserta['rank']}")

                            try:
                                pilihan = int(input("Pilih nomor peserta yang akan dihapus: ")) - 1
                                if 0 <= pilihan < len(pendaftar):
                                    id_peserta = list(pendaftar.keys())[pilihan]
                                    del pendaftar[id_peserta]
                                    print("Pendaftar berhasil dihapus.")
                                else:
                                    print("Pilihan tidak valid.")
                            except ValueError:
                                print("Input harus berupa angka.")

                    elif admin_choice == "5":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")
            elif role == "pendaftar":
                if username in pendaftar:
                    print(f"Selamat datang kembali, {pendaftar[username]['nama']}!")
                else:
                    print(f"Selamat datang, {username}!")
                while True:
                    print("\n=== Menu Pendaftar ===")
                    print("1. Daftar Turnamen")
                    print("2. Lihat Status Pendaftaran")
                    print("3. Logout")
                    pendaftar_choice = input("Pilih menu: ")

                    if pendaftar_choice == "1":  
                        if username in pendaftar:
                            print("Anda sudah terdaftar dalam turnamen.")
                        else:
                            nama = input("Masukkan nama: ")
                            while True:
                                try:
                                    usia = int(input("Masukkan usia: "))
                                    if usia >= 17:
                                        break
                                    else:
                                        print("Usia harus minimal 17 tahun.")
                                except ValueError:
                                    print("Usia harus berupa angka. Silakan coba lagi.")

                            while True:
                                rank = input("Masukkan rank (Warrior, Elite, Master, Grandmaster, Epic, Legend, Mythic): ").capitalize()
                                if rank in ["Warrior", "Elite", "Master", "Grandmaster", "Epic", "Legend", "Mythic"]:
                                    if rank in ["Epic", "Legend", "Mythic"]:
                                        break
                                    else:
                                        print("Rank di bawah Epic tidak diizinkan.")
                                else:
                                    print("Rank tidak valid. Silakan coba lagi.")

                            pendaftar[username] = {"nama": nama, "usia": usia, "rank": rank}
                            print(f"Pendaftaran berhasil untuk {nama}.")

                    elif pendaftar_choice == "2":  
                        if username in pendaftar:
                            data_saya = pendaftar[username]
                            print(f"Nama: {data_saya['nama']}, Usia: {data_saya['usia']}, Rank: {data_saya['rank']}")
                        else:
                            print("Anda belum mendaftar ke turnamen.")

                    elif pendaftar_choice == "3":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak valid.")
        else:
            print("Username atau password salah.")

    elif choice == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
