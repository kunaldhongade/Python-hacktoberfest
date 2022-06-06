# Write a Python script to check if a given key aleready exists in a dictionary


dict1 = {1:3,2:4,3:5}
print(dict1)

key = int(input("Enter key"))
if key in dict1.keys():
    print(key," is present")
else : 
    print(key," is not present")