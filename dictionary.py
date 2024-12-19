#dictionary
pep = {"nama": "asep",  "umur": 90, "kota": "bogor"}

#Manggil data variabel di dalam dictionary
print(pep)
print(pep["nama"])
print(pep["umur"])
print(pep["kota"])

#Nambah  data dalam dictionary
pep["job"] = "merchant"

print(pep)

#Hapus data dalam dictionary
del pep["job"]
print(pep)