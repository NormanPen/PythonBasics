# Tic Tac Toe Game


# Initiiert Das Spielbrett
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Initiiert zwei Spieler
player_one = input( "Wie heißt du?")
player_two = input( "Wie heißt du?")

# Gibt das Spielfeld aus
def print_board(board):
    print("==========")
    print(board[0] + " " + board[1] + " " + board[2])
    print(board[3] + " " + board[4] + " " + board[5])
    print(board[4] + " " + board[7] + " " + board[8])
    print("==========")
print_board(board)

# Spielerzug gibt Eingabe des jeweiligenspielers zurück
def player_move(player):
    if player == player_one:
        p1 = input(player_one + " Wähle ein Feld:")
        return p1
    else:
        p2 = input(player_two + " Wähle ein Feld")
        return p2

move_p1 = player_move(player_one)
move_p2 = player_move(player_two)

# Verändert das Spielfeld entsprechend der Eingabe // Es muss noch eine Überprüfung her welcher Spieler die Eingabe gemacht hat
def change_board(move):
    if move == "1":
        board[0] = "X"
    elif move == "2":
        board[1] = "X"

# Überprüft ob Spieler gewonnen hat
def win(board):
    if board[0] == board[1] and board[0] == board[2]:
        print("Du hast gewonnen")
        exit()
    else:
        print("Weiter gehts")
        return True



# Hier muss eine Schleife drum herum die solange durchläuft wie win() true zurückgibt
win(board)
change_board(move_p1)
print_board(board)

change_board(move_p2)
print_board(board)
win(board)
#########################################