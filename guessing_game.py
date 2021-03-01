import random

def start_game():

    random_number = random.randint(1, 10)
    number_range = range(1, 11, 1) # Returns a range of 1 to 10.
    range_array = []
    guesses = 0
    high_score = 0 # The 'high score' counter that will be overwritten at the end of the game

    for index in number_range:
        range_array.append(index)

    print('\n******THE NUMBER GUESSING GAME******\r')
    players_choice = input('PICK A NUMBER FROM 1 TO 10 (INCL. 1 AND 10): ')

    while True:
        try:
            if int(players_choice) in range_array:
                while players_choice != random_number:
                    if int(players_choice) < random_number:
                        guesses += 1
                        players_choice = input('HIGHER. Try again. ')
                    elif int(players_choice) > random_number:
                        guesses += 1
                        players_choice = input('LOWER. Try again. ')
                    else:
                        guesses+= 1
                        print(f'ATTEMPT(S): {guesses}.')
                        if high_score == 0 or guesses < high_score:
                            high_score = guesses
                            guesses = 0
                            print(f'NEW HIGH SCORE: {high_score}')
                        players_choice = input('CORRECT!! Would you like to play again? (YES/NO): ')
                        if players_choice.upper() == 'YES' or players_choice.upper() == 'Y':
                            random_number = random.randint(1, 10)
                            print(f'CURRENT HIGH SCORE: {high_score}')
                            players_choice = input('PICK A NUMBER FROM 1 TO 10 (INCL. 1 AND 10): ')
                        elif players_choice.upper() == 'NO' or players_choice.upper() == 'N':
                            return print('\nThank you for playing. Goodbye.\n')
            else:
                players_choice = input("SELECTION OUT OF RANGE. Please try again: ")
        except ValueError:
            players_choice = input('\nINVALUD ENTRY. Please try again: ')


# Kick off the program by calling the start_game function.
start_game()