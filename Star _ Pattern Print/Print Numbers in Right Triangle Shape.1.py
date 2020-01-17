num = int(input("Enter the number of rows: "))
for i in range(num):
    for j in range(i+1):
        x = 0
        for k in range(j):
            x = x+num-k
        if j%2==0:
            print(x+i-j+1, end=" ")
        else:
            print(x+num-i ,end=" ")                
    print()  