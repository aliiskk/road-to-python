website = "http://wwww.aliiskece.com"
course = "Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizsinin baş ve sondaki karakterlerini silin.
# message = " Hello World "
# message = message.strip()
# print(message)

#2- 'wwww.aliiskece.com' içindeki aliiskece bilgisi haricindeki her karakteri silin.
# message = "www.aliiskece.com"
# message = message.strip("www.")
# message = message.strip(".com")
# print(message)

#3- 'course' karakter dizisnini tüm karakterlerini küçük harf yap
# course = course.lower()
# print(course)

#4- 'website' içinde kaç tane a karakteri vardır ? (count(a))
# website = website.count("a") # count(a) kaç tane a oldugunu buldurur
# print(website)

#5- 'website' www ile başlayıp com ile bitiyor mu ?
# website = website.startswith("www")  # Hayır, www ile başlamıyor, http ile  başlıyor
# website = website.endswith("com")      # Evet, com ile bitiyor
# print(website)

#6- 'website' içinde '.com' ifadesi var mı ?
# website = website.f(".com") # Evet var, 21. indexte başlıyor
# print(website)

#7- 'course' içindeki karakterlerin hepsi alfabetik mi ? 
# course = course.isalpha()
# course = course.isdigit()  #hayır degil
# print(course)

#8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve solun * ekleyiniz
# result = "Contens"
# result = result.center(50,"*")
# print(result)

#9- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak degiştir.
# message = "Hello World"
# message = message.replace("World","There")
# print(message)

#10- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
# course = course.replace(" ","-")
# print(course)

#11- 'course' karakter dizisin boşluk karakterlerinden ayırın(tek dizi haline getir)
# course = course.split(" ")
# course = course[5]   #course dizisi içindeki 5. index'in Programlama oldugunu gosterir 
# print(course)
