from random import randint  # Do not delete this line


def displayIntro():
    fileName = "hangman-ascii.txt"
    file = open(fileName, "r")
    n = 0
    for x in file:
        if n == 24:
            break
        print(x, end="")
        n += 1

    file.close()


def displayEnd(result):
    fileName = "hangman-ascii.txt"
    file = open(fileName, "r")
    lines = file.readlines()
    win = 190
    lose = 99
    if result:
        while win != 203:
            print(lines[win], end="")
            win += 1
    else:
        while lose != 111:
            print(lines[lose], end="")
            lose += 1

    file.close()


def displayHangman(state):
    fileName = "hangman-ascii.txt"
    file = open(fileName, "r")
    lines = file.readlines()
    if state == 5:
        for x in range(24, 32):
            print(lines[x], end="")
    elif state == 4:
        for x in range(37, 45):
            print(lines[x], end="")
    elif state == 3:
        for x in range(50, 58):
            print(lines[x], end="")
    elif state == 2:
        for x in range(63, 71):
            print(lines[x], end="")
    elif state == 1:
        for x in range(76, 84):
            print(lines[x], end="")
    elif state == 0:
        for x in range(89, 97):
            print(lines[x], end="")

    file.close()


def getWord():
    fileName = "hangman-words.txt"
    file = open(fileName, "r")
    lines = file.readlines()
    counter = 0
    while counter < len(lines):
        lines[counter] = lines[counter].strip("\n")
        counter += 1
    word = lines[randint(0, len(lines))]
    file.close()
    return word


def valid(c):
    c = str(c)
    return c.isalpha() and c.islower() and len(c) == 1


def play():
    word = getWord()
    lives = 5
    currWord = ""
    result = False

    for x in range(len(word)):
        currWord += "_"

    while lives != 0:
        letterIsNot = True
        displayHangman(lives)
        print("Guess the word:", currWord)
        print("Enter the letter: ")
        letter = input()
        if valid(letter):
            currWordList = list(currWord)
            n = 0
            for x in word:
                if x == letter:
                    currWordList[n] = letter
                    letterIsNot = False
                n += 1
            if letterIsNot:
                lives = lives - 1
            else:
                currWord = ""
                for x in currWordList:
                    currWord += x
                if currWord == word:
                    print("Hidden word was:", word)
                    result = True
                    break

    if lives == 0:
        displayHangman(lives)
        print("Hidden word was:", word)

    return result


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        print("Do you want to play again? (yes/no)")
        playAgain = input()
        if playAgain == "no":
            break


if __name__ == "__main__":
    hangman()
