# Listen
# Speichern mehrere Werte
names = ["Berbel", "Hans", "Peter"]

# Alternative leere Listen:
empty_list_1 = []
empty_list_2 = list()

# Zugriff auf Elemente
names[0] # "Berbel"
names[2] # "Peter"
names # "Berbel", "Hans", Peter

# Länge der Liste:
#names.len() # 3

# Tuples speichern mehrere Werte, die Informationen sind unveränderlich
names_tuple = ("Sandra", "Tim", "Florian")

# Zugriff
names_tuple[0] # "Sandra"
# names_tuple[0] = "Sanni" kann nicht geändert werden


#Dictionaries in JS Objecte

person_phone = { "Tim" : "iphone",
"Julia" : "Galaxy S",
"Mark" : "NoPhone"
}

print(person_phone)
print(person_phone["Mark"])
person_phone["Julia"] = "NewPhone"
print(person_phone["Julia"])


#set
#wird nur ein u ausgegeben/ keine duplikate
vowels ={'a', 'e', 'i', 'o', 'u', 'u'}
vowels2 ={'aeiouu'}
print(vowels)


fruits = {"Apple", "Banana"}
print(fruits)
fruits.add("Banana")
print(fruits)
fruits.add("Kiwi")
print(fruits)
fruits.remove("Apple")
print(fruits)

for x in fruits:
    print(x)
