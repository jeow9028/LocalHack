# Chessboard.py

import numpy as np

def board ():
	# Creates an 8x8
# 
# [[0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
# 

	z = np.random.randint(64, size=(8, 8))
	print z	()
	int x = 1;		#White space
	int y = x+1;	#Black space

def turn():
	# Makea function for the turn you have if you are a white piece or black piece
	# if turn is 0 then white pice starts

	white = 0
	black  = 0

	turn = 0
	turn = turn +1
	if (turn == 0)
	

def movement():



def main ():

	"""Main function that will welcome the player to the game."""

    print("\tWelcome to Chess Slaughter house! This is a turn based Chess simulator where")
    print("\tTeam white or team black shall vanquish")

    print("\nHow to play.\n\nPlayers take turn to choose a move.")
    print("Choose tou piece and hope to win")
    print("(Still in Beta)")

    print("\nThat's it! Good luck")

    """#################################"""
    while play:

	    turn  = random.randint(1,2)
	    if turn ==1:
	    	white  = True
	    	black = False
	    	print ("\n White player will commence!")
	    else
	    	white = False
	    	black = True
	    	print ("\n White player will commence!")



	board()
	turn()
	movement()
	# Calls Functions for 
	# Chess board / pieces
	# Matrix 8x8

