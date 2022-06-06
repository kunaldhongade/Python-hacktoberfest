# Write a pthon program to create a dictionary from two lists without losing duplicate
# values 
# Sample lists : ['Class - V','Class - VI','Class - VII','Class - VIII']
# ,[1,2,2,3]
# Expected output: 
# defaultdict(<class 'set'>, {'Class-VII' : {2}, 'Class - VI':{2}, 'Class - VIII' : {3}, 'Class - V' : {1}})



from collections import defaultdict
class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
temp = defaultdict (set)
for c, i in zip(class_list, id_list) :
    temp[ c ].add ( i )

print (temp)