
# coding: utf-8

# In[47]:

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
    
        def movement(kind):   
            if(kind =="king"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Your King is dead, check Mate!")
            
            elif(kind =="queen"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Your Queen is dead")
            
            elif(kind== "bishop"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Your Bishop is dead")
            
            elif(kind== "rook"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Your Rook is dead")  
            
            elif(kind =="knight"):
                while(life!=0):
                    print("Hello world")
                else:
                    print("Your Bishop is dead")
            
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

    #for i in range(0,8):
       # str(i)
        #pawn_white.i = Pieces('pawn', 'white',1)
        #pawn_black.i = Pieces('pawn', 'black',1)
    
    def createboard():
        #list(string.ascii_lowercase)
        chessboard = [[1] * 8 for i in range(8)] # Change into a 2d Array
        for i in range(0,8):
            [chr(i) for j in range(ord('a'),ord('h')+1)]:
                str(j)
                chessboard[i][j] = 'i'+j
        return chessboard

    #def populate(chessboard):
     #   for i in range(0,8):
      #      chessboard[1][i] = rook4
       #     chessboard[6][i] = rook4
        
    chessboard = createboard()
    print (chessboard)


# In[ ]:



