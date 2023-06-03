                              #mport mysql.connector  
import mysql.connector 
conn=mysql.connector.connect(host="localhost", user="root", passwd="", database="amit")
cur=conn.cursor()
c=input("enter your name=")
name=input("enter your name you want change=")
if conn:
    cur.execute("update mark set name='%s' WHERE name='%s'"%(c,name))
    conn.commit()
    if cur:
        print("name update sucsses")
    else:
        print("Failed")