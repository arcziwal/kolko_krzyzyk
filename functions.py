import random
import time
import const_and_var


def print_text_with_border(text_to_border):  # just border any text with '='
    print('=' * len(text_to_border))
    print(text_to_border)
    print('=' * len(text_to_border))


def print_bar(how_long):  # just print some '='
    print("=" * how_long)


def who_starts(user_choice):
    possible_choices = ['X', 'O']
    if user_choice == '':  # chooses for user
        computer_sign = random.choice(possible_choices)
        return computer_sign
    elif str(user_choice.upper()) == 'X':  # if user entered "X"
        computer_sign = "O"
        return computer_sign
    elif str(user_choice.upper()) == "O":  # if user entered "O"
        computer_sign = "X"
        return computer_sign
    else:
        print("Błędny znak")
        return None  # return to main loop


def computer_turn(board, computer_sign):
    list_of_empty_fields = []  # will contain fields possible to choose
    for key, value in board.items():  # searching for empty fields
        if value == ' ':
            list_of_empty_fields.append(key)
    print("Trwa wykonywanie ruchu przez komputer...")
    time.sleep(0.5)
    computer_choice = random.choice(list_of_empty_fields)  # computer turn
    # TODO: implement simple AI to play smarter than just randomly pick empty fields
    board[computer_choice] = computer_sign  # assign computer turn to board
    print_board(board)
    result = find_winning(board, computer_sign)  # check if computer win
    if result:
        print("Komputer zwyciężył.\nNaciśnij enter aby zagrać ponownie.\nWpisz exit i wciśnij enter aby zakończyć grę.")
        return None  # return to main loop
    draw = draw_finder(board)  # check if any field is still empty
    if draw:
        print("Remis! \nNaciśnij enter aby zagrać ponownie.\nWpisz exit i naciśnij enter aby zakończyć grę.")
        return None  # return to main loop
    input("Naciśnij enter aby przejść do swojego ruchu")
    if computer_sign == "O":
        user_turn(board, "X")  # move to user's turn
    elif computer_sign == "X":
        user_turn(board, "O")  # move to user's turn


def print_board(board):  # just show board with actual moves
    print(f"{board['7']}|{board['8']}|{board['9']}")
    print('-+-+-')
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print('-+-+-')
    print(f"{board['1']}|{board['2']}|{board['3']}")


def user_turn(board, user_sign):
    list_of_empty_fields = []  # will contain fields with " "
    time.sleep(0.5)
    print("NUMERY PÓL NA PLANSZY:")
    print(const_and_var.board_scheme)  # print numbers scheme of board
    while True:  # loop until user choose empty field
        print(f"Podaj numer pola gdzie chcesz postawić {user_sign}")
        for key, value in board.items():
            if value == " ":
                list_of_empty_fields.append(key)  # add key (num of field) to list if field is empty
        user_choice = input()
        if user_choice in list_of_empty_fields:  # check if user choose empty field
            board[user_choice] = user_sign  # add user sign to chosen field
            print_board(board)  # prints board with user's move
            break  # move is correct so it's possible to exit the loop
        else:
            print(type(user_choice))
            if user_choice in const_and_var.possible_fields:  # check if user_choice is > 0 and < 10
                print("To pole jest już zajęte. Wybierz inne")
                continue
            else:  # if user give any other sign
                print("Błędna wartość. Wybierz ponownie")
                continue
    result = find_winning(board, user_sign)  # check if user win
    if result:
        print_text_with_border("Zwyciężyłeś!\nNaciśnij enter aby zagrać ponownie.\nWpisz exit i naciśnij enter aby zakończyć grę.")
        return None  # return to main loop
    draw = draw_finder(board)  # check if any fields are still empty
    if draw:
        print("Remis! \nNaciśnij enter aby zagrać ponownie.\nWpisz exit i naciśnij enter aby zakończyć grę.")
        return None  # return to main loop
    if user_sign == "O":
        computer_turn(board, "X")  # moves to computer turn
    elif user_sign == "X":
        computer_turn(board, "O")  # moves to computer turn


def find_winning(board, sign):
    fields_with_sign = []  # will keep nums of fields with users sign
    for key, value in board.items():  # loop to find fields with users sign
        if value == sign:
            fields_with_sign.append(key)  # adds nums of fields with particular sign to list
            for combination in const_and_var.winning_combinations.values():  # iterate through every combination...
                score_counter = 0  # to find how many fields in every combination are filled
                for number in combination:
                    if number not in fields_with_sign:
                        break  # if any number isn't in combination, switch to another one
                    else:
                        score_counter += 1  # if number is in combination, adds 1 to score
                if score_counter == 3:  # means that all 3 fields are filled with valid sign
                    return True
                else:
                    continue
    return False


def draw_finder(board):
    for value in board.values():
        if value == " ":  # if there is no " " on boards, means there's draw
            return False
    return True
