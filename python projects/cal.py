#Task 2 Given by Codsoft
# Python program to create a simple calculator

import tkinter as tk
# Define the on_click function:
def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)
        
# define button
def create_button(text, row, col, col_span=1):
    button = tk.Button(root, text=text, font=("Helvetica", 18), bd=5)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
    button.bind("<Button-1>", on_click)  # Bind the button click event to the on_click() function
    return button

# Create the main tkinter window:
root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

# Create the heading label:
heading_label = tk.Label(root, text="Calculator", font=("Helvetica", 16, "bold"),highlightcolor=("red"))
heading_label.grid(row=0, column=0, columnspan=4, pady=20)

# Create the entry field:
entry = tk.Entry(root, font=("Helvetica", 24), bd=5, justify=tk.LEFT)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)


create_button("7", 2, 0)
create_button("8", 2, 1)
create_button("9", 2, 2)
create_button("/", 2, 3)
# This line creates a button with the label "4" and places it on the grid layout. Here's what each argument does:
# "4" is the text displayed on the button.
# 3 is the row in which the button is placed. In this case, it's the fourth row (0-based index).
# 0 is the column in which the button is placed. Here, it's the first column (0-based index).
create_button("4", 3, 0)
create_button("5", 3, 1)
create_button("6", 3, 2)
create_button("*", 3, 3)

create_button("1", 4, 0)
create_button("2", 4, 1)
create_button("3", 4, 2)
create_button("-", 4, 3)

create_button("0", 5, 0)
create_button(".", 5, 1)
create_button("=", 5, 2)
create_button("+", 5, 3)

create_button("C", 6, 0, 3)

root.mainloop()