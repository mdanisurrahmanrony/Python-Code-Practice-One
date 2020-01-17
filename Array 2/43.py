num = int(input("Enter the size of array: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
print(arr)
flag = 0
num2 = int(input("Enter another number: "))     
for i in range(num):
        if(arr[i]==num2):
                flag=1
                break
        else:
                flag=0
if(flag==1):
        print("yes")
else:
        print("no")