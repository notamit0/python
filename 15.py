from tkinter import *
def add():
    c=int(txt1.get())+int(txt2.get())
    lbl.config(text=str(c))
def sup():
    c=int(txt1.get())-int(txt2.get())
    lbl.config(text=str(c))

root=Tk()
txt1=Entry(root)
txt2=Entry(root)
btn=Button(root,text="SUM", command=add)
btn2=Button(root,text="sup", command=sup)
lbl=Label()
txt1.pack()
txt2.pack()
btn.pack()
btn2.pack()
lbl.pack()

root.mainloop()