import mysql.connector 
n=int(input("enter a number(1 Add 2 Delete 3 update 4 found):>"))
conn=mysql.connector.connect(host="localhost", user="root", passwd="", database="amit")
cur=conn.cursor()
if conn:
    
    if n==1:
        a=input("enter the name:)")
        b=input("enter the mal:)")
        c=input("enter the eng:)")
        d=input("enter the math:)")
        cur.execute("insert into mark value('%s',%s,%s,%s)"%(a,b,c,d))
        conn.commit()
        print("Data Saved Succes")
# creating table
    elif n==2:
        cur=conn.cursor()
        name=input("enter the name:")
        cur.execute("delete from mark where name='%s'"%name)
        conn.commit()
        print("deleted")
#deleting table
    elif n==3:
        cur=conn.cursor()
        g=input("enter the name:")
        f=input("enter the name you want chang:") 
        cur.execute("update mark set name='%s' where name='%s'"%(g,f))
        conn.commit()
        print("update")
#updating table
    elif n==4:
        cur=conn.cursor()
        h=input("enter the name:")
        cur.execute("select*from mark where name='%s'"%h)
        result=cur.fetchall()
        for a in result:
            print(a)
        print("found")
#found the table
else:
    print("")
    print("FAIEd")
print("")
print("")
print("thanks for chosing as")