import numpy as np
import random

board = np.zeros((3, 3)).astype(int) # Initialize a 3x3 game board with zeros
turn = 1 # Player 1 starts the game
move = 9 # Total number of moves available

# print("Initial game board:")
# print(board)

def play_turn():
    if(turn ==1):
        x = int(input(f"What is player {turn}'s x position?"))  # Player 1 inputs their x position
        y = int(input(f"What is player {turn}'s y position?"))  # Player 1 inputs their y position
    else:
        x = random.randint(0,2); # Player 2's x position is randomly chosen
        y = random.randint(0,2); # Player 2's y position is randomly chosen
       
    try: # section explained (a)
        if board[y, x]==0:    #Check if the chosen position is empty
            board[y, x]=turn  # Place the player's mark on the board
        else:                                       
            if(turn == 1):                           
                print("The board already contains") # Inform Player 1 that the position is occupied
            play_turn() #retry the turn
    except IndexError:        
        print("Input error")  
        play_turn()           

def check_win():
    if any(np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board[::-1]))==3:
        return True
    if any(np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board[::-1]))==-3:
        return True
    return False


while move >0:
    
#         a
#----------------------
    print (board) # Draw the board
    play_turn()   
#----------------------
    if check_win():
#         b
#--------------------------------------------
        print (f"Player {turn} has won!")
        break
#--------------------------------------------
#         c
#--------------------------------------------
    turn = turn*-1 #Switches the current player.
    move = move -1 # Decreases the number of remaining moves.
#--------------------------------------------
