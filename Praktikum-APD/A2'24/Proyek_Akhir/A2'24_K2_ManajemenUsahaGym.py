import csv
from datetime import datetime
import os
import time
from rich.progress import track
from time import sleep 

class style():
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'
    
    CBLACK  = '\33[30m'
    CRED    = '\33[31m' 
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'
    
    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'
    
    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'
    
    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

FILE_ADMIN = 'admin.csv'
FILE_PENGGUNA = 'pengguna.csv'
FILE_PRODUK = 'produk.csv'
FILE_ANGGOTA = 'anggota.csv'

admin = ('fajar', 'fajar123')
pengguna = {}
keranjang = {'addons': [], 'membership': []}
username_login = None
daftar_anggota=[]

def initialize_data():
    # Periksa apakah file sudah ada; jika ada, biarkan saja
    try:
        with open(FILE_PRODUK, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Kategori', 'Nama', 'Harga', 'Deskripsi'])  # Header
            writer.writerows([
                ['Addons', 'Air Mineral', 10000,'-'],
                ['Addons', 'Steroid', 50000,'-'],
                ['Addons', 'Protein Powder', 150000,'-'],
                ['Membership', 'Basic', 300000,'Akses penuh ke area gym utama dengan fasilitas dasar seperti peralatan kardio dan angkat beban.\n Tidak termasuk kelas grup atau fasilitas tambahan (Masa Berlaku 1 bulan).'],
                ['Membership', 'Premium', 750000,'Akses ke seluruh fasilitas gym, termasuk kelas grup seperti yoga dan pilates.\n Juga mencakup satu sesi konsultasi bulanan dengan personal trainer (Masa Berlaku 3 Bulan).'],
                ['Membership', 'Elite', 1500000,'Akses tak terbatas ke semua fasilitas gym, termasuk kelas grup, ruang sauna, dan ruang uap.\n Menyediakan 4 sesi personal trainer per bulan dan akses 24 jam (Masa Berlaku 6 Bulan).'],
            ])
            print("Data awal berhasil diinisialisasi!")
    except FileExistsError:
        print("Data sudah ada. Tidak perlu inisialisasi ulang.")

# Fungsi dasar untuk menyimpan data ke CSV
def simpan_ke_csv(nama_file, data, header):
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

# Fungsi dasar untuk memuat data dari CSV
def muat_dari_csv(nama_file, header):
    data = []
    if os.path.exists(nama_file):
        with open(nama_file, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=header)
            next(reader)  # Skip header
            data = [row for row in reader]
    return data

# Fungsi untuk menyimpan data pengguna
def simpan_pengguna():
    pengguna_data = [{"Username": username, "Password": data['password'], "Role": data['role']} for username, data in pengguna.items()]
    simpan_ke_csv(FILE_PENGGUNA, pengguna_data, ["Username", "Password", "Role"])

# Fungsi untuk memuat data pengguna
def muat_pengguna():
    pengguna_data = muat_dari_csv(FILE_PENGGUNA, ["Username", "Password", "Role"])
    for row in pengguna_data:
        pengguna[row["Username"]] = {"password": row["Password"], "role": row["Role"]}

def muat_anggota():
    """Fungsi untuk memuat data anggota dari file CSV."""
    global daftar_anggota
    try:
        with open('anggota.csv', mode='r') as file:
            reader = csv.DictReader(file)
            daftar_anggota = [
                {
                    'nama': row['Nama'],
                    'membership': row['Membership'],
                    'tanggal_pembelian': datetime.strptime(row['Tanggal Pembelian'], "%Y-%m-%d %H:%M:%S"),
                    'tanggal_kadaluarsa': datetime.strptime(row['Tanggal Kadaluarsa'], "%Y-%m-%d %H:%M:%S"),
                }
                for row in reader
            ]
    except FileNotFoundError:
        daftar_anggota = []

def simpan_anggota():
    """Menyimpan data anggota ke file CSV."""
    with open(FILE_ANGGOTA, mode='w', newline='') as file:
        fieldnames = ['Nama', 'Membership', 'Tanggal Pembelian', 'Tanggal Kadaluarsa']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for anggota in daftar_anggota:
            writer.writerow({
                'Nama': anggota['nama'],
                'Membership': anggota['membership'],
                'Tanggal Pembelian': anggota['tanggal_pembelian'].strftime("%Y-%m-%d"),
                'Tanggal Kadaluarsa': anggota['tanggal_kadaluarsa'].strftime("%Y-%m-%d"),
            })

# Fungsi untuk menyimpan data admin
def simpan_admin():
    admin_data = [{"Username": admin[0], "Password": admin[1]}]
    simpan_ke_csv(FILE_ADMIN, admin_data, ["Username", "Password"])

# Fungsi untuk menyimpan semua data
def simpan_semua_data():
    simpan_pengguna()
    simpan_admin()

def proses():
    for _ in track(range(100), description='[read]Sedang Memuat'):
        sleep(0.01)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def input_salah() :
    print(style.CRED+style.CBOLD +"| Input Tidak Valid, Masukkan Input Yang Benar !"+ style.CEND)

def enter() :
    while True :
        pilih = input("\n| Tekan Enter Untuk Kembali...")
        if pilih == "":
            break
        else :
            input_salah()
            sleep (1)

    
def tampilan_utama() :
    print(style.CBLUE+"============================================================================="+style.CEND)
    print(style.CYELLOW+style.CBOLD+"""
    ||                          SELAMAT DATANG                         ||  
    ||                                DI                               ||
    ||     ______  __  __  __    __  ______  __   __  __  ______       ||
    ||    /\  ___\/\ \_\ \/\ "-./  \/\  __ \/\ "-.\ \/\ \/\  __ \      ||
    ||    \ \ \__ \ \____ \ \ \-./\ \ \  __ \ \ \-.  \ \ \ \  __ \     ||
    ||     \ \_____\/\_____\ \_\ \ \_\ \_\ \_\ \_\\\\"\_\ \_\ \_\ \_\    || 
    ||      \/_____/\/_____/\/_/  \/_/\/_/\/_/\/_/ \/_/\/_/\/_/\/_/    ||
    ||                                                                 ||
    ||                              OLEH                               ||
    ||    KELOMPOK 2A2 -  INFORMATIKA 2024 - UNIVERSITAS MULAWARMAN    ||
"""+style.CEND)
    print(style.CBLUE+"============================================================================="+style.CEND)

def register():
    while True :
        clear()
        tampilan_utama()
        print("""
========================================================================
    ||            ___ ___ ___ ___ ___ _____ ___ ___              ||
    ||            | _ \ __/ __|_ _/ __|_   _| __| _ \            ||
    ||            |   / _| (_ || |\__ \ | | | _||   /            ||
    ||            |_|_\___\___|___|___/ |_| |___|_|_\            ||        
    ||                                                           ||
=======================================================================
    """)
        username_baru = input("Masukkan Username: ").strip()
        if username_baru in pengguna or username_baru in admin :
            print(style.CYELLOW+'Username telah digunakan. Masukkan username lain !'+style.CEND)
            sleep(1)
        elif " " in username_baru or not username_baru:
            print(style.CYELLOW +"Username tidak boleh mengandung spasi atau kosong. Masukkan username lain."+ style.CEND)
            sleep(1)
        else :
            while True :
                password_baru = input("Masukkan Password: ")
                if " " in password_baru or not password_baru :
                    print(style.CYELLOW +'Password tidak boleh mengandung spasi atau kosong. Masukkan password lain.'+style.CEND)
                    sleep(1)
                else :
                    pengguna[username_baru] = {'password': password_baru, 'role' : 'pengguna'}
                    for _ in track(range(100), description='[read]Register Berhasil, Melanjutkan ke Halaman Utama'):
                        sleep(0.01)
                    simpan_pengguna()
                    break
        break

def login():
    global username_login
    muat_pengguna()
    while True :
        clear()
        tampilan_utama()
        print("""
    ========================================================================
        ||                     _    ___   ___ ___ _  _                ||
        ||                    | |  / _ \ / __|_ _| \| |               ||
        ||                    | |_| (_) | (_ || || .` |               ||
        ||                    |____\___/ \___|___|_|\_|               ||
        ||                                                            ||
    =======================================================================
    """)
        username = input("| Masukkan username: ")
        password = input("| Masukkan password: ")

        if username ==admin[0] and password == admin[1]:
            proses()
            admin_utama()
            break
        elif username in pengguna and pengguna[username]['password'] == password:
            print(f"\nLogin berhasil sebagai {username}\n")    
            if pengguna[username]['role'] == 'pengguna':
                username_login = username
                proses()
                menu_pengguna()
                break
            elif pengguna[username]['role'] == 'admin':
                proses()
                menu_admin()
                break
        else:
            print(style.CRED+"Login gagal! Username atau password salah."+style.CEND)
            sleep(1)



def logout() :
    print("========================================================================")
    print("|           Terimakasih Telah Mengunjungi Program GYMANIA !            |")
    print("========================================================================")
    exit()

def beli_produk():
    while True :
        clear()
        tampilan_pengguna()
        print("""
===========================================
|                BELI PRODUK              |
===========================================
|      ADDONS       |     MEMBERSHIP      |
===========================================""")
        pilih_beli= input('| Produk apa yang ingin dibeli? ').lower()
        if pilih_beli == 'addons' :
            beli_addons()
            break
        elif pilih_beli == 'membership' :
            beli_membership()
            break
        else :
            input_salah()
            sleep(1)

def beli_addons() :
    addons = []

    try:
        with open(FILE_PRODUK, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                kategori = row[0]
                nama = row[1]
                harga = row[2]

                # Kelompokkan berdasarkan kategori
                if kategori.lower() == 'addons':
                    addons.append((nama, harga))

        while True :
            clear()
            tampilan_pengguna()
            if addons :
                print("""
===========================================
|               DAFTAR PRODUK             |
===========================================
|       Nama           |    Price list    |""")
                print("===========================================")
                print("|                  ADDONS                 |")
                print("===========================================")
            
                for i, (nama, harga) in enumerate(addons, 1):
                    print(f"[{i}]. {nama:<23} Rp.{harga:<10}|")
                print("===========================================")

                try:
                    pilihan = int(input("Pilih ID Addons Yang Ingin Dibeli: ")) - 1
                    if 0 <= pilihan < len(addons):
                        nama, harga = addons[pilihan]
                        harga = int(harga)
                        jumlah = int(input("Masukkan Jumlah Yang Ingin Dibeli: "))
                        if jumlah >= 1:
                            total_harga = harga * jumlah
                            keranjang['addons'].append((nama, total_harga, jumlah))
                            proses()
                            print(f"{jumlah}x '{nama}' berhasil dimasukkan ke keranjang dengan total Rp{total_harga}!")
                            sleep(1)
                            break
                        else:
                            input_salah()
                    else:
                        input_salah()
                        sleep(1)
                except ValueError:
                    input_salah()
                    sleep(1)

            if not addons :
                print("Addons kosong. Tambahkan addons terlebih dahulu.")
                sleep(1)
                break
    except FileNotFoundError:
        print("File belum ditemukan. Inisialisasi data terlebih dahulu.")


def beli_membership():
    membership = []

    try:
        with open(FILE_PRODUK, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                kategori = row[0]
                nama = row[1]
                harga = row[2]
                deskripsi = row[3]

                # Kelompokkan berdasarkan kategori
                if kategori.lower() == 'membership':
                    membership.append((nama, harga, deskripsi))

        while True :
            clear()
            tampilan_pengguna()
            
            if keranjang['membership']:
                print("Anda sudah memiliki membership dalam keranjang. Tidak dapat membeli membership lagi.")
                sleep(1)
                break

            if  membership :
                print("""
===========================================
|               DAFTAR PRODUK             |
===========================================
|       Nama           |    Price list    |""")    
            print("===========================================")
            print("|               MEMBERSHIP                |")
            print("===========================================")

            for i, (nama, harga, deskripsi) in enumerate(membership, 1):
                print(f"[{i}]. {nama:<23} Rp.{harga:<10}|")
            print("===========================================")
            try :
                pilihan = int(input("| Pilih nomor membership yang ingin dibeli: ")) - 1
                if 0 <= pilihan < len(membership):
                    nama, harga, deskripsi = membership[pilihan]
                    harga = int(harga)
                    print(f"\nSetelah memesan {nama} Membership, Anda akan mendapatkan:")
                    print(deskripsi)
                    while True :
                        konfirmasi = input("\n| Apakah Anda ingin melanjutkan pembelian membership ini? (ya/tidak): ").lower()
                        if konfirmasi == 'ya':
                            keranjang['membership'].append((nama, harga))
                            proses()
                            print(f"Membership '{nama}' Berhasil Dimasukkan Ke Keranjang!")
                            sleep(1)
                            clear()
                            return
                        elif konfirmasi == 'tidak' :
                            print('Pembelian Membership Dibatalkan.')
                            sleep(1)
                            clear()
                            return
                        else:
                            input_salah() 
                            sleep(1)
                else :
                    input_salah()
                    sleep(1)
                    clear()
            except ValueError :
                input_salah()
                sleep(1)
                clear()

            if not membership:
                print("Membership kosong. Tambahkan membership terlebih dahulu.")
    except FileNotFoundError:
        print("File belum ditemukan. Inisialisasi data terlebih dahulu.")


def menu_keranjang() :
    while True :
        clear()
        tampilan_pengguna()
        print("""
| [1] Lihat Keranjang
| [2] Hapus Keranjang
| [3] Checkout Keranjang
""")
        pilih= input("Masukkan Pilihan Anda :")
        if pilih == '1':
            lihat_keranjang()
            break
        elif pilih == '2':
            hapus_produk_keranjang()
            break
        elif pilih == '3' :
            checkout_keranjang()
            break
        else :
            input_salah()
            sleep(1)
            clear()

def lihat_keranjang() :
    clear()
    tampilan_pengguna()
    if not keranjang['membership'] and not keranjang['addons']:
        print("Keranjang Anda kosong, silakan memesan produk di GYM kami terlebih dahulu.")
        enter()
    
    print("""===========================================
|             KERANJANG BELANJA           |
===========================================
|       PRODUK           |    TOTAL       |""")
    print("===========================================")
    print("|                  MEMBERSHIP             |")
    print("===========================================")
    
    if keranjang['membership']:
        for nama, harga in keranjang['membership']:
            print(f"- {nama}: \t Rp{harga}")

    else:
        print('-')
    
    print("===========================================")
    print("|                  ADDONS                 |")
    print("===========================================")
    
    if keranjang['addons']:
        b = 0
        for nama, total_harga, jumlah in keranjang['addons']:
            print(f"[{b+1}] {nama} (x{jumlah}): \t Rp{total_harga}")

    else:
        print('-')
    print("===========================================")

    while True :
        pilih = input("\n Tekan Enter Untuk Kembali...")
        if pilih == "":
            menu_pengguna()
            break
        else :
            input_salah()
            sleep (1)

def hapus_produk_keranjang():
    clear()
    tampilan_pengguna()
    if not keranjang['membership'] and not keranjang['addons']:
        print("Keranjang Anda kosong, silakan memesan produk di GYM kami terlebih dahulu.")
        sleep(1)
        return


    while True:
        clear()
        tampilan_pengguna()
        print("===========================================")
        print("|                HAPUS KERANJANG          |")
        print("===========================================")
        
        if keranjang['membership']:
            print("Membership:")
            for i, (nama, harga) in enumerate(keranjang['membership'], start=1):
                print(f"[{i}] {nama} - Rp{harga}")
                print("===========================================")
        else:
            print("Membership kosong.")

        if keranjang['addons']:
            print("\nAddons:")
            for i, (nama, total_harga, jumlah) in enumerate(keranjang['addons'], start=1):
                print(f"[{i}] {nama} (x{jumlah}) - Rp{total_harga}")
        else:
            print("Addons kosong.")
        print("===========================================")

        try:
            jenis = input("Ingin menghapus dari [1] Membership atau [2] Addons? (1/2): ")
            if jenis == "1" and keranjang['membership']:
                nomor = int(input("Masukkan nomor membership yang ingin dihapus: "))
                if 1 <= nomor <= len(keranjang['membership']):
                    produk = keranjang['membership'].pop(nomor - 1)
                    proses()
                    print(f"Membership '{produk[0]}' berhasil dihapus dari keranjang.")
                    sleep(1)
                else:
                    input_salah()
                    sleep(1)
                break
            elif jenis == "2" and keranjang['addons']:
                nomor = int(input("Masukkan nomor addons yang ingin dihapus: "))
                if 1 <= nomor <= len(keranjang['addons']):
                    produk = keranjang['addons'].pop(nomor - 1)
                    proses()
                    print(f"Addons '{produk[0]}' berhasil dihapus dari keranjang.")
                    sleep(1)
                else:
                    input_salah()
                    sleep(1)
                break
            else:
                input_salah()
                sleep(1)
        except ValueError:
            input_salah()
            sleep(1)

    print("===========================================")


def checkout_keranjang():
    clear()
    tampilan_pengguna()
    if not keranjang['membership'] and not keranjang['addons']:
        print("Keranjang Anda kosong, silakan memesan produk di GYM kami terlebih dahulu.")
        sleep(1)
        return
    
    total = 0
    print("""===========================================
|             KERANJANG BELANJA           |
===========================================
|       PRODUK           |    TOTAL       |""")
    print("===========================================")
    print("|                  MEMBERSHIP             |")
    print("===========================================")
    
    if keranjang['membership']:
        for nama, harga in keranjang['membership']:
            print(f"- {nama}: \t Rp{harga}")
            total += harga
    else:
        print('-')
    
    print("===========================================")
    print("|                  ADDONS                 |")
    print("===========================================")
    
    if keranjang['addons']:
        b = 0
        for nama, harga_total, jumlah in keranjang['addons']:
            print(f"[{b+1}] {nama} (x{jumlah}): \t Rp{harga_total}")
            total += harga_total
    else:
        print('-')
    print("===========================================")

    print(f"Total Pembayaran: Rp{total}")
    
    while True :
        konfirmasi = input("| Apakah Anda ingin melanjutkan pesanan? (ya/tidak): ").lower()
        if konfirmasi == 'ya':
            nama_pengguna = input("| Masukkan Nama Pengguna :")
            from datetime import datetime, timedelta
            tanggal_pembelian = datetime.now()

            pembayaran(total)
            
            # Mendapatkan masa berlaku membership
            if keranjang['membership']:
                membership_type = keranjang['membership'][0][0]
                if membership_type == 'Basic':
                    masa_berlaku = timedelta(days=30)
                elif membership_type == 'Premium':
                    masa_berlaku = timedelta(days=90)
                elif membership_type == 'Elite':
                    masa_berlaku = timedelta(days=180)
                
                tanggal_kadaluarsa = tanggal_pembelian + masa_berlaku
                daftar_anggota.append = {
                    'nama': nama_pengguna,
                    'membership': membership_type,
                    'tanggal_pembelian': tanggal_pembelian,
                    'tanggal_kadaluarsa': tanggal_kadaluarsa
                }
                simpan_anggota()
            proses()
            print("Pesanan berhasil diproses.")
            keranjang['membership'] = []
            keranjang['addons'] = []
            break
        elif konfirmasi == 'tidak':
            print("Pesanan dibatalkan.")
            break
        else :
            input_salah()
    
    sleep(2)

def pembayaran(total):
    while True:
        try :
            uang_dibayar = int(input("Masukkan jumlah uang yang dibayar: Rp."))
            if uang_dibayar >= 1 :
                if uang_dibayar >= total:
                    kembalian = uang_dibayar - total
                    print(f"Pembayaran berhasil. Uang kembalian: Rp{kembalian}")
                    break
                else:
                    print(f"Uang yang dibayar kurang. Bayar ulang !")
            else :
                input_salah()
                sleep(1)
                clear()
        except ValueError :
            input_salah()
            sleep(1)



def lihat_anggota_saya():
    clear()
    tampilan_pengguna()

    if not username_login:
        print("Anda harus login terlebih dahulu!")
        enter()
        return

    anggota_saya = [anggota for anggota in daftar_anggota if anggota['nama'].lower() == username_login.lower()]

    print("========================================")
    print("|          STATUS KEANGGOTAAN          |")
    print("========================================")
    
    if anggota_saya:
        for anggota in anggota_saya:
            print(f"Nama: {anggota['nama']}")
            print(f"Membership: {anggota['membership']}")
            print(f"Tanggal Pembelian: {anggota['tanggal_pembelian'].strftime('%d-%m-%Y')}")
            print(f"Tanggal Kadaluarsa: {anggota['tanggal_kadaluarsa'].strftime('%d-%m-%Y')}")
            print("----------------------------------------")
    else:
        print("Anda belum memiliki membership yang aktif.")
    
    input("Tekan Enter untuk kembali.")

def lihat_semua_anggota():
    daftar_anggota=[]
    try :
        with open(FILE_ANGGOTA, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    nama = row[0]
                    membership = row[1]
                    tanggal_pembelian  = row[2]
                    tanggal_kadaluarsa = row[3]
                    daftar_anggota.append((nama,membership,tanggal_pembelian,tanggal_kadaluarsa))

        if daftar_anggota :
            print("========================================================")
            print("|                 DATA SEMUA ANGGOTA                   |")
            print("========================================================")
            for i, (nama,membership,tanggal_pembelian,tanggal_kadaluarsa) in enumerate(daftar_anggota, 1):
                print(f"[{i}]\tNama \t\t\t: {nama}")
                print(f"\tMembership \t\t: {membership}")
                print(f"\tTanggal Pembelian \t: {tanggal_pembelian}")
                print(f"\tTanggal Kadaluarsa \t: {tanggal_kadaluarsa}")
                print("-----------------------------------------------------------")
                enter()
        else:
            print("Belum ada anggota yang terdaftar.")

    except FileNotFoundError :
        print("File belum ditemukan. Inisialisasi data terlebih dahulu.")

    


def lihat() :
    addons = []
    membership = []

    try:
        with open(FILE_PRODUK, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                kategori = row[0]
                nama = row[1]
                harga = row[2]

                # Kelompokkan berdasarkan kategori
                if kategori.lower() == 'addons':
                    addons.append((nama, harga))
                elif kategori.lower() == 'membership':
                    membership.append((nama, harga))

        # Tampilkan Addons
        if addons or membership :
            print("""
===========================================
|               DAFTAR PRODUK             |
===========================================
|       Nama           |    Price list    |""")
        print("===========================================")
        print("|                  ADDONS                 |")
        print("===========================================")
        
        for i, (nama, harga) in enumerate(addons, 1):
            print(f"[{i}]. {nama:<23} Rp.{harga:<10}|")
        
        print("===========================================")
        print("|               MEMBERSHIP                |")
        print("===========================================")

        for i, (nama, harga) in enumerate(membership, 1):
            print(f"[{i}]. {nama:<23} Rp.{harga:<10}|")
        print("===========================================")

        if not addons and not membership:
            print("Produk kosong. Tambahkan produk terlebih dahulu.")
    except FileNotFoundError:
        print("File belum ditemukan. Inisialisasi data terlebih dahulu.")



def tambah() :
    while True :
        clear()
        tampilan_admin()
        kategori = input("Masukkan kategori (Addons/Membership): ").capitalize()
        if kategori == 'Addons' or kategori == 'Membership' :
            while True :
                clear()
                tampilan_admin()
                nama = input("Masukkan nama produk: ").strip()
                if " " in nama or not nama:
                    print(style.CYELLOW +"Nama Addons tidak boleh mengandung spasi atau kosong. Masukkan nama addons lain."+ style.CEND)
                else :
                    try :
                        harga = int(input("Masukkan harga produk: "))
                        deskripsi = input("Masukkan deskripsi produk :")
                        with open(FILE_PRODUK, mode='a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([kategori, nama, harga, deskripsi])
                        proses()
                        print(f"Produk '{nama}' berhasil ditambahkan!")
                        sleep(1)
                        break
                    except ValueError:
                        input_salah()
                        sleep(1)
            break
        else :
            input_salah()
            sleep(1)


def edit():
    clear()
    tampilan_admin()
    lihat()
    nama_produk = input("Masukkan nama produk yang ingin diperbarui: ")
    ada = False
    edit_baris = []

    with open(FILE_PRODUK, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ambil header
        edit_baris.append(header)  # Tambahkan header ke edit_baris
        for row in reader:
            if row[1].lower() == nama_produk.lower():
                ada = True
                print(f"Produk ditemukan: Kategori: {row[0]}, Nama: {row[1]}, Harga: {row[2]}, Deskripsi: {row[3]}")

                kategori_baru = input("Masukkan kategori (Addons/Membership) (Kosongkan jika tidak diubah): ").capitalize().strip()
                if kategori_baru not in ['', 'Addons', 'Membership']:
                    print("Kategori tidak valid! Perubahan dibatalkan.")
                    sleep(1)
                    edit_baris.append(row)
                    continue  # Lanjutkan ke baris berikutnya
                
                nama_baru = input("Masukkan nama baru (Kosongkan jika tidak diubah): ").strip()
                
                try:
                    harga_baru = input("Masukkan harga baru (Kosongkan jika tidak diubah): ").strip()
                    harga_baru = int(harga_baru) if harga_baru else row[2]
                    deskripsi_baru = input("Masukkan Deskripsi Baru :").strip
                except ValueError:
                    print("Harga harus berupa angka! Perubahan dibatalkan.")
                    sleep(1)
                    edit_baris.append(row)
                    continue  # Lanjutkan ke baris berikutnya
                
                # Perbarui data produk
                row[0] = kategori_baru if kategori_baru else row[0]
                row[1] = nama_baru if nama_baru else row[1]
                row[2] = harga_baru if harga_baru else row[2]
                row[3] = deskripsi_baru if deskripsi_baru else row[3]
                proses()
                print("Produk berhasil diperbarui!")
            
            # Tambahkan baris ke edit_baris
            edit_baris.append(row)

    if not ada:
        print("Produk tidak ditemukan.")
        sleep(1)

    # Simpan perubahan ke file
    with open(FILE_PRODUK, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(edit_baris)

            
def hapus():
    clear()
    tampilan_admin()
    lihat()
    nama_produk = input("Masukkan nama produk yang ingin dihapus: ")
    found = False
    updated_rows = []

    with open(FILE_PRODUK, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ambil header
        for row in reader:
            if row[1].lower() != nama_produk.lower():
                updated_rows.append(row)
            else:
                found = True

    if found:
        proses()
        print(f"Produk '{nama_produk}' berhasil dihapus!")
        sleep(1)
    else:
        print("Produk tidak ditemukan.")
        sleep(1)

    # Tulis ulang data ke file
    with open(FILE_PRODUK, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Tulis header
        writer.writerows(updated_rows)          
            

def buat_admin():
    while True:
        clear()
        tampilan_admin()
        username_baru = input("Masukkan Username Admin Baru: ").strip()
        if username_baru in pengguna or username_baru in admin :
            print(style.CYELLOW+'Username telah digunakan. Masukkan username lain !'+style.CEND)
            sleep(1)
        elif " " in username_baru or not username_baru :
            print(style.CYELLOW +"Username tidak boleh mengandung spasi atau kosong. Masukkan username lain."+ style.CEND)
            sleep(1)
        else:
            password_baru = input("Masukkan Password Baru: ")
            pengguna[username_baru] = {'password': password_baru, 'role': 'admin'}
            proses()
            print("Akun admin berhasil ditambahkan!\n")
            sleep(1)
            simpan_pengguna()
            break

def tampilkan_admin() :
    admin = []

    try:
        with open(FILE_PENGGUNA, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                username = row[0]
                password = row[1]
                role = row[2]

                # Kelompokkan berdasarkan kategori
                if role.lower() == 'admin':
                    admin.append((username, password))

        # Tampilkan Addons
        if admin :
            print("""
===========================================
|               DAFTAR ADMIN              |
===========================================
|       Username         |    Password    |""")
            print("===========================================")
            
            for i, (username, password) in enumerate(admin, 1):
                print(f"[{i}]. {username:<23} \t{password:<10}|")
            print("===========================================")
        

        if not admin :
            print("Admin kosong. Tambahkan akun admin terlebih dahulu.")
            sleep(1)
    except FileNotFoundError:
        print("File belum ditemukan. Inisialisasi data terlebih dahulu.")    

def hapus_admin():
    clear()
    tampilan_admin()
    tampilkan_admin()
    
    # Cek apakah ada admin yang terdaftar
    admin = []
    try:
        with open(FILE_PENGGUNA, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[2].lower() == 'admin':
                    admin.append((row[0], row[1]))
    except FileNotFoundError:
        print("File belum ditemukan. Inisialisasi data terlebih dahulu.")
        return

    # Jika tidak ada admin, keluar dari fungsi
    if not admin:
        sleep(1)
        return

    # Lanjutkan proses jika admin tersedia
    nama_admin = input("Masukkan username admin yang ingin dihapus: ")
    ada = False
    edit_baris = []

    with open(FILE_PENGGUNA, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ambil header
        for row in reader:
            if row[0] != nama_admin:  # row[0] != nama_admin True: Jika nilai di row[0] tidak sama dengan nama_admin. False: Jika nilai di row[0] sama dengan nama_admin.
                edit_baris.append(row)
            else:
                ada = True

    if ada:
        proses()
        print(f"Admin dengan username '{nama_admin}' berhasil dihapus!")
        sleep(1)
    else:
        print(f"Admin dengan username '{nama_admin}' tidak ditemukan.")
        sleep(1)

    with open(FILE_PENGGUNA, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  
        writer.writerows(edit_baris)


# def tampilan_admin_utama() :
#     print("""
# =============================================================================
#          __  __ _____ _   _ _   _      _    ____  __  __ ___ _   _     _ 
#         |  \/  | ____| \ | | | | |    / \  |  _ \|  \/  |_ _| \ | |   / |
#         | |\/| |  _| |  \| | | | |   / _ \ | | | | |\/| || ||  \| |   | |
#         | |  | | |___| |\  | |_| |  / ___ \| |_| | |  | || || |\  |   | |
#         |_|  |_|_____|_| \_|\___/  /_/   \_\____/|_|  |_|___|_| \_|   |_|

# =============================================================================           
# """)

def admin_utama():
    while True :
        clear()
        tampilan_admin()
        print("""
| [1] lihat produk
| [2] Tambah produk
| [3] Edit produk
| [4] Hapus produk
| [5] Lihat anggota
| [6] buat akun admin
| [7] hapus akun admin
| [8] Logout
    """)
        pilihan = input("Masukkan pilihan anda = ")
        if pilihan == '1':
            lihat()
            enter()
        elif pilihan == '2':
            tambah()
        elif pilihan == '3':
            edit()
        elif pilihan == '4':
            hapus()
        elif pilihan == '5':
            lihat_semua_anggota()
        elif pilihan == '6':
            buat_admin()
        elif pilihan == '7':
            hapus_admin()
        elif pilihan == '8':
            proses()
            break
        else:
            print("Pilihan tidak valid")
            sleep(1)

def tampilan_admin() :
    print("""
=============================================================================
         __  __ _____ _   _ _   _      _    ____  __  __ ___ _   _ 
        |  \/  | ____| \ | | | | |    / \  |  _ \|  \/  |_ _| \ | |
        | |\/| |  _| |  \| | | | |   / _ \ | | | | |\/| || ||  \| |
        | |  | | |___| |\  | |_| |  / ___ \| |_| | |  | || || |\  |
        |_|  |_|_____|_| \_|\___/  /_/   \_\____/|_|  |_|___|_| \_|
          
=============================================================================
""")
def menu_admin():
    while True :
        clear()
        tampilan_admin()
        print("""
| [1] Lihat Produk
| [2] Tambah Produk
| [3] Edit Produk
| [4] Hapus Produk
| [5] Lihat Anggota
| [6] Logout
""")
        pilihan = input("Masukkan pilihan anda = ")
        if pilihan == '1':
            lihat()
            enter()
        elif pilihan == '2':
            tambah()
        elif pilihan == '3':
            edit()
        elif pilihan == '4':
            hapus()
        elif pilihan == '5':
            lihat_semua_anggota()
        elif pilihan == '6':
            proses()
            break
        else:
            print("Pilihan tidak valid")
            sleep(1)

def tampilan_pengguna() :
    print("""
=============================================================================
     __  __ _____ _   _ _   _   ____  _____ __  __ ____  _____ _     ___ 
    |  \/  | ____| \ | | | | | |  _ \| ____|  \/  | __ )| ____| |   |_ _|
    | |\/| |  _| |  \| | | | | | |_) |  _| | |\/| |  _ \|  _| | |    | | 
    | |  | | |___| |\  | |_| | |  __/| |___| |  | | |_) | |___| |___ | | 
    |_|  |_|_____|_| \_|\___/  |_|   |_____|_|  |_|____/|_____|_____|___|

=============================================================================
""")

def menu_pengguna():
    while True:
        clear()
        tampilan_pengguna()
        print("""                                                                                                                                                                            
| [1] Lihat Produk
| [2] Beli Produk
| [3] Keranjang
| [4] Lihat Status Keanggotaan Saya
| [5] Logout
""")
        
        pilihan = input("| Masukkan Pilihan Anda = ")
        if pilihan == '1':
            lihat()
            enter()
        elif pilihan == '2':
            beli_produk()
        elif pilihan == '3':
            menu_keranjang()
        elif pilihan == '4':
            lihat_anggota_saya()
        elif pilihan == '5':
            proses()
            break
        else:
            input_salah()
            sleep(1)


def menu():
    initialize_data()
    while True:
        clear()
        tampilan_utama()
        print("""
|   [1] Register
|   [2] Login
|   [3] Logout
""")

        pilihan = input("\nPilih Menu: ")

        if pilihan == '1':
            register()
        elif pilihan == '2' :
            login()
        elif pilihan == '3' :
            logout()
            simpan_semua_data()
            sleep(1)
            break
            
        else:
            input_salah()
            sleep(1)

menu()