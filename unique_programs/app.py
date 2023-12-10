class BankAccount:
    def _init_(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def transfer(self, amount, recipient_account):
        if amount <= 0 or amount > self.balance:
            print("Invalid transfer amount")
            return

        self.balance -= amount
        recipient_account.balance += amount

        print(f"Transferred {amount} from account {self.account_number} to account {recipient_account.account_number}")
        print(f"New balance for account {self.account_number}: {self.balance}")
        print(f"New balance for account {recipient_account.account_number}: {recipient_account.balance}")


# Example usage:
# Create two accounts
account1 = BankAccount(account_number="123456", balance=1000)
account2 = BankAccount(account_number="789012", balance=500)

# Transfer money from account1 to account2
transfer_amount = float(input("Enter the amount to transfer: "))
account1.transfer(transfer_amount, account2)