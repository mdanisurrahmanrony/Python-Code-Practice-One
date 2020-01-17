num = int(input("Enter the number of array elements: "))
arr = []
count = 0
for i in range(num):
    x = int(input())
    arr.append(x)
for i in range(num):
    if(arr[i]<10):
        count = count+1
print(count)
