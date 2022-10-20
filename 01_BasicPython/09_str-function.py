import string


story = "once upon a time there was a man named satoshi nakamoto who invented bitcoin peer to peer payment system."
#          0    1  2  3    4     5  6  7   8       9       10     11   12       13     14  15  16   17        18
# string functions

print(len(story))
print(story.endswith("satoshi nakamoto who invented bitcoin peer to peer payment system."))
print(story.count("time"))
print(story.count("peer to peer"))
print(story.capitalize())
print(story.find("once"))
print(story.replace("payment", "transaction"))

