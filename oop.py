class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

# create an instance of BankAccount
account = BankAccount("123456789", 1000)

# deposit money into the account
account.deposit(500)

# withdraw money from the account
account.withdraw(2000)

# get the account balance
balance = account.get_balance()
print("Account balance:", balance)
