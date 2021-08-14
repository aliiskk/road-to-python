# values types == string , number(int,float..)
x = 5 
y = 25
#burada 5 olan x değerine 25 atamış oldum yani y değerini
x = y

y = 10 
#burada 25 değerini 10 ile değiştirdim fakat x değişmedir

# print(x,y)

# reference types == list 
a = ["apple","banana"]
b = ["apple","banana"]

a = b
#aynı olan iki list değerine altta b'nin 0. indexine grapeyi atayıp print
# ettigim zaman aynı listeler karşımıza çıkar yani iki listeninde 0. indexi aynı olur
b[0] = "grape"

print(a,b)

# values typesta : verinin kendisiyle
# reference typesta: listenin adresiyle ilgileniriz