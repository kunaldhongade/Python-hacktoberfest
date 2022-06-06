# Write a python program to remove the characters which have odd index values of a given string.

string = "this is string"

for i in range(0,len(string)):
    if(i%2 == 1):
        print(string[i])