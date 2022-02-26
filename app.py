# Tic Tac Toe
# Author: Thomas Vargas
# CSE210 01



from math import pow
import os
board = ['']
a = []
gridSize = int(input("Select number of rows and columns: "))

def createBoard(gridsize):
    max = int(pow(gridSize, 2))
    iteration = 1
    for i in range(gridSize):
        for i in range(gridSize):
            board.append(str(iteration))
            a.append(iteration)
            iteration += 1
            if (iteration <11):
                board.append(' | ')
            else:
                board.append('| ')
        board.pop()
        board.append("\n")
        for i in range(gridSize):
            board.append('--')
            board.append('+-')
        board.pop()
        board.append("\n")
    for i in range(gridSize*2):
        board.pop()
    
    return board

def game(grid, xTurn):
    gameWon = False
    choice = 0
    xInput = ("x's turn to choose a square (1-" + str(grid) + "): ")
    yInput = ("o's turn to choose a square (1-" + str(grid) + "): ")
    brk = ''

    if xTurn == True:
        choice = int(input(xInput))
        xTurn = False
        a[choice-1] = True
    elif xTurn == False:
        choice = int(input(yInput))
        xTurn = True
        a[choice-1] = False

    for i in range(len(board)):
        if board[i] == str(choice) and xTurn == False :
            board[i] = "x"
        elif board[i] == str(choice) and xTurn == True :
            board[i] = "o"
        brk = ''.join([brk, "_"])
    
    x = gridSize
    for i in range(grid):
        t = a[i]
        try:
            z = (t == a[(i-x-1)] == a[(i+x+1)])
            b = (t == a[(i-x)] == a[i+x])
            c= (t == a[(i-x+1)] == a[(i+x-1)])
            d = (t == a[(i-1)] == a[(i+1)])
        
        except:
            pass

        else:
            if(z or b or c or d):
                gameWon = True
            else:
                continue

    print(''.join([brk, "_____\n"]))
        
    return xTurn, gameWon

def main():
    xTurn = True
    win = False
    board = createBoard(gridSize)
    print("\n")
    print(' '.join(board))
    grid = gridSize * gridSize
    while win == False:
        xTurn, win = game(grid, xTurn) #game handler
        print(' '.join(board)) #display handler
    
    print("Game over!")
    if xTurn:
        print("O wins\n")
    else:
        print("X WINS\n")



main()

# create a seperate indexed array that the game logic can be proccessed o
# proccess the game with that array
# return it with Xturn and recieve it in main
# create win/loss message 