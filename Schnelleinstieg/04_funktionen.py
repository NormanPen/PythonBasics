# Funktionen

# Funktionen aufrufen
# funktion_name(Argument1, Argument2, ... Argument5, ...)
print("Das ist ein Funktionesaufruf mit einem String als Argument")

# Eigenene Funktionen definieren

def add (value1, value2): # Funktions mit dem namen add und zwei Parametern
    return value1 + value2 # gibt val1 + val 2 zurück

# Speichert Funktionsaufruf in einer Variable, damit das Ergebnis gespeichert wird
result = add(23, 42) # ruft Funktion add mit zwei Argumenten auf


print(result) # Gibt das result auf die Kommantoteile aus

# Spezialfall: Kein Rückgabewert

def greet(name):
    print(name) # Kein return


# Aufruf mit einem Argument
greet("Michael Jackson")
# Ausgabe: Michael Jackson

# Kombination mit Bedingungen

def min_of_3(x, y, z):
    if x < y:
        if x < z:
            return x
        else:
            return y
    else:
        return z

min_of_3(1, 2, 3) # 1
min_of_3(11, 5, 3) # 3
min_of_3(16, 22, 55) # 16

# Funktionen als wiederverwendbare Bausteine

def min_of(x, y):
    if x < y:
        return x
    else:
        return y

# Kürzere Schreibweise
def min_of_schorter(x, y):
    return x if x < y else y

def min_of_three(x, y, z):
    return min_of(x, min_of(x, y))

min_of_three(1, 2, 3) # 1
min_of_three(11, 5, 3) # 3
min_of_three(16, 22, 55) # 16


