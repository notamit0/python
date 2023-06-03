n=input("enter a number(1 Add 2 Delete 3 Select):>")
if n=='1':
    a=input("enter the name:)")
    file=open("test.txt","a")
    if file:
        file.write(a+"\n")
    file=open("test.txt","r")
    if file:
        cont=file.read()
# this is for to add words to txt 1
elif n=='2':
    a=input("enter the name:)")
    file = open("test.txt","r")
    content=file.read()
    if a in content:
        li = list(content.split("\n"))
        del li[li.index(a)]
        str=''.join(map(str,li))
        file=open("test.txt","w")
        file.write(str)
    #this isf  for delete 2
elif n=='3':
    a=input("enter the name:)")
    file=open("test.txt","a")
    if file:
        file.write(a+"\n")
    file=open("test.txt","r")
# THIS FOR SEEEING WHAT YOU TYPED