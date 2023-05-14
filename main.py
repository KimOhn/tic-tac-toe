from tiktactoe import Tiktactoe

play = False

start = input("Would you like to play the Tiktactoe game? (y/n)")
if start.upper() == "Y":
    play = True
    game = Tiktactoe()

    game.first_turn()


while play:
    print(f"Player {game.current_player}'s turn")
    game.print_board()
    row, col = list(map(int, input("Enter row and column numbers to mark your spot: ").split()))
    game.mark_spot(row,col)
    if game.win():
        print(f"{game.current_player} won.")
        play = False
    elif game.is_board_occupied():
        play = False
        print("the game is over - the result is a tie")
    else:
        game.switch_player()

print("the final result is:")
game.print_board()

