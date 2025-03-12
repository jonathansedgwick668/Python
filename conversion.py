import tkinter as tk

root = tk.Tk()
root.title("Weight Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

amount_label = tk.Label(frame, text="Enter the amount:")
amount_label.pack()
amount_entry = tk.Entry(frame)
amount_entry.pack()

conversion_type = tk.StringVar(value="lb_to_kg")
lb_to_kg_radio = tk.Radiobutton(frame, text="Pounds to Kilograms", variable=conversion_type, value="lb_to_kg")
lb_to_kg_radio.pack()
kg_to_lb_radio = tk.Radiobutton(frame, text="Kilograms to Pounds", variable=conversion_type, value="kg_to_lb")
kg_to_lb_radio.pack()

def calculate():
    try:
        amount = float(amount_entry.get())
        if conversion_type.get() == "lb_to_kg":
            result = amount * 0.453592
            result_label.config(text=f"{amount} lbs is {result:.2f} kg")
        else:
            result = amount / 0.453592
            result_label.config(text=f"{amount} kg is {result:.2f} lbs")
    except ValueError:
        result_label.config(text="Please enter a valid number")

calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

root.mainloop()
