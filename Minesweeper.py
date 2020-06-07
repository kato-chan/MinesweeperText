import random

game = 1
height = 8
width = 8
bombs = 10


def startScreen(h, w):
    board = [["x" for x in range(w)] for x in range(h)]
    return board


def buildBoard(width, height, bombs):
    fieldList = []

    for x in range(bombs):
        fieldList.append("*")
    for x in range(height * width - bombs):
        fieldList.append("#")
    random.shuffle(fieldList)

    endList = [[fieldList[y * width + x] for x in range(width)] for y in range(height)]

    for x in range(height):
        for y in range(width):
            if endList[x][y] != "*":
                bomb_count = 0
                if x == 0:
                    if y == 0:
                        for i in range(x, x + 2):
                            for j in range(y, y + 2):
                                if endList[i][j] == "*":
                                    bomb_count += 1
                    elif y == width - 1:
                        for i in range(x, x + 2):
                            for j in range(y - 1, y + 1):
                                if endList[i][j] == "*":
                                    bomb_count += 1
                    else:
                        for i in range(x, x + 2):
                            for j in range(y - 1, y + 2):
                                if endList[i][j] == "*":
                                    bomb_count += 1
                elif x == height - 1:
                    if y == 0:
                        for i in range(x - 1, x + 1):
                            for j in range(y, y + 2):
                                if endList[i][j] == "*":
                                    bomb_count += 1
                    elif y == width - 1:
                        for i in range(x - 1, x + 1):
                            for j in range(y - 1, y + 1):
                                if endList[i][j] == "*":
                                    bomb_count += 1
                    else:
                        for i in range(x - 1, x + 1):
                            for j in range(y - 1, y + 2):
                                if endList[i][j] == "*":
                                    bomb_count += 1
                elif y == 0:
                    for i in range(x - 1, x + 2):
                        for j in range(y, y + 2):
                            if endList[i][j] == "*":
                                bomb_count += 1
                elif y == width - 1:
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 1):
                            if endList[i][j] == "*":
                                bomb_count += 1
                else:
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            if endList[i][j] == "*":
                                bomb_count += 1
                endList[x][y] = bomb_count
    return endList


def uncover (initialBoard, endList, i, j, width, height):
    if i > 0 and j > 0:
        if str(endList[i - 1][j - 1]) == "0" and str(initialBoard[i - 1][j - 1]) == "x":
            initialBoard[i - 1][j - 1] = endList[i - 1][j - 1]
            a = i -1;
            b = j - 1;
            uncover(initialBoard, endList, a, b, width, height)
        else:
            initialBoard[i - 1][j - 1] = endList[i - 1][j - 1]
    if i > 0:
        if str(endList[i - 1][j]) == "0" and str(initialBoard[i - 1][j]) == "x":
            initialBoard[i - 1][j] = endList[i - 1][j]
            c = i -1
            uncover(initialBoard, endList, c, j, width, height)
        else:
            initialBoard[i - 1][j] = endList[i - 1][j]
    if i > 0 and j < width - 1:
        if str(endList[i - 1][j + 1]) == "0" and str(initialBoard[i - 1][j + 1]) == "x":
            initialBoard[i - 1][j + 1] = endList[i - 1][j + 1]
            d = i - 1
            e = j + 1
            uncover(initialBoard, endList, d, e, width, height)
        else:
            initialBoard[i - 1][j + 1] = endList[i - 1][j + 1]
    if j > 0:
        if str(endList[i][j - 1]) == "0" and str(initialBoard[i][j - 1]) == "x":
            initialBoard[i][j - 1] = endList[i][j - 1]
            f = j - 1
            uncover(initialBoard, endList, i, f, width, height)
        else:
            initialBoard[i][j - 1] = endList[i][j - 1]
    if j > 0 and i < height -1:
        if str(endList[i + 1][j - 1]) == "0" and str(initialBoard[i + 1][j - 1]) == "x":
            initialBoard[i + 1][j - 1] = endList[i + 1][j - 1]
            g = i + 1
            h = j - 1
            uncover(initialBoard, endList, g, h, width, height)
        else:
            initialBoard[i + 1][j - 1] = endList[i + 1][j - 1]
    if j < width - 1:
        if str(endList[i][j + 1]) == "0" and str(initialBoard[i][j + 1]) == "x":
            initialBoard[i][j + 1] = endList[i][j + 1]
            k = j + 1
            uncover(initialBoard, endList, i, k, width, height)
        else:
            initialBoard[i][j + 1] = endList[i][j + 1]
    if i < height - 1:
        if str(endList[i + 1][j]) == "0" and str(initialBoard[i + 1][j]) == "x":
            initialBoard[i + 1][j] = endList[i + 1][j]
            l = i + 1
            uncover(initialBoard, endList, l, j, width, height)
        else:
            initialBoard[i + 1][j] = endList[i + 1][j]
    if i < height - 1 and j < width - 1:
        if str(endList[i + 1][j + 1]) == "0" and str(initialBoard[i + 1][j + 1]) == "x":
            initialBoard[i + 1][j + 1] = endList[i + 1][j + 1]
            m = i + 1
            n = j + 1
            uncover(initialBoard, endList, m, n, width, height)
        else:
            initialBoard[i + 1][j + 1] = endList[i + 1][j + 1]


print("Welcome to Minesweeper!\n")

while game == 1:
    initialBoard = startScreen(height, width)
    endList = buildBoard(width, height, bombs)

    for x in initialBoard:
        for y in x:
            print(y, end="  ")
        print()
    print("\n")

    while initialBoard != endList:
        while True:
            try:
                userX = input("Write row #: ")
                assert int(userX) <= height
                break
            except (AssertionError, ValueError) as e:
                print("Please write a number no greater than " + str(height))
        while True:
            try:
                userY = input("Write column #: ")
                assert int(userY) <= width
                break
            except (AssertionError, ValueError) as e:
                print("Please write a number no greater than " + str(width) + " :")
        while True:
            try:
                isBomb = input("Is it a bomb (Y/N)?: ")
                assert (isBomb == "Y" or isBomb == "N")
                break
            except AssertionError:
                print("Please write Y or N")

        userX = int(userX)
        userY = int(userY)
        maxH = height
        minH = -1

        if isBomb == "N":
            if str(endList[userX - 1][userY - 1]) == "*":
                break
            elif str(endList[userX - 1][userY - 1]) == "0":
                initialBoard[userX - 1][userY - 1] = endList[userX - 1][userY - 1]
                uncover(initialBoard, endList, userX - 1, userY - 1, width, height)
            else:
                initialBoard[userX - 1][userY - 1] = endList[userX - 1][userY - 1]
        else:
            initialBoard[userX - 1][userY - 1] = "*"

        print("\n")
        for x in initialBoard:
            for y in x:
                print(y, end="   ")
            print()
        print("\n")

    if initialBoard == endList:
        print("Congratulation, you won!\n")
    else:
        print("\n")
        print("You lost!\n")
        for x in endList:
            for y in x:
                print(y, end="   ")
            print()
        print("\n")

    repeat = True
    while repeat:
        gameState = input("Do you want to start new game? Y/N ")
        if gameState == "N" or gameState == "Y":
            print("\n")
            repeat = False
        else:
            print("Please write Y or N\n")

    if gameState == "Y":
        game = 1
    else:
        game = 0

print ("Thank you for playing!")



