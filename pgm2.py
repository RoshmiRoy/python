class bankaccount:
    def __init__(self):
        self.balance = 0
        self.name = input("enter the name")
        self.accountnumber = input("enter the  account number")
        print("hello welcome")
    def deposit(self):
        amount = float(input("enter the amount to deposite"))
        self.balance = self.balance + amount
        print("amount depoited",amount)
    def withdrow(self):
        amount = float(input("enter the amount to withdrow"))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("amount withdrowed",amount)
        else:
            print("transcation declied due to insufficient balance")
    def display(self):
           print("__________________________________________________")
           print(self.name, "has the balanced amount",self.balance  )
           print("thank you vist again")
           print("__________________________________________________")
bankaccount1 = bankaccount()
bankaccount1.deposit()
bankaccount1.withdrow()
bankaccount1.display()