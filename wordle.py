import random
import sys


def main():
    # Get a random word.
    answer = getRandomWord()

    # Start by asking the user for their initial guess
    attempts = 0
    guess = ""

    while attempts < 6 and guess != answer:
        guess = input("Enter a 5 letter guess?\n")
        attempts += 1 

        printGuessColors(guess, answer)

        if attempts > 5 and guess != answer:
            print(f"You lost. The answer was {answer}.")
            break
        elif guess == answer:
            print(f"You Won! That took {attempts} guess(es).")
            break


# A helper method that prints the guess with the
# correct colors to the console.
def printGuessColors(guess, answer):
        for index in range(len(guess)):
            result = letterColor(index, guess, answer)
            print(f"{guess[index]} - {result}")
          

# A helper method that determines the color
# of the letter in the guess. 
def letterColor(index, guess, answer):
    if guess[index] in answer:
        if guess[index] == answer[index]:
            return "Green"
        else:
            return "Yellow"
    else:
        return "Red"


# A method that gets a random word from a file.
def getRandomWord():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)

main()
