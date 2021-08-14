# 1- Girilen 2 sayıdan hangisi büyüktür

# a = int(input("a: "))
# b = int(input("b: "))

# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ort. hesaplatın
#   -Eger ortalama 50 ve üstünde ise geçti değilse kaldır yazdırın 

# a = float(input("1.Vize notunuzu girin: "))
# b = float(input("2.Vize notunuzu girin: "))
# c = float(input("Final notunuzu girin: "))

# ortalama = ((a + b) * 0.6) + (c * 0.4)
# print(f'Not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın

# sayi = int(input("Sayinizi Giriniz : "))
# tekcift = (sayi % 2 == 0)
# print(f'girilen sayı çift olma durumu : {tekcift}')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın

# sayi = int(input("Sayi Giriniz: "))
# negpoz = (sayi > 0)
# print(f'girilen sayının pozitif olma durumu: {negpoz}')

# 5- Parola ve email bilgisin isteyip doğruluğunu kontrol edin
#   -(email: email.@aliiskece.com parola: abc123)

a = str(input("Mailinizi girin: "))
b = str(input("Parolanızı girin: "))

truemail = (a == "email.@aliiskece.com")
truepasw = (b == "abc123")

print(f'Girilen email doğru mu: {truemail} ve girilen password doğru mu: {truepasw}')