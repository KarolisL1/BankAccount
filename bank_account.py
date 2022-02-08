class BankAccount:
# don't forget to add some default values for these parameters!
    def __init__(self):
        self.int_rate = 0.01
        self.balance = 0
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self

account_1 = BankAccount().deposit(50).deposit(20).deposit(20).withdraw(50).yield_interest().display_account_info()
account_2 = BankAccount().deposit(200).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()





