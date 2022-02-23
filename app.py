from math import pow
board = ['']
gridSize = int(input("Select number of rows and columns: "))

def createBoard(gridsize):
    max = int(pow(gridSize, 2))
    iteration = 1
    for i in range(gridSize):
        for i in range(gridSize):
            board.append(str(iteration))
            iteration += 1
            if (iteration <11):
                board.append(' | ')
            else:
                board.append('| ')
        board.pop()
        board.append("\n")
        for i in range(gridSize):
            board.append('- ')
            board.append('+ ')
        board.pop()
        board.append("\n")
    for i in range(gridSize*2):
        board.pop()
    return board

def game(grid, xTurn):
    choice = 0
    xInput = ("x's turn to choose a square (1-" + str(grid) + "): ")
    yInput = ("o's turn to choose a square (1-" + str(grid) + "): ")

    if xTurn == True:
        choice = int(input(xInput))
        xTurn = False
        print(xTurn)
    elif xTurn == False:
        choice = int(input(yInput))
        xTurn = True
        print(xTurn)

    for i in range(len(board)):
        if board[i] == str(choice) and xTurn == False :
            board[i] = "x"
        elif board[i] == str(choice) and xTurn == True :
            board[i] = "o"

    return xTurn

def main():
    xTurn = True
    win = False
    board = createBoard(gridSize)
    print(' '.join(board))
    grid = gridSize * gridSize
    while win == False:
        xTurn = game(grid, xTurn)
        print(' '.join(board))


main()

# create a seperate indexed array that the game logic can be proccessed o
# proccess the game with that array
# return it with Xturn and recieve it in main
# create win/loss message 