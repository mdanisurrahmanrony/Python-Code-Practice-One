num = int(input("Enter number of array elements: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
max = arr[0]
for i in range(num):
    if(arr[i]>max):
        max = arr[i]
        loc = i 
print("largest number "+str(max)+" was found at location "+str(loc))