from random import randint
Spiele = True
print('Geisterspiel')
while Spiele:
    du_bist_mutig = True
    Mut = 3
    score = 0
    Spiele = True
    falsch = True
    while du_bist_mutig:
        if Mut <= 0:
            du_bist_mutig = False
        geistertuer = randint(1, 3)
        print('Vor dir sind drei Türen')
        print('Hinter einer ist ein Geist')
        print('Welche Tür wirst du öffnen?')
        while True:
            try:
                tuer = input('1, 2 oder 3?')
                tuer_nummer = int(tuer)
                break
            except ValueError:
                print('Dies steht nicht zur Asuwahl')
                print('Versuche es nochmal')
        if tuer_nummer == geistertuer:
            print('Geist!!!')
            print('sei beim nächsten Mal vorsichtiger')
            Mut = Mut - 1
            print(Mut)
        elif tuer_nummer != geistertuer and (tuer_nummer > 3 or tuer_nummer < 1):
            print('Die Zahl: ', tuer, ' steht nicht zur Auswahl')
            print('Versuch es nocheinmal, ein bisschen Zeit bleibt noch.')

        else:
            print('Kein Geist!')
            print('du bist mutig')
            score = score + 1
            Mut = Mut + 0.5
            print(Mut)
    print('Lauf!!!')
    print('Spiel vorbei! Deine Punkte:', score)
    while falsch:
        Abfrage = input('möchtest du weiter spielen? (ja oder nein)')
        if Abfrage == 'ja':
            Spiele = True
            du_bist_mutig = True
            Mut = 3
            score = 0
            falsch = False
        elif Abfrage == 'nein':
            Spiele = False
            falsch = False
        else:
            falsch = True






