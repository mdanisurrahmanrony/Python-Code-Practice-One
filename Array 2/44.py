num = int(input("Enter the size of array: "))
arr = []
for i in range(num):
    x = int(input())
    arr.append(x)
print(arr)
count = 0
for i in range(10):
        count = 0
        for j in range(num):
                if(i==arr[j]):
                        count = count + 1
        print(str(i)+" has been entered "+str(count)+" times by user.")
