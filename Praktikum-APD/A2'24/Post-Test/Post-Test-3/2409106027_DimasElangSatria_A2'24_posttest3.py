nama = input("Masukkan Nama Lengkap: ")
nim = input("Masukkan NIM: ")
pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
lama = int(input("Masukkan Lama Cicilan (tahun): "))

if lama==1 : 
  BungaTahunan = 0.07
  JumlahBulan = 12 
elif lama==2 : 
  BungaTahunan = 0.13
  JumlahBulan = 24 
elif lama==3 : 
  BungaTahunan = 0.19
  JumlahBulan = 36 
else :
  print ("Maaf", nama, "Opsi lama cicilan hanya tersedia untuk 1 tahun, 2 tahun dan 3 tahun")
  exit ()
  
BungaPerBulan = (BungaTahunan/12) * pinjaman
TotalBunga = BungaPerBulan * JumlahBulan
CicilanPerBulan = ((pinjaman + TotalBunga)/JumlahBulan)

print (f"{nama}, NIM: {nim}, memiliki total pinjaman Rp. {pinjaman} dengan lama cicilan {lama} tahun, sehingga jumlah cicilan per bulan: Rp. {CicilanPerBulan}")
