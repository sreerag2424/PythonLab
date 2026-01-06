n1=int(input("Enter number of elemnts: "))
dict1={}
for i in range(n1):
 key=input("Enter key: ")
 value=input("Enter value: ")
 dict1[key]=value
print("Dictionary is ",dict1)

dict_asc=sorted(dict1.items())
print("Sorted in ascending order: ",dict_asc)

dict_dsc=sorted(dict1.items(),reverse="True")
print("Sorted in descending order: ",dict_dsc)


