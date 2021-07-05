from prettytable import PrettyTable
import random
from termcolor import colored, cprint

# Start, Einleitung in das Spiel
cprint('--------------------', 'magenta')
cprint('\n\n\n\n\nWILLKOMMEN BEI BUZZWORD BINGO\n\n\n\n\n', 'magenta', attrs=['reverse', 'blink'])
cprint('--------------------', 'magenta')
input("Um fortzusetzen, drücken Sie im Spielverlauf bitte die Enter-Taste")
cprint('--------------------', 'yellow')

# einzelspielermodusFrage = input("Bitte drücken Sie auf die Enter taste, wenn Sie im Einzelspielermodus fortfahren möchten. \nFalls nicht, tippen Sie bitte 'Nein':")
# if einzelspielermodusFrage=="Nein" or einzelspielermodusFrage=="nein":

# Abfrage + spieler gibt die gewünschte größe für die Bingokarte ein
print(
    "\n\nZunächst wird eine Bingokarte generiert.\nHierfür geben Sie im nächsten Schritt an, für welche größe Sie sich entscheiden möchten")
print("\n\n3x3 = 3 \n4x4 = 4 \n5x5 = 5 \n6x6 = 6 \n7x7 = 7")
laenge_breite = int(input("\n\nBitte geben Sie Ihre Auswahl für die Länge/Breite der Bingokarte ein: "))
cprint('--------------------', 'yellow')

# Felderanzahl wird berechnet
felderAnzahl = laenge_breite * laenge_breite

# Textdatei wird in ein Array gespeichert für die Buzzwords
txt = open('BuzzwordTextDatei', 'r')
arr = txt.readlines()

# Textdatei wird in ein Array gespeichert für die WinnerWords -> gezogenen Wörter
winntxt = open('WinnerWords.txt')
winnarr = winntxt.readlines()

# Hier werden random wörter aus der Textdatei für die buzzword gewählt
buzzWord = list()
for x in range(felderAnzahl):
    randomnumber = random.randint(0, len(arr))  # generiert random Woerter
    while arr[randomnumber] == 'x':
        if arr[randomnumber] == 'x':
            randomnumber = random.randint(0, len(arr))
    buzzWord.append(arr[randomnumber].strip('\n'))
    arr[randomnumber] = 'x'

# Hier werden random wörter aus der Textdatei für die Winnerwords gewählt
winnerWords = list()
for x in range(felderAnzahl):
    randomnumber = random.randint(0, len(winnarr))  # generiert random Woerter
    while winnarr[randomnumber] == 'x':
        if winnarr[randomnumber] == 'x':
            randomnumber = random.randint(0, len(winnarr))
    winnerWords.append(winnarr[randomnumber].strip('\n'))
    winnarr[randomnumber] = 'x'


# karte wird erstellt
def karte_erstellen(h, b):
    karte_new = [[0 for x in range(h)] for y in range(b)]
    return karte_new


# karte wird gefüllt mit den Buzzwords
def karte_fullen(h, b, karte, buzzWord):
    counter = 0
    for x in range(h):
        for y in range(b):
            karte[x][y] = buzzWord[counter]  # die woerter in die Liste rein
            counter += 1

    # Joker wir in der Miter der Feldern 5x5 & 7x7 eingegeben
    if felderAnzahl == 25:
        karte[2][2] = "JOKER"
    elif felderAnzahl == 49:
        karte[3][3] = "JOKER"
    return karte


karte = karte_erstellen(laenge_breite, laenge_breite)
karte_new = karte_fullen(laenge_breite, laenge_breite, karte, buzzWord)
# print(karte_new)


laenge_breite2 = laenge_breite

# für die eingabe die der Benutzer macht um zu bestätigen ob die Wörter sich auf der Bingokarte befinden
ja = "Ja"
nein = "Nein"
enter = ""

print("Das Spiel geht", felderAnzahl, "Runden")
input("Ob Sie gewonnen haben, werden Sie im Anschluss erfahren")
cprint('--------------------', 'yellow')
cprint("\n\n\nSPIELSTART\n\n\n")
cprint('--------------------', 'yellow')

