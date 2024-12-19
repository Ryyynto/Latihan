def suhu(entry, exit, hasil) :  
    if entry == 1 :
        if exit == 1 : 
            print(hasil)
         
        elif exit == 2 :
            print(hasil + 273)
        
        elif exit == 3 :
            print(hasil * 4/5)

        elif exit == 4 :
            print(9/5 * hasil + 32)
        
        else :
            print("input tidak valid")

    elif entry == 2 :
        if exit == 1 : 
            print(hasil - 273)
         
        elif exit == 2 :
            print(hasil)

        elif exit == 3 :
            print(9/5 * (hasil - 273) +32)

        elif exit == 4 :
            print(4/5  * (hasil - 732))

        else :
            print("input tidak valid")

    elif entry == 3 :
        if exit == 1 : 
            print(5/9 * (hasil - 32))
         
        elif exit == 2 :
            print(5/9 * (hasil - 32) + 273)
        
        elif exit == 3 :
            print(hasil)

        elif exit == 4 :
            print(4/9 * (hasil - 32))
        
        else :
            print("input tidak valid")

    elif entry == 4 :
        if exit == 1 : 
            print(5/4 * hasil)
         
        elif exit == 2 :
            print(5/4 * hasil + 273)
        
        elif exit == 3 :
            print(9/4 * hasil + 32)

        elif exit == 4 :
            print(hasil)

        else :
            pass
            print("input tidak valid")
    
    else :
        pass
        print("input tidak valid")

print("Pilih Satuan Suhu Awal")
print("1. Celcius")
print("2. Kelvin")
print("3. Fahrenheit")
print("4. Reamur")

entry = int(input("Entry Satuan 1/2/3/4 "))

print("Pilih Satuan Suhu Tujuan")
print("1. Celcius")
print("2. Kelvin")
print("3. Fahrenheit")
print("4. Reamur")

exit = int(input("Entry Tujuan 1/2/3/4 "))

hasil = int(input("Masukkan suhu awal : "))

suhu(entry, exit, hasil)



