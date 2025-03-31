import tkinter as tk

root = tk.Tk()
root.title("Christmas Tree")

canvas = tk.Canvas(root, width=400, height=300, bg='black', borderwidth=2)
canvas.pack()

canvas.create_polygon(200, 50, 250, 150, 150, 150, outline='green', fill='green', width=5)
canvas.create_rectangle(175, 154, 225, 175, outline='brown', fill='brown', width=1)

canvas.create_oval(180, 120, 190, 130, outline='red', fill='red', width=2)
canvas.create_oval(200, 100, 210, 110, outline='blue', fill='blue', width=2)
canvas.create_oval(210, 130, 220, 140, outline='yellow', fill='yellow', width=2)


canvas.create_text(200, 250, text="Happy Holidays!", font=('Arial', 20), fill='white')

root.mainloop()
