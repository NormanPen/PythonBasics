# Wir bekommen einen Auftrag und sollen 1000 Kisten ausliefern. In unseren LKW passen pro Fahrt nur 75 Kisten. Berechnen Sie, 
# wie oft  wir fahren muessen und wie viele Kisten in der letzten Fahrt transportiert werden. Verwenden Sie sprechende Variablennamen.

bestellmenge = 1_000
lkw_kapazitaet = 75

fahrten = bestellmenge // lkw_kapazitaet
rest = bestellmenge % lkw_kapazitaet
if rest > 0:
    fahrten += 1

print("Wir muessen " + str(fahrten) + " fahren")
print("Bei der letzen Fahrt transportieren wir " + str(rest) + " Kisten")

# Loesung
bestellmenge = 1_000
lkw_kapazitaet = 75
restmenge = bestellmenge % lkw_kapazitaet
anzahl_fahrten = bestellmenge // lkw_kapazitaet
if restmenge != 0:
    anzahl_fahrten += 1

print(anzahl_fahrten)
