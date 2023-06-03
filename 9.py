file = open("test.txt","r")
content=file.read()
a=input("enter a name:>")
if a in content:
    print("Name Available")
    li = list(content.split("\n"))
    del li[li.index(a)]
    str=''.join(map(str,li))
    file=open("test.txt","w")
    file.write(str)
else:
    print("Name is not Availbel")