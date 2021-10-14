import random

def randomGuess(num):
    num = random.randint(1, 100)
    tries = 0
    guess = 0
    while guess != num:
        guess = int(input("\nPlease enter a guess: "))
        tries += 1
        if guess > num:
            print("Lower")
        elif guess < num:
            print("Higher")
        else:
            print("Congratulations. You guessed it!"
                  "\nIt took you", tries, "guesses.")
            
print("Welcome to the number guessing game!")
seedTest = input("Enter random seed: ")
random.seed(seedTest)
num = random.randint(1, 100)
tries = 0
guess = 0
while guess != num:
    guess = int(input("\nPlease enter a guess: "))
    tries += 1
    if guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
    else:
        print("Congratulations. You guessed it!"
              "\nIt took you", tries, "guesses.")
        
        decision = input("\nWould you like to play again (yes/no)? ")
        while decision == "yes":
            if decision == "yes":
                randomGuess(num)
                decision = input("\nWould you like to play again (yes/no)? ")
            else:
                break
        print("Thank you. Goodbye.")