# Write a program which accepts an integer value as command line and print "OK"
# if values between 1 to 50 both inclusive otherwise it print out of range

num = int(input("Enter number\n"));
if(num>=1 and num<=50):
    print("OK")
else:
    print("Out of range");