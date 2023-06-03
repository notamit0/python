class num:
    def __init__(self,a,b):
        self.a=a 
        self.b=b
    def sum(self):
        x=self.a+self.b
        print("sum:",x)

    def sub(self):
        x=self.a-self.b
        print("sub:",x)
    
    def mult(self):
        x=self.a*self.b
        print("mult:",x)


x=num(10,5)
x.sum()
x.sub()
x.mult()