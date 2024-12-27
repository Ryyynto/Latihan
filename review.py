toxic = ["anjing", "babi", "kampret", "monyet"]

while True : 
    kata = input("Masukkan kalimat :").lower()
    
    if kata == "keluar" :
        break

    for huruf in toxic :  
        kata = kata.replace(huruf, "*" * len(huruf))   

    print(kata)
    
