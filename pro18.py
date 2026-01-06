Num_list=[]
n=int(input("Enter no of elements in list: "))
for i in range(0,n):
 numbers=int(input("Enter numbers: "))
 Num_list.append(numbers)
print("Numbers in list : ",Num_list)

Sum=0
for i in range(0,n):
 Sum=Sum+Num_list[i]
print("Sum of the numbers : ",Sum)
