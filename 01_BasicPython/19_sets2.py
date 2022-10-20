b = set()
print(type(b))

# addding value to an empty set

b.add(4)
b.add(5)
b.add(4)
b.add(5)
b.add(4)
b.add(5)
b.add(5)


b.add((9,0,8)) # this is tuple in set
str = "kunal"
# b.add([32,33,33])   we cannot add add list & dictionary in set
# hashabe object lach set madhe taku shakto 
# tech taku shakto jyache content aapan change karu shakat nahi
b.add(str)
b.add(True)
b.add('c')
print(b)
