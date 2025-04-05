
import tkinter as tk
from random import randint

class GuessTheNumberGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guess The Number Game")

        
        self.number_to_guess = randint(1, 100)


        self.num_guesses = 0

        
        tk.Label(self.window, text="Guess a number between 1 and 100:").grid(row=0, column=0)
        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.grid(row=0, column=1)


        self.result_label = tk.Label(self.window, text="")
        self.result_label.grid(row=1, column=0, columnspan=2)


        tk.Button(self.window, text="Guess", command=self.check_guess).grid(row=2, column=0, columnspan=2)

    def check_guess(self):
        try:

            guess = int(self.guess_entry.get())


            self.num_guesses += 1


            if guess < self.number_to_guess:
                self.result_label.config(text="Too small, try again!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too large, try again!")
            else:
                self.result_label.config(text=f"Congratulations! You guessed the number in {self.num_guesses} guesses.")
                self.guess_entry.config(state="disabled")
        except ValueError:
            self.result_label.config(text="Invalid input! Please enter a number.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.run()
