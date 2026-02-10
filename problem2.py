#Problem 2 (Medium): Bank Account Management
class BankAccount:
    bank_name = "Urgench Bank"
    total_accounts = 0
    min_balance = 10
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance
        BankAccount.total_accounts += 1
    def deposit(self, amount):
        new_balance = self.balance + amount
        if amount > 0:
        
            self.balance = new_balance
            print(f"Deposited {amount}. New balance: {new_balance}")

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance < BankAccount.min_balance:
            print("Insufficient funds or below minimum balance")
            
        else:
            
            print(f"Withdrew {amount}. New balance: {new_balance}")
            self.balance = new_balance
            
               
    def display_account_info(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}, Bank: {BankAccount.bank_name}")
account1 = BankAccount("Ali", 100)
account1.display_account_info()
account1.deposit(50)
account1.withdraw(80)

account2 = BankAccount("Vali", 50)
account2.display_account_info()
account2.withdraw(100)
print(f"Total accounts created:{BankAccount.total_accounts}")


        

        