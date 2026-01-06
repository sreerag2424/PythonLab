word_list=[]
n=int(input("Enter no(elements): "))
for i in range(0,n):
 words=input("Enter Words: ")
 word_list.append(words)
print("List of words are: ",word_list)

str=word_list[0]
length=len(word_list[0])

for i in range(0,n):
 if(len(word_list[i])>length):
  str=word_list[i]
  length=len(word_list[i])
print(str,length)
