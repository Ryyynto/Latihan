from sensor import *

while True :
    kalimat = input("Masukkan kalimat : ").lower()

    if kalimat == "keluar" :
        break

    else :
        hasil = sensor(kalimat)
        print(hasil)
    
