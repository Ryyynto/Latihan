angka1=input(" Masukkan angka pertama ")
angka2=input(" Masukkan angka kedua ")
simbol=input(" Masukkan operator ")
angka3=int(angka1)
angka4=int(angka2)

#Perkalian 
if simbol== "*" :
    print(angka3*angka4)

#Pembagian 
elif simbol== "/" :
    print(angka3/angka4)
#Pertambahan
elif simbol=="+" :
    print(angka3+angka4)

#Pengurangan
elif simbol=="-" :
    print(angka3-angka4)

#Else
else :
    print("Operator tidak terdaftar")
