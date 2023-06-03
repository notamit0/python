a=1
s=0
m=0
n=int(input("enter the number"))
for a in range(1,n+1):
    s=a+s
    print(a)
    m=m+1
print("total",s)
print("count",m)
avg=s/m 
print("Avg :",avg)
