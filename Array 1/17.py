num = int(input("Enter number of array elements: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
max = arr[0]
for i in range(1,num):
    if(arr[i]>max):
        max = arr[i]    
print(max)