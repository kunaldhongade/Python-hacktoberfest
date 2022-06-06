    # Write a program to display following pattern 

    # 1   2   3   4
    # 1   2   3
    # 1   2
    # 1
n = 4
for i in range(1,n+1):
    print("\n")
    for j in range(1,n+1):
        print(j, end=' ')
    n-=1
