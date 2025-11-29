def gcd(n1,n2):
 gcd=1
 n=min(num1,num2)
 for i in range(1,n):
   if (num1%i==0) and (num2%i==0):
     gcd=i
 print("Gcd is ",gcd)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
gcd(num1,num2)
