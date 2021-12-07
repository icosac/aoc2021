#!/usr/bin/env python3
import os

DIR_MAIN_FILE = os.path.dirname(os.path.abspath(__file__))
FILE_PUZZLE_INPUT = os.path.join(DIR_MAIN_FILE,'input.txt')


def open_puzzle_input():
    puzzle_input = open(FILE_PUZZLE_INPUT)
    return puzzle_input

def get_random_numbers(puzzle_input: object):
    random_numbers = puzzle_input.readline()
    return list(random_numbers)


def create_list(string_in: str):
    return [f for f in string_in]

def get_arr_len(arr: list):
    arr_len = 0
    for _ in arr:
        arr_len += 1
    return arr_len


def get_bingo_board_rows(puzzle_input: object):

    bingo_boards = { 0: [], 1: [] } # 0 = ignore, 1 = keep
    line = puzzle_input.readline()
    while get_arr_len(line) > 0:
        line = create_list(line)
        res = ( get_arr_len(line) > 2 )
        bingo_boards[res].append(create_list(line))
        line = puzzle_input.readline()

    return bingo_boards[1]


def extract_bingo_board_numbers(bingo_boards: list):
    total_arrays = get_arr_len(bingo_boards)
    new_bingo_boards = []
    index = 0
    while total_arrays > 0:
        cur_array = bingo_boards[index]
        index += 1
        total_arrays -= 1

        cur_array = remove_array_delimitter(cur_array, ' ')
        cur_array = one_dimesion_down_number_array(cur_array)
        new_bingo_boards.append(cur_array)

    return new_bingo_boards


def remove_array_delimitter(arr: list, delimitter: str):
    '''
        turns [
                ['4', '9', ',', '4', '8', ',', '9', '8']
              ]

        into  [
                ['4', '9'], ['4', '8'], ['9', '8']
              ]
        where delimitter = ","
    '''

    delimitter_count = 0
    is_delimitter = 0
    temp_number_register = { 0: [], 1: [], }
    key_register = { 0: [], 1: [], }
    arr_index = 0
    while ( arr_index + 1 ) < get_arr_len(arr):

        # store first character in the array
        arr_element = arr[arr_index]

        # if delimitter is found: is_delimitter = 1
        is_delimitter = 1 * ( arr_element == delimitter )

        # index based on how many delimitters we have counted
        delimitter_count += is_delimitter

        insert_dict = {delimitter_count:arr_element}
        temp_number_register[is_delimitter].append(insert_dict)
        key_register[is_delimitter].append(delimitter_count)

        arr_index += 1

    number_register_dict = {}
    key_register = key_register[0]
    arr = temp_number_register[0]

    # add designated key value that holds a list for each number
    for key in key_register:
        number_register_dict[key] = []

    # append each number as its own list into its correct key
    for dict in arr:
        for key in dict:
            # some keys are the same, this way we preserve the digits
            number_register_dict[key].append(dict[key])

    # finally push all the values into a 2 dimensional list
    final_list = []
    for key in number_register_dict:
        final_list.append(number_register_dict[key])

    return final_list


def one_dimesion_down_number_array(number_list: list):
    '''
        turns [
                [ ['1'], ['2'] ] , [ ['1'] ]
              ]

        into  [
                ['12'] , ['1']
              ]
    '''
    extracted_numbers = []
    iterator = 0
    while get_arr_len(number_list) > 0:
        current_number = number_list[iterator]
        index = 0
        n = ''
        while get_arr_len(current_number) > index:
            n += str(current_number[index])
            index += 1

        del number_list[0]
        extracted_numbers.append(n)

    return extracted_numbers


def organize_bingo_boards_into_keys(bingo_boards: list):
    bingo_board_register = {}
    board_dimension = get_arr_len(bingo_boards[0])
    row_count = get_arr_len(bingo_boards)

    row = 0
    columns = board_dimension
    column = 0
    board_number = 0
    board_count = int( row_count / board_dimension )
    while board_number < board_count:
        bingo_board_register[board_number] = []

        while columns > column:
            bingo_board_register[board_number].append(bingo_boards[row])
            column += 1
            row += 1

        board_number += 1
        columns = get_arr_len(bingo_boards[0])
        column = 0

    return bingo_board_register


def check_if_won(bool_board: list):
    board_dimension = get_arr_len(bool_board)
    won = 0
    row = 0
    res = 0
    has_won = { 0:0, 1:0 } # 1:1 = has won
    # for each row
    while row < board_dimension:
        vertical = 0
        horizontal = 0
        col = 0
        # for each column
        while col < board_dimension:
            vertical += bool_board[col][row]
            horizontal += bool_board[row][col]
            col += 1

        v = vertical == board_dimension
        h = horizontal == board_dimension
        res = or_bool_value(v, h)
        has_won[res] = res
        row += 1

    return has_won[1]


def sum_of_unmarked_numbers(bool_board: list, bingo_board: list):
    # we use the bool table to ignore numbers with 0 val
    # this would not have worked if we were to actually get the numbers
    # but since we only neew the sum, we can care less about ambiguous concerns
    board_dimension = get_arr_len(bingo_board)
    sum_unmarked = 0
    row = 0
    # for each row
    while row < board_dimension:
        col = 0
        # for each column
        while col < board_dimension:
            bool_val = bool_board[row][col]
            bingo_val = bingo_board[row][col]
            bool_val = binary_swap(bool_val)
            new_val = 1 * ( int(bingo_val) * int(bool_val) )
            sum_unmarked += int (new_val)

            col += 1
        row += 1
    return sum_unmarked


