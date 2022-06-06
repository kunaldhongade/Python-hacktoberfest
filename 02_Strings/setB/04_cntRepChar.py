# 4. Write a python program to count repeated characters in a string.
# Sample string 'hello world'
# Expected output:
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

word = 'thequickbrownfoxjumpsoverthelazydog'

st = [char for char in word]

di = {}
for i in st:
    if i in di:
        di[i] = di[i]+1
    else:
        di[i] = 1
print(di)