# Write a Python program to change a given string to a new string where the first and last chars have been exchanged

string = "goooooooooood"
string2 = string[-1]+string[1:-1]+string[0]
print(string2)