buah = ["apel", "jeruk", "mangga", "pisang"]

print(buah)

tambah = input("Masukkan buah yang ingin ditambahkan ").lower()
hapus = input("Masukkan buah yang ingin dihapus ").lower()
buah.append(tambah)
buah.remove(hapus)

print("Hasil akhir adalah : ", buah)
