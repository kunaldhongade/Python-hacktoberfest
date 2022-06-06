# Write a Python program to add and remove operation on set

set1 = {1,2,3,4,5}
set2 = {7,8,9}

#for adding elements in set
set1.add(6)
print(set1)
set1.update(set2)
print(set1)

#for deleting elements from the set

set1.pop()
print(set1)

set1.discard(3)
print(set1)

set1.remove(6)
print(set1)