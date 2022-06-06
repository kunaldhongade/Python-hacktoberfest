# Write a python program to check whether an element exits within a tuple

tup = (1,2,3,4,5,6)
num = int(input("Enter number"))

if num in tup:
    print(num," is present")
else:
    print(num,"is not present")