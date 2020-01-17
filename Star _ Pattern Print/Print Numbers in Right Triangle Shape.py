num = int(input("Enter the number of rows: "))
for row in range(num):
    value = row+1
    dec = num-1
    for col in range(row+1):
        print(format(value,"<4"),end=" ")
        value = value+dec
        dec = dec-1
    print()  