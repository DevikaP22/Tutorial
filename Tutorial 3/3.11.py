
import tkinter as tk

class QuadrantFinder:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quadrant Finder")

        
        tk.Label(self.window, text="X Coordinate:").grid(row=0, column=0)
        self.x_entry = tk.Entry(self.window)
        self.x_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Y Coordinate:").grid(row=1, column=0)
        self.y_entry = tk.Entry(self.window)
        self.y_entry.grid(row=1, column=1)

        
        tk.Button(self.window, text="Find Quadrant", command=self.find_quadrant).grid(row=2, column=0, columnspan=2)

        
        self.result_label = tk.Label(self.window, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def find_quadrant(self):
        try:
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())

            if x > 0 and y > 0:
                self.result_label.config(text="Point is in Quadrant I")
            elif x < 0 and y > 0:
                self.result_label.config(text="Point is in Quadrant II")
            elif x < 0 and y < 0:
                self.result_label.config(text="Point is in Quadrant III")
            elif x > 0 and y < 0:
                self.result_label.config(text="Point is in Quadrant IV")
            else:
                self.result_label.config(text="Point is on an axis")
        except ValueError:
            self.result_label.config(text="Error: Invalid input. Please enter valid numbers.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    finder = Quadr
