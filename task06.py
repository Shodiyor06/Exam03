class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, depo):
        self.depo = depo
        
    def withdraw(self, withdraw):
        self.withdrav = withdraw 
        

    def get_balance(self):
        print(f"{self.balance + self.depo - self.withdrav} ")

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())