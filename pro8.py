vowel_list='aeiouAEIOU'
word_list=[]
word=input("Enter a word: ")
n=len(word)
for i in range(0,n):
 if(vowel_list==word[i]):
  word_list=word[i]
print("Vowels in given word are ",word_list)

