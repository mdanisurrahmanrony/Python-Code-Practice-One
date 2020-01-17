num = int(input("Enter the size of array: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
print(arr)
arr.reverse()
print(arr)
arr2 = [3,1,9,7,20,4]
print(arr2)
a = arr2[::-1]
print(a)