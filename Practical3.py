# Winning combinations based on board positions 1-9
WIN_COMBOS = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
    [1, 5, 9], [3, 5, 7]             # diagonals
]

board = [" " for _ in range(9)]

def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(symbol):
    for combo in WIN_COMBOS:
        if all(board[pos - 1] == symbol for pos in combo):
            return True
    return False

def check_draw():
    return " " not in board

# --- Main Game Setup ---

# Player symbol choice
player1 = input("Player 1, choose X or O: ").upper()
while player1 not in ["X", "O"]:
    player1 = input("Invalid choice. Choose X or O: ").upper()

player2 = "O" if player1 == "X" else "X"

print(f"Player 1 is {player1}")
print(f"Player 2 is {player2}")

current_player = player1

# --- Game Loop ---
while True:
    display_board()
    
    try:
        move = int(input(f"Player ({current_player}), choose position (1-9): "))
        
        # Validation for board range and empty spots
        if move < 1 or move > 9 or board[move - 1] != " ":
            print("Invalid move. Try again.")
            continue
            
        board[move - 1] = current_player
        
        if check_win(current_player):
            display_board()
            print(f"🎉 Player ({current_player}) wins!")
            break
            
        if check_draw():
            display_board()
            print("🤝 Game Draw!")
            break
            
        # Switch turns
        current_player = player2 if current_player == player1 else player1
        
    except ValueError:
        print("Please enter a valid number between 1 and 9.")