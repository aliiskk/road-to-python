x = 6

result = 5 < x < 10 

# and

# True , True => True
# True , False => False

result = (x > 5) and (x < 10) #(True) x = 6 değeri için True 5 değeri için False gelir
                              # Mantık kapılarıdır.

# or

# True , False  => True
# True , True   => True
# False ,False  => False

result = (x > 0) and (x % 2 == 0) # (True)x sıfırdan büyük mü ve mod2 si sıfır mı

# not

result = not(x > 0)

# x, 5-10 arasında olan bir çift sayı mı ?

result = ((x>5) and (x<10)) and (x%2==0) # True

print(result)