list = [1,2,3]

tuple = (1,"iki",3)

# print(type(list))
# print(type(tuple))
#                     #   boyut,tip ve indexten bulma aynı
# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

list = ["ali","veli"]
tuple =  ("damla","ayşe","damla")
names = ("demet","ahmet","muhittin") + tuple 

#şimdi burada listeyi guncelledi tuple'da guncelledi

list[0] = "ahmet"   # burada listenin 0. elemanını ahmet ile değiştiririz
# tuple[0] = "deniz"  # burada tuple'nin 0. elemanını deniz ile  değiştiremeyiz
# Çünkü: tuple'da herhangi bir elemana atama işlemi yapamayız

print(tuple.count("damla")) # iki adet damla oldugunu burada soyler
print(tuple.index("damla")) # 0. index damla

print(list)
print(tuple)

print(names) #şimdi burada names ile tuple listesini birbirine eklemiş olduk
#tupleler tamamen liste ile aynı diyebiliriz fakat tuple elemanına herhangi
#bir silme,ekleme işlemi yapamayız