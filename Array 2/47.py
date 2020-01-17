num = int(input("Enter the size of array: "))
arr1 = []
arr2 = []
arr3 = []
for i in range(num):
    x = int(input())    
    arr1.append(x)
    if(x%2!=0):
            arr2.append(x)
    else:
            arr3.append(x)
print(arr1)
arr2.extend(arr3)                                    
print(arr2)