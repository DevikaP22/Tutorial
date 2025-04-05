
import tkinter as tk

class UpperCaseConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Upper Case Converter")


        tk.Label(self.window, text="Enter text:").grid(row=0, column=0)
        self.input_entry = tk.Entry(self.window)
        self.input_entry.grid(row=0, column=1)


        tk.Label(self.window, text="Upper case text:").grid(row=1, column=0)
        self.output_text = tk.Text(self.window, height=10, width=40)
        self.output_text.grid(row=1, column=1)


        tk.Button(self.window, text="Convert to Upper Case", command=self.convert_to_upper_case).grid(row=2, column=1)

    def convert_to_upper_case(self):
        input_text = self.input_entry.get()
        upper_case_text = input_text.upper()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, upper_case_text)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    converter = UpperCaseConverter()
    converter.run()

