import random

number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
GameRunning = True

while GameRunning:
    guess = int(raw_input("Guess a number between 1-100: "))

    if guess == number:
        GameRunning = False
        print("You guessed correctly!")
        
    elif guess > number:
        GameRunning = True
        print("Your guess was too high!")
        
    elif guess < number:
        GameRunning = True
        print("Your guess was too low!")

# Need to change so that another random number is picked, while the user
# is still in the loop after guessing correctly.
