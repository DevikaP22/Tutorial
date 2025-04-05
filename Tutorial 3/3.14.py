
import tkinter as tk
from math import sqrt

class SquareRootCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Square Root Calculator")

      
        tk.Label(self.window, text="Enter a number:").grid(row=0, column=0)
        self.input_entry = tk.Entry(self.window)
        self.input_entry.grid(row=0, column=1)


        tk.Label(self.window, text="Square root:").grid(row=1, column=0)
        self.output_text = tk.Text(self.window, height=1, width=20)
        self.output_text.grid(row=1, column=1)


        tk.Button(self.window, text="Calculate", command=self.calculate_square_root).grid(row=2, column=1)

    def calculate_square_root(self):
        try:
            input_number = float(self.input_entry.get())
            if input_number < 0:
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, "Error: Square root of negative number is not a real number.")
            else:
                square_root = sqrt(input_number)
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, str(square_root))
        except ValueError:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Error: Invalid input. Please enter a number.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = SquareRootCalculator()
    calculator.run()
