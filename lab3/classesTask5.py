class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("+", amount, "=>", self.balance)
        else:
            print("nope")

    def withdraw(self, amount):
        if amount > self.balance:
            print("no money")
        elif amount <= 0:
            print("nope")
        else:
            self.balance -= amount
            print("-", amount, "=>", self.balance)


acc = Account("Axa", 100)
acc.deposit(50)
acc.withdraw(30)   
acc.withdraw(200)
acc.deposit(-10)
acc.withdraw(-5)