# das eigentliche spiel beginnt ab hier:
# Je nach größe der Bingokarte wird mit dem Spiel gestartet.
if laenge_breite == 3:
    x3 = PrettyTable()  # hiermit wird die bingokarte dargestellt
    x3.field_names = ["3x3", "0", "1", "2"]
    x3.add_row(["0", karte_new[0][0], karte_new[0][1], karte_new[0][2]])
    x3.add_row(["1", karte_new[1][0], karte_new[1][1], karte_new[1][2]])
    x3.add_row(["2", karte_new[2][0], karte_new[2][1], karte_new[2][2]])
    print(x3)
    cprint('--------------------', 'yellow')
    for element in range(felderAnzahl):
        print("Das gezogene Wort ist: " + colored(winnerWords[element],
                                                  'cyan'))  # das gezogene winnerword wird farbig angezeigt
        cprint('--------------------', 'yellow')
        antwortBenutzer = input(
            "Steht das gezogene Wort auf ihrem Bingofeld? \n(Mit Ja/Nein/Enter-Taste antworten): ")  # spieler muss bestätigen ob sich das wort auf seiner Bingokarte befindet
        cprint('--------------------', 'yellow')
        if antwortBenutzer == "Ja" or antwortBenutzer == "ja":  # Falls ja, muss er die Koordinaten eingeben um das Wort zu makieren
            xkoordinate = int(input("\nBitte geben Sie die X Kooridnate an, damit das Wort markiert werden kann: "))
            ykoordinate = int(input("\nBitte geben Sie die Y Koordinate an, damit das Wort markiert werden kann: "))
            cprint('--------------------', 'yellow')
            print(colored(karte_new[ykoordinate][xkoordinate], 'red'))  # das makierte wort wird einzelnd angezeigt
            karte_new[ykoordinate][xkoordinate] = "x"
            cprint('--------------------', 'yellow')
            z3 = PrettyTable()
            z3.field_names = ["3x3", "0", "1",
                              "2"]  # neue Binfokarte mit dem ausgewählten wort makiert bzw. durch ein x ersetzt
            z3.add_row(["0", karte_new[0][0], karte_new[0][1], karte_new[0][2]])
            z3.add_row(["1", karte_new[1][0], karte_new[1][1], karte_new[1][2]])
            z3.add_row(["2", karte_new[2][0], karte_new[2][1], karte_new[2][2]])
            print(z3)
            cprint('--------------------', 'yellow')
        elif antwortBenutzer == "Nein" or antwortBenutzer == "nein" or antwortBenutzer == "":  # Falls der benutzer nein schreibt oder die Enter-Taste drückt, wird das Spiel fortgesetzt
            print("Kein Feld wurde markiert")
            cprint('--------------------', 'yellow')

        else:
            print(
                "Eingabe war nicht Korrekt. Das Spiel wird fortgesetzt...")  # bei anderen eingaben wird das spiel ebenso fortgesetzt

    # hier wird geprüft ob der spieler gewonnen hat
    # Abfrage kreuz
    if karte_new[0][0] == "x" and karte_new[1][1] == "x" and karte_new[2][2] == "x" or karte_new[0][2] == "x" and \
            karte_new[1][1] == "x" and karte_new[2][0] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen1', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen  (zeilen)
    elif karte_new[0][0] == "x" and karte_new[0][1] == "x" and karte_new[0][2] == "x" or karte_new[1][0] == "x" and \
            karte_new[1][1] == "x" and karte_new[1][2] == "x" or karte_new[2][0] == "x" and karte_new[2][1] == "x" and \
            karte_new[2][2] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen2', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen (spalten)
    elif karte_new[0][0] == "x" and karte_new[1][0] == "x" and karte_new[2][0] == "x" or karte_new[0][1] == "x" and \
            karte_new[1][1] == "x" and karte_new[2][1] == "x" or karte_new[0][2] == "x" and karte_new[1][2] == "x" and \
            karte_new[2][2] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen3', 'green', attrs=['reverse', 'blink'])

    else:
        cprint('\nSie haben leider nicht gewonnen :/ \n vielleicht beim nächsten Mal :)', 'red',
               attrs=['reverse', 'blink'])

