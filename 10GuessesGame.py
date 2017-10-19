from random import randint

print("This is the Guessing Game! You have 10 guesses, choose wisely (and randomly)!")

def secret_number():
    secret_number = randint(0,101)
    guesses = 0
    while guesses < 11:
        guess = int(raw_input("Guess a number from 1 - 100:  "))
        while guess != secret_number:
            guesses += 1
            if guess < secret_number:
                print("Your guess was too low, try again.")
            else:
                print("Your guess was too high, try again.")           
        else:
            print("You guessed correctly! Congratulations!")
    print("Sorry, you ran out of guesses.")

secret_number()
