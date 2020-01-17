num = int(input("Enter number of array elements: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
print(arr)
arr.sort()
print("Array sorted in ascending order: ")
print(arr)