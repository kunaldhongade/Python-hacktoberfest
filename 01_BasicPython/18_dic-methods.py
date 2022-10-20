
myDict = {
    "harry" : "Coder",
    'kunal' : "successfull Enterpeneure",
    'marks' : [1, 2, 4],
    'Dict2' : {'hello' : 'hii'},
    1 : 10,
    'year' : 200,
    'kkk' : True

}

print(myDict.keys()) #print the keys of the dictionary
print(type(myDict)) 
print(list(myDict.keys()))
print(type(myDict.keys()))

print(myDict.values()) # prints the keys of the dictionary

print(myDict.items()) # prints the (key, value) for all contents of the dictionary

print(myDict)
updateDict = {
    'raju' : 'akashay kumar',
    'harry' : 'Teacher',
    'marval': 'Iron man'
}

myDict.update(updateDict) # updates the dictionary by adding key-value pairs form updateDict
print(myDict)

print(myDict.get("harry")) #returns value for perticular key using get method if key is not present it returns none no throws error msg
print(myDict['kunal']) # returns value for perticular key using indexing but if key is not present it throws error msg

print(myDict.items())
print(myDict.keys())
print(myDict.update({'kgf' : 'great'}))
print(myDict)
print(myDict.get('kgf'))