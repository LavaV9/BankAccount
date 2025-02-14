from bank_account import BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_num, routing_num, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_num, routing_num)
        self.transfer_limit = transfer_limit  # max amnt

    def transfer(self, amount, recipient):
        if amount > self.transfer_limit:
            print(f"{self.customer_name}: Transfer denied. Exceeds limit of {self.transfer_limit}.")
        elif self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            recipient.current_balance += amount
            print(f"{self.customer_name}: Transferred {amount} to {recipient.customer_name}. New balance: {self.current_balance}")
        else:
            print(f"{self.customer_name}: Transfer denied. Insufficient funds.")
