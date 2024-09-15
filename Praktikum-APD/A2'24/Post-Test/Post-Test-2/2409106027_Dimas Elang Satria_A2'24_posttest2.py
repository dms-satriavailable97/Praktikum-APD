#Input Nama Lengkap, NIM, dan Harga Beras
nama = input("Masukkan Nama :")
nim = input("Masukkan NIM :")

harga = int(input("Masukkan harga beras :"))

#Persentase diskon masing-masing merk beras
diskon_beras_mawar = 11 / 100
diskon_beras_sania = 14 / 100
diskon_beras_maknyus = 17 / 100

#Pehitungan harga beras setelah di diskon
harga_beras_mawar = harga - (harga * diskon_beras_mawar)
harga_beras_sania = harga - (harga * diskon_beras_sania)
harga_beras_maknyus = harga - (harga * diskon_beras_maknyus)

#Output hasil perhitungan
print(nama, "dengan NIM",nim  , "ingin membeli beras seharga Rp.",harga)
print ("Jika dia membeli beras Mawar ia harus membayar Rp.", harga_beras_mawar, "Setelah mendapat diskon 11%.")
print ("Jika dia membeli beras Sania ia harus membayar Rp.", harga_beras_sania, "Setelah mendapat diskon 14%.")
print ("Jika dia membeli beras Maknyus ia harus membayar Rp.", harga_beras_maknyus, "Setelah mendapat diskon 17%.")