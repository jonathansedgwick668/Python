'''
Best Practices Assignment
Name: Jonathan Sedgwick
github link: https://github.com/jonathansedgwick668/Python/blob/main/best_practices.py
'''



def compare_and_print(num1, num2):
  
  # Checks if either value is 0
  # and prints "Zero Found" is one
  # value is 0
  if num1 == 0 or num2 == 0:
    return "Zero found"

  # Handles positive values and
  # finds the smaller and larger
  # values, prints the values an 
  # amount of times based on which is
  # larger
  if num1 > 0 and num2 > 0:
    smaller_value = min(num1, num2)
    larger_value = max(num1, num2)

    for i in range(smaller_value):
      print(larger_value)
      return

  # Handles negative values,
  # returning the difference.
  if num1 < 0 or num2 < 0:
    return num1 - num2
