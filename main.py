from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

def main():
    Gru_checking = CheckingAccount("Gru", 200, 0, "9999", "0", 50)
    Gru_checking.deposit(100)
    Gru_checking.withdraw(50)
    Gru_checking.print_customer_information()

    Minion_savings = SavingsAccount("M", 10000, 0, "5555", "0", 9)
    Minion_savings.deposit(1000)
    Minion_savings.withdraw(3001)
    Minion_savings.print_customer_information()
    Minion_savings.apply_interest()

if __name__ == "__main__":
    main()
