#Creating a very simple 'guess the number' app

#Imports
import random
import os


def GuessTheNumber():
    number = random.choice(range(0,100))

    os.system("cls")
    print("The app has chosen a random number from 0 to 100, guess what the number is.")
    guess = int(input("Guess:"))

    while guess != number:
        os.system("cls")
        print("\nThats not the number")
        print("You are {} away from the number.".format(abs(number-guess)))
        guess = int(input("Guess:"))

    if guess == number:
        print("\nThats right. The number was {}!".format(number))

if __name__ == "__main__":
    GuessTheNumber()