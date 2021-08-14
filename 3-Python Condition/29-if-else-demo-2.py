"Girilen bir sayını 0-100 arasında olup olmad. kontrol ediniz."
"""
sayi = float(input('sayı:'))
result = (sayi > 0) and (sayi<=100)
print(f'sayı 0-100 arasındamı: {result})
"""
# sayi = float(input("sayi girin: "))

# if (sayi > 0) and (sayi >101):  # ya da (sayi <=100) da yazılabilir
#     print("sayı 0-100 arasındadır")
# else:
#     print("sayı 0-100 arasında degildir")

"""
2- girilen bir sayını pozitif çift sayı olup olm. kontrol et

sayi = int('sayı:')
result = (sayi > 0) and (sayi % 2 ==0)
print(f'girilen sayı pozitif çift sayı mı: {result}')

"""
# sayi = int(input("Sayı giriniz: "))
# # result = (sayi>0) and (sayi % 2 == 0)
# if (sayi > 0) and (sayi % 2 == 0):
#     print("sayı pozitif çift sayı")
# elif (sayi > 0) and (sayi % 2 == 1):
#     print("sayı pozitif tek sayı")
# elif (sayi < 0) and (sayi % 2 == 0):
#     print("sayı negatif çift sayı")
# elif (sayi < 0) and (sayi % 2 == 1):
#     print("sayı negatif tek sayı")
# else:
#     print("sayı yok") # sıfır girilirse gelir


"""
3- email ve parola bilgileri ile giriş kontrolü yapınız.

email = 'email@email_com'
password = "asd123"

girilenEmail = input('email:')
girilenPassword = input('password: ')

reulst = (girilenEmail == email) and (girilenPassword == password)

"""
# email = "email@gmail.com"
# passwd = "asd123"

# girilenMail = input("Mail: ")
# girilenPasswd = input("Password: ")

# if (email == girilenMail) and (passwd == girilenPasswd):
#     print("Giriş başarılı")
# elif (email != girilenMail):
#     print("Mail yanlış")
# elif (passwd != girilenPasswd):
#     print("Parola yanlış")
# else:
#     print("Bilgi yok")

"""
4- girilen 3 sayıyı büyüklük olarak karşılaştırınız
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

result = (a>b) and (a>c)
print(f'a en büyük sayıdır: {result}')

result = (b>a) and (b>c)
print(f'b en büyük sayıdır: {result}')

result = (c>a) and (c>b)
print(f'c en büyük sayıdır: {result}')

"""

# sayiA = int(input("A sayısını giriniz: "))
# sayiB = int(input("B sayısını giriniz: "))
# sayiC = int(input("C sayısını giriniz: "))

# if(sayiA>sayiB) and (sayiA>sayiC):
#     print(f'A en büyük sayıdır')
# elif(sayiB>sayiC) and (sayiB>sayiC):
#     print(f'B en büyük sayıdır')
# elif(sayiC>sayiA) and (sayiC>sayiB):
#     print(f'C en büyük sayıdır')

"""
5- Kullanıcıdan 2 vize %60 ve final %40 notunu alıp ort. hesapla
Eger 50 ve üstüyse geçti değilse kaldı yazdır.
a- ort. 50 olsa bile final notu en az 50 olmalı
b- finalden 70 alındıgında ort. onemsiz olsun

"""
# vize1 = float(input("1.Vize: ")) 
# vize2 = float(input("2.Vize: "))
# final = float(input("Final: "))

# ortalama = (((vize1 + vize2)/2)*0.4 + (final*0.6))

# if (ortalama > 50):
#     if (final >= 50):
#         print(f"{ortalama} ortalama ile geçtiniz")
# elif (final >= 70):
#     print(f"{final} olan final notunuz ile geçtiniz")
# else:
#     print(f"{ortalama} ile kaldınız")


"""
6- Kişinin ad,soyad kilo ve boy bilgilerini alıp kilo indexlerini hesapla
    Formül: (kilo/boy'un karesi)
    Tablosu:
    0-18.4 :: zayıf
    18.5-24.9 :: normal
    25.0-29.9 :: fazla kilolu
    30.0-34.9 :: şişman (obez)

"""
print("Lütfen kilonuzu normal boyunuzu nokta ile yazınız(orn: 1.80)")
name = input("Adınız: ")
kg = float(input("Kilonuz: "))
boy = float(input("Boyunuz: "))

index = (kg) / (boy**2)

if (index > 0 ) and (index < 18.5):
    print(f"Sayın {name} zayıfsınız")
elif (index > 18.5 ) and (index < 25):
    print(f"Sayın {name} normalsiniz")
elif (index > 25 ) and (index < 30):
    print(f"Sayın {name} fazla kilolusunuz")
elif (index > 30 ) and (index < 35):
    print(f"Sayın {name} şişmansınız, doktora görünmelisiniz")
else:
    print("wrong")
