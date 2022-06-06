# Write a Python program to count the occurrences of each word in a given sentence

string = "This is sentence is over"

string1  = string.split(" ")

di = {}
for i in string1:
    if i in di:
        di[i] = di[i]+1
    else:
        di[i]=1
print(di)
