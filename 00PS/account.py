class Account:
    def __init__(self, title, balance, account_no, interest_rate):
        self.title = title
        self.balance = balance
        self.account_no = account_no
        self.interest_rate = interest_rate

    def change_title(self, new_title):
        self.title = new_title

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient money")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} New balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} New balance: {self.balance}")

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Added interest. New balance: {self.balance}")
        
my_account = Account("Savings", 1000, "123456789", 2.0)
my_account.change_title("Checking")
my_account.withdraw(500)
my_account.deposit(200)
my_account.add_interest()
