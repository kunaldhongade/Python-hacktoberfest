# Write a Python program to get a single string from two given strings, seperated by a space and 
# swap the first two characters of each string.
# Sample String : 'abc','xyz'
# Expected Result : 'xycabz'

string1 = "xyz"
string2 = "abc"

string3 = string1[0]+string1[1]+string2[2:]+string2[0]+string2[1]+string1[2:];
print(string3)