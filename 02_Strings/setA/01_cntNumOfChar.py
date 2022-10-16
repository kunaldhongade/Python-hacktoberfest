# Write a python program to count the number of 
# characters(character frequency ) in a string Sample string : 
# google.com' Expected Result : {'o':3,'g':2,'.':1,'e':1,'l':1,'m':1,'c':1}

string  = "google.com"
t = {}
for i in string:
    if i in t:
        t[i] = t[i]+1
    else:
        t[i] = 1
print(t)
