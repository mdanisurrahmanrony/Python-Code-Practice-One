num = int(input("Enter number of array elements: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
max = arr[0]
for i in range(num):
    if(arr[i]>max):
        max = arr[i]
        loc1 = i
min = arr[0]
for i in range(num):
    if(arr[i]<min):
        min = arr[i]
        loc2 = i

print("smallest number "+str(min)+" was found at location "+str(loc2))
print("largest number "+str(max)+" was found at location "+str(loc1))