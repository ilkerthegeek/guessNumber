import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guees a number between 1 and {x}"))
        if guess < random_number:
            print("It is too small , guess again!")
        elif guess > random_number:
            print("It is too high, guess again!")

    print(f"Congratulations!! you guessed correct number as {random_number} and you win the game!!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low
        feedback = input(f'Is {guess} , Too High (H), Too low (L) or correct (C)').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yay, The computer guessed your number {guess} correctly ")


computer_guess(100)