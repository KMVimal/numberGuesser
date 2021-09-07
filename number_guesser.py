import random

topOfRange = input("Type a number: ")

if topOfRange.isdigit():
    topOfRange = int(topOfRange)
    if topOfRange <= 0:
        print("Type a number greater than 0 next time.")
        quit()
else:
    print("Type a number next time.")
    quit()

randomNumber = random.randint(0, topOfRange)
guesses = 0

while True:
    guesses += 1
    userGuess = input("Make a guess:")

    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Type a number next time.")
        continue

    if userGuess == randomNumber:
        print("you got it!")
        break
    elif userGuess > randomNumber:
        print("you were greater than the number")
    else:
        print("you were below the number")

print("You got it in ", guesses, " guesses")
