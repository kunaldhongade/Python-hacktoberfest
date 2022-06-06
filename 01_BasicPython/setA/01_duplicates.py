# Write a program which acceps % integer values and prints "Duplicates"
# if any of the values entered are duplicates otherwise it print " All Unique"
# Example Let 5 integers are 32,45,90,45,6 then output "Duplicates " to be printed

a = [1,2,3,4,5]
counter = 0
print(len(a))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i] == a[j]):
            print("Dublicate")
            counter+=1


if(counter==0):
    print("all unique")


    