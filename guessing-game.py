import random

player_one_number = random.randint(1,10)

player_two_guess = int(input("Guess player one's number!"))

while player_two_guess != player_one_number:
    if player_two_guess < player_one_number:
        print("You're low!")
        player_two_guess = int(input("Wrong, try again:"))
    elif player_two_guess > player_one_number:
        print("Youre high!")
        player_two_guess = int(input("Wrong, try again:"))
    else:
        player_two_guess = player_one_number:
        print("You are correct. See ya nerd.")
        