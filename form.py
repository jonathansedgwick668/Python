import tkinter as tk

root = tk.Tk()

root.title("Form")
root.geometry("300x100")

name_label = tk.Label(root, text="Name:")
email_label = tk.Label(root, text="Email:")
password_label = tk.Label(root, text="Password:")

name_label.grid(row=0, column=0)
email_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)

name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
email_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

root.mainloop()
