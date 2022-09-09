# Schreiben Sie eine Funktion, die einen Punktestand daraufhin prueft,
# ob dieser einen neuen Highscore darstellt. Das trifft dann zu, wenn die aktuelle Punktezahl groesser
# als der momentne Highscore ist. In dem Fall soll eine Meldung auf die Konsole ausgegeben werden.
# Als Ausgangsbasis dienen folgende Anweisungen:

points = 1234
highscore = 1000

def check_highscore(highscore, points):
    if points > highscore:
        print("Congratulation, " + str(points) + " is a new highscore")

check_highscore(highscore, points)
check_highscore(1000, 4345)





