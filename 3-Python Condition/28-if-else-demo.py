# 1- Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#   durmunu kontrol et. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#   lise ya da üniversite olmalıdır.

# isim = (input("Ad Soyad: "))
# yas = int(input("Yaş: "))
# egitim = (input("Eğitim seviyeniz: "))

# if (yas >=18) and (egitim == "Lise" or egitim == "Üniversite"):
#     print("Yaş ve eğitim ehliyet almaya uygundur.")
# if (yas < 18):
#     print("Yaş ehliyet almaya uygun değildir.")
# if ( egitim == "İlkokul" or egitim == "Yok"):
#     print("Eğitim ehliyet almaya uygun değildir.")
# else:
#     print("Yaş veya eğitim ehliyet almaya uygun değildir.") ## Dogru olan

# if (yas >=18) and (egitim == "Lise" or egitim == "Üniversite"):
#      print(f'Sayın "{isim}" yaşınız ve eğitiminiz ehliyet almaya uygundur.')
# if (yas < 18):
#     print(f'Sayın "{isim}" yaşınız ehliyet almanıza uygun değildir.')
# if (egitim == "İlkokul" or egitim == "Ortaokul"):
#     print(f'Sayın "{isim}" eğitiminiz ehliyet almaya uygun değildir.')



# 2- Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre
#   not aralığına karşılık gelen not bilgisini yazdırınız.
#   Not karşılıkları:
#   0-24 => 0 
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100 => 5

# yazili1 = float(input("1. yazılı notunuz: "))
# yazili2 = float(input("2. yazılı notunuz: "))
# sozlu = float(input("Sözlü notunuz: "))
# ortalama = (yazili1 + yazili2 + sozlu) / 3

# if ( ortalama >=0 ) and (ortalama < 25):
#     print(f"Ortalamanız: {ortalama} Notunuz: 0")
# elif ( ortalama >=25 ) and (ortalama < 45):
#     print(f"Ortalamanız: {ortalama} Notunuz: 1")
# elif ( ortalama >=45 ) and (ortalama < 5):
#     print(f"Ortalamanız: {ortalama} Notunuz: 2")
# elif ( ortalama >=55 ) and (ortalama < 70):
#     print(f"Ortalamanız: {ortalama} Notunuz: 3")
# elif ( ortalama >=70 ) and (ortalama < 85):
#     print(f"Ortalamanız: {ortalama} Notunuz: 4")
# elif ( ortalama >=85 ) and (ortalama < 100):
#     print(f"Ortalamanız: {ortalama} Notunuz: 5")
# else:
#     print("Yanlış bilgi girdiniz.")



# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilg. göre hesapla
#   1.Bakım => 1.yıl
#   2.Bakım => 2.yıl
#   3.Bakım => 3.yıl
#   **Süre hesabını alınan gün,ay,yıl bilgisine göre gün bazlı hesapla
#   *** datetime modulunu kullan
#   (simdi) - (10/8/2021) === gün



import datetime # önce datetime modülü import edilir.

tarih = input("aracınız hangi tarihte trafiğe çıktı (2021/8/9):") # "kaç gündür" yerine "hangi tarih" sorulur
tarih = tarih.split("/") # / ile ayrılır
# print(tarih)    #kullanıcı gelip bilgi girer
# print(tarih[0])   #1. index   -yıl-   
# print(tarih[1])   #2. index   -ay-
# print(tarih[2])   #3. index   -gün-

#amaç verilen tarih ile şimdiki tarih bilgisi arasınada ki farkı bulup
#şimdiki tarihi bulmak

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now() #şu anın tarihi gelir
fark = simdi - trafigeCikis
# print(fark.days) # aracın kaç yıldır trafikte oldugu ortaya çıkar
#burada farkın içinde days'i çekeriz çünkü kaç gün olduğunu bulmaya çalışıyoruz
#fakat bunu yazdırmak yerine bunu days objesinin içine alalım:
days = fark.days

# print(simdi - tarih)    #şimdiki tarihten kullanıcıdan aldığımız tarihi çıkarırız
                        #bu çıkarma işlemini yapaiblmemiz için kull. alınan bilgiyi datetime 
                        #şekline çevirmeliyiz


if days<=365:
    print("1.servis aralığı")
elif days>365 and days<=365*2:
    print("2.servis aralığı")
elif days>365*2 and days<=365*3:
    print("3.servis aralığı")
else:
    print("hatalı süre")
# yukarıda yaptığımız: gün bilgisine göre aralık belirlemek kolay
