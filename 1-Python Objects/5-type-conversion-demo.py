"""
Daire Alanı : pi*r**2
Daire ÇEvresi: 2*pi*r

**Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız
**  (r: 3.14)
"""

pi = 3.14 #zorunlu deger

r= float(input("Yarı Çapı Giriniz: ")) # burada tek girdimiz r(yarıçap) olduğu için input degeri verdik çünkü alan ve çevre hesabı yapılırken yarıçap kullanılmaktadır.
# Ayrıca float'a donusturme nedinmiz r(yarıçapın) ondalıklı olma ihtimali yüzündendir

alan = pi*r**2
cevre = float(2*pi*r)

print("Alanı: ", str(alan) + " Çevresi:", str(cevre)) # BURADA str(alan) - str(cevre) yapma nedenimiz: float sayılar ile string birleştirme işleminde kullanmadıgımızdan dolayı

# print("Dairenin Alanı: ",alan)
# print("Dairenin Çevre Uzunluğu", cevre)