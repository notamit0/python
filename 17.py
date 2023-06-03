from tkinter import*
import mysql.connector 
import tkinter.messagebox as messagebox
conn=mysql.connector.connect(host="localhost", user="root", passwd="", database="tastmark")
cur=conn.cursor()
def ok():
    name=e1.get()
    mark1=e2.get()
    mark2=e3.get()
    mark3=e4.get()
    if name=='' or mark1=='' or mark2=='' or mark3=='':
        messagebox.showerror("School","Plase fill all fields")
    else:
        cur.execute("insert into mark value('%s',%s,%s,%s)"%(name,mark1,mark2,mark3))
        conn.commit()
        print("Data Saved Succes")
def de():
    name=e1.get()
    if name=='':
        messagebox.showerror("School","Plase fill all fields")
    else:
        cur.execute("delete from mark where name='%s'"%name)
        conn.commit()
        
        print("deleted")
def fd():
    name=e1.get()
    if name=='':
        messagebox.showerror("School","Plase fill all fields")
    else:
        cur.execute("select *from mark where name='%s'"%name)
        result=cur.fetchall()
        for a in result:
            e2.insert(0,a[1])
            e3.insert(0,a[2])
            e4.insert(0,a[3])
        print("found")
def ut():
    name=e1.get()
    mark1=e2.get()
    cur.execute("update mark set name='%s'where name='%s'"%(name,mark1))
    conn.commit()
    print("update")
def cr():
    e1.delete(0,END)     
    e2.delete(0,END)     
    e3.delete(0,END)     
    e4.delete(0,END)     

root=Tk()
root.title("mysql")
root.geometry("500x500")
root.iconbitmap("dragon.ico")
root.attributes('-topmost',True)
root.attributes('-alpha',10)
root.config(bg='#0a1460')
lable=Label(root,text="welcome to marklist.com",bg="#0a1460",fg="white",)
lable.place(x=155,y=0)
lable=Label(root,text="name", bg="#0a1460", fg="white",)
lable.place(x=5,y=50)
lable=Label(root,text="mark1", bg="#0a1460", fg="white",)
lable.place(x=5,y=100)
lable=Label(root,text="mark2", bg="#0a1460", fg="white",)
lable.place(x=5,y=150)
lable=Label(root,text="mark3", bg="#0a1460", fg="white",)
lable.place(x=5,y=200)
e1=Entry(root)
e1.place(x=50,y=50,height=25,width=200)
e2=Entry(root)
e2.place(x=50,y=100,height=25,width=150)
e3=Entry(root)
e3.place(x=50,y=150,height=25,width=150)
e4=Entry(root)
e4.place(x=50,y=200,height=25,width=150)


b1=Button(root,text="save",command=ok)
b1.place(x=300,y=50)
b2=Button(root,text="delete",command=de)
b2.place(x=300,y=100)
b3=Button(root,text="found",command=fd)
b3.place(x=300,y=150)
b3=Button(root,text="update",command=ut)
b3.place(x=300,y=200)
b3=Button(root,text="clear",command=cr)
b3.place(x=300,y=250)

root.mainloop()