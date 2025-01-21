'''
Homework1
Name: Jonathan Sedgwick
github link: 
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:

    # Initializer that takes in a name and starting 
    # amount and creates a Bank Account object,
    # also establishes the account_balance variable 
    # and sets it equal to starting_amount.
    def __init__(self,name,starting_amount):
        self.name = name
        self.starting_amount = starting_amount
        self.account = self.starting_amount
    
    # A repr statement that outputs information
    # about the object, such as the name and
    # account balance.
    def __repr__(self):
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"
    
    # A str statement that outputs information
    # about the object, such as the name and
    # account balance, in a formatted way.
    def __str__(self):
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"
    

    # Takes in an amount. If the amount is less than
    # zero, then the balance won't change. If the 
    # amount is greater than zero, then the balance
    # will increase by that amount.
    def deposit(self,amount):
        if(amount <= 0):
            print("Please deposit a positive number.")
        else:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")

    # Takes in an amount. If the amount is greater than 
    # zero and it doesn't overdraw the account, the amount
    # be withdrawn from account_balance. If the amount is
    # greater than the account_balance, then the amount will
    # not be drawn.
    def withdraw(self,amount):
        if(amount <= 0):
            print("Please withdraw an amount greater than zero.")
        elif(amount > self.account):
            print("Insufficient funds.")
        else:
            self.account -= amount
            print(f"{amount} withdrawn. New balance: {self.account}")

    # Outputs the current account balance
    def check_balance(self):
        print(f"Balance: {self.account}")

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))
