from bank_account import BankAccount

account = BankAccount("Hind", 1000)

print("Account holder:", account.get_account_holder())
print("Initial balance:", account.get_balance())

account.deposit(500)
print("After deposit:", account.get_balance())

try:
    account.withdraw(2000)
except Exception as e:
    print("Error:", e)

print("Final balance:", account.get_balance())
