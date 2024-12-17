a=input("Masukkan angka awal ")
b=input("Masukkan angka akhir ")
c=input("Masukkan kelipatan ")
d=int(a)
e=int(b)
f=int(c)

for i in range(d,e) :
    if i%f==0 : 
        print(i)