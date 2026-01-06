list=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
 val=int(input("Enter values: "))
 list.append(val)
print("\nThe original list is: ",list)

for i in range(0,n):
 if(list[i]>100):
  list[i]="Over"
 else:
  list[i]
print("\nThe list after manipulation is: ",list)
