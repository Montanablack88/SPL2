 #Grundlagen-Python.py
import random
# Kommentare efolgen mit Hashtack

# Ausgabe von daten

# Variable definieren (kann ohne Typ erfolgen)
heimat = "Erde"


# Mehrere Varinblen werden mit , getrennt
print(heimat, "an World: ", "Hallo!")

# Eingabe 
wer = input("Und wer bist du? ")

# und gibt den text wieder aus
if (wer == "ich"):
    print ("Hallo DU!")
else:
    print("Hallo", wer)    

    lieblingszahl = input("Was ist deine Lieblingszahl? ")
    print("Super, ich mag dei Zahl ", lieblingszahl)
    print("Aber die coolere Zahl ", int(lieblingszahl)+10, " mag ich noch mehr")

    runden = input("Wie viele Runden sollen wir Spielen? ")
    runden = int(runden)
siege_computer = 0    
siege_ich = 0
for runde in range(1,runden+1):
    sieger = ""
    #zufallszahl erzeugen
    zufallszahl = random.randint(1,6)
    #sonst ist der Computer sieger
    if (zufallszahl == 1 or zufallszahl == 3 or zufallszahl == 5):
        sieger = "ich"
        siege_ich += 1
    else:
        siege = "computer"
        siege_computer += 1
    print("Runde" , runde, "von", runden, ": Sieger :", sieger, ": gewuerfelt wurde:", zufallszahl)
if (siege_ich > siege_computer):
    print("Du gewinnst")
elif (siege_computer > siege_ich):
    print("Du verlierst")    
else:
     print("Unentschieden")
print("game over.")        
