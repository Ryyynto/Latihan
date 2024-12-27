chance = 3

while chance > 0 :
    tebak = input("Masukkan tebakan anda (even/odd) : ").lower()

    if tebak == "odd" : 
        print("Anda salah menebak")
        chance -= 1
        print("Anda memiliki", chance, "kesempatan lagi")

    elif  tebak == "even" : 
        print("Anda benar")
        break

if chance == 0 :
    print("Kesempatan anda telah habis")