N = int(input("Enter how many numbers: "))
sum = 0
for i in range(0,N+1,1):
    sum+=i
res = str(sum)
n = str(N)
print("Sum of first "+n+"positive numbers is: "+res)