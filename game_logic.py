import random

class GuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 20)
        self.attempts = 0
        self.max_attempts = 5

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            return "Congratulations! You've guessed the number!"

    def is_game_over(self):
        return self.attempts == self.max_attempts

    def get_secret_number(self):
        return self.secret_number
