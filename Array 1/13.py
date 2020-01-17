num = int(input("Enter the number of array elements: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
for i in range(num):
    if(arr[i]<10):
        print(arr[i],end=" ")