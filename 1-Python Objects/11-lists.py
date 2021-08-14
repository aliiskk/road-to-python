message = "Hello there. My name is Ali İskeçe".split()
# print(message[0])

# my_list = [1,2,3,4]
# my_list = ["bir",2,False,5.6]
# print(my_list)

list1 = ["one","two","three"]
list2 = ["four","five","six"]

numbers = list1 + list2
# print(numbers)   #sonuç ['one', 'two', 'three', 'four', 'five', 'six'] gelir
# print(len(numbers))  #numbersın uzunlugu "6"
# print(numbers[2])  # numbersın 2. indexinin degeri "three"

userA =  ["Ali",22]
userB =  ["Enes",19]
# print(userA)
# print(userB)

users = [userA + userB]  #userA ile userB listelerinin kendi içinde users şeklide liste yapar
# print(users)

print(users[0][1])  # users listesinin 0.indexinin(['Ali', 22, 'Enes', 19]) 1.elemanı(22)
