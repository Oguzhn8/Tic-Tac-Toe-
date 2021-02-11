# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:07:43 2021

@author: pc
"""

game_board = [["___", "___", "___"],    #In order to make changes to it later, 
              ["___", "___", "___"],    #we need to define our game board in list data type.                     
              ["___", "___", "___"]]
                                     

print("\n*"*10)
for i in game_board:
    print("\t".expandtabs(20), *i, end="\n"*2 ) #we indented list items from the top left.

win_criteria = [[[0, 0], [1, 0], [2, 0]],
               [[0, 1], [1, 1], [2, 1]],
               [[0, 2], [1, 2], [2, 2]],
               [[0, 0], [0, 1], [0, 2]],
               [[1, 0], [1, 1], [1, 2]],
               [[2, 0], [2, 1], [2, 2]],
               [[0, 0], [1, 1], [2, 2]],
               [[0, 2], [1, 1], [2, 0]]] #The first number in each list indicates the vertical plane,
                                         #the second number the horizontal plane.
x_situation = []
o_situation = []

move = 1
while True:                             #We created a sequence system using even and odd numbers.
    if move % 2 == 0:
        mark = "X".center(3)
    else:
        mark = "O".center(3)
    move =+ 1
    print()
    print("MARK: {}\n".format(mark))
    x = input("Enter the location where you want to put your mark from left to right"
              +"for exit please press q".ljust(20))
    if x == "q":
        break
    
    y = input("Enter the location where you want to put your mark from up to down"+
              "please press q for exit game".ljust(20))
    if y == "q":
        break
    x = int(x)-1
    y = int(y)-1
    
    print("\n"*15)
    if game_board[x][y] == "___":    #control fulll or empty
        game_board[x][y] = mark
        if mark == "X".center(3):    #if region empty and move right to X we direct to X
            x_situation += [[x,y]]
        elif mark == "O".center(3):  #if region empty and move right to O we direct to O
            o_situation += [[x,y]]
            move += 1
        else:
            print("\n There is full,please try again\n")
    
for i in win_criteria:
    o = [z for z in i if z in o_situation] #By comparing win_criteria and O/X_situation
    x = [z for z in i if z in x_situation] #if the number of common items reached three
    if len(o) == len(i):                   # the game is won  
        print("O WINNING!")
        quit()
    if len(x) == len(i):
        print("X WINNING!")
        quit()
    
    




    
    
    
    
    