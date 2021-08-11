class User:		# here's what we have so far
    # Constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    # adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    # adding the withdrawal method
    def make_withdrawal(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance -= amount	# the specific user's account decrease by the amount of the value withdrawn
        return self

    # adding the display method
    def display_user_balance(self):	# no arguments needed. Prints the user name and its actual balance
        print(f"User:{self.name}, Balance: {self.account_balance}")
        return self

    # adding the transfer method
    def transfer_money(self, amount, user_recipient): # takes two argumens: the amount transfered and the user who is going to receive the transfer
        self.account_balance -= amount
        user_recipient.account_balance += amount
        return self

# 3 users are created
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
greg = User("Greg Petersen", "greg@python.com")

# First user make 3 deposits and 1 withdrawals
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(250).display_user_balance()

# Second user make 2 deposits and 2 withdrawals
monty.make_deposit(500).make_deposit(300).make_withdrawal(100).make_withdrawal(150).display_user_balance()

# Third user make 1 deposits and 3 withdrawals
greg.make_deposit(500).make_deposit(50).make_withdrawal(100).make_withdrawal(50).display_user_balance()

# Third user transfer money to thir user

guido.transfer_money(50, greg).display_user_balance()
greg.display_user_balance()