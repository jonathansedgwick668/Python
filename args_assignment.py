def conference_signup(*names, **info):
    if not names:
        print("Not enough data provided")
    else:
        print("Conference Participants and Their Contact Details:")
        print("--------------------------------------------------")
        for name in names:
            print(f"Name: {name}")
            try:
                if (len(info[name]) == 2):
                    print(f"Email: {info[name][0]}\nPhone: {info[name][1]}")
                else:
                    print(f"Email: {info[name]}")
                    print("Phone: N/A")
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