num = int(input("Enter the size of array: "))
arr = []
for i in range(num):
    x = int(input())
    for j in range(len(arr)):
        if(arr[j]==x):
            x = int(input("Enter a different number: "))
            continue
    arr.append(x)
    print(arr)                                    