# der obige vorgang wiederholt sich in den kommenden Schritten für die Bingokarten der größe 4x4, 5x5, 6x6 und 7x7
elif laenge_breite == 4:
    x4 = PrettyTable()
    x4.field_names = ["4x4", "0", "1", "2", "3"]
    x4.add_row(["0", karte_new[0][0], karte_new[0][1], karte_new[0][2], karte_new[0][3]])
    x4.add_row(["1", karte_new[1][0], karte_new[1][1], karte_new[1][2], karte_new[1][3]])
    x4.add_row(["2", karte_new[2][0], karte_new[2][1], karte_new[2][2], karte_new[2][3]])
    x4.add_row(["3", karte_new[3][0], karte_new[3][1], karte_new[3][2], karte_new[3][3]])
    print(x4)
    cprint('--------------------', 'yellow')
    for element in range(felderAnzahl):
        print("Das gezogene Wort ist: " + colored(winnerWords[element], 'cyan'))
        antwortBenutzer = input("Steht das gezogene Wort in auf ihrem Bingofeld? (Mit Ja/Nein/Enter Taste antworten): ")
        cprint('--------------------', 'yellow')
        if antwortBenutzer == "Ja" or antwortBenutzer == "ja":
            xkoordinate = int(input("Bitte geben Sie die X Kooridnate an, damit das Wort markiert werden kann: "))  #
            ykoordinate = int(input("Bitte geben Sie die Y Koordinate an, damit das Wort markiert werden kann: "))  #
            cprint('--------------------', 'yellow')
            print(colored(karte_new[ykoordinate][xkoordinate], 'red'))
            karte_new[ykoordinate][xkoordinate] = "x"
            cprint('--------------------', 'yellow')
            z4 = PrettyTable()
            z4.field_names = ["4x4", "0", "1", "2", "3"]
            z4.add_row(["0", karte_new[0][0], karte_new[0][1], karte_new[0][2], karte_new[0][3]])
            z4.add_row(["1", karte_new[1][0], karte_new[1][1], karte_new[1][2], karte_new[1][3]])
            z4.add_row(["2", karte_new[2][0], karte_new[2][1], karte_new[2][2], karte_new[2][3]])
            z4.add_row(["3", karte_new[3][0], karte_new[3][1], karte_new[3][2], karte_new[3][3]])
            print(z4)
            cprint('--------------------', 'yellow')

        elif antwortBenutzer == "Nein" or antwortBenutzer == "nein" or antwortBenutzer == "":
            print("Kein Feld wurde markiert")
            cprint('--------------------', 'yellow')

        else:
            print("Eingabe war nicht Korrekt. Das Spiel wird fortgesetzt...")
            cprint('--------------------', 'yellow')

    # Abfrage kreuz
    if karte_new[0][0] == "x" and karte_new[1][1] == "x" and karte_new[2][2] == "x" and karte_new[3][3] == "x" or \
            karte_new[0][3] == "x" and karte_new[1][2] == "x" and karte_new[2][1] == "x" and karte_new[3][0] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen
    elif karte_new[0][0] == "x" and karte_new[0][1] == "x" and karte_new[0][2] == "x" and karte_new[0][3] == "x" or \
            karte_new[1][0] == "x" and karte_new[1][1] == "x" and karte_new[1][2] == "x" and karte_new[1][3] == "x" or \
            karte_new[2][0] == "x" and karte_new[2][1] == "x" and karte_new[2][2] == "x" and karte_new[2][3] == "x" or \
            karte_new[3][0] == "x" and karte_new[3][1] == "x" and karte_new[3][2] == "x" and karte_new[3][3] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen
    elif karte_new[0][0] == "x" and karte_new[1][0] == "x" and karte_new[2][0] == "x" and karte_new[3][0] == "x" or \
            karte_new[0][1] == "x" and karte_new[1][1] == "x" and karte_new[2][1] == "x" and karte_new[3][1] == "x" or \
            karte_new[0][2] == "x" and karte_new[1][2] == "x" and karte_new[2][2] == "x" and karte_new[3][2] == "x" or \
            karte_new[0][3] == "x" and karte_new[1][3] == "x" and karte_new[2][3] == "x" and karte_new[3][3] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

    else:
        cprint('\nSie haben leider nicht gewonnen :/ \n vielleicht beim nächsten Mal :)', 'red',
               attrs=['reverse', 'blink'])

