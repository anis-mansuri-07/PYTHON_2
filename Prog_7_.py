from Module_7 import *

print_board()
l=0
for turn in range(9):
    if turn % 2 == 0:
        print("Player's turn:")
        player_move()
    else:
        print("Computer's turn:")
        computer_move()

    print_board()

    if check_winner('X'):
        print("Player wins!")
        l=1
        break
    elif check_winner('O'):
        print("Computer wins!")
        l=1
        break

if l==0:
        print("It's a draw!")