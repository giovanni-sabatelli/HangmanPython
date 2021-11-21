#Hangman Attempt

#Imports
# sourcery skip: for-index-underscore
import hangstages as hs
import time

#Initialization
conf = hs.config(True); currRes = round(conf["desiredWidth"]/10)*10
startText = "Welcome to my Python 3.9 Implementation of Hangman"
customSpace = " " * ((currRes-+len(startText))//2)
word = "UNITED ARAB EMIRATES"; charDict = hs.wordDict(word)
guesses = 0

#Console Start
print("-"*currRes); print(customSpace+startText)

#Resolution Change Question
resList = hs.spriteRes(currRes)

#Initial Guess
hs.displayCurrStage(resList, True)
hiddenPhrase = hs.guessHandler(word, None, None, True)

while "_" in hiddenPhrase:
    print("\n" + hiddenPhrase + "\n")
    guess = input("What letter do you want to guess?: ")
    newPhrase = hs.guessHandler(hiddenPhrase, charDict, guess)

    if newPhrase == False:
        print("\nSorry that letter isn't in the phrase!")
        guesses += 1
        time.sleep(1)
        hs.displayCurrStage(resList)
    else:
        hiddenPhrase = newPhrase
        print(f"\nGood Guess, that letter was in the phrase {len(charDict[guess.lower()])} times!")
        guesses += 1
        time.sleep(1)
        hs.displayCurrStage(resList, True)
        if "_" not in hiddenPhrase:
            print("\n" + hiddenPhrase + "\n")
        
print(f"You guessed the secret word in only {guesses} guesses!\n")

