import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    guess_count = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        guess_count +=1
        if guess < random_number:
            print("Sorry guess again. Too low")
        elif guess > random_number:
            print("Sorry guess again. Too high")
                        
    print(f"Congrats you have guessed the number {random_number} in {guess_count} gusses")
guess(20)