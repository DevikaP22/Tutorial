import tkinter as tk

class TemperatureConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Temperature Converter")

        # Create labels and entry fields
        tk.Label(self.window, text="Fahrenheit").grid(row=0, column=0)
        tk.Label(self.window, text="Celsius").grid(row=0, column=1)

        self.fahrenheit_entry = tk.Entry(self.window)
        self.fahrenheit_entry.insert(0, "32")
        self.fahrenheit_entry.grid(row=1, column=0)

        self.celsius_entry = tk.Entry(self.window)
        self.celsius_entry.insert(0, "0.0")
        self.celsius_entry.grid(row=1, column=1)

       
        tk.Button(self.window, text=">>>>", command=self.fahrenheit_to_celsius).grid(row=2, column=0)
        tk.Button(self.window, text="<<<<", command=self.celsius_to_fahrenheit).grid(row=2, column=1)

    def fahrenheit_to_celsius(self):
        try:
            fahrenheit = float(self.fahrenheit_entry.get())
            celsius = (fahrenheit - 32) * 5/9
            self.celsius_entry.delete(0, tk.END)
            self.celsius_entry.insert(0, str(celsius))
        except ValueError:
            self.celsius_entry.delete(0, tk.END)
            self.celsius_entry.insert(0, "Invalid input")

    def celsius_to_fahrenheit(self):
        try:
            celsius = float(self.celsius_entry.get())
            fahrenheit = celsius * 9/5 + 32
            self.fahrenheit_entry.delete(0, tk.END)
            self.fahrenheit_entry.insert(0, str(fahrenheit))
        except ValueError:
            self.fahrenheit_entry.delete(0, tk.END)
            self.fahrenheit_entry.insert(0, "Invalid input")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    converter = TemperatureConverter()
    converter.run()


