'''
A file that defines a calculator class and then
tests the class using different values.
'''


class Calculator:
    '''
    A class that defines functions for a calculator such as:
    add, subtract, multiply, divide, and the ability to clear
    and get a value.
    '''
    def __init__(self, value=0):
        '''
        Initializes the value variable,
        making it 0 as default.
        '''
        self.value = value

    def add(self, num):
        '''
        Adds the num variable to the 
        value variable.
        '''
        self.value += num

    def subtract(self, num):
        '''
        Subtracts the num variable from the 
        value variable.
        '''
        self.value -= num

    def multiply(self, num):
        '''
        Multiplies the num variable by the 
        value variable and sets the value variable
        to that number.
        '''
        self.value *= num

    def divide(self, num):
        '''
        Divides the value variable by the num variable
        unless it is zero.
        '''
        if num != 0:
            # If statement to check if the inputted
            # number is 0, since you can't divide by 0.
            self.value /= num
        else:
            # Raises exception if the inputted number is zero
            raise ValueError("Cannot divide by zero")

    def clear(self):
        '''
        Clears the value variable by setting
        it to 0.
        '''
        self.value = 0

    def get_value(self):
        '''
        Returns the value variable.
        '''
        return self.value

def main():
    calc = Calculator()
    calc.add(10)
    calc.subtract(2)
    calc.multiply(5)
    try:
        calc.divide(0)
    except ValueError as e:
        print(e)
    calc.divide(4)
    print(f"Final value: {calc.get_value()}")
    print(help(calc))

if __name__ == "__main__":
    main()
