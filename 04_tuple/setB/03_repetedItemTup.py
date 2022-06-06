# Write a python program to find the repeated items of a tuple

tup = (1,2,3,4,2,5)
di = {}

for i in tup:
    if i in di:
        di[i] = di[i]+1
    else:
        di[i]=1
print(di)