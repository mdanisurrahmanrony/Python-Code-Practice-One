num = int(input("Enter the size of array: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
print(arr)
arr.reverse()
for i in range(num):    
    if(arr[i]%2==0):
        print(arr[i],end=" ")       