import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, bg="white", fg="black", text="Hover over me", cursor="hand2")
button1.pack(pady=20)

button2 = tk.Button(window, bg="green", fg="blue", text="Hover over me", cursor="hand2")
button2.pack(pady=20)

button3 = tk.Button(window, bg="purple", fg="gray", text="Hover over me", cursor="hand2")
button3.pack(pady=20)

label1 = tk.Label(window, text="Hello world!", font=("Arial", 20, "bold"), bd=5, relief="solid", anchor="w")
label2 = tk.Label(window, text="Hello world!", font=("Times New Roman", 24, "italic"), underline=True, anchor="e")
label3 = tk.Label(window, text="Hello world!", font=("Courier New", 28, "underline"), bg="blue", fg="white", anchor="n")

label1.pack(pady=5)
label2.pack(pady=5)
label3.pack(pady=5)

window.mainloop()
