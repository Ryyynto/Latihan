while True :
    print("Pilih Satuan Suhu Awal")
    print("1. Celcius")
    print("2. Kelvin")
    print("3. Fahrenheit")
    print("4. Reamur")

    entry=input("Entry Satuan 1/2/3/4 ")
    entri=int(entry)

    if entri==1  : #Celcius
        print("Pilih Satuan Suhu Tujuan")
        print("1. Celcius")
        print("2. Kelvin")
        print("3. Fahrenheit")
        print("4. Reamur")

        exit=input("Entry Tujuan 1/2/3/4 ")
        eksit=int(exit)

        if eksit==1 : #Celcius ke Celcius
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat celcius = ", cuaca, "Derajat celcius")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        elif eksit==2 : # Celcius ke Kelvin
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat celcius = ", cuaca+273, "Derajat kelvin")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        elif eksit==3 : # Celcius ke Fahrenheit 
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat celcius = ", cuaca*9//5+32, "Derajat fahrenheit")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        elif eksit==4 : # Celcius ke Reamur
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat celcius = ", cuaca*4//5, "Derajat reamur")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        else :
            print("Masukkan satuan dengan benar")

    elif entri==2  : #Kelvin
        print("Pilih Satuan Suhu Tujuan")
        print("1. Celcius")
        print("2. Kelvin")
        print("3. Fahrenheit")
        print("4. Reamur")

        exit=input("Entry Tujuan 1/2/3/4 ")
        eksit=int(exit)

        if eksit==1 : #Kelvin ke Celcius
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat kelvin = ", cuaca-273, "Derajat celcius")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        elif eksit==2 : # Kelvin ke Kelvin
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)
            print(cuaca, "Derajat kelvin = ", cuaca, "Derajat kelvin")
            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        elif eksit==3 : # Kelvin ke Fahrenheit 
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat kelvin = ", (cuaca-273)*9//5+32, "Derajat fahrenheit")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break
        
        elif eksit==4 : # Kelvin ke Reamur
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat celcius = ", (cuaca-732)*4//5, "Derajat reamur")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        else :
            print("Masukkan satuan dengan benar")

    elif entri==3  : #Fahrenheit
        print("Pilih Satuan Suhu Tujuan")
        print("1. Celcius")
        print("2. Kelvin")
        print("3. Fahrenheit")
        print("4. Reamur")

        exit=input("Entry Tujuan 1/2/3/4 ")
        eksit=int(exit)

        if eksit==1 : #Fahrenheit ke Celcius
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat fahrenheit = ", (cuaca-32)*5//9, "Derajat celcius")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()

        elif eksit==2 : # Fahrenheit ke Kelvin
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat fahrenheit = ",  (cuaca-32)*5//9+273, "Derajat kelvin")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        elif eksit==3 : # Fahrenheit ke Fahrenheit 
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat fahrenheit = ", cuaca, "Derajat fahrenheit")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break
        
        elif eksit==4 : # Fahrenheit ke Reamur
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat fahrenheit = ", (cuaca-32)*4//9, "Derajat reamur")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        else :
            print("Masukkan satuan dengan benar")

    elif entri==4 : #Reamur
        print("Pilih Satuan Suhu Tujuan")
        print("1. Celcius")
        print("2. Kelvin")
        print("3. Fahrenheit")
        print("4. Reamur")

        exit=input("Entry Tujuan 1/2/3/4 ")
        eksit=int(exit)

        if eksit==1 : # Reamur ke Celcius
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat reamur = ", cuaca*5//4, "Derajat celcius")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        elif eksit==2 : # Reamur ke Kelvin
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat reamur = ",  cuaca*5//4+273, "Derajat kelvin")
            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()

            if jawab=="n" :
                break

        elif eksit==3 : # Reamur ke Fahrenheit 
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)
            
            print(cuaca, "Derajat reamur = ", cuaca*9//4+32, "Derajat fahrenheit")

            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        elif eksit==4 : # Reamur ke Reamur
            suhu=input("Masukkan suhu yang akan dikonversi: ")
            cuaca=int(suhu)

            print(cuaca, "Derajat reamur = ", cuaca, "Derajat reamur")
            
            jawab=input("Apakah anda ingin mengkonversi suhu lain? y/n ").lower()
            if jawab=="n" :
                break

        else :
            print("Masukkan satuan dengan benar")

    else :
        print("Masukkan satuan awal dengan benar")








    




        



