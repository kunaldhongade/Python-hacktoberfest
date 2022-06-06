#Write a Python program to get a string made of the first 2 and last 2 chars 
#from a given a string. If the string length is less than 2, return instead of 
# the empty string. 



string = "2"
if(len(string)>2):
    string = string[-1]+string[-2]+string[2:-2]+string[1]+string[0]
    print(string)
elif(len(string)<2):
    string = " ";
    print(string)