Pinjaman = int(input("Jumlah Pinjaman : "))
Lama = int(input("Lama Cicilan (tahun) : "))

if Lama==1 : 
  BungaTahunan = 0.07
  JumlahBulan = 12 
elif Lama==2 : 
  BungaTahunan = 0.13
  JumlahBulan = 24 
elif Lama==3 : 
  BungaTahunan = 0.19
  JumlahBulan = 36 
else :
  print ("Opsi lama cicilan hanya tersedia untuk 1 tahun, 2 tahun dan 3 tahun.")
  exit ()
  
BungaPerBulan = (BungaTahunan/12) * Pinjaman
TotalBunga = BungaPerBulan * JumlahBulan
CicilanPerBulan = ((Pinjaman + TotalBunga)/JumlahBulan)

print ("Cicilan Per Bulan = Rp", CicilanPerBulan)
