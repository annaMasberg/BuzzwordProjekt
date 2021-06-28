import random

# Benutzer eingabe durch Input
name = input('Geben Sie Bitte ihr Name ein:')
print(name, 'Willkommen zu Buzzword-Bingo-Spiel')
print()

# Benutzer waelht die groesse von die Karten
print('Waehlen Sie Bitte die Hoehe und Breite der Karte!')
hoehe = 1
breite = 0
while hoehe != breite:
    print('Hoehe und Breite sollen gleich sein')
    hoehe = int(input('Geben Sie bitte die Hoehe der Spalte'))
    breite = int(input('Geben Sie bitte die Breite der Spalte'))

# Falls die Karte nicht symmetrisch ist
print()
print('Hoehe ist:', hoehe)
print('Breite ist:', breite)
print()

# hoehe und breite multiplizieren um die groesser der Karte zu wissen
felderAnzahl = hoehe * breite
print('Anzahl der Felder betraegt: ', felderAnzahl)
print('Spiel faengt an')
print()

# Textdatei in Array speichern
txt = open('BuzzwordTextDatei', 'r')
arr = txt.readlines()

# random generieren damit die Karten auf zufaellige Woertern greifen
# woerter werden einmalig gegeben
#\n werden entfernt

buzzWord = list()
for x in range(felderAnzahl):
    randomnumber = random.randint(0, len(arr))  # generiert random Woerter
    while arr[randomnumber] == 'x':
        if arr[randomnumber] == 'x':
         randomnumber = random.randint(0, len(arr))
    buzzWord.append(arr[randomnumber].strip('\n'))
    arr[randomnumber] = 'x'

#karte wird gestellt
def karte_erstellen(h, b):
    karte_new = [[0 for x in range(h)]for y in range(b)]
    return karte_new

#karte wird ausgefullt
def karte_fullen(h, b, karte, buzzWord):
    counter = 0
    for x in range(h):
        for y in range(b):
            karte[x][y] = buzzWord[counter]  # einzel die woerter in die Liste rein
            counter += 1

#Joker wir in der Miter der Feldern 5x5 & 7x7 eingegeben
    if felderAnzahl == 25:
        karte[2][2] = "JOKER"
    elif felderAnzahl == 49:
        karte[3][3] = "JOKER"
    return karte

karte = karte_erstellen(hoehe, breite)
karte_new = karte_fullen(hoehe, breite, karte, buzzWord)

#Ausgabe damit die Woertern untereinander + Kaestchen die selbe laenge haben.
N = 15
def generateCard(word):
    if len(word) > N:
        word = word[0:N]
    elif len(word) < N:
        word += ' '* (N - len(word))
    return word

for row in karte_new:
    for word in row:
        print('|', generateCard(word), end=' | ')
    print()


