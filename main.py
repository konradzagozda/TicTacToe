def make_board(players_choices):

    board = f'''
            ***7******8*****9***
            *     *      *     *
            *  {players_choices[7]}  *   {players_choices[8]}  *  {players_choices[9]}  *
            *     *      *     *
            ***4******5*****6***
            *     *      *     *
            *  {players_choices[4]}  *   {players_choices[5]}  *  {players_choices[6]}  *
            *     *      *     *
            ***1******2*****3***
            *     *      *     *
            *  {players_choices[1]}  *   {players_choices[2]}  *  {players_choices[3]}  *
            *     *      *     *
            ******************** 
'''
    return board


def change_sign(current_sign):
    if current_sign == 'X':
        next_sign = 'O'
    else:
        next_sign = 'X'
    return next_sign


def single_turn(current_sign, players_choices):

    print(f'Player "{current_sign}" make move now!')
    failed = False
    move = input(f'WHERE DO U WANT TO PLACE AN "{current_sign}"?(1-9)')
    if players_choices[int(move)] == ' ':
        players_choices[int(move)] = current_sign
    else:
        failed = True

    return players_choices, failed


def check_for_win(players_choices, current_sign):
    possible_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]
    # check if player 'X' won:
    for x in possible_wins:
            if players_choices[x[0]] == players_choices[x[1]] == players_choices[x[2]] == current_sign:
                return True
    return False


def play_again():
    if input('Do you want to play again? Y/N?').lower() == 'y':
        return True
    return False


def play_game():

    # Needed variables:
    blank_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    players_choices = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    turn_counter = 1
    current_sign = 'X'
    keep_playing = True

    winning_string = f'''
            ********************************************************************
            *                                                                  *
            *        CONGRATZ FOR PLAYER {current_sign}!!!! YOU HAVE WON THE GAME!          *
            *                                                                  *
            ********************************************************************
    
    '''

    # Logic of the game:

    print(make_board(players_choices))
    while keep_playing:
        print(f'TURN {turn_counter}')
        players_choices, failed = single_turn(current_sign, players_choices)
        print(make_board(players_choices))
        if failed:
            print('HEY ! This is already taken space! YOU CAN\'T CHEAT!')
            continue
        if check_for_win(players_choices, current_sign):
            print(winning_string)
            keep_playing = play_again()
            players_choices = blank_board
            turn_counter = 1
            print(make_board(players_choices))
        current_sign = change_sign(current_sign)
        turn_counter += 1
        if turn_counter == 10:
            print('DRAW')
            keep_playing = play_again()
            players_choices = blank_board
            turn_counter = 1
            print(make_board(players_choices))




play_game()