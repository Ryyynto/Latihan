from matauang import *

print("Selamat datang, pilih mata uang yang anda ingin cek")
print("1. Yen")
print("2. Dollar")
print("3. Euro")
print("4. Poundsterling")

uang = int(input("Pilih mata uang : "))
nominal =  int(input("Input nominal : "))

if uang == 1 :
    print(yen(nominal))

elif uang == 2 :
    print(dollar(nominal))

elif uang == 3 :
    print(euro(nominal))

elif uang == 4 :
    print(poundsterling(nominal))

else :
    print("Input tidak  valid")