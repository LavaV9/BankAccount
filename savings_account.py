from bank_account import BankAccount

class SavingsAccount(BankAccount):
    interest_rate = 0.05
    interest_as_percent = interest_rate * 100
    def inetrest_function(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance = self.current_balance + interest
        print("New balance with interest is",self.current balance, ". An interest rate of", interest_as_percent,"%")