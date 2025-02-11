'''
Homework3
Name: Jonathan Sedgwick
github link: https://github.com/jonathansedgwick668/Python/edit/main/homework3%20(1).py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''


'''
A class decorator that takes in a function
and outputs the steps that the function takes
'''
class Decorator:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwds):
        result = self.func(*args, **kwds)
        return result
    
'''
A class that takes in a number and prints
each step in finding the factorial of that number
'''
@Decorator
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(f"Factorial product = {factorial}. Currently multiplying by {i}")
    print(factorial)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))
    
