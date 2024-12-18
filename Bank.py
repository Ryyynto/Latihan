nama = "Pak Susanto"
saldo = 10000

while True : 

    print("="*30)
    print("Selamat Datang di Bank")
    print("="*30)
    print("1. Cek Saldo")
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Transfer Uang")
    print("5. Berhenti Transaksi")
    print("="*30)

    opsi =  int(input("Masukkan pilihan (1/2/3/4/5) : "))

#SISTEM CEK SALDO

    if opsi == 1 :
        print("="*30)
        print("Saldo", nama, ":", saldo)
        print("="*30)
        print("")
        print("")
    
#SISTEM SETOR TUNAI

    elif  opsi == 2 :
        setor = int(input("Masukkan jumlah uang yang ingin disetor : "))
        if setor<0 :
            print("Mohon masukkan angka dengan benar")
            
        else :
            saldo = saldo + setor

            print("="*30)
            print("Berhasil setor tunai", setor, ", Saldo anda sekarang", saldo)
            print("="*30)
            print("")
            print("")

#SISTEM TRANSFER

    elif opsi == 3 :
        tarik = int(input("Masukkan jumlah uang yang ingin ditarik : "))
        
        if tarik > saldo :
            print("Saldo tidak cukup")
            print("="*30)
            continue

        else :
            saldo = saldo - tarik

        print("="*30)
        print("Berhasil tarik tunai", tarik, ", Saldo anda sekarang", saldo)
        print("="*30)
        print("")
        print("")

#SISTEM  TRANSFER
    elif opsi == 4 :
        transfer = int(input("Masukkan jumlah uang yang ingin trasnfer : "))
        if setor > saldo :
            print("Saldo tidak cukup")
            print("="*30)
            continue

        else :
             saldo = saldo - transfer

        print("="*30)
        print("Berhasil tarik tunai", tarik, ", Saldo anda sekarang", saldo)
        print("="*30)
        print("")
        print("")
#KALO SELESAI

    elif opsi == 5 :
        print("Terimakasih")
        break

#KALO SALAH MASUKIN INPUT AWAL

    else :
        print("Tolong masukkan input dengan benar")
        continue
        

    

        
