'''
Homework4
Name: Jonathan Sedgwick
github link: https://github.com/jonathansedgwick668/Python/blob/main/homework4%20(1).py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

# A class that defines a car
class Car:
    # Class variable that tracks 
    # total number of cars
    total_cars = 0
    
    # Init functiont that defines the
    # variables brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    # Prints the car info in a 
    # formatted way
    def display_info(self):
        print(f"'Car: {self.brand} {self.model}'")
    
    # Updates the class variable
    # with the value of count
    @classmethod
    def update_total_cars(cls, count):
        cls.total_cars = count
    
    # Prints general info about cars
    @staticmethod
    def general_info():
        print("'Cars are a mode of transportation.'")

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))

