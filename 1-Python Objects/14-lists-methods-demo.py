names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
# names.append("Cenk")
# print(names)

# 2- "Sena" değerini listenin başına ekleyiniz.
# names.insert(0,"Sena")
# print(names)

# 3- "Deniz" ismini listeden siliniz
# names.remove("Deniz")
# print(names)

# 4- "Deniz" isminin indexi nedir ?
# index = names.index("Deniz")
# print(index)

# 5- "Ali" listenin bir elemanı mıdır ?
# result = "Ali" in names
# print(result)

# 6- Liste elemanlarını ters çevirin
# names.reverse()
# print(names)

# 7- Liste elemanlarını alfabetik olarak sıralayanız
# names.sort()
# print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız
# years.sort()
# print(years)

# 9- str = "Chevrolet,Dacia" karakter dizisinin listeye çeviriniz
# str = "Chevrolet,Dacia"
# result = str.split(",")
# print(result)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
# minyears = min(years)
# print(minyears)
# maxyears = max(years)
# print(maxyears) 
 
# 11- years dizisinde kaç tane 1998 değeri vardır ?
# print(years.count(1998)) 

# 12- years dizisnin tüm elemanlarını siliniz
# years.clear()
# print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
markalar = []

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

print(markalar)

#13. Uygulamada marka değerlerin girip bunu liste olarak çıkartan kodu yazdık