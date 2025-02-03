'''
args_assignment.py
Name: Jonathan Sedgwick
github link: https://github.com/jonathansedgwick668/Python/edit/main/args_assignment.py
'''

# Function to print out a formatted
# list of participants and their contact
# details.
def conference_signup(*names, **info):
    # If a list of names is not provided,
    # then the function outputs a message
    # saying that not enough data was provided
    if not names:
        print("Not enough data provided")
    else:
        print("Conference Participants and Their Contact Details:")
        print("--------------------------------------------------")
        # A for loop that runs through the list of names and prints
        # the details
        for name in names:
            print(f"Name: {name}")
            try:
                # Checks if the tuple given in the info dictionary
                # has both an email and phone
                if (len(info[name]) == 2):
                    print(f"Email: {info[name][0]}\nPhone: {info[name][1]}")
                # If the tuple doesn't have an email and a number,
                # then the function prints out just the email.
                else:
                    print(f"Email: {info[name]}")
                    print("Phone: N/A")
            # Catches the error for when a name is given in the names list,
            # but details are not given in the info dictionary
            except KeyError:
                print("Email: N/A\nPhone: N/A")
            print("--------------------------------------------------")
            


conference_signup("John", "Sam", "Becky", "Carl", 
                  John = ("john@gmail.com","123-456-7890"),
                  Sam = ("sam@gmail.com", "143-256-7500"),
                  Carl = ("carl@gmail.com"))



print("\n")


conference_signup("John", "Sam",
                  John = ("john@gmail.com"),
                  Sam = ("sam@gmail.com", "143-256-7500"))
print("\n")

conference_signup("John", "Sam")

print("\n")

conference_signup()
