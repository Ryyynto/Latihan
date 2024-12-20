from matauang import *

print("Selamat datang, pilih mata uang yang anda ingin cek")
print("1. Yen")
print("2. Dollar")
print("3. Euro")
print("4. Poundsterling")

uang = int(input("Pilih mata uang : "))
nominal =  int(input("Input nominal : "))

if uang == 1 :
    print(nominal, "IDR =", yen(nominal), "Yen")
    print()
    print("Konversi ke JPY :", yen(nominal)/nominal * 100,"%")

elif uang == 2 :
    print(nominal, "IDR =", dollar(nominal), "dollar")
    print()
    print("Konversi ke USD :", dollar(nominal)/nominal * 100,"%")

elif uang == 3 :
    print(nominal, "IDR =", euro(nominal), "euro")
    print()
    print("Konversi ke EUR :", euro(nominal)/nominal * 100,"%")

elif uang == 4 :
    print(nominal, "IDR =", poundsterling(nominal), "poundsterling")
    print()
    print("Konversi ke GBP :", poundsterling(nominal)/nominal * 100,"%")

else :
    print("Input tidak  valid")