n = input("Enter Number to calculate sum: ")
n = int (n)
average = 0
sum = 0
for num in range(0,n+1,1):
    sum = sum+num
average = sum / n
print("SUM of first ", n, "numbers is: ", sum )
print("Average of first ", n, "number is: ", average)