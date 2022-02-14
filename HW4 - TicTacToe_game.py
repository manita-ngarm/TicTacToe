#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
def new_board():
    print("Here is a board game with the (x,y) position")
    return(np.array([['(0,0)','(0,1)','(0,2)'],
                     ['(1,0)','(1,1)','(1,2)'],
                     ['(2,0)','(2,1)','(2,2)']]))

def update_board(board,s):
    x = int(s[0])
    y = int(s[1])
    board[x,y] = s[2]
    return(board)

    #8 ways to win    
def check_winner(board):
    for i in range(2):
        if (board[i,0] == board[i,1]) and (board[i,1] == board[i,2]) and (board[i,0] == board[i,2]):
            return True           
    for i in range(2):
        if (board[0,i] == board[1,i]) and (board[1,i] == board[2,i]) and (board[0,i] == board[2,i]):
            return True
    if (board[0,0] == board[1,1]) and (board[1,1] == board[2,2]) and (board[0,0] == board[2,2]):
        return True
    if (board[0,2] == board[1,1]) and (board[1,1] == board[2,0]) and (board[0,2] == board[2,0]):
        return True
    else: return False
    
    
def game():
    print("Welcome to Tic Tac Toe game\nIn this game, we will have 2 symbols which are only 'x' and 'o'")
    board = new_board()
    print(board)
    count = 0
    winner = ""
    
    while winner =="":
        for player in [1,2]:
            print("\nPlayer: %s"%(player))
            s = list(input("It's your turn, please give your next x,y position and your symbol(x/o) e.g. 01x, 22o\n"))
            #check wrong symbol
            if (count >= 2):
                if ((player == 2) and (s[2] != sym2)) or ((player == 1) and (s[2] != sym1)):
                    print("Wrong symbol!!!")
                    s = list(input("It's your turn, please give your next x,y position and your symbol(x/o) e.g. 01x, 22o\n"))              
            if (s[2] != 'x') and (s[2] != 'o'):
                print("Wrong symbol!!!")
                s = list(input("It's your turn, please give your next x,y position and your symbol(x/o) e.g. 01x, 22o\n"))
            board = update_board(board,s)
            count += 1
            print(board)
            #lock symbol with player
            if(count == 1):
                sym1 = s[2]
            if(count == 2):
                sym2 = s[2]
            if(count == 9):
                return ("Sorry! no one is the winner")
            if(count > 4):
                if check_winner(board) == True:
                    return "Congratulation, player number %s with symbol %s is the winner!!!"%(player,s[2])
print(game())

