# Write a program which finds sum of digits of a number example n = 125 then output is 8 1+2+5

num = int(input("Enter number\n"))
sum = 0;
rem = 0;
for i in range(0,num):
    rem = num%10;
    sum = rem+sum;
    num = num/10;

print(int(sum))