elif laenge_breite == 5:
    x5 = PrettyTable()
    x5.field_names = ["5x5", "0", "1", "2", "3", "4"]
    x5.add_row(["0", karte_new[0][0], karte_new[0][1], karte_new[0][2], karte_new[0][3], karte_new[0][4]])
    x5.add_row(["1", karte_new[1][0], karte_new[1][1], karte_new[1][2], karte_new[1][3], karte_new[2][4]])
    x5.add_row(["2", karte_new[2][0], karte_new[2][1], karte_new[2][2], karte_new[2][3], karte_new[2][4]])
    x5.add_row(["3", karte_new[3][0], karte_new[3][1], karte_new[3][2], karte_new[3][3], karte_new[3][4]])
    x5.add_row(["4", karte_new[4][0], karte_new[4][1], karte_new[4][2], karte_new[4][3], karte_new[4][4]])
    print(x5)
    cprint('--------------------', 'yellow')

    for element in range(felderAnzahl):
        print("Das gezogene Wort ist: " + colored(winnerWords[element], 'cyan'))
        antwortBenutzer = input("Steht das gezogene Wort in auf ihrem Bingofeld? (Mit Ja/Nein/Enter Taste antworten): ")
        cprint('--------------------', 'yellow')
        if antwortBenutzer == "Ja" or antwortBenutzer == "ja":
            xkoordinate = int(input("Bitte geben Sie die X Kooridnate an, damit das Wort markiert werden kann: "))  #
            ykoordinate = int(input("Bitte geben Sie die Y Koordinate an, damit das Wort markiert werden kann: "))  #
            cprint('--------------------', 'yellow')
            print(colored(karte_new[ykoordinate][xkoordinate], 'red'))
            karte_new[ykoordinate][xkoordinate] = "x"
            cprint('--------------------', 'yellow')
            z5 = PrettyTable()
            z5.field_names = ["5x5", "0", "1", "2", "3", "4"]
            z5.add_row(["0", karte_new[0][0], karte_new[0][1], karte_new[0][2], karte_new[0][3], karte_new[0][4]])
            z5.add_row(["1", karte_new[1][0], karte_new[1][1], karte_new[1][2], karte_new[1][3], karte_new[1][4]])
            z5.add_row(["2", karte_new[2][0], karte_new[2][1], karte_new[2][2], karte_new[2][3], karte_new[2][4]])
            z5.add_row(["3", karte_new[3][0], karte_new[3][1], karte_new[3][2], karte_new[3][3], karte_new[3][4]])
            z5.add_row(["4", karte_new[4][0], karte_new[4][1], karte_new[4][2], karte_new[4][3], karte_new[4][4]])
            print(z5)
            cprint('--------------------', 'yellow')

        elif antwortBenutzer == "Nein" or antwortBenutzer == "nein" or antwortBenutzer == "":
            print("Kein Feld wurde markiert")
            cprint('--------------------', 'yellow')

        else:
            print("Eingabe war nicht Korrekt. Das Spiel wird fortgesetzt...")
            cprint('--------------------', 'yellow')

    # Abfrage kreuz
    if karte_new[0][0] == "x" and karte_new[1][1] == "x" and karte_new[2][2] == "x" and karte_new[3][3] == "x" and \
            karte_new[4][4] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

    elif karte_new[0][4] == "x" and karte_new[1][3] == "x" and karte_new[2][2] == "x" and karte_new[3][1] == "x" and \
            karte_new[4][0] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen
    elif karte_new[0][0] == "x" and karte_new[0][1] == "x" and karte_new[0][2] == "x" and karte_new[0][3] == "x" and \
            karte_new[0][4] == "x" or karte_new[1][0] == "x" and karte_new[1][1] == "x" and karte_new[1][2] == "x" and \
            karte_new[1][3] == "x" and karte_new[1][4] == "x" or karte_new[2][0] == "x" and karte_new[2][1] == "x" and \
            karte_new[2][2] == "x" and karte_new[2][3] == "x" and karte_new[2][4] == "x" or karte_new[3][0] == "x" and \
            karte_new[3][1] == "x" and karte_new[3][2] == "x" and karte_new[3][3] == "x" and karte_new[3][4] == "x" or \
            karte_new[4][0] == "x" and karte_new[4][1] == "x" and karte_new[4][2] == "x" and karte_new[4][3] == "x" and \
            karte_new[4][4] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen
    elif karte_new[0][0] == "x" and karte_new[1][0] == "x" and karte_new[2][0] == "x" and karte_new[3][0] == "x" and \
            karte_new[4][0] == "x" or karte_new[0][1] == "x" and karte_new[1][1] == "x" and karte_new[2][1] == "x" and \
            karte_new[3][1] == "x" and karte_new[4][1] == "x" or karte_new[0][2] == "x" and karte_new[1][2] == "x" and \
            karte_new[2][2] == "x" and karte_new[3][2] == "x" and karte_new[4][2] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])
    # Abfrage y reihe 2.0
    elif karte_new[0][3] == "x" and karte_new[1][3] == "x" and karte_new[2][3] == "x" and karte_new[3][3] == "x" and \
            karte_new[4][3] == "x" or karte_new[0][4] == "x" and karte_new[1][4] == "x" and karte_new[2][4] == "x" and \
            karte_new[3][4] == "x" and karte_new[4][4] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])
    else:
        cprint('\nSie haben leider nicht gewonnen :/ \n vielleicht beim nächsten Mal :)', 'red',
               attrs=['reverse', 'blink'])

elif laenge_breite == 6:
    x6 = PrettyTable()
    x6.field_names = ["6x6", "0", "1", "2", "3", "4", "5"]
    x6.add_row(
        ["0", karte_new[0][0], karte_new[0][1], karte_new[0][2], karte_new[0][3], karte_new[0][4], karte_new[0][5]])
    x6.add_row(
        ["1", karte_new[1][0], karte_new[1][1], karte_new[1][2], karte_new[1][3], karte_new[1][4], karte_new[1][5]])
    x6.add_row(
        ["2", karte_new[2][0], karte_new[2][1], karte_new[2][2], karte_new[2][3], karte_new[2][4], karte_new[2][5]])
    x6.add_row(
        ["3", karte_new[3][0], karte_new[3][1], karte_new[3][2], karte_new[3][3], karte_new[3][4], karte_new[3][5]])
    x6.add_row(
        ["4", karte_new[4][0], karte_new[4][1], karte_new[4][2], karte_new[4][3], karte_new[4][4], karte_new[4][5]])
    x6.add_row(
        ["5", karte_new[5][0], karte_new[5][1], karte_new[5][2], karte_new[5][3], karte_new[5][4], karte_new[5][5]])
    print(x6)
    cprint('--------------------', 'yellow')

    for element in range(felderAnzahl):
        print("Das gezogene Wort ist: " + colored(winnerWords[element], 'green'))
        antwortBenutzer = input("Steht das gezogene Wort in auf ihrem Bingofeld? (Mit Ja/Nein/Enter Taste antworten): ")
        cprint('--------------------', 'yellow')
        if antwortBenutzer == "Ja" or antwortBenutzer == "ja":
            xkoordinate = int(input("Bitte geben Sie die X Kooridnate an, damit das Wort markiert werden kann: "))  #
            ykoordinate = int(input("Bitte geben Sie die Y Koordinate an, damit das Wort markiert werden kann: "))  #
            cprint('--------------------', 'yellow')
            print(colored(karte_new[ykoordinate][xkoordinate], 'red'))
            karte_new[ykoordinate][xkoordinate] = "x"
            cprint('--------------------', 'yellow')
            z6 = PrettyTable()
            z6.field_names = ["6x6", "0", "1", "2", "3", "4", "5"]
            z6.add_row(["0", karte_new[0][0], karte_new[0][1], karte_new[0][2], karte_new[0][3], karte_new[0][4],
                        karte_new[0][5]])
            z6.add_row(["1", karte_new[1][0], karte_new[1][1], karte_new[1][2], karte_new[1][3], karte_new[1][4],
                        karte_new[1][5]])
            z6.add_row(["2", karte_new[2][0], karte_new[2][1], karte_new[2][2], karte_new[2][3], karte_new[2][4],
                        karte_new[2][5]])
            z6.add_row(["3", karte_new[3][0], karte_new[3][1], karte_new[3][2], karte_new[3][3], karte_new[3][4],
                        karte_new[3][5]])
            z6.add_row(["4", karte_new[4][0], karte_new[4][1], karte_new[4][2], karte_new[4][3], karte_new[4][4],
                        karte_new[4][5]])
            z6.add_row(["5", karte_new[5][0], karte_new[5][1], karte_new[5][2], karte_new[5][3], karte_new[5][4],
                        karte_new[5][5]])
            print(z6)
            cprint('--------------------', 'yellow')

        elif antwortBenutzer == "Nein" or antwortBenutzer == "nein" or antwortBenutzer == "":
            print("Kein Feld wurde markiert")
            cprint('--------------------', 'yellow')

        else:
            print("Eingabe war nicht Korrekt. Das Spiel wird fortgesetzt...")
            cprint('--------------------', 'yellow')

    # Abfrage kreuz
    if karte_new[0][0] == "x" and karte_new[1][1] == "x" and karte_new[2][2] == "x" and karte_new[3][3] == "x" and \
            karte_new[4][4] == "x" and karte_new[5][5] == "x" or karte_new[0][5] == "x" and karte_new[1][4] == "x" and \
            karte_new[2][3] == "x" and karte_new[3][2] == "x" and karte_new[4][1] == "x" and karte_new[5][0] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen /zeilen
    elif karte_new[0][0] == "x" and karte_new[0][1] == "x" and karte_new[0][2] == "x" and karte_new[0][3] == "x" and \
            karte_new[0][4] == "x" and karte_new[0][5] == "x" or karte_new[1][0] == "x" and karte_new[1][1] == "x" and \
            karte_new[1][2] == "x" and karte_new[1][3] == "x" and karte_new[1][4] == "x" and karte_new[1][5] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen 2.0 /zeilen
    elif karte_new[2][0] == "x" and karte_new[2][1] == "x" and karte_new[2][2] == "x" and karte_new[2][3] == "x" and \
            karte_new[2][4] == "x" and karte_new[2][5] == "x" or karte_new[3][0] == "x" and karte_new[3][1] == "x" and \
            karte_new[3][2] == "x" and karte_new[3][3] == "x" and karte_new[3][4] == "x" and karte_new[3][5] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen 3.0 /zeilen
    elif karte_new[4][0] == "x" and karte_new[4][1] == "x" and karte_new[4][2] == "x" and karte_new[4][3] == "x" and \
            karte_new[4][4] == "x" and karte_new[4][5] == "x" or karte_new[5][0] == "x" and karte_new[5][1] == "x" and \
            karte_new[5][2] == "x" and karte_new[5][3] == "x" and karte_new[5][4] == "x" and karte_new[5][5] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen /spalten
    elif karte_new[0][0] == "x" and karte_new[1][0] == "x" and karte_new[2][0] == "x" and karte_new[3][0] == "x" and \
            karte_new[4][0] == "x" and karte_new[5][0] == "x" or karte_new[0][1] == "x" and karte_new[1][1] == "x" and \
            karte_new[2][1] == "x" and karte_new[3][1] == "x" and karte_new[4][1] == "x" and karte_new[5][1] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen 2.0 /spalten
    elif karte_new[0][2] == "x" and karte_new[1][2] == "x" and karte_new[2][2] == "x" and karte_new[3][2] == "x" and \
            karte_new[4][2] == "x" and karte_new[5][2] == "x" or karte_new[0][3] == "x" and karte_new[1][3] == "x" and \
            karte_new[2][3] == "x" and karte_new[3][3] == "x" and karte_new[4][3] == "x" and karte_new[5][3] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen 3.0 /spalten
    elif karte_new[0][4] == "x" and karte_new[1][4] == "x" and karte_new[2][4] == "x" and karte_new[3][4] == "x" and \
            karte_new[4][4] == "x" and karte_new[5][4] == "x" or karte_new[0][5] == "x" and karte_new[1][5] == "x" and \
            karte_new[2][5] == "x" and karte_new[3][5] == "x" and karte_new[4][5] == "x" and karte_new[5][5] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

    else:
        cprint('\nSie haben leider nicht gewonnen :/ \n vielleicht beim nächsten Mal :)', 'red',
               attrs=['reverse', 'blink'])
elif laenge_breite == 7:
    x7 = PrettyTable()
    x7.field_names = ["7x7", "0", "1", "2", "3", "4", "5", "6"]
    x7.add_row(
        ["0", karte_new[0][0], karte_new[0][1], karte_new[0][2], karte_new[0][3], karte_new[0][4], karte_new[0][5],
         karte_new[0][6]])
    x7.add_row(
        ["1", karte_new[1][0], karte_new[1][1], karte_new[1][2], karte_new[1][3], karte_new[1][4], karte_new[1][5],
         karte_new[1][6]])
    x7.add_row(
        ["2", karte_new[2][0], karte_new[2][1], karte_new[2][2], karte_new[2][3], karte_new[2][4], karte_new[2][5],
         karte_new[2][6]])
    x7.add_row(
        ["3", karte_new[3][0], karte_new[3][1], karte_new[3][2], karte_new[3][3], karte_new[3][4], karte_new[3][5],
         karte_new[3][6]])
    x7.add_row(
        ["4", karte_new[4][0], karte_new[4][1], karte_new[4][2], karte_new[4][3], karte_new[4][4], karte_new[4][5],
         karte_new[4][6]])
    x7.add_row(
        ["5", karte_new[5][0], karte_new[5][1], karte_new[5][2], karte_new[5][3], karte_new[5][4], karte_new[5][5],
         karte_new[5][6]])
    x7.add_row(
        ["6", karte_new[6][0], karte_new[6][1], karte_new[6][2], karte_new[6][3], karte_new[6][4], karte_new[6][5],
         karte_new[6][6]])
    print(x7)
    cprint('--------------------', 'yellow')

    for element in range(felderAnzahl):
        print("Das gezogene Wort ist: " + colored(winnerWords[element], 'cyan'))
        antwortBenutzer = input("Steht das gezogene Wort in auf ihrem Bingofeld? (Mit Ja/Nein/Enter Taste antworten): ")
        cprint('--------------------', 'yellow')
        if antwortBenutzer == "Ja" or antwortBenutzer == "ja":
            xkoordinate = int(input("Bitte geben Sie die X Kooridnate an, damit das Wort markiert werden kann: "))  #
            ykoordinate = int(input("Bitte geben Sie die Y Koordinate an, damit das Wort markiert werden kann: "))  #
            cprint('--------------------', 'yellow')
            print(colored(karte_new[ykoordinate][xkoordinate], 'red'))
            karte_new[ykoordinate][xkoordinate] = "x"
            z7 = PrettyTable()
            z7.field_names = ["7x7", "0", "1", "2", "3", "4", "5", "6"]
            z7.add_row(["0", karte_new[0][0], karte_new[0][1], karte_new[0][2], karte_new[0][3], karte_new[0][4],
                        karte_new[0][5], karte_new[0][6]])
            z7.add_row(["1", karte_new[1][0], karte_new[1][1], karte_new[1][2], karte_new[1][3], karte_new[1][4],
                        karte_new[1][5], karte_new[1][6]])
            z7.add_row(["2", karte_new[2][0], karte_new[2][1], karte_new[2][2], karte_new[2][3], karte_new[2][4],
                        karte_new[2][5], karte_new[2][6]])
            z7.add_row(["3", karte_new[3][0], karte_new[3][1], karte_new[3][2], karte_new[3][3], karte_new[3][4],
                        karte_new[3][5], karte_new[3][6]])
            z7.add_row(["4", karte_new[4][0], karte_new[4][1], karte_new[4][2], karte_new[4][3], karte_new[4][4],
                        karte_new[4][5], karte_new[4][6]])
            z7.add_row(["5", karte_new[5][0], karte_new[5][1], karte_new[5][2], karte_new[5][3], karte_new[5][4],
                        karte_new[5][5], karte_new[5][6]])
            z7.add_row(["6", karte_new[6][0], karte_new[6][1], karte_new[6][2], karte_new[6][3], karte_new[6][4],
                        karte_new[6][5], karte_new[6][6]])
            print(z7)
            cprint('--------------------', 'yellow')

        elif antwortBenutzer == "Nein" or antwortBenutzer == "nein" or antwortBenutzer == "":
            print("Kein Feld wurde markiert")
            cprint('--------------------', 'yellow')

        else:
            print("Eingabe war nicht Korrekt. Das Spiel wird fortgesetzt...")
            cprint('--------------------', 'yellow')

    # Abfrage kreuz
    if karte_new[0][0] == "x" and karte_new[1][1] == "x" and karte_new[2][2] == "x" and karte_new[3][3] == "x" and \
            karte_new[4][4] == "x" and karte_new[5][5] == "x" and karte_new[6][6] == "x" or karte_new[0][6] == "x" and \
            karte_new[1][5] == "x" and karte_new[2][4] == "x" and karte_new[3][3] == "x" and karte_new[4][2] == "x" and \
            karte_new[5][1] == "x" and karte_new[6][0] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen /zeilen
    elif karte_new[0][0] == "x" and karte_new[0][1] == "x" and karte_new[0][2] == "x" and karte_new[0][3] == "x" and \
            karte_new[0][4] == "x" and karte_new[0][5] == "x" and karte_new[0][6] == "x" or karte_new[1][0] == "x" and \
            karte_new[1][1] == "x" and karte_new[1][2] == "x" and karte_new[1][3] == "x" and karte_new[1][4] == "x" and \
            karte_new[1][5] == "x" and karte_new[1][6] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen 2.0 /zeilen
    elif karte_new[2][0] == "x" and karte_new[2][1] == "x" and karte_new[2][2] == "x" and karte_new[2][3] == "x" and \
            karte_new[2][4] == "x" and karte_new[2][5] == "x" and karte_new[2][6] == "x" or karte_new[3][0] == "x" and \
            karte_new[3][1] == "x" and karte_new[3][2] == "x" and karte_new[3][3] == "JOKER" and karte_new[3][
        4] == "x" and karte_new[3][5] == "x" and karte_new[3][6] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen 3.0 /zeilen
    elif karte_new[4][0] == "x" and karte_new[4][1] == "x" and karte_new[4][2] == "x" and karte_new[4][3] == "x" and \
            karte_new[4][4] == "x" and karte_new[4][5] == "x" and karte_new[4][6] == "x" or karte_new[5][0] == "x" and \
            karte_new[5][1] == "x" and karte_new[5][2] == "x" and karte_new[5][3] == "x" and karte_new[5][4] == "x" and \
            karte_new[5][5] == "x" and karte_new[5][6] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage x reihen 4.0 /zeilen
    elif karte_new[6][0] == "x" and karte_new[6][1] == "x" and karte_new[6][2] == "x" and karte_new[6][3] == "x" and \
            karte_new[6][4] == "x" and karte_new[6][5] == "x" and karte_new[6][6] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen /spalten
    elif karte_new[0][0] == "x" and karte_new[1][0] == "x" and karte_new[2][0] == "x" and karte_new[3][0] == "x" and \
            karte_new[4][0] == "x" and karte_new[5][0] == "x" and karte_new[6][0] == "x" or karte_new[0][1] == "x" and \
            karte_new[1][1] == "x" and karte_new[2][1] == "x" and karte_new[3][1] == "x" and karte_new[4][1] == "x" and \
            karte_new[5][1] == "x" and karte_new[6][1] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen 2.0 /spalten
    elif karte_new[0][2] == "x" and karte_new[1][2] == "x" and karte_new[2][2] == "x" and karte_new[3][2] == "x" and \
            karte_new[4][2] == "x" and karte_new[5][2] == "x" and karte_new[6][2] == "x" or karte_new[0][3] == "x" and \
            karte_new[1][3] == "x" and karte_new[2][3] == "x" and karte_new[3][3] == "x" and karte_new[4][3] == "x" and \
            karte_new[5][3] == "x" and karte_new[6][3] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen 3.0 /spalten
    elif karte_new[0][4] == "x" and karte_new[1][4] == "x" and karte_new[2][4] == "x" and karte_new[3][4] == "x" and \
            karte_new[4][4] == "x" and karte_new[5][4] == "x" and karte_new[6][4] == "x" or karte_new[0][5] == "x" and \
            karte_new[1][5] == "x" and karte_new[2][5] == "x" and karte_new[3][5] == "x" and karte_new[4][5] == "x" and \
            karte_new[5][5] == "x" and karte_new[6][5] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])

        # Abfrage y reihen 4.0 /spalten
    elif karte_new[0][6] == "x" and karte_new[1][6] == "x" and karte_new[2][6] == "x" and karte_new[3][6] == "x" and \
            karte_new[4][6] == "x" and karte_new[5][6] == "x" and karte_new[6][6] == "x":
        cprint('\nHerzlichen Glückwunsch! \n Sie haben gewonnen', 'green', attrs=['reverse', 'blink'])
    else:
        cprint('\nSie haben leider nicht gewonnen :/ \n vielleicht beim nächsten Mal :)', 'red',
               attrs=['reverse', 'blink'])

else:
    print(
        "Es besteht nur die Möglichkeit mit Bingokarten der größe 3x3, 4x4, 5x5, 6x6 und 7x7 zu spielen.\nStarten Sie das Spiel neu, um eine neue Auswahl zu treffen.")
