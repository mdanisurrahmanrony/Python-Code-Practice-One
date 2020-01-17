num = int(input("Enter number of array elements: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
print(arr)
revArr = []
for i in range(num-1,-1,-1):
    x = arr[i]
    revArr.append(x)
print(revArr)