class User:		# here's what we have so far
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account = BankAccount
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account += amount
        return self	# the specific user's account increases by the amount of the value recei
    def make_withdrawal(self, amount):
        self.account -= amount
        return self
    def display_user_balance(self, amount):
        self.account == self.account
        return self

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