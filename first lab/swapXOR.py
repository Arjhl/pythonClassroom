a = int(input("enter a number"))
b= int(input("enter another number"))

a = a ^ b; 
b = a ^ b; 
a = a ^ b;
print(a,b)