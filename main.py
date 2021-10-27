import functions
import const_and_var
import sys
import time

functions.print_text_with_border(const_and_var.welcome_text)
print(const_and_var.rules)

while True:  # main program loop
    print('Aby samemu wybrać znak wpisz "O" (kółko) lub "X" (krzyżyk) i naciśnij enter')
    print('Jeśli chcesz wylosować znak którym zagrasz, nie wpisuj nic i naciśnij enter')
    board_copy = const_and_var.board.copy()  # creates copy of board for one game
    while True:  # loop until user choose proper sign
        decision_who_start = input()
        if decision_who_start.upper() in const_and_var.possible_starts:  # check if user give any of predefined signs
            break  # exit loop if chosen sign is correct
        else:
            print("Błędny znak. Wpisz wybór ponownie")
    computer_sign = functions.who_starts(decision_who_start)  # draws who starts or assign computer with opposite sign than user
    if computer_sign == 'X':
        print(f'Twój znak to "O". Rozpoczynasz grę!')
        functions.user_turn(board_copy, "O")  # first move if computer_sign == X, so user starts
    else:
        print(f'Twój znak to "X". Komputer rozpoczyna grę!')
        functions.computer_turn(board_copy, computer_sign)  # first move if computer_sign == O, so computer starts
    #  now the game is between functions in functions.py
    decision = input()
    if decision.upper() == "EXIT":
        sys.exit("Dziękuję za grę!")
    else:
        time.sleep(1)
        del board_copy
