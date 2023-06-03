from tkinter import *
def clicked(num):
    first_num=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(first_num)+str(num))
root=Tk()
root.geometry("320x350")
root.title("dragon")
root.iconbitmap("dragon.ico")
root.config(background="gray") 
root.attributes('-topmost',True) 
btn1=Button(text="9",height=3,width=10,command=lambda:clicked(9)).grid(column=1,row=10)
btn2=Button(text="8",height=3,width=10,command=lambda:clicked(8)).grid(column=2,row=10)
btn3=Button(text="7",height=3,width=10,command=lambda:clicked(7)).grid(column=3,row=10)
btnx=Button(text="x",height=3,width=10,command=lambda:clicked()).grid(column=4,row=10)
btn4=Button(text="6",height=3,width=10,command=lambda:clicked(6)).grid(column=1,row=11)
btn5=Button(text="5",height=3,width=10,command=lambda:clicked(5)).grid(column=2,row=11)
btn6=Button(text="4",height=3,width=10,command=lambda:clicked(4)).grid(column=3,row=11)
btnsub=Button(text="-",height=3,width=10,command=lambda:clicked()).grid(column=4,row=11)
btn7=Button(text="3",height=3,width=10,command=lambda:clicked(3)).grid(column=1,row=12)
btn8=Button(text="2",height=3,width=10, command=lambda:clicked(2)).grid(column=2,row=12)
btn9=Button(text="1",height=3,width=10, command=lambda:clicked(1)).grid(column=3,row=12)
btnsum=Button(text="+",height=3,width=10,command=lambda:clicked()).grid(column=4,row=12)
btn0=Button(text="0",height=3,width=10,command=lambda:clicked(0)).grid(column=2,row=13)
btndot=Button(text=".",height=3,width=10,command=lambda:clicked()).grid(column=3,row=13)
btn=Button(text="=",height=3,width=10,command=lambda:clicked()).grid(column=4,row=13)
btn0=Button(text="%",height=3,width=10,command=lambda:clicked()).grid(column=1,row=13)
e1=Entry(root).grid(column=0, row=5)







root.mainloop()