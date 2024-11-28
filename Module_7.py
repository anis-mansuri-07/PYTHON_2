import random

# Initialize the board
board = ['_','_','_','_','_','_','_','_','_']

def print_board():
   for i in range(0,8,3):
       print("{}|{}|{}".format(board[i],board[i+1],board[i+2]))

 

def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for i in win_conditions:
        if(board[i[0]]==player and board[i[1]]==player and board[i[2]]==player):
            return 1
    return 0
    

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == '_':
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_move():
    availables = []
    for i in range(9):
         if(board[i]=='_'):
             availables.append(i)
    move = random.randint(0,8)
    if(move in availables):
         board[move] = 'O'
    else:
        while(True):
            move=random.randint(0,8)
            if(move in availables):
                board[move]='O'
                break