class start:
    def type(self):
        self.a=int(input("Enter 1st number"))
        self.b=int(input("Enter 2nd number"))
# for typing the number you whant to ues
class adding(start):
    def sun(self):
        c=self.a+self.b 
        print("Sum   :",c)
class sub:
    def sub(self):
        c=self.a-self.b
        print("Sub  :",c)
# ths is for addin su
class py:
    def sv(self):
        c=self.a+self.b 
        print("test   :",c)

class deve(adding,sub,py):
    def div(self):
        c=self.a*self.b 
        print("dev   :",c)
t=deve()
t.type()
t.sun()
t.sub()
t.div()
t.sv()