message = "Hello there. My name is Ali İskeçe"

# message = message.upper()         # .upper() kodu mesaj içindeki her harfi büyük harfle yazar
# message = message.lower()         # .lower() kodu mesak içindeki her harfi küçük harfle yazar
# message = message.title()         # .title() her kelimenin baş harfini büyük harfle yazar
# message = message.capitalize()    # .capitalize() sadece ilk kelimeinin baş harfini büyük yazar
# message = message.strip()         #  elimizde olan mesaj yazısının başında boşluk varsa .strip() komutu bu boşluğu ortadan kaldırır
# message = message.split()         # .split() kodu her kelimeyi tek tek dizi haline getirir(ayırır.)
# message = message.split(".")      # .split(".") şeklinde ki yazım noktaya kadar olan diziyi ayrı noktadan sonra olanları ayrı şekilde alıp ilk başta
# kullanıdıgımız .split() gibi tek tek ayırmak yerine 2 şekilde ayırmış olur **

# message = "*-*".join(message)      #sadece yıldız eklemek her harften sonra yıldız atar fakat ben burada .split() kullanarak ekledim o yuzden
#her kelimeden sonra yıldız atadı

# index = message.find("Ali")        #buradaki find komutu ise aratılan kelimenin indexinin kaçtan başladıgını soyler
# print(index)

# isFound = message.startswith("H")  # H ile mi başlıyor sorusu olarak açıklayabiliriz.
# isFound = message.endswith("e")    # e ile mi bitiyor sorusu olarak açıklayabiliriz. True-False olarak yanıt alırız
# print(isFound)

# message = message.replace("Ali","İskeçe")     # burada .replace komutu mesajda yazan Ali yerine İskeçe yazdırmaya ise yarar
# message = message.replace("ç","c")            #ç harfi yerine c yazdırdım 

# message = message.center(75,"*")              # burada sağdan ve soldan 75lik bir boşluk atadı,site tasarımı vb. kullanılabilir. 
# yıldızı kendim boşlukları gormek için ekledim

print(message)