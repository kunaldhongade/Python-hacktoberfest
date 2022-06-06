# Write a Python program to create a list of tuples with the first element as the number and second element as the square of the number
num = int(input("Enter number\n"))
x = [(x,x*x) for x in range(0,num)]
print(x)