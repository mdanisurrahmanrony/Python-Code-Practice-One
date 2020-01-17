num = int(input("Enter the number of  rows: "))
for row in range(1,num+1):
    for col in range(1,2*num):
        if row==num or row+col==num+1 or col-row==num-1:
            print("*",end="")
        else:
            print(end=" ")
    print()