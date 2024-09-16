class BankAccount:
    def __init__(self, account_id, balance=1000):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def get_balance(self):
        return self.balance
def display_balance(amount):
   account1 = BankAccount("12345")
   account1.deposit(amount)
   return account1.get_balance()


amount = 500
result = display_balance(amount)

print(result)