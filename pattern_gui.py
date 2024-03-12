import tkinter as tk
from tkinter import ttk
from pattern_generator import PatternGenerator

class PatternGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Pattern Generator")

        self.pattern_var = tk.StringVar()
        self.pattern_var.set("Pyramid")

        self.label_pattern = tk.Label(master, text="Select Pattern:")
        self.label_pattern.pack()

        self.combo_pattern = ttk.Combobox(master, textvariable=self.pattern_var, values=["Pyramid", "Square", "Alternating"])
        self.combo_pattern.pack()

        self.label_rows = tk.Label(master, text="Number of Rows:")
        self.label_rows.pack()

        self.entry_rows = tk.Entry(master)
        self.entry_rows.pack()

        self.generate_button = tk.Button(master, text="Generate Pattern", command=self.generate_pattern)
        self.generate_button.pack()

        self.result_text = tk.Text(master, height=10, width=30)
        self.result_text.pack()

    def generate_pattern(self):
        pattern_type = self.pattern_var.get()
        rows = self.get_number_of_rows()

        if pattern_type == "Pyramid":
            pattern = PatternGenerator.generate_pyramid(rows)
        elif pattern_type == "Square":
            pattern = PatternGenerator.generate_square(rows)
        elif pattern_type == "Alternating":
            pattern = PatternGenerator.generate_alternating(rows)
        else:
            pattern = "Invalid pattern type."

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, pattern)

    def get_number_of_rows(self):
        try:
            rows = int(self.entry_rows.get())
            return rows
        except ValueError:
            return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = PatternGeneratorGUI(root)
    root.mainloop()