def get_strike_numbers(bool_board: list, bingo_board: list):

    strike_index = { 'col': {0:[], 1:[] }, 'row': {0:[], 1:[]}  }

    row = 0
    # for each row
    board_dimension = get_arr_len(bingo_board)
    while row < board_dimension:
        row_idx = []
        col_idx = []
        vertical = 0
        horizontal = 0
        col = 0
        # for each column
        while col < board_dimension:
            vertical += bool_board[col][row]
            horizontal += bool_board[row][col]
            row_idx.append(bingo_board[row][col])
            col_idx.append(bingo_board[col][row])
            col += 1

        vertical_found = vertical == board_dimension
        horizontal_found = horizontal == board_dimension
        strike_index['row'][horizontal_found] = row_idx
        strike_index['col'][vertical_found] = col_idx

        row += 1

    # only one will have values, the other will be empty
    strike_numbers = []
    for axis in strike_index:
        for number in strike_index[axis][1]:
            strike_numbers.append(number)

    return strike_numbers


def run_bingo_numbers(bingo_numbers: list, bingo_boards: list, win_cond):

    win_condition = { 'first': 1, 'last': 0 }

    # bool board to mark found numbers as 1 and not found numbers as 0
    bool_boards = {}

    # start with all numbers = 0 in the bool_board
    for board in bingo_boards:
        bool_boards[board] = []
        for row in bingo_boards[board]:
            l = []
            for _ in row:
                l.append(0)
            bool_boards[board].append(l)

    # read the first boards dimensions to get length / width
    board_dimension = get_arr_len(bingo_boards[0])

    # for iterationg boards
    board_numbers = get_arr_len(bingo_boards)

    # register boards that have won
    all_winners = {}
    board_number = 0
    while board_number < board_numbers:
        win_condition['last'] += 1
        all_winners[board_number] = { 0:0, 1:0 }
        board_number += 1

    win_condition_met = 0
    winner_board_number = None
    last_played_bingo_number = None
    bingo_num_length = get_arr_len(bingo_numbers)
    bingo_number_index = 0
    while bingo_number_index < bingo_num_length:
        current_bingo_number = bingo_numbers[bingo_number_index]
        last_played_bingo_number = current_bingo_number

        board_number = 0
        while board_number < board_numbers:

            row = 0
            while row < board_dimension:
                col = 0
                while col < board_dimension:

                    # this is where we compare the bingo numbers
                    player_number = bingo_boards[board_number][row][col]
                    current_match = player_number == current_bingo_number
                    old_match = bool_boards[board_number][row][col]
                    new_match = or_bool_value(old_match, current_match)
                    bool_boards[board_number][row][col] = new_match

                    col += 1
                row += 1

            # for each bingo number, check if we have a winner
            is_winner = check_if_won(bool_boards[board_number])
            all_winners[board_number][is_winner] = 1
            winner_board_number = board_number

            winners_found = 0
            for _k in all_winners:
                winners_found += all_winners[_k][1]

            win_condition_met = ( winners_found == win_condition[win_cond] )


            # end while loop by forcing 0 on board_numbers if winner
            board_numbers = ( board_numbers * binary_swap(win_condition_met) )
            board_number += 1

        # end while loop by forcing 0 on bingo_num_length if winner
        bingo_num_length = ( bingo_num_length * binary_swap(win_condition_met) )
        bingo_number_index += 1

    # extract winner board (bool and bingo)
    win_bool_board = bool_boards[winner_board_number]
    win_bingo_board = bingo_boards[winner_board_number]

    # we did not need to know the winner numbers, but i keep this here anyways
    strike_numbers = get_strike_numbers(win_bool_board, win_bingo_board)
    str_numbers = ''
    for n in strike_numbers:
        str_numbers += n + ','
    print('Winner row = ' + str_numbers)

    sum_umarked_num = sum_of_unmarked_numbers(win_bool_board, win_bingo_board)

    return ( int(sum_umarked_num) * int(last_played_bingo_number) )


def or_bool_value(bool_1, bool_2):
    a = ( 1 * ( int(bool_1) == 0 ) )
    b = ( 1 * ( int(bool_2) == 0 ) )
    return 1 - ( 1 * a ) * ( 1 * b )

def xor_bool_value(bool_1, bool_2):
    return ( 1 - ( int(bool_1) == int(bool_2) ) )

def and_bool_value(bool_1, bool_2):
    return ( int(bool_1) == 1 ) * ( int(bool_2) == 1 )

def binary_swap(binary):
    return ( 1 * (int(binary) == 0) )



if __name__ == '__main__':

    # fetch raw input data
    puzzle_input_file = open_puzzle_input()
    raw_bingo_numbers = get_random_numbers(puzzle_input_file)
    raw_bingo_boards = get_bingo_board_rows(puzzle_input_file)
    puzzle_input_file.close()

    # organize input data
    bingo_numbers = remove_array_delimitter(raw_bingo_numbers, ',')
    bingo_numbers = one_dimesion_down_number_array(bingo_numbers)
    raw_bingo_boards = extract_bingo_board_numbers(raw_bingo_boards)
    bingo_boards = organize_bingo_boards_into_keys(raw_bingo_boards)


    final_result = run_bingo_numbers(bingo_numbers, bingo_boards, 'first')
    print('Final score for first winner = '+ str(final_result))

    final_result = run_bingo_numbers(bingo_numbers, bingo_boards,'last')
    print('Final score for last winner = '+ str(final_result))
