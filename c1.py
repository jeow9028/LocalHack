
# coding: utf-8

# In[64]:

import numpy as np
import string


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
        
        chessboard[0][0] = rook3
        chessboard[0][1] = knight3
        chessboard[0][2] = bishop3
        chessboard[0][3] = king2
        chessboard[0][4] = queen2
        chessboard[0][5] = bishop4
        chessboard[0][6] = knight4
        chessboard[0][7] = rook4
        
        chessboard[7][0] = rook1
        chessboard[7][1] = knight1
        chessboard[7][2] = bishop1
        chessboard[7][3] = queen1
        chessboard[7][4] = king1
        chessboard[7][5] = bishop2
        chessboard[7][6] = knight2
        chessboard[7][7] = rook2
        
        for i in range(0,8):
            chessboard[1][i] = pawn_black[i] 
            chessboard[6][i] = pawn_white[i]
            
        return chessboard
        
    chessboard = createboard()
    print (populate(chessboard))


# In[ ]:



