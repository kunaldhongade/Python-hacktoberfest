# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to
# '$', except the first char itself. Sample String : 'restart'
# Expected Result : 'resta$t'


s = input("string")
s1 = s[0]
for i in range(1,len(s)):
    s2 = s[1:].replace(s1,"$")
print(s+s2)
