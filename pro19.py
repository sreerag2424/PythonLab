n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
gcd=1
n=min(n1,n2)

for i in range(1,n):
 if(n1%i==0 and n2%i==0):
  gcd=i
print("Gcd is : ",gcd)

