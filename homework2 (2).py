'''
Homework2
Name: Jonathan Sedgwick
github link: https://github.com/jonathansedgwick668/Python/blob/main/homework2%20(2).py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        # your code here
        self.name=name
        self.account = starting_amount
    
    def __repr__(self):
        # your code here
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"
    
    def __str__(self):
        # your code here:
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"
    
    def deposit(self,amount):
        # your code here
        if amount>0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print(f"Please deposit a positive number.")
    
    def withdraw(self,amount):
        if amount>0:
            if self.account-amount>=0:
                self.account-=amount
                print(f"{amount} withdrawn. New balance: {self.account}")
            else:
                print(f"Insufficient funds.")
        else:
            print(f"Please withdraw an amount greater than zero.")

    
    def check_balance(self):
        """
        Check and return the balance of the account holder's account.
        """
        print(f"Balance: {self.account}")

# Savings Account class that takes in a name, starting amount
# and an interest rate. It inherits from the Bank_Account class.
class SavingsAccount(Bank_Account):
    
    # Initializer function that creates a new SavingsAccount object.
    # It calls the init function from BankAccount and adds the variable
    # interest_rate as well.
    def __init__(self, name, starting_amount, interest_rate = 1):
        super().__init__(name, starting_amount)
        self.interest_rate = interest_rate

    # Repr function that outputs the object as a string
    def __repr__(self):
        return f"SavingsAccount(account_holder='{self.name}', balance={self.account}, interest_rate={format(self.interest_rate, '.1f')}%)"

    # Str function that outputs the function in a more
    # formatted way
    def __str__(self):
        return f"Savings Account - {self.name}: Balance = ${format(self.account, '.2f')}, Interest Rate = {format(self.interest_rate, '.1f')}%"

    # Function that adds interest to the
    # account balance by using the interest_rate
    # variable in the interest rate equation.
    def apply_interest(self):
        self.account += (self.account * (self.interest_rate/100))
        print(self.account)

# Checking account class that takes in a name,
# starting amount, and overdraft limit. It 
# inherits from the Bank_Account class.
class CheckingAccount(Bank_Account):
    

    # Initializer function that creates a new CheckingAccount object.
    # It calls the init function from BankAccount and adds the variable
    # overdraft_limit as well.
    def __init__(self, name, starting_amount, overdraft_limit = 100):
        super().__init__(name, starting_amount)
        self.overdraft_limit = overdraft_limit

    # Repr function that outputs the object as a string
    def __repr__(self):
        return f"CheckingAccount(account_holder='{self.name}', balance={self.account}, overdraft_limit={format(self.overdraft_limit, '.1f')})"
    
    # Str function that outputs the function in a more
    # formatted way
    def __str__(self):
        return f"Checking Account - {self.name}: Balance = ${format(self.account, '.2f')}, Overdraft Limit = ${format(self.overdraft_limit, '.2f')}"

    # Function that substracts the withdraw amount
    # from the balance if the amount is greater
    # than 0 and less than the overdraft limit.
    def withdraw(self, withdraw):
        if (withdraw <= 0):
            print("Withdrawal amount must be positive.")
        elif (withdraw > self.overdraft_limit):
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.account -= withdraw
            print(self.account)
            


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))
