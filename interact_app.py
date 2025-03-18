import tkinter as tk

root = tk.Tk()
root.geometry("400x400")  
root.configure(bg="white")  

goodbye_button = tk.Button(root, text="Goodbye!", command=root.destroy)

def change_color():
    root.configure(bg="purple")

def change_size():
    
    if root.winfo_width() == 400 and root.winfo_height() == 400:
        root.geometry("1000x1000")
    else:
        root.geometry("400x400")

def change_text():
    
    if goodbye_button.cget("text") == "Goodbye!":
        goodbye_button.configure(text="Hello!")
    else:
        goodbye_button.configure(text="Goodbye!")

root.after(5000, change_color)

goodbye_button.pack(pady=20)
goodbye_button.focus_set()

size_button = tk.Button(root, text="Size", command=change_size)
size_button.pack(pady=20)

change_button = tk.Button(root, text="Change", command=change_text)
change_button.pack(pady=20)


root.mainloop()
