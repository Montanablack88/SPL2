 #Grundlagen-Python.py

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

    lieblingszahl = input("Was ist deine Lieblingszahl")
    print("Super, ich mag dei Zahl", lieblingszahl)
    print("Aber die coolere Zahl", int(lieblingszahl)+10, "mag ich noch mehr")

    runden = input("Wie viele Runden sollen wir Spielen? ")
    runden = int(runden)