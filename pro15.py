list1=[1,2,3,4,5]

list2=[3,4,6,5]

if(len(list1)==len(list2)):
 print("Two lists are in same length")
else:
 print("Two lists are in different length")


if(sum(list1)==sum(list2)):
 print("Sum of two list are same")
else:
 print("Sum of two list are different")
list=[] 
for i in list1:
 for j in list2:
  if(i==j):
   list=i
  else:
   print("No common elements found")
