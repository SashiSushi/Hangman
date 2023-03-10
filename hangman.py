import turtle


def main():
    # function that defines whether the letter chosen by the user is not present in the guessing word (wordList)
    def checkLetters():
        track = 0
        for i in range(len(wordList)):
            if user != wordList[i]:
                track += 1
            else:
                track += 0

        if track == len(wordList):
            # this means that the letter chosen by the user (user) is not present within the wordList
            return True
        else:
            return False

    # function that determines whether a letter has been already used or not
    def letterTaken():
        for i in wrongLetter:
            if user == i:
                return True
        return False

    # function that determines whether a letter has been guessed or not
    def letterGuessed():
        for i in emptyList:
            if user == i:
                return True
        return False

    # start
    attempts = 0
    print("Please choose a word to guess")
    word = input(": ")
    word = word.lower()
    drawChoice = input("Do you want to draw the hangman?: ")
    drawChoice = drawChoice.lower()

    if drawChoice == "yes":
        hangman = True
        attempts = 9
        # start turtle
        rocky = turtle.Turtle()
        rocky.speed(0)

    if drawChoice == "no":
        hangman = False
        attempts = int(input("How many attempts would you like to have?: "))

    # convert the string into two lists
    wordList = list(word)
    emptyList = list(word)

    # "w" -> "_"
    for i in range(len(emptyList)):
        if emptyList[i] == " ":
            emptyList[i] = " "
        else:
            emptyList[i] = "_"

    # create the UI
    UI = ""
    for i in range(len(emptyList)):
        UI += " " + emptyList[i]

    wrongLetter = ""
    turtleTracker = 0

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSTART")
    print(UI)
    while attempts > 0:
        user = input("choose a letter: ")
        user = user.lower()

        if checkLetters():
            if letterTaken():
                print("Letter is already taken, chose another one.")
            else:
                attempts -= 1
                turtleTracker += 1
                wrongLetter += user + ", "
                print("\nWrong!")
                print(UI)
                print(" Wrong letters: " + wrongLetter)
                print("Attempts remaining: " + str(attempts))

                # TURTLE:
                if hangman:
                    # base
                    if turtleTracker == 1:
                        rocky.left(180)
                        rocky.forward(100)

                    if turtleTracker == 2:
                        rocky.right(90)
                        rocky.forward(200)

                    if turtleTracker == 3:
                        rocky.right(90)
                        rocky.forward(60)

                    # head
                    if turtleTracker == 4:
                        rocky.right(90)
                        rocky.forward(40)

                        rocky.right(90)
                        n = 80
                        for i in range(n):
                            rocky.left(360 / n)
                            rocky.forward(1.5)

                        for i in range(int(n / 2)):
                            rocky.left(360 / n)
                            rocky.forward(1.5)

                    # body
                    if turtleTracker == 5:
                        rocky.right(90)
                        rocky.forward(65)
                    # left arm
                    if turtleTracker == 6:
                        # go back
                        rocky.back(42)

                        rocky.right(45)
                        rocky.forward(35)

                    if turtleTracker == 7:
                        # go back
                        rocky.right(180)
                        rocky.forward(35)

                        # right arm
                        rocky.right(90)
                        rocky.forward(35)

                    if turtleTracker == 8:
                        # go back
                        rocky.back(35)

                        # lower body
                        rocky.right(45)
                        rocky.forward(50)

                        # left leg
                        rocky.right(45)
                        rocky.forward(45)

                    if turtleTracker == 9:
                        # go back
                        rocky.right(180)
                        rocky.forward(45)

                        # right leg
                        rocky.right(90)
                        rocky.forward(45)

                    print()
                else:
                    print()

        if letterGuessed():
            print("Letter already guessed.")
        else:
            for i in range(len(wordList)):
                if user == wordList[i]:
                    emptyList[i] = user
                    UI = ""
                    for j in range(len(emptyList)):
                        UI += " " + emptyList[j]
        if not checkLetters():
            print(UI)

        # check if the game is finished
        tracker = 0
        for i in range(len(wordList)):
            if emptyList[i] == wordList[i]:
                tracker += 1
            else:
                tracker += 0

        if tracker == len(wordList):
            print("")
            print("You guessed the word!")
            exit()

    print("You don't have any more attempts! \n The word was: " + word)


main()
turtle.done()
