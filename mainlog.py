# HangmanPython

# Imports
import hangstages as hs
import time
import random

# Initialization
with open("D:\\OldFiles\\FullTop\\LeetcodeAttempt\\hangman\\wordBank.txt", "r+") as words:
    wordBank = words.read().split(", ")

conf = hs.config(True)
currRes = round(conf["desiredWidth"]/10)*10
startText = "Welcome to my Python 3.9 Implementation of Hangman"
customSpace = " " * ((currRes-len(startText))//2)
word = random.choice(wordBank) + " " + \
    random.choice(wordBank) + " " + random.choice(wordBank)
charDict = hs.wordDict(word)
guesses = 0
status = "playing"

# Console Start
print("-"*currRes)
print(customSpace+startText)


# Resolution Change Question
resList = hs.spriteRes(currRes)

# Initial Guess
hs.displayCurrStage(resList, True)
hiddenPhrase = hs.guessHandler(word, None, None, True)

while status == "playing":
    print("\n" + hiddenPhrase + "\n")
    guess = input("What letter do you want to guess?: ")

    newPhrase = hs.guessHandler(hiddenPhrase, charDict, guess)

    if newPhrase == "False":
        print("\nSorry that letter is not in the phrase!")
        guesses += 1
        time.sleep(1)
        hs.displayCurrStage(resList)
        if len(resList) == 1:
            status = "loss"
    elif "Error" in newPhrase:
        status = "error"
    else:
        hiddenPhrase = newPhrase
        print(
            f"\nGood Guess, that letter was in the phrase {len(charDict[guess.lower()])} times!")
        guesses += 1
        time.sleep(1)
        hs.displayCurrStage(resList, True)
        if "_" not in hiddenPhrase:
            print("\n" + hiddenPhrase + "\n")
            status = "win"

match status:
    case "win":
        print(f"You guessed the secret word in only {guesses} guesses!\n")
    case "loss":
        print(f"You Ran of Lives! The secret word was {word}!")
    case "error":
        print(newPhrase)
