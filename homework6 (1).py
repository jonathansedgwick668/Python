'''
Homework6
Name: Jonathan Sedgwick
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

'''
A base class that defines a device with a name
and a status of on or off
'''
class Device:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"

    # Sets the status variable to ON and
    # prints a confirmation
    def turn_on(self):
        self.status = "ON"
        print(f"{self.name} is now ON.")

    # Sets the status variable to OFF and
    # prints a confirmation
    def turn_off(self):
        self.status = "OFF"
        print(f"{self.name} is now OFF.")

'''
A class that inherits from the Device class
and additionally defines a brightness variable
'''
class Light(Device):
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self.brightness = brightness
    
    # A function that sets the level of brightness
    # if the value inputted is between 0 and 100
    def set_brightness(self, level):
        if (level >= 0 and level <= 100):
            self.brightness = level
            print(f"{self.name} brightness set to {level}.")
        else:
            print("Invalid brightness level. Must be between 0 and 100.")

'''
A class that inherits from the Light class
and defines an additional color variable 
'''
class LEDLight(Light):
    def __init__(self, name, brightness=50, color="White"):
        super().__init__(name, brightness)
        self.color = color
    
    # Changes the color variable to the inputted
    # value and prints a confirmation
    def set_color(self, color):
        self.color = color
        print(f"{self.name} color changed to {color}.")

'''
A class that inherits from the Light class
and defines an additional smart mode variable 
'''
class SmartBulb(Light):
    def __init__(self, name, brightness=50, smart_mode=False):
        super().__init__(name, brightness)
        self.smart_mode = smart_mode
    
    # Sets the smart_mode variable to true
    # and prints confirmation
    def enable_smart_mode(self):
        self.smart_mode = True
        print(f"{self.name} smart mode enabled.")
    
    # Sets the smart_mode variable to false
    # and prints confirmation
    def disable_smart_mode(self):
        self.smart_mode = False
        print(f"{self.name} smart mode disabled.")

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest6.py'))

