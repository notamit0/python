title=input("Enter your Website name (⇀‸↼‶)ᕗ:")
heading=input("enter the heading")
name=[]
print("enter 5 name")
for a in range(5):
    n=input()
    name.append(n)
    print(name)
file=open("website.html","w")
file.write(
    """
    <html>
        <head>
            <title>%s</title>
        </head>
        <body>
            </h1>%s</h1>
            <nam>%s</name>
         </body>
    </html>
    """ %(title,heading,name)
)
print("the website is created ᕙ(⇀‸↼‶)ᕗ")

