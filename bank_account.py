class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.__account_holder = account_holder
        self.__balance = initial_balance if initial_balance >= 0 else 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.__balance:
            raise Exception("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder
