letter = '''dear <|name|>,

Greetings from Submux inc, We are happy to you about your selection

You are selected in top 10!
Have a great day ahead!
Thanks and regards,

Date: <|Date|>

'''

name = input("Enter your name \n")
date = input("enter date\n")

letter = letter.replace("<|name|>", name)
letter = letter.replace("<|Date|>", date)

print("\n")
print(letter)
