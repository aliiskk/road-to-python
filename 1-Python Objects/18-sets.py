furits = { "orange", "apple","banana"}

# print(furits[0]) # set'ler indexlenemez.

for x in furits:
    print(x)    # bu dongude elemanları sıra sıra ulaşabiliriz.
                # bu listeyi sıralayamayız

furits.add("cherry")   # burada cherry'i listeye ekler
furits.update(["mango","grape","apple"]) # update kullanarak birden fazla da iletebiliriz
# not: elemanlar tekrarlanmaz burada appleyi denedim.

furits.remove("mango") # furits içinden mango'yu silelim
furits.discard("apple") # furits içinden apple'yi sildim
furits.pop()    # pop komutu listedeki gibi degildir rastgele birini siler.
furits.clear() # tüm elemanlar silinir
print(furits)

# myList = [1,2,5,4,4,2,1]
# print(set(myList))  # eger burada set olarak yazdırırsam tekrarlayan elemanlar yazdırılmaz
# print(myList)   # eger liste olarak yazdırırsak aynı şekilde yazdırılır.

