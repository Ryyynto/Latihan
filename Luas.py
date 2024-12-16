#Masukan bentuk
bentuk=input(" Masukkan Bentuk Lahan (persegi,  lingkaran, segitiga) ").strip().lower()

#Kalo salah bentuk
if bentuk not in ["persegi", "lingkaran", "segitiga"]:
    print("Tolong masukkan bentuk dengan benar")

#Ngitung Bentuk
else : 
    sisi=input(" Masukkan panjang sisi atau radius pertama ")
    radius=input(" Masukkan panjang sisi atau radius kedua ")
    v1=float(sisi)
    v2=float(radius)
     

    if bentuk=="persegi" :
        print(v1*v2, "meter")

    elif bentuk=="lingkaran" :
        print((v1+v2)*3.14, "meter")

    elif bentuk=="segitiga" :
        print(v1*v2*0.5, "meter")

    else :
        print("Tolong masukkan angka dengan benar")

   