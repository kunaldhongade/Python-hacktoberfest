name = "kunal"

# [ k  u  n  a  l ]
#   0  1  2  3  4
#  -5 -4 -3 -2 -1

print(name[1:2])

# negative slicing

print(name[-4:-3])
print(name[2:4])
print(name[-1:])

print("\n\n\n\n")

# string sliceing skipping

str = "KunalIsGoodBoy"
#      01234567890123
s = str[0::3] # first paramenter is for startindex and last is for endindex Third parameter is for skipping
t = str[:7]
g = str[0:]
j = str[0:14:2]
f = str[0:14]

print(s)
print(t)
print(g)
print(j)
print(f)