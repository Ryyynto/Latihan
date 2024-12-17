bulan=("januari", "februari", "maret", "april", "mei", "juni", "agustus", "september", "oktober", "november", "desember")


a=input("Cek Bulan anda disini ").lower()

if a not in bulan :
    print(a, "tidak ada dalam kalender")

else :
    print("Bulan", a, "ada di kalender")