str=list(input("Enter a string: ").split(' '))
for i in range(len(str)):
	if(str[i][-3:]=="ing"):
		str[i]=str[i]+"ly"
	else:
		str[i]=str[i]+"ing"
print("New string is ",str)
