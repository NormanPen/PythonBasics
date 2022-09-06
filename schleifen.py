# Indexbasierte for-in Schleife
"""
for : in range(2,6):
    print("Durchlauf:", i)

Durchlauf: 2
Durchlauf: 3
Durchlauf: 4
Durchlauf: 5
"""

names = ["Barb", "Felix", "Lilly"]
for i in range(len(names)):
    print(names[i])

"""
Barb
Felix
Lilly
"""

# Wertebasierte for-in-Schleife

for current_name in ["Barb", "Felix", "Lilly"]:
    print(current_name)
"""
Barb
Felix
Lilly
"""

# While Schleife
i = 0
while i < 5:
    print(i)
    i += i
"""
0
1
2
3
4
"""