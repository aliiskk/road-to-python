# dictionary'de key-value ilişkisi vardır

# 41 = kocaeli , 34 = istanbul

# sehirler = ["kocaeli","istanbul"]
# plakalar = [41,34]

# print(plakalar[sehirler.index("kocaeli")])

# print(plakalar["kocaeli"]) == 41
# print(plakalar["istanbul"]) == 34

plakalar = {"kocaeli" : 41, "istanbul" : 34}

# plakalar["ankara"] = 6 # burada plakalar datasına ankarayı eklemiş oldum
# plakalar["kocaeli"] = "yeni plaka degeri" # burada da kocaeli 41 degerini degiştirdim
# print(plakalar)

users = {
    "aliiskece" : {
        "age" : 22,
        "mail" : 'ali@hotmail.com',
        "address" : "bursa",
        "phone" : 987654321

    },
    "enesiskece" : {
        "age" : 19,
        "mail" : "enes@hotmail.com",
        "address" : "bursa",
        "phone" : 123456789
    }

}

print(users["aliiskece"]["mail"])
print(users["aliiskece"]["phone"])
print(users["enesiskece"]["mail"])
print(users["enesiskece"]["phone"])

