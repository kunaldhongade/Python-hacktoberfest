# Write a python program to create a shallow copy of sets
# note: Shallow copy is a bit- wise copy of an object. 
# A new object is created that has an exact copy of the values in the original object
import copy 

set1 = {1,2,3,4,5}
set2 ={}
print("Starting  >>>>")
print(set1)
print(set2)
print("Shallow copy >>>")
set2 = copy.copy(set1)
set1.add(33)
print(set1)
print(set2)
print("Deep copy>>>>")
set2 = copy.deepcopy(set1)
set1.add(33)
print(set1)
print(set2)


