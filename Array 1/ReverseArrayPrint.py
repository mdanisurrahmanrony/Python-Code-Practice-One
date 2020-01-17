num = int(input("Enter the number of array elements: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
print("Array elements are: ")
print(arr)
arr.reverse()
print("Reverse array elements are: ")
print(arr)
Array = [1,2,3,4,5,6]
P = Array[::-1]
print(P)
for i in range(len(Array)-1,-1,-1):
    print(Array[i])
for i in range(len(Array)-1,-1,-1):
    print(Array[i],end=" ")