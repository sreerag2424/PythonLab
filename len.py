def long_word():
   words=input("Enter a list of words separated by spaces: ").split()
   long_word=max(words,key=len)
   print(f"Longest word: {long_word}")
   print(f"Length: {len(long_word)}")
long_word()
