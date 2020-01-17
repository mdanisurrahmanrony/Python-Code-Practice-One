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
        break
    else:
        flag = 0
if(flag==1):
    print(str(num2)+" was found")
else:
    print(str(num2)+" was not found")