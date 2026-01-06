n1=int(input("Enter number of elemnts: "))
dict1={}
for i in range(n1):
 key=input("Enter key: ")
 value=input("Enter value: ")
 dict1[key]=value
print(dict1)


n2=int(input("Enter number of elemnts: "))
dict2={}
for i in range(n2):
 key=input("Enter key: ")
 value=input("Enter value: ")
 dict2[key]=value
print(dict2)

merge_dict={}
merge_dict=dict1.copy()
merge_dict.update(dict2)
print(merge_dict)
