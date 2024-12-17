f=input("Input Berapa Bilangan Fibonacci ")
p=int(f)

#variable awal
a=0
b=1

#mulai 
while p>0 :
    #print angka awal = 0
    print (a)
    a=b  #tambah kelipatan
    b=a+b #bantu a kelipatan
    p = p-1 #operasi hitung mundur

    