make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
display_user_balance(self) - have this method print the user's name and account balance to the terminal
eg. "User: Guido van Rossum, Balance: $150
BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


 Create a file with the User class, including the __init__ and make_deposit methods
 Add a make_withdrawal method to the User class
 Add a display_user_balance method to the User class
 Create 3 instances of the User class
 Have the first user make 3 deposits and 1 withdrawal and then display their balance
 Have the second user make 2 deposits and 2 withdrawals and then display their balance
 Have the third user make 1 deposits and 3 withdrawals and then display their balance
 BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

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

Maxine.make_deposit(3000).make_deposit(2000).make_deposit(100).make_withdrawal(100)
print(Maxine.account_balance)
print(f"{Maxine.name} {Maxine.email} {Maxine.account_balance}")

Christine.make_deposit(200).make_deposit(200).make_deposit(200).make_deposit(200)
print(Christine.account_balance)

Robert.make_deposit(500).make_withdrawal(100).make_withdrawal(100)
print(Robert.account_balance)

