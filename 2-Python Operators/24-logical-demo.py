# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol edin

# a = float(input("Bir Sayı Giriniz: "))
# result = (0 <= a <= 100)
# print(f'Sayınız: {result}. 0 ile 100 arasındadır. ')

# 2- Girilen bir sayını pozitif çift sayı olup olmadığını kontrol edin

# a = int(input("Bir Sayı Giriniz: "))
# result = (a>0) and (a%2==0)
# print(f'Girilen sayı pozitif çift sayı mı: {result}')


# 3- Email ve parola bilgileri ile giriş kontrolü yapın

# mail = "asdf"
# password = "123"

# a = (input("Mail:"))
# b = (input("Password: "))

# result = (a == mail) and (b == password )
# print(f'Giriş başarılı mı: {result}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırın

# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))

# result = (a>b) and (a>c)
# print(f'a en büyük sayıdır: {result}')

# result = (b>a) and (b>c)
# print(f'b en büyük sayıdır: {result}')

# result = (c>a) and (c>b)
# print(f'c en büyük sayıdır: {result}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ort. hesapla
# Eğer ortalama 50 ve üstüyse geçti değilse kaldı yazdır
# a-) Ort. 50 olsa bile final notu en az 50 olmalıdır
# b-) Finalden 70 alındığında ort. önemi olmasın

# a = float(input("1.Vize notunuzu girin: "))
# b = float(input("2.Vize notunuzu girin: "))
# c = float(input("Final notunuzu girin: "))
# ortalama = ((a + b)/2)*0.6 + (c * 0.4) / 2
# result = (ortalama > 50) 
# print(f'ortalaması:{ortalama} ortalama ile mi geçti: {result}')
# result1 = (c >= 70 )
# print(f'final notunuz {c} final notu ile mi geçti: {result1}')

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indexlerini hesapla
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tablo göre kişi hangi gruba girmektedir
# 0-18.4 = Zayıf 
# 18.5-24.9 = Normal
# 25.0-29.9 = Fazla Kilolu
# 30.0-34.9 = Şişman (Obez)

ad = (input("Adınız: "))
kilo = float(input("Kilonuz: "))
boy = int(input("Boyunuz: "))

index  = ((kilo / boy)**2)

zayif  = (index <= 18.4) 
normal = (18.5 <= index <=24.9)
kilolu = (25.0 <= index <=29.9)
obez   = (30.0 <= index <=34.9)

print(f'{ad} Kilo indexiniz: {index} ve boy-kütle indexiniz: {zayif}')
print(f'{ad} Kilo indexiniz: {index} ve boy-kütle indexiniz: {normal}')
print(f'{ad} Kilo indexiniz: {index} ve boy-kütle indexiniz: {kilolu}')
print(f'{ad} Kilo indexiniz: {index} ve boy-kütle indexiniz: {obez}')