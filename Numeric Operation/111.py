N = int(input("Enter how many numbers: "))
sum = 0

for i in range(N):
    numbers = float(input("Enter numbers: "))
    sum+=numbers

average = str(sum/N)

print("Average: "+average)