
import tkinter as tk
from random import randint

class GuessTheNumberGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guess The Number Game")

      
        self.number_to_guess = randint(1, 100)


        self.computer_guess = randint(1, 100)

        
        self.guess_label = tk.Label(self.window, text=f"Computer's guess: {self.computer_guess}")
        self.guess_label.grid(row=0, column=0, columnspan=3)


        tk.Button(self.window, text="Too small", command=self.too_small).grid(row=1, column=0)
        tk.Button(self.window, text="Too large", command=self.too_large).grid(row=1, column=1)
        tk.Button(self.window, text="Correct", command=self.correct).grid(row=1, column=2)


        tk.Button(self.window, text="New game", command=self.new_game).grid(row=2, column=0, columnspan=3)

    def too_small(self):
        
        self.computer_guess = randint(self.computer_guess + 1, 100)
        self.guess_label.config(text=f"Computer's guess: {self.computer_guess}")

    def too_large(self):
        
        self.computer_guess = randint(1, self.computer_guess - 1)
        self.guess_label.config(text=f"Computer's guess: {self.computer_guess}")

    def correct(self):
        
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Button) and widget['text'] != "New game":
                widget.config(state="disabled")
        self.guess_label.config(text=f"Computer guessed it! The number was {self.number_to_guess}.")

    def new_game(self):
        
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Button) and widget['text'] != "New game":
                widget.config(state="normal")

        self.number_to_guess = randint(1, 100)
        self.computer_guess = randint(1, 100)
        self.guess_label.config(text=f"Computer's guess: {self.computer_guess}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.run()
