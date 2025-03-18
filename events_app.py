import tkinter as tk

# Create window and set default values
window = tk.Tk()
window.title("Cool App")
window.geometry("500x500")
window.configure(bg="pink")

# Create the poem label and create
# variable to keep track of which line
# should be shown
poem_label = tk.Label()
poem_line = 0

# Create the count label and create
# variable that keeps track of the number
# of clicks
count_label = tk.Label(text="0")
count_number = 0

# Function to change background color
def change_background():
    
    if window.cget('bg') == "pink":
        window.configure(bg="gray")
    else:
        window.configure(bg="pink")


# Function to switch between lines of a poem
def show_poem():
    global poem_line
    if (poem_line == 0):
        poem_label.configure(text="I never saw a purple cow")
        poem_line += 1
    elif (poem_line == 1):
        poem_label.configure(text="I never hope to see one")
        poem_line += 1
    elif (poem_line == 2):
        poem_label.configure(text="But I can tell you, anyhow")
        poem_line += 1
    elif (poem_line == 3):
        poem_label.configure(text="I'd rather see than be one!")
        poem_line = 0
        
# Function to change the text of the label
# to show the number of clicks
def change_count():
    new_count = int(count_label.cget("text")) + 1
    count_label.configure(text=(str(new_count)))


background_button = tk.Button(window, text="Change Background", command=change_background)
count_button = tk.Button(window, text="Click me", command=change_count)
poem_button = tk.Button(window, text="Poem!", command=show_poem)

background_button.pack(pady=20)
poem_button.pack(pady=20)
poem_label.pack(pady=20)
count_button.pack(pady=20)
count_label.pack(pady=20)

window.mainloop()
