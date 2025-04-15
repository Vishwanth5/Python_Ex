import random
random_number = random.randint(1,10)
while True:
    guess = input("pick a number from 1 to 10")
    guess =int(guess)
    if guess <random_number:
        print("Too low")
    elif guess >random_number:
        print("Too high")
    else:
        print("You Won")
        play_again = input("you want to play again (Y/N)")
        if play_again == "Y":
            random_number = random.randint(1,10)
            guess=None
        else:
            print("Thank You for playing")
            break
