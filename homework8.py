'''
Homework8
Name: Jonathan Sedgwick
github link: https://github.com/jonathansedgwick668/Python/blob/main/homework8.py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''


class InsufficientFundsError(Exception):
    '''
    Defines a custom error to handle a case where
    there is insufficient funds
    '''
    def __init__(self, message):
        super().__init__(f"InsufficientFundsError: {message}")


class InvalidAmountError(Exception):
    '''
    Defines a custom error to handle a case where
    the amount variable is of invalid type
    '''
    def __init__(self, message):
        super().__init__(f"InvalidAmountError: {message}")

# Function to withdraw money
def withdraw_money(balance, amount):
    '''
    Outputs the amount withdrawn from the account based on the
    inputted values, also handles potential errors
    '''
    try:
        # Checks to see if the amount variable is the right type
        if not isinstance(amount, (int, float)):
           raise InvalidAmountError("Amount must be a positive number.")
        
        # Checks to see if the amount variable is a positive number
        if amount < 0:
           raise InvalidAmountError("Amount must be a positive number.")

        # Checks to see if the amount is greater than the balance
        if amount > balance:
            raise InsufficientFundsError("Insufficient funds in account.")
    
        # Outputs the amount withdrawn 
        print(balance - amount)
    
    except InvalidAmountError as amounterror:
        print(amounterror)
    except InsufficientFundsError as fundserror:
        print(fundserror)
    
        
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py'))

