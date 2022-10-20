from types import BuiltinFunctionType


myDict = {
    "Fast" : "in a quick manner",
    "blockchain" : "Immutable ledger",
    "Computer" : "Dumb machine",
    "Marks" : [1, 2, 3],
    "bitcoin" : "Peer to peer payment Network",
    "anotherDict" : {"harry" : 'player'}

}

print(myDict["bitcoin"])
print(myDict['Marks'])
print(myDict["anotherDict"])
print(myDict["anotherDict"]["harry"]) #nested dictionary