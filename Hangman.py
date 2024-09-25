import random

with open("quotes.txt", "r") as file:
    lines = file.readlines()
    randLine = random.choice(lines)
    randLine = randLine[:-1]
    randLine = randLine.lower()

print("How many lives do you want?")
validInput = False
while(not validInput):
    userInput = input("Easy - 9, Normal - 6, Hard - 3 \n")
    lives = int(userInput)
    if(lives in [3, 6, 9]):
        validInput = True

blanks = ""
print("Hangman Game")
print("Guess the quote")
for  i in randLine:
    if(i == " "):
        blanks += " "
    elif(not i.isalpha()):
        blanks += i
    else:
        blanks += "_"
gameLoop = True

while(gameLoop):
    print()
    print("Lives: " + str(lives))
    print(blanks)
    print()

    validate = False
    while(not validate):
        userInput = input("Enter a letter: \n")
        if(userInput.isalpha() and len(userInput) == 1):
            validate = True

    indices = [i for i, c in enumerate(randLine) if c == userInput]
    if(len(indices) == 0):
        lives = lives - 1
    else:
        for i in indices:
            blanks = blanks[:i] + userInput + blanks[i + 1:]
    if(lives == 0):
        print("Sorry, you lost")
        print(randLine)
        gameLoop = False
    if(blanks.find("_") == -1):
        print("You win")
        print(randLine)
        gameLoop = False
    
