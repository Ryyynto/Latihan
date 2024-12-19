angka1 = int(input("Masukkan angka pertama : "))
angka2 = int(input("Masukkan angka kedua : "))
angka3 = int(input("Masukkan angka ketiga : "))
tuple = (angka1, angka2, angka3)

cari = int(input("Masukkan angka yang ingin dicari : "))
if cari in tuple :
    print("Angka", cari, "ada didalam tuple")

else :
    print("Angka", cari, "tidak ada didalam tuple")

awal = int(input("Masukkan indeks awal (0-based) : "))
akhir = int(input("Masukkan indeks akhir (Exclusive) : "))
panjang = len(tuple)

if awal >= 0 :
    if  akhir > panjang :
        print("Input tidak valid")

    elif akhir < 0 : 
        print("Input tidak valid")

    else :
        print(tuple[awal : akhir])

elif awal < 0 :
    print("Input tidak valid")

elif awal >= akhir :
    print("Input tidak valid")




