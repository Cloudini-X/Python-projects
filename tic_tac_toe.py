def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("--+---+--")
    print("\n")

def check_winner(board, player):
    win_condition = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,4,8], #coloums        
        [0,4,8], [2,4,6]          # diagonals
    ]

    for condition in win_condition:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False
    
def tic_tac_toe(): 
    board = [" " for _ in range(9) ]
    current_player = "X"

    for turn in range(9):
        print_board(board)

        #take input
        move = int(input(f"player{current_player}, enter your move(1-9):")) -1

        #check if valid
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = current_player

        #check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"player{current_player} wins!")
            return
        
        #switch player
        current_player = "0" if current_player == "X" else "X"

        #if loop finishes (tie)
        print_board(board)
        print("It's a tie!")

#start the game
tic_tac_toe()




