import random

player_one_number = random.randint(1,10)

player_two_guess = int(input("Guess player one's number: "))

guess = 1

while player_two_guess != player_one_number:
    if player_two_guess < player_one_number:
        print("You're low!")
        player_two_guess = int(input("Try again: "))
        guess = guess + 1
    elif player_two_guess > player_one_number:
        print("Youre high!")
        player_two_guess = int(input("Try again: "))


print("You are correct. It only took you", guess,"guesses. See ya nerd.")
        