# Cria jogo da velha para 2 jogadores

from random import randint


def start():
    print('When playing, choose each square according to the example below:')
    tab = [["   |   |   "],
           [" 1 | 2 | 3 "],
           ["   |   |   "],
           ["-----------"],
           ["   |   |   "],
           [" 4 | 5 | 6 "],
           ["   |   |   "],
           ["-----------"],
           ["   |   |   "],
           [" 7 | 8 | 9 "],
           ["   |   |   "]]
    show_board(tab)
    iniciator = randint(0, 1)
    if iniciator == 0:
        print("\nLet's Go. X starts!")
    elif iniciator == 1:
        print("\nLet's go. O starts!")
    return iniciator


def show_board(board):  # shows the current board
    for line in board:
        print(line[0])


def marking(board, square, marker):
    global gameboard, markingboard
    for i in range(3):
        gameboard[1][0] = ' ' + markingboard[0] + ' | ' + markingboard[1] + ' | ' + markingboard[2] + ' '
        gameboard[5][0] = ' ' + markingboard[3] + ' | ' + markingboard[4] + ' | ' + markingboard[5] + ' '
        gameboard[9][0] = ' ' + markingboard[6] + ' | ' + markingboard[7] + ' | ' + markingboard[8] + ' '


def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or  # vitória pelo topo
            (board[3] == mark and board[4] == mark and board[5] == mark) or  # pelo meio
            (board[6] == mark and board[7] == mark and board[8] == mark) or  # por baixo
            (board[0] == mark and board[3] == mark and board[6] == mark) or  # pela esquda
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # pelo meio
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # pela direita
            (board[2] == mark and board[4] == mark and board[6] == mark) or  # diagonal
            (board[0] == mark and board[4] == mark and board[8] == mark))  # diagonal


"""
Starting game
"""
while True:
    player_turn = start()
    gameboard = [["   |   |   "],
                 ["   |   |   "],
                 ["   |   |   "],
                 ["-----------"],
                 ["   |   |   "],
                 ["   |   |   "],
                 ["   |   |   "],
                 ["-----------"],
                 ["   |   |   "],
                 ["   |   |   "],
                 ["   |   |   "]]
    markingboard = []
    for i in range(9):
        markingboard.append(' ')

    for i in range(9):
        if player_turn == 0:
            marker = 'X'
            move = input("X's turn. What's your move? ")
            while True:
                if not move.isnumeric():
                    move = input("Wrong input, X's. Try again. ")
                elif markingboard[int(move)-1] in ['X', 'O']:
                    move = input("This square is already filled, X's. Try again. ")
                else:
                    break
            markingboard[int(move) - 1] = marker
            marking(markingboard, move, marker)
            player_turn += 1
            if win_check(markingboard, marker):
                show_board(gameboard)
                print('X won!')
                break
        elif player_turn == 1:
            marker = 'O'
            move = input("O's turn. What's your move? ")
            while True:
                if not move.isnumeric():
                    move = input("Wrong input, O's. Try again. ")
                elif markingboard[int(move)-1] in ['X', 'O']:
                    move = input("This square is already filled, O's. Try again. ")
                else:
                    break
            markingboard[int(move) - 1] = marker
            marking(gameboard, move, marker)
            player_turn -= 1
            if win_check(markingboard, marker):
                show_board(gameboard)
                print('O won!')
                break
        show_board(gameboard)

    breaking = input("Thanks for playing. Want to play again? 'y' for yes, 'n' for no. ")
    if breaking == "n":
        print('See ya!')
        break