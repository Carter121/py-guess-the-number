import random

def guess():
    guess = 0
    i = 0
    while guess != randNum:
        print("Whats your guess?")
        guess = int(input())

        i += 1

        if guess == randNum:
            print(f"Thats Correct!\nYou got it in {i} guesses!")
        if guess > randNum:
            print("Lower")
        if guess < randNum:
            print("Higher")

print("What is the max number?")
maxNum = int(input())

randNum = random.randrange(1, maxNum)

guess()