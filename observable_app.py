import tkinter as tk

root = tk.Tk()
root.title("Greeting App")

name_var = tk.StringVar()
age_var = tk.StringVar()
message_var = tk.StringVar()

tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)

def update_message(*args):
    name = name_var.get()
    age = age_var.get()
    
    if name and age:
        message_var.set(f"Hello, {name}! You are {age} years old.")
    else:
        message_var.set("")

name_var.trace_add("write", update_message)
age_var.trace_add("write", update_message)

tk.Label(root, textvariable=message_var).grid(row=2, columnspan=2)

root.mainloop()
