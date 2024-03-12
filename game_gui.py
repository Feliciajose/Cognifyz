import tkinter as tk
from tkinter import messagebox
from game_logic import GuessingGame

class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        
        self.game = GuessingGame()
        
        self.label = tk.Label(master, text="Guess a number between 1 and 20:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack()

    def submit_guess(self):
        try:
            guess = int(self.entry.get())
            result = self.game.check_guess(guess)
            
            if result == "Congratulations! You've guessed the number!":
                messagebox.showinfo("Congratulations!", result)
                self.master.quit()
            elif self.game.is_game_over():
                messagebox.showinfo("Game Over!", f"The number was {self.game.get_secret_number()}")
                self.master.quit()
            else:
                messagebox.showinfo("Result", result)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()
