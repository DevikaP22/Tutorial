
import tkinter as tk

class BouncyProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bouncy Program")


        tk.Label(self.window, text="Initial Height:").grid(row=0, column=0)
        self.initial_height_entry = tk.Entry(self.window)
        self.initial_height_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Bounciness Index:").grid(row=1, column=0)
        self.bounciness_index_entry = tk.Entry(self.window)
        self.bounciness_index_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Number of Bounces:").grid(row=2, column=0)
        self.num_bounces_entry = tk.Entry(self.window)
        self.num_bounces_entry.grid(row=2, column=1)


        tk.Button(self.window, text="Calculate Total Distance", command=self.calculate_total_distance).grid(row=3, column=0, columnspan=2)


        self.result_label = tk.Label(self.window, text="")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def calculate_total_distance(self):
        try:
            initial_height = float(self.initial_height_entry.get())
            bounciness_index = float(self.bounciness_index_entry.get())
            num_bounces = int(self.num_bounces_entry.get())

            total_distance = initial_height * (1 + bounciness_index * num_bounces)
            self.result_label.config(text=f"Total Distance: {total_distance:.2f} units")
        except ValueError:
            self.result_label.config(text="Error: Invalid input. Please enter valid numbers.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    program = BouncyProgram()
    program.run()
