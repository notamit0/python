a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=a+b 
d=a/b
f=a-b
g=a*b
print("division:",c)
print("subtraction:",d)
print("multipication:",f)
print("sum:",g)




a=input("enter the name:)")
file=open("test.txt","w")
if file:
    file.write(a+"\n")
file=open("test.txt","r")
if file:
    cont=file.read()
    print(cont)






    a=input("enter the name:)")
file=open("test.txt","")
if file:
    file.write(a+"\n")
    file=open("test.txt","r")