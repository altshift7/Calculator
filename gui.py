import tkinter as tk
from math_operations import evaluate_expression

def on_button_click(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Window setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

# Display Entry
entry = tk.Entry(root, width=30, font=('Arial', 18), borderwidth=5, relief="sunken")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/', 'sin(',
    '4', '5', '6', '*', 'cos(',
    '1', '2', '3', '-', 'tan(',
    '0', '.', '^', '+', 'log(',
    'sqrt(', 'π', '(', ')', 'C',
    'magnitude(', 'P',
    'C', 'dot', 'cross', '|', '='
]

# Button layout
row, col = 1, 0
for btn in buttons:
    if btn == '=':
        action = calculate_result
    elif btn == 'C':
        action = clear_entry
    else:
        action = lambda x=btn: on_button_click(x)

    tk.Button(root, text=btn, width=8, height=2, command=action).grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Start the GUI loop
root.mainloop()
