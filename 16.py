color_list1=[]
n=int(input("Enter number of colours in list 1: "))
for i in range(0,n):
 colours=input("Enter colours(list 1) : ")
 color_list1.append(colours)
print("Colour List 1 : ",color_list1)

color_list2=[]
n=int(input("Enter number of colours in list 2: "))
for i in range(0,n):
 colours=input("Enter colours(list 2) : ")
 color_list2.append(colours)
print("Colour List 2 : ",color_list2)

set1=set(color_list1)
set2=set(color_list2)

print("All colors from color-list1 not contained in color-list2 : ",set1-set2)
