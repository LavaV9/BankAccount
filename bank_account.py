class BankAccount:
    title = "the Bank of Evil"

    def __init__(self, customer_name, current_balance, minimum_balance, account_num,routing_num):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_num = account_num
        self.__routing_num = routing_num

    def deposit(self, amount):
        self.current_balance += amount
        print(f"{self.current_balance} is your new current balance")

    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f" Your new balance is {self.current_balance} because you withdrew {amount}")
        else:
            print("User cannot withdraw")

    def print_customer_information(self):
        print(f"The customer's name is {self.customer_name} and their current balance is {self.current_balance} at {self.title}")


a1 = BankAccount("Gru", 200, 0)
a1.deposit(100)
a1.withdraw(50)
a1.print_customer_information()

a2 = BankAccount("Minion", 10000, 8000)
a2.deposit(1000)
a2.withdraw(3001)
a2.print_customer_information()