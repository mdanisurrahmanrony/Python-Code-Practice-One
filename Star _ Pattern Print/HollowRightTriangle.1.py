num = int(input("Enter the number of rows: "))
for row in range(0,num):
    for col in range(0,num):
        if(row==0 or col==num-1 or row==col):
            print("*",end="")
        else:
            print(end=" ")
    print()