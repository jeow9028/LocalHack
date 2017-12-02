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

