from random import randint

"""A simple random numbers game"""

answer = randint(0, 10)
count = 3

while count:
    guess = input("Guess a number between 0 and 10: ")
    try:
        if int(guess) == answer:
            print("You got it!")
            break
        else:
            if count == 0:
                print("You lose")
            else:
                print("Nope, Try again")
            count -= 1
            print(f"You have {count} guess(s) left.")
    except ValueError:
        print("That's not a number!")


print("Game Finished!")