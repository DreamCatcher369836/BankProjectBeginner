class Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number 
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive")

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        else:
            self._balance -= amount
            return True
