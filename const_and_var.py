welcome_text = "Witaj w grze w kółko i krzyżyk".upper()

possible_starts = ['X', 'O', '']

possible_fields = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

rules = '''
W tej grze gracze na zmianę wstawiają na podanej planszy kółko "O" lub krzyżyk "X".
Wygrywa osoba, która pierwsza zajmie 3 znajdujące się obok siebie pola.
Pola mogą być zajmowane w pionie, w poziomie lub po ukosie.
Jeżeli żadnemu z graczy nie uda się ustawić obok siebie 3 znaków będzie to oznaczało remis.
Aby wybrać pole w którym chcesz umieścić znak, wystarczy, że wybierzesz cyfrę 1-9 odpowiadającą danemu polu
Możesz wybrać, czy chcesz sam wybrać swój znak, czy wolisz losowanie.
POWODZENIA!
'''

board_scheme = '''
7|8|9
-+-+-
4|5|6
-+-+-
1|2|3
'''

board = {
    '7': ' ',
    '8': ' ',
    '9': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '1': ' ',
    '2': ' ',
    '3': ' ',
}

winning_combinations = {
    1: ['1', '2', '3'],
    2: ['4', '5', '6'],
    3: ['7', '8', '9'],
    4: ['1', '4', '7'],
    5: ['2', '5', '8'],
    6: ['3', '6', '9'],
    7: ['1', '5', '9'],
    8: ['3', '5', '7']
}
