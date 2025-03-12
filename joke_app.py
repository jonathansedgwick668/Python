import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Joke")
root.geometry("300x150")

joke_label = tk.Label(root, text="What is a tornado's favorite game to play?")
joke_label.pack(pady=20)

def show_punchline():
    messagebox.showinfo("Punchline", "Twister!")
    root.destroy()

punchline_button = tk.Button(root, text="Show Punchline", command=show_punchline)
punchline_button.pack(pady=10)

root.mainloop()
