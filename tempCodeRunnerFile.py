class User:		# here's what we have so far
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self	# the specific user's account increases by the amount of the value recei
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self, amount):
        self.account_balance == account_balance
        return self
Maxine = User('Maxine Causevic', 'maxine@fitmaxpersonaltraining.com',(10000))
Christine = User('Christine Chaikouang', 'cchaikouang@gmail.com', (20000))
Robert = User('Robert Chaikouang', 'rchaikouang@gmail.com', (30000))

print(Maxine.account_balance)
Maxine.make_deposit(3000)
print(Maxine.account_balance)
Maxine.make_deposit(2000)
Maxine.make_deposit(100)
Maxine.make_withdrawal(100)
print(f"{Maxine.name} {Maxine.email} {Maxine.account_balance}")

Christine.make_deposit(200).make_deposit(200).make_deposit(200)