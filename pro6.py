integerlist=[]
poslist=[]
n=int(input("Enter number of integers: "))
for i in range(0,n):
 integer=int(input("Enter integers: "))
 integerlist.append(integer)
 if(integer%2!=0):
  poslist.append(integer)
print("Intergers is ",integerlist)
print("List of Positive number is ",poslist)

