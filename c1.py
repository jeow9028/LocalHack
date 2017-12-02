
# coding: utf-8

# In[64]:

import numpy as np
import string
import math


class Pieces(object):
    
    kind =""
    color =""
    life = 1
    
    def __init__(self, kind, color, life):
        
        self.kind = kind
        self.color =color
        self.life = life
    
        def life(kind):   
            if(kind =="king"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Enemy King is dead, check Mate!")
            
            elif(kind =="queen"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Enemy Queen is dead")
            
            elif(kind== "bishop"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Enemy Bishop is dead")
            
            elif(kind== "rook"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Enemy Rook is dead")  
            
            elif(kind =="knight"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Enemy Bishop is dead")
            
            elif(kind == "pawn"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Your Pawn is dead")

if __name__ == '__main__':
                    
    king1 = Pieces('king','white',1)
    king2 = Pieces('king','black',1)

    queen1 = Pieces('king','white',1)
    queen2 = Pieces('king','black',1)

    bishop1 = Pieces('bishop','white',1)
    bishop2 = Pieces('bishop','white',1)
    bishop3 = Pieces('bishop','black',1)
    bishop4 = Pieces('bishop','black',1)

    rook1 = Pieces('rook','white',1)
    rook2 = Pieces('rook','white',1)
    rook3 = Pieces('rook','black',1)
    rook4 = Pieces('rook','black',1)

    knight1 = Pieces('knight', 'white',1)
    knight2 = Pieces('knight', 'white',1)
    knight3 = Pieces('knight','black',1)
    knight4 = Pieces('knight', 'black',1)

        
    pawn_white = []
    pawn_black = []
    for i in range(0,8): 
        pawn_white.append(Pieces('pawn', 'white',1))
        pawn_black.append(Pieces('pawn', 'black',1))
    
    def createboard():
        alphabet = list(string.ascii_lowercase)
        chessboard = [[1] * 8 for i in range(8)] # Change into a 2d Array 
        for i in range(0,8):
            for j in range(0,8):    
                chessboard[i][j] = str(i) + alphabet[j]
        return chessboard

    def populate(chessboard):
        
        chessboard[0][0] = rook3.kind
        chessboard[0][1] = knight3.kind
        chessboard[0][2] = bishop3.kind
        chessboard[0][3] = king2.kind
        chessboard[0][4] = queen2.kind
        chessboard[0][5] = bishop4.kind
        chessboard[0][6] = knight4.kind
        chessboard[0][7] = rook4.kind
        
        chessboard[7][0] = rook1.kind
        chessboard[7][1] = knight1.kind
        chessboard[7][2] = bishop1.kind
        chessboard[7][3] = queen1.kind
        chessboard[7][4] = king1.kind
        chessboard[7][5] = bishop2.kind
        chessboard[7][6] = knight2.kind
        chessboard[7][7] = rook2.kind
        
        for i in range(0,8):
            chessboard[1][i] = pawn_black[i] 
            chessboard[6][i] = pawn_white[i]
            
        return chessboard
        
    chessboard = createboard()
    print (populate(chessboard))

'''###############################
    def movement(Pieces, chessboard):
        
    -Rook
    -Knight
    -Bishop
    -Queen
    -King
    -Pawn       

        '''###############################

    def KnightMovement(Pieces, chessboard):
        if (Pieces.kind == "knight")
        i,j = row,column
            resolve = []    #Replaces set index

            # TopLeft
            try:
                Lvalue = chessboard[i-1][j+2]
                resolve.append([i-1,j+2])
            except
                pass

            # TopRight
            try:
                Lvalue = chessboard[i+1][j+2]
                resolve.append([i+1,j]+2)
            except
                pass

            # RightTop
            try:
                Lvalue = chessboard[i+2][1+j]
                resolve.append([i+2, j+1])
            except
                pass

            # LeftTop
            try:
                Lvalue = chessboard[i-2][1+j]
                resolve.append([i-2, j+1])
            except
                pass
            # Null
            try:
                Lvalue = chessboard[i][j]
                resolve.append([i, j])
            except
                pass

            # LeftBottom
            try:
                Lvalue = chessboard[i-2][j-1]
                resolve.append([i-2, j-1])
            except
                pass
            # RightBottom
            try:
                Lvalue = chessboard[i+2][j-1]
                resolve.append([i+2, j-1])
            except
                pass

            # BottomLeft
            try:
                Lvalue = chessboard[i-1][j-2]
                resolve.append([i-1, j+2])
            except
                pass

            # BottomRight
            try:
                Lvalue = chessboard([i+1][j-2])
                resolve.append([i+1, j-2])
            except
                pass


    def RookMovement(Pieces, chessboard):
        resolve 

    def BishopMovement(Pieces, chessboard):




    def main ():

       """Main function that will welcome the player to the game."""

       print("\tWelcome to Chess Slaughter house! This is a turn based Chess simulator where")
       print("\tTeam white or team black shall vanquish")

       print("\nHow to play.\n\nPlayers take turn to choose a move.")
       print("Choose tou piece and hope to win")
       print("(Still in Beta)")

       print("\nThat's it! Good luck")

       """#################################"""
    # Calls and initalize the function for making the board
    board()
    play = True
    while play:

        # Plays with the turn
        turn  = random.randint(1,2)
        if turn ==1:
            white  = True
            black = False
            print ("\n White player will commence!")
         else
            white = False
            black = True
            print ("\n White player will commence!")
        # Choose player

        try:
            Player_white = raw_input('w')
            except
            player_black = raw_input('b')

        # Switch turns
        white = not black
        black = not white


        print("\nWhite Player: ", white, "Computer health: ", black)
        print("\nCongratulations! You have won. You're an animal!!")
    else:
        print("\nPlayer health: ", white , "Computer health: ", black)

        print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            play_again = False

            main()
            else
            print("\nThank you for playing!!")
            exit = raw_input('q')
            play = False
            exit = play
            main()

            # Calls Functions for 
            # Chess board / pieces
            # Matrix 8x8


    # In[ ]:



