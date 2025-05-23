import random 
secret = random.randint(1,5)

try:
    guess= int(input("select a number between 1,5"))
    if guess==secret:
        print(f"you got it right it was {guess} hurray!")
    else:
        print("Try again")
except ValueError:
    ("you have to enter a number")

