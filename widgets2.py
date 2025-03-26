import tkinter as tk

root = tk.Tk()
root.title("Label Widget Example")
root.geometry("300x250")

frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame.pack(padx=10, pady=10)

dynamic_text = tk.StringVar()
dynamic_text.set("This is text.")
dynamic_label = tk.Label(frame, textvariable=dynamic_text)
dynamic_label.pack()

message = tk.Message(frame, text="Enter text in the entry below and the text above will change.")
message.pack()

labelframe = tk.LabelFrame(root, text="Enter text here", padx=10, pady=10)
labelframe.pack(padx=10, pady=10)

entry = tk.Entry(labelframe)
entry.pack()

def show_entry_data():
    entry_data = entry.get()
    dynamic_text.set(entry_data)

button = tk.Button(labelframe, text="Show Entry Data", command=show_entry_data)
button.pack()

root.mainloop()
