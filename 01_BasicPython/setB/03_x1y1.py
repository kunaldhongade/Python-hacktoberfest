# Write a program that finds distance betn 2 points (x1,y1) and (x2,y2) using the equation 
# squrt((x2 - x1)^2 + (y2-y1)^2)

from math import sqrt
#Enter points
x1 = int(input("Enter x1 : "))
x2 = int(input("Enter x2 : "))
y1 = int(input("Enter y1 : "))
y2 = int(input("Enter y2 : "))

dis = sqrt((((x2-x1)**2) + ((y2-y1)**2)))

print("The distance betn two points is : ",dis)