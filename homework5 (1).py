'''
Homework5
Name: Jonathan Sedgwick
github link: https://github.com/jonathansedgwick668/Python/blob/main/homework5%20(1).py
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class BakeryItem:
    """Abstract class representing a bakery item."""
    
    def __init__(self, size, flavor):
        self.size = size
        self.flavor = flavor
        self.add_ins = []
    
    def add_add_ins(self, add_in):
        """Abstract method to add an ingredient to the item."""
        pass

    def get_description(self):
        """Abstract method to get the item description."""
        pass

class Croissant(BakeryItem):
    """Concrete class representing a croissant."""
    
    # Initializes the class with size and flavor
    # using the BakeryItem initializer
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    # Defines the add_add_ins method,
    # adds the inputed add in to the add_in list
    # and prints out a message confirming it
    def add_add_ins(self, add_in):
        self.add_ins.append(add_in)
        print(f"Added {add_in} to the croissant.")
    
    # Prints a formatted description of the
    # item including the add ons
    def get_description(self):
        return f"{self.size} {self.flavor} croissant with {self.add_ins[0]}."

class Muffin(BakeryItem):
    """Concrete class representing a muffin."""
    
    # Initializes the class with size and flavor
    # using the BakeryItem initializer
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    # Defines the add_add_ins method,
    # adds the inputed add in to the add_in list
    # and prints out a message confirming it
    def add_add_ins(self, add_in):
        self.add_ins.append(add_in)
        print(f"Added {add_in} to the muffin.")
    
    # Prints a formatted description of the
    # item including the add ons
    def get_description(self):
        return f"{self.size} {self.flavor} muffin with {self.add_ins[0]}."


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest5.py'))
