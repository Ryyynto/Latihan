#Struktur data set
var = {1, 2, 3, 4, 5, 6, 7, 8}

print(var)

var.add(9)
var.add(11)

print(var)

#Menghilangkan angka 3 dalam set
var.remove(3)

print(var)

bis = {1, 2, 3}
set = {4, 5, 6}

#Union
print(bis | set)

#Intersection 
print(var & bis)

#Difference
print(var - bis)