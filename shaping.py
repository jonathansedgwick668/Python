import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My Window")
root.geometry("400x500")  
root.minsize(300, 300) 
root.maxsize(500, 500)  

def on_closing():
    if messagebox.askokcancel("Quit", "Close window?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def show_messages():
    messagebox.showerror("Error", "This is an error")
    messagebox.showwarning("Warning", "This is a warning")
    messagebox.showinfo("Information", "This is information")

message_button = tk.Button(root, text="Show Messages", command=show_messages)
message_button.pack()

def askyesno():
    response = messagebox.askyesno("Question", "Do you want to proceed?")
    if response:
        messagebox.showinfo("Decision", "You chose yes!")   
    else:
        messagebox.showinfo("Decision", "You chose no!")

def askokcancel():
    response = messagebox.askokcancel("Confirmation", "Do you want to continue?")
    if response:
        messagebox.showinfo("Decision", "You want to continue!")   
    else:
        messagebox.showinfo("Decision", "You don't want to continue!")   

def askretrycancel():
    response = messagebox.askretrycancel("Retry", "Do you want to retry?")
    if response:
        messagebox.showinfo("Decision", "You want retry!")  
    else:
        messagebox.showinfo("Decision", "You want to cancel!")  

yesno_button = tk.Button(root, text="Yes or no", command=askyesno)
yesno_button.pack()
okcancel_button = tk.Button(root, text="Okay or cancel", command=askokcancel)
okcancel_button.pack()
retrycancel_button = tk.Button(root, text="Retry or cancel", command=askretrycancel)
retrycancel_button.pack()

root.mainloop()
