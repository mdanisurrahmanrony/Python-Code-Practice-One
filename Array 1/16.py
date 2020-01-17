num = int(input("Enter number of array elements: "))
arr = []
flag = 0
for i in range(num):
    x = int(input())
    arr.append(x)
num2 = int(input("Enter the number: "))
for i in range(num):
    if(arr[i]==num2):
        flag = 1
        loc = i
        break
    else:
        flag = 0
if(flag==1):
    print(str(num2)+" was found at location "+str(loc))
else:
    print(str(num2)+" was not found")