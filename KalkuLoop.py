#Input angka awal
awal=input("Masukkan angka awal ") 

  #Input angka akhir
akhir=input("Masukkan angka akhir ")

 #Input kelipatan
kelipatan=input("Masukkan angka kelipatan ")

#variable dan konversi data
a=int(awal)
b=int(akhir)
c=int(kelipatan)
d=range(a,b)

#Hasil
for i in range(a,b) : 
    print(c, "x", i, "=", i*c)