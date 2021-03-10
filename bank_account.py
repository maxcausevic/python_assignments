class BankAccount:
    def __init__(self, int_rate, account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance < amount:
            print("Insufficient funds: Charging a $5 fee and deduct $5")
        return self

    def display_account_info(self):
        self.account_balance == self.account_balance
        return self

    def yield_interest(self):
        self.account_balance = (self.int_rate * self.account_balance)+self.account_balance


account1 = BankAccount(.03, 200)
account2 = BankAccount(.04, 400)

account1.deposit(200).deposit(100).deposit(100).withdraw(100).yield_interest()
print(account1.account_balance)

account2.deposit(200).deposit(200).withdraw(100).withdraw(200).withdraw(100).withdraw(100).yield_interest()
print(account2.account_balance)