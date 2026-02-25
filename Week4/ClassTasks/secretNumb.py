import random

secretNumber = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")
guess = int(input("Take a guess: "))

while guess != secretNumber:
    if guess < secretNumber:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Take a guess: "))

print("Good job! You guessed my number.")