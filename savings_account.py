from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_num, routing_num, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_num, routing_num)
        self.interest_rate = interest_rate  # whole number that is later made to be percentage

    def apply_interest(self):
        interest = self.current_balance * (self.interest_rate / 100)
        self.current_balance += interest
        print(f"{self.customer_name}: Interest applied at {self.interest_rate}%. New balance: {self.current_balance}")