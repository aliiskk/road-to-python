# is operatörü

# x = y = [1,2,3]
# z = [1,2,3]

# print(x==y)   # x,y'ye eşit mi 
# print(x==z)   # x,z'ye eşit mi 
# print(x is y) # ==> x,y' ye eşit mi demek
# print(x is z) # ==> x,z' ye eşi mi demek

# x = [1,2,3]
# y = [2,4]

# del x[2]
# y[1] = 1
# y.reverse()
# print(x==y)     # True
# print(x is y)   # x,y' ye eşit mi (False)
#print(x is not y)

# in operatörü

x = ["apple","banana"]
print("banana" in x) # x'in içinde banana var mı ? 

name = "Ali"
print("A" in name)     # name'in içinde A var mı ? (True)
print("A" not in name) # name'in içinde A yok mu ? (False)
