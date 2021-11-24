def enterX():
    # Will enter "O" where player O chooses so, if the place is already marked, will return False
    global cpuX
    global counter
    global row
    global line
    if database[row][line] == "_":
        counter = counter + 1
        database[row][line] = "X"
        return True
    if not cpuX:
        print("This has already been marked, please select a new tile")
    return False

def enterO():
    # Will enter "O" where player O chooses so, if the place is already marked, will return False
    global cpuO
    global counter
    global row
    global line
    if database[row][line] == "_":
        counter = counter + 1
        database[row][line] = "O"
        return True
    if not cpuO:
        print("This has already been marked, please select a new tile")
    return False

def check_winner():
    # Checks if there is a winner
    test_line = True
    test_row = True
    test_diagonal = True
    for i in range(len(database)):
        if database[i][line] != database[row][line]:
            test_line = False
        if database[row][i] != database[row][line]:
            test_row = False
        if database[i][i] != database[row][line]:
            test_diagonal = False
    if test_row or test_line or test_diagonal:
        return True
    return False


def testInput():
    # Will check the player's input and return the input only when valid
    number = input()
    if re.match(pattern, number):
        return int(number)
    print("Please enter a valid input ")
    return testInput()


def boardstatus():
    # Prints the current board status for the players after every play
    for i in range(len(database)):
        print("\n")
        for x in range(len(database)):
            print(database[i][x], end='')
    print("\n")


def game():
    # The game itself, will call all relevant functions.
    global row
    global line
    global counter
    while counter != 9:
        while True:
            if cpuX:
                row = random.randint(0, len(database) - 1)
                line = random.randint(0, len(database) - 1)
            else:
                print("Player X, please enter row number ")
                row = testInput()
                print("Player X, please enter line number ")
                line = testInput()
            if enterX():
                break
        boardstatus()
        if check_winner():
            print("The winner is player X")
            break
        if counter == 9:
            break
        while True:
            if cpuO:
                row = random.randint(0, len(database) - 1)
                line = random.randint(0, len(database) - 1)
            else:
                print("Player O, please enter row number ")
                row = testInput()
                print("Player O, please enter line number ")
                line = testInput()
            if enterO():
                break
        boardstatus()
        if check_winner():
            print("The winner is player O")
            break
    if not check_winner():
        print("There is no winner")


import re
import random
cpuX = False
cpuO = False
if input("To play on 4X4 board please type 'Y' ") == "Y":
    pattern = "[0-3]"
    database = [["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"]]
    counter = -7
else:
    database = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    pattern = "[0-2]"
    counter = 1
if input("To have the cpu play player X please type 'Y' ") == "Y":
    cpuX = True
if input("To have the cpu play player O please type 'Y' ") == "Y":
    cpuO = True
row = 0
line = 0
game()
