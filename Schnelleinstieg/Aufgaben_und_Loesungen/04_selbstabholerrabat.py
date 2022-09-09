# In dieser Aufgabe sollen Sie fuer einen Pizzaliefersevice die Preisberechnung  implentieren. Nehmen wir vereinfacht an, 
# jede Pizza kostet 11 Euro. Dabei gelten folgende Regelungen zum Rabatt: Wenn wir 5 oder mehr Pizzen bestellen, dann erhalten 
# wir einen Rabat von 10%. WEnn wir die Pizza selber abholen, dann erhalten weir pro Pizza einen Nachlass von 2 Euro. 
# Schreiben Sie eine Funktion, die den Rechungsbetrag erittelt.

def preis_berechnen(anzahl, abholer):
    pizza = 11
    prozent_rabat = 10
    abhol_rabat = 2


    if anzahl >= 5:
        kosten = (pizza * anzahl) - ((pizza * anzahl) // 100 * prozent_rabat)
        if abholer == True:
            return kosten - abhol_rabat
        else: 
            return kosten
             
    else:
        if abholer == True:
            return pizza * anzahl - abhol_rabat
        else:
            return pizza * anzahl


print(preis_berechnen(2, True))
print(preis_berechnen(2, False))

print(preis_berechnen(10, True))
print(preis_berechnen(10, False))
        

