"""

Code for a Number Guessing Game that Utilizes the Python Programming Language.

"""

import random
import os
import time
import tkinter as tk
from tkinter import messagebox
bg="#4f91f3"

class NGG:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("350x250")

        self.max_attempts = 5
        self.attempts = 0
        self.number_to_guess = random.randint(1, 10)

        self.label = tk.Label(root, text="Guess a number between 1 and 10")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.status = tk.Label(root, text=f"Attempts left: {self.max_attempts}")
        self.status.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")
            return

        self.attempts += 1
        remaining = self.max_attempts - self.attempts
        self.status.config(text=f"Attempts left: {remaining}")

        if guess == self.number_to_guess:
            messagebox.showinfo(
                "Congratulations",
                f"You guessed the number {self.number_to_guess} in {self.attempts} attempts."
            )
            self.root.destroy()
            return
        else:
            messagebox.showwarning("Wrong", "Wrong guess!")

        if self.attempts >= self.max_attempts:
            messagebox.showerror("Game Over", f"You lost! The number was {self.number_to_guess}.\nThe game will close in 5 seconds.")
            self.root.after(5000, self.root.destroy)
            messagebox.showwarning("Lost", "You Lost Buddy!!")

            #To Delete Files Use Next Lines          
            #os.remove("Here_Paste_Your_Path")

root = tk.Tk()
game = NGG(root)

root.mainloop()
