"""
Aşağıdaki bilgilerle değişken oluştur

Müşteri Adı
Müşteri Soyadı
Müşteri ad + soyad
Müşteri Cinsiyeti
Müşteri TC Kimliği
Müşteri Doğum Yılı
Müşteri Adres Bilgisi
Müşteri Yaşı

"""
musteriAd = "Ali"
musteriSoyad = "İskeçe"
musteriAdSoyad = musteriAd + " " + musteriSoyad
musteriCinsiyet = True # Erkek
musteriTcKimlik = "123465789"
musteriDogumYili = 1999
musteriAdres = "Bursa Yıldırım"
musteriYas = 2021 - musteriDogumYili

#print(musteriYas)
#print(musteriTcKimlik)
print(musteriCinsiyet)
print(musteriAdSoyad)

"""
Toplam siparis bilgisi bulma

siparis1 = 110 TL
siparis2 = 1100.5 TL
siparis3 = 356.95 TL

"""

order1  = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3
print("Total:",total)