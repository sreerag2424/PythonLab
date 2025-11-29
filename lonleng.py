str=list(input("Enter words comma seperated: ").split('.'))
wordlen=0
word=''

for words in str:
  if len(words)>wordlen:
    wordlen=len(words)
    word=words
print(f"Longest word:{word},word len=:{wordlen}")
