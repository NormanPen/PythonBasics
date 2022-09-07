# Tic Tac Toe Game

# Initiiert zwei Spieler
player_one = "Max"
player_two = "Ulla"

# Initiiert Das Spielbrett
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Gibt das Spielfeld aus
def print_board(board):
    print(board[0] + " " + board[1] + " " + board[2])
    print(board[3] + " " + board[4] + " " + board[5])
    print(board[4] + " " + board[7] + " " + board[8])

print_board(board)

# Spielerzug gibt Eingabe des jeweiligenspielers zurück
def player_move(player):
    if player == player_one:
        p1 = input(player_one + " Wähle ein Feld:")
        return p1
    else:
        p2 = input(player_two + " Wähle ein Feld")

move = player_move(player_one)

# Verändert das Spielfeld entsprechend der Eingabe
def change_board(move):
    if move == "1":
        board[0] = "X"

# Überprüft ob Spieler gewonnen hat
def win(board):
    if board[0] == board[1] and board[0] == board[2]:
        print("Du hast gewonnen")
    else:
        print("Weiter gehts")


win(board)

change_board(move)

print_board(board)