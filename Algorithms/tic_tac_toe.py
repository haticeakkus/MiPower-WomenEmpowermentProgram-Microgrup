# Initialize the board 
def init_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(f" {board[row][col]} ", end="")
            if col < len(board[row]) - 1:
                print("|", end="")
        print()
        if row < len(board) - 1:
            print("---|---|---")
    print()

# Check if a player wins
def check_winner(board, symbol, player1_name, player2_name):
    # Horizontal check
    for row in board:
        if all(s == symbol for s in row):
            print(f"Congratulations, {player1_name if symbol == 'X' else player2_name} wins!")
            print_board(board)
            return True

    # Vertical check
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            print(f"Congratulations, {player1_name if symbol == 'X' else player2_name} wins!")
            print_board(board)
            return True

    # Diagonal check
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2-i] == symbol for i in range(3)):
        print(f"Congratulations, {player1_name if symbol == 'X' else player2_name} wins!")
        print_board(board)
        return True
    
    return False

# Check if the game ended in a tie
def check_tie(board):
    return all(cell != " " for row in board for cell in row)

# Main function to start the game
def tic_tac_toe():
    print("Welcome to XOX (Tic-Tac-Toe) Game!")
    print("Player 1 represents X symbol.")
    print("Player 2 represents O symbol.")
    print("Each player will choose a cell in turn, for example, '0,0' represents the top left corner, '2,2' represents the bottom right corner. \n")

    # Get player names
    player1_name = input("Player 1, please enter your name: ")
    player2_name = input("Player 2, please enter your name: ")

    # Initialize scores
    player1_score = 0
    player2_score = 0

    while True:
        print(f"Scores: {player1_name}: {player1_score}, {player2_name}: {player2_score}")

        board = init_board()
        current_player = player1_name
        
        while True:
            print_board(board)
            try:
                row, col = map(int, input(f"{current_player}, please select row and column (0, 1, 2): ").split(','))
            except ValueError:
                print("Please enter valid two numbers separated by a comma.")
                continue
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Please select a row and column between 0-2.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = "X" if current_player == player1_name else "O"
            else:
                print("This cell is already occupied, please choose another cell.")
                continue
            
            if check_winner(board, "X", player1_name, player2_name):
                if current_player == player1_name:
                    player1_score += 1
                else:
                    player2_score += 1
                break
            
            if check_winner(board, "O", player1_name, player2_name):
                if current_player == player1_name:
                    player1_score += 1
                else:
                    player2_score += 1
                break
            
            if check_tie(board):
                print_board(board)
                print("It is a tie!")
                break
            
            # Change turn
            current_player = player2_name if current_player == player1_name else player1_name
        
        # Check if a player reached 3 points
        if player1_score == 3 or player2_score == 3:
            print("Game Over!")
            print(f"Final Scores: {player1_name}: {player1_score}, {player2_name}: {player2_score}")
            if player1_score > player2_score:
                print(f"Congratulations, {player1_name} wins the match!")
            elif player1_score < player2_score:
                print(f"Congratulations, {player2_name} wins the match!")
            break

# Start the game
tic_tac_toe()
