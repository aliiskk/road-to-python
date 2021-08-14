name = "Ali"
surname = "İskeçe"
age =" 22"

# print("My name is {} {}".format(name,surname))
# print("My name is {1} {0}".format(name,surname)) #burada çıktı My name is İskeçe Ali olur.
# print("My name is {s} {n}".format(n=name,s=surname))
# print("My name is {n} {s}".format(n=name,s=surname))
# print("My name is {} {} and I'm {} years old.".format(name,surname,"22")) #burada yaş degerini age olarak atama yapmadım ama alttaki kodda yaptım
# print("My name is {} {} and I'm {} years old.".format(name,surname,age))

# result = 200/700
# print("the result is {r:1.4}".format(r=result)) #burada da farklı formatlama yazım şeklinin incelemiş oluruz

print(f"My name is {name} {surname} and I'm {age} years old.")

#Şimdi üstteki kodda da formatlama yaptık fakat burada ki pythonın bize
#sağlamış oldugu avantajlardan diyebiliriz bence en kolayı bu bunu kullanabilirim.
#f orada ki format olayını ve süslü parantezlerin içine yazdıklarımızda
#bizim degişkenlerimiz, degerlerimiz