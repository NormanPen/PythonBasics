# Gegeben: Fuktion die pueft, ob ihre beiden Eingabeparameter in 
# einem gewissen Wertebereich liegen. Vereinfachen Sie die Umsetzung

"""
def do_something(x, y)
    if x > 0 and x < 100 and y > 10 and y < 20:
        print("VALID RANGE)
"""


# Loesung
def do_something(x, y):
    if 0 < x < 100 and 10 <y < 20:
        print("VALID RANGE")