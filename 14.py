from tkinter import *

root = Tk()
root.title("dragon") #name
root.geometry("500x300") #size
root.resizable(True,True) #to allow size or not
root.iconbitmap("dragon.ico") #icone
root.configure(background='#0015a0') #background color
root.attributes('-topmost',True) #pin it as top
lable=Label(root,text="Welcome", bg="#0015a0", fg="white",).place(x=130,y=10)
lable=Label(root,text="mark 1", bg="#0015a0", fg="white",).place(x=10,y=50)
lable=Label(root,text="mark 2", bg="#0015a0", fg="white",).place(x=10,y=100)
e1=Entry(root).place(x=90,y=50)
e2=Entry(root).place(x=90,y=100)
btn=Button(root,text="SUM")
root.mainloop()