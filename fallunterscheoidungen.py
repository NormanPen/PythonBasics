# Bedingungen mit if

"""
if consition
    Aktin
"""

if 6 * 7 == 42:
    print("We found the answer")
# Ausgabe: We found the answer

age = 27
if age >= 18:
    print("You are allowed to drive a car ...")
    print("- in case you have adriving licens")

# Ausgabe: ou are allowed to drive a car ...
#           - in case you have adriving licens

# if und else in Kombination
user = "Micheal"
if user == "Michael":
    print("Access granted")
else:
    print("Access denied")
# Ausgabe: Access granted

# Kurzschreibweise:
#positivCase if comdition else negativCase
result = "allowed" if age > 18 else "Not Allowed"


#if, elsif und alse in Kombination

time = 15
if time < 12:
    print("Good morning")
elif time < 18:
    print("Good afternoon")
elif time < 22:
    print("Good evening")
else:
    print("good night")
# Ausgabe: Good afternoon

# Funktionen

# Funktion definieren
"""
def funktion_name(Parameter1, Parameter2, ...):
    Anweisung1
    Anweisung2
"""

# Funktion aufrufen
# funktion_name(argument1, argument2)
# MERKE: In der definition ist das was in den Klammern steht ein Parameter, beim Auffrug wird ein Argument übergeben

# Beispiel Print Funktion
print("Hallo", "du", "da") #Der Funktion print werden drei Argumente übergeben, "Hallo" "Du" und "Da" Ausgabe: Hallo du da

# Eigene Funktionen definieren
def add(value1, value2): # Erstellen der Funktion add mit den Parametern value1 und value 2
    return value1 + value2 # return Rückgabewert
# Aufruf:
print(add(23, 42)) # Um add auf die Konsole auszugeben wird print die Funktion add mit den Argumenten 2 und 4 übergeben
# Ausgabe: 64

# Spezialfall: Keine Rückgabewerte
def greet(name):
    print("Hallo " + name)
    # Es gibt keinen return, es wird einfach etwas auf die Konsole ausgegeben
greet("Holger")
# Ausgabe: Hallo Holger

# Kombination mit Bedingungen
def min_of_tree(x, y, z):
    if x < z:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z
min_of_tree(1, 2, 3)
#1
min_of_tree(11,2,3)
#2
min_of_tree(11,22,3)
#3





