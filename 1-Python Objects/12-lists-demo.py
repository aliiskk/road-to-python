# 1- 'Bmw','Mercedes','Opel','Mazda' listesini olustur
arabalar = ['Bmw','Mercedes','Opel','Mazda']
# 2- Bu liste kaç elemanlıdır
print(len(arabalar)) #4 elemanlıdır
# 3- Listenin ilk ve son elemanı nedir ?
print(arabalar[0])  # Bmw
print(arabalar[1])  # Mercedes
# 4- Mazda degerini Toyota ile değiştirin
arabalar[3] = "Toyota"
print(arabalar)
# 5- Mercedes listenin elemanımıdır ? 
solve = "Mercedes" in arabalar
print(solve)
# 6- Listenin -2 indeksindeki değer nedir ? 
print(arabalar[-2])
# 7- Listenin ilk 3 elemanını alın
print(arabalar[0:3])
# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekle
arabalar[-2:] = ["Toyota","Renault"]
print(arabalar)
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekle
yeniArabalar = arabalar + ["Audi","Nissan"]
print(yeniArabalar)
# 10- Listenin son elemanını silin
del arabalar[-1]
print(arabalar)
# 11- Listenin elemanlarını tersten yazdırınız
ters = arabalar[::-1]
print(ters)
# 12- Aşağıdaki verileri bir liste içinde saklayınız

    #  studentA: Yiğit Bilgi 2010, (70,60,70)
    #  studentB: Semşi Turan 1999, (80,80,70)
    #  studentC: Ahmet Yılmaz 1998, (80,70,90)

studentA = ["Yiğit Bilgi", 2010, [70,60,70]]
studentB = ["Semşi Turan",1999, [80,80,70]]
studentC = ["Ahmet Yılmaz",1998, [80,70,90]]

listStudent = [studentA + studentB + studentC]
print(listStudent)

#13 - Liste elemanlarını ekrana yazdırınız.    
aboutStudent = f"{studentA[0]}  9 yaşında ve not ortalaması 66 {(studentA[2][0]+ studentA[2][1]+ studentA[2][2])/3}"
print(aboutStudent)
