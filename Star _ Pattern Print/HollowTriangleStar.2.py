num = int(input("Enter the number of  rows: "))
k=2
for row in range(1,num+1):
    for col in range(1,2*num):
        if row+col==num+1 or col-row==num-1:
            print("*",end="")
        elif row==num and col!=k:
                print("*",end="")
                k=k+2            
        else:
            print(end=" ")
    print()