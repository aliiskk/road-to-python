"""
ogrenciler = {
    "120" : {
        "ad" : "Ali",
        "soyad" : "Yılmaz",
        "telefon" : "532 000 00 01"
    },
    "125" : {
        "ad": "Can",
        "soyad" : "Korkmaz",
        "telefon" : "532 000 00 02"
    },
    "128" : {
        "ad" : "Volkan",
        "soyad" : "Yükselen",
        "telefon" : "532 000 00 03"
    },   
}

"""

# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
# dictionary içine saklayınız.

# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz.

students = {}

number = input("student number: ")
name = input("student name: ")
surname = input("student surname: ")
phone = input("stundent phone number: ")

# students[number] = {
#     "ad" : name,
#     "soyad" : surname,
#     "telefon" : phone
# }

students.update({       #update'de birden çok ekleyebiliriz(1)
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})

number = input("student number: ")
name = input("student name: ")
surname = input("student surname: ")
phone = input("stundent phone number: ")

students.update({       #update'de birden çok ekleyebiliriz(2)
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})

number = input("student number: ")
name = input("student name: ")
surname = input("student surname: ")
phone = input("stundent phone number: ")

students.update({       #update'de birden çok ekleyebiliriz(3)
    number : {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})      #1. soru cevabı


print(students)

ogrNo = input("Ogrenci no: ")
ogrenci = students[ogrNo]
print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefon numarası: {ogrenci['telefon']}")
