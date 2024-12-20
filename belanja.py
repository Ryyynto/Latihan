from matauang import *

nama = input("Masukkan nama barang : ")
jumlah = int(input("Masukkan jumlah barang : "))
harga = int(input("Masukkan harga per barang (IDR) : "))

print("Pilih mata uang yang diingikan :")
print("1 - YEN")
print("2 - USD")
print("3 - EUR")
print("4 - GBP")
opsi = int(input("Masukkan pilihan anda : "))

total = jumlah * harga 

if opsi == 1 :
    print("Jumlah total belanja untuk", jumlah, nama, "adalah", yen(total), "yen")

elif opsi == 2 :
    print("Jumlah total belanja untuk", jumlah, nama, "adalah", dollar(total), "dollar")

elif opsi == 3 :
    print("Jumlah total belanja untuk", jumlah, nama, "adalah", euro(total), "euro")

elif opsi == 4 :
    print("Jumlah total belanja untuk", jumlah, nama, "adalah", poundsterling(total), "poundsterling")

else :
    print("Input tidak  valid")