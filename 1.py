list=[]
n=int(input("Enter the no of integers: "))

for i in range(0,n):
    num=int(input("Enter the numbers: "))
    list.append(num)
print("The list is ",list)

oddlist=[]
for num in list:
    if(num % 2!=0):
        oddlist.append(num)
print("The list of odd numbers are ",oddlist)

