n=int(input("Enter the no of terms: "))
a,b=0,1
print(f"The first {n} terms of the fibnocci series are: ")
for _ in range(n):
  print(a,end=" ")
  a,b=b,a+b
