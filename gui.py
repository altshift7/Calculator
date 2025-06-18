import tkinter as tk
from tkinter import messagebox
from math_operations import evaluate_expression

DARK_BG = "#1e1e1e"
DARK_FG = "#ffffff"
LIGHT_BG = "#ffffff"
LIGHT_FG = "#000000"

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        self.dark_mode = False
        self.history = []

        # === Input ===
        self.input_var = tk.StringVar()
        self.input_var.trace("w", self.update_preview)

        self.input_entry = tk.Entry(root, textvariable=self.input_var, font=("Arial", 16), width=30)
        self.input_entry.pack(pady=10)

        # === Result ===
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()

        # === Buttons ===
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        buttons = [
            "7", "8", "9", "+", "sin",
            "4", "5", "6", "-", "cos",
            "1", "2", "3", "*", "tan",
            "0", ".", "^", "/", "sqrt",
            "log", "π", "(", ")", "Clr"
        ]

        for i, btn in enumerate(buttons):
            b = tk.Button(button_frame, text=btn, width=5, height=2,
                          command=lambda val=btn: self.on_button_click(val))
            b.grid(row=i // 5, column=i % 5, padx=3, pady=3)

        # === Submit ===
        tk.Button(root, text="Evaluate", command=self.evaluate).pack(pady=5)

        # === History ===
        self.history_box = tk.Text(root, height=5, font=("Arial", 10))
        self.history_box.pack(pady=5)

        # === Dark Mode ===
        self.dark_button = tk.Button(root, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.dark_button.pack(pady=5)

        self.apply_theme()

    def on_button_click(self, value):
        if value == "Clr":
            self.input_var.set("")
            self.result_label.config(text="")
        elif value == "π":
            self.input_var.set(self.input_var.get() + "π")
        else:
            self.input_var.set(self.input_var.get() + value)

    def evaluate(self):
        expr = self.input_var.get()
        result = evaluate_expression(expr)
        self.result_label.config(text=result)

        if "Error" not in result:
            self.history.append(f"{expr} = {result}")
            self.update_history()
        else:
            messagebox.showerror("Calculation Error", result)

    def update_history(self):
        self.history_box.delete(1.0, tk.END)
        for item in self.history[-5:]:
            self.history_box.insert(tk.END, item + "\n")

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        bg = DARK_BG if self.dark_mode else LIGHT_BG
        fg = DARK_FG if self.dark_mode else LIGHT_FG

        self.root.configure(bg=bg)
        self.input_entry.configure(bg=bg, fg=fg, insertbackground=fg)
        self.result_label.configure(bg=bg, fg=fg)
        self.history_box.configure(bg=bg, fg=fg, insertbackground=fg)
        self.dark_button.configure(bg=bg, fg=fg)

    def update_preview(self, *args):
        expr = self.input_var.get()
        if expr.strip():
            result = evaluate_expression(expr)
            self.result_label.config(text=result)
        else:
            self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
