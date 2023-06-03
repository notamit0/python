class num:
    def __init__(self,name,age,amount,year):
        self.name=name
        self.age=age
        self.amount=amount
        self.year=year
    def display(self):
        print("Customer Name:",self.name)
        print("customer Acc No :",self.age)
        print("Balance :",self.amount)
    def div(self):
        balance=self.amount*10/100;
        print("Intrest   :",balance)
        self.balance=balance
    def yr(self):
        ye=self.year*self.balance
        print("your year intrest:",ye)
        self=ye=ye
    def mt(self):
        mo=self.balance//12
        print("your monthly intrest:",mo)

name=input("Enter Customer Name->")
age=input("Enter Customer Acc No->")
amount=int(input("Enter Customer Acc Balance:->"))
year=int(input("enter the year->"))
print("thank for choseing as. your details is here")
print("")
print("")
x=num(name,age,amount,year)
x.display()
x.div()
x.yr()
x.mt()
print("")
print("if you can give as your feedback it can help an inprove")
n=(input("enter your feedback->"))
print("thank for the feedback")

