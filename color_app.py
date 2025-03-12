import tkinter as tk

root = tk.Tk()

root.title("App")
root.geometry("300x100")

def on_button_press(event):
    event.widget.config(fg='black')

def on_button_release(event):
    event.widget.config(fg='white')

button1 = tk.Button(root, text="Press Me", bg='blue', fg='white')

button1.bind('ButtonPress-1', on_button_press)
button1.bind('<ButtonRelease-1>', on_button_release)

button2 = tk.Button(root, text="Press Me", bg='green', fg='white')
button2.bind('<Button-1>', on_button_press)
button2.bind('<ButtonRelease-1>', on_button_release)

button3 = tk.Button(root, text="Press Me", bg='red', fg='white')
button3.bind('<Button-1>', on_button_press)
button3.bind('<ButtonRelease-1>', on_button_release)

label1 = tk.Label(root, text="Blue Button")
label2 = tk.Label(root, text="Green Button")
label3 = tk.Label(root, text="Red Button")


button1.grid(row=0, column=1)
button2.grid(row=1, column=1)
button3.grid(row=2, column=1)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)


root.mainloop()
