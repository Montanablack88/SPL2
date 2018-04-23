#zahlenraten.py

import random
max = 200
gewonnen = 0
Zufallszahl = random.randint(1,max)
versuche = 0
print("Zufallszahlen-rate: bitte eine zahl zwischen 1 und", max, "eingebn")
while(gewonnen == False):
    zahl = input("Welche Zahl? ")
    zahl = int(zahl)
    versuche += 1
    if(zahl == Zufallszahl):
        gewonnen = True
    if ( zahl < Zufallszahl):
        print("mehr")
        
    if (zahl > Zufallszahl):
        print("weniger") 
      


print("Bravo - Sie haben die Zahl in", versuche, "Versuchen erraten")