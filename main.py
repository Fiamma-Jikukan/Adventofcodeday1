from os import remove

dial = 50


def read_file_to_list(filepath, strip_newlines=True):
    """
    Reads a text file line by line and returns a list of strings.

    Args:
        filepath (str): The path to the file to read.
        strip_newlines (bool): If True, removes trailing newline characters
                               from each line. Defaults to True.

    Returns:
        list: A list where each element is a line from the file.
        None: Returns None if the file is not found or an error occurs.
    """
    try:
        # 'r' mode is for reading. encoding='utf-8' is good practice.
        with open(filepath, 'r', encoding='utf-8') as file:
            if strip_newlines:
                # strip() removes leading/trailing whitespace including \n
                # rstrip('\n') would remove only trailing newlines if preferred
                lines = [line.strip() for line in file]
            else:
                # readlines() keeps the \n characters
                lines = file.readlines()
        return lines

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def read_ranges_to_list(filepath):
    """
    Reads a text file containing comma-separated ranges and returns a list of range strings.

    Example file content: "1-14,46452718-46482242,16-35"
    Returns: ['1-14', '46452718-46482242', '16-35']

    Args:
        filepath (str): The path to the file to read.

    Returns:
        list: A list where each element is a range string from the file.
        None: Returns None if the file is not found or an error occurs.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            # Read the entire content of the file
            content = file.read()

            # Remove any potential whitespace (like newlines at the end)
            # and split by comma
            ranges = [item.strip() for item in content.split(',') if item.strip()]

        return ranges

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def rotate(rotation, curr_dial):
    rotation_num = int(rotation[1:])
    num_of_clicks = 0

    if rotation[0] == 'R':
        curr_dial += rotation_num
        while curr_dial > 99:
            num_of_clicks += 1
            print("click")
            curr_dial -= 100

    if rotation[0] == 'L':
        for ding in range(rotation_num):
            if curr_dial == 0:
                curr_dial += 99
            curr_dial -= 1
            if curr_dial == 0:
                num_of_clicks += 1
                print("click")

    return curr_dial, num_of_clicks


def find_top_and_bottom(range_IDs):
    dash_index = 0
    for i in range(len(range_IDs)):
        if range_IDs[i] == '-':
            dash_index = i
    bottom_range = range_IDs[:dash_index]
    top_range = range_IDs[dash_index + 1:]
    return int(bottom_range), int(top_range)


def is_valid_id_old(id):
    id_str = str(id)
    if len(id_str) % 2 != 0:
        return True
    half_point = int(len(id_str) / 2)
    for i in range(half_point):
        if id_str[i] != id_str[half_point + i]:
            return True
    return False


def divide_str(str, num):
    # print("from divided str num: ", num)

    divided_str = []
    index = 0
    while index < len(str):
        divided_str.append(str[index: index + num])
        index += num
    # print("from divided str: ", divided_str)
    return divided_str


def is_valid_id(id):
    id_str = str(id)
    # print("this is the id to divide:", id_str)
    num_of_digits = len(id_str)
    if num_of_digits == 1:
        return True
    for i in range(1, num_of_digits):
        if num_of_digits % i != 0:
            continue
        divided_i = divide_str(id_str, i)
        # print("divided number:", divided_i, "it's devided into:", i, "parts")
        num_of_divided_digits = len(divided_i)
        all_part_the_same_sum = 0
        for j in range(1, num_of_divided_digits):
            # print("all_part_the_same_sum:", all_part_the_same_sum)
            if divided_i[0] == divided_i[j]:
                # print("parts are the same!")
                all_part_the_same_sum += 1
        # print("all_part_the_same_sum after loop:", all_part_the_same_sum)

        if all_part_the_same_sum == num_of_divided_digits - 1:
            # print("All parts are the same!")
            return False
        all_part_the_same_sum = 0
    return True


def IDs_finder(range_IDs):
    top_and_bottom = find_top_and_bottom(range_IDs)
    top_range = top_and_bottom[1]
    bottom_range = top_and_bottom[0]
    invalid_ids = []
    for i in range(bottom_range, top_range + 1):
        valid_id = is_valid_id(i)
        if not valid_id:
            invalid_ids.append(i)
    print(invalid_ids)
    return invalid_ids


def find_index_of_largest_dig(arr):
    "find the possition of the largest digit in an array"
    index_of_arr = 0
    for i in range(len(arr)):
        if arr[i] > arr[index_of_arr]:
            index_of_arr = i
    return index_of_arr


def find_two_largest_batteries(bank):
    "get two largest numbers from a string of numbers"
    battaries_arr = divide_str(bank, 1)
    print(battaries_arr)
    # battaries_arr.sort()
    # print(battaries_arr)
    largest_index = find_index_of_largest_dig(battaries_arr)
    print(battaries_arr[largest_index], "largest index:", largest_index)
    second_largest_after_largest = battaries_arr[largest_index + 1:]
    print(second_largest_after_largest)

    if second_largest_after_largest == []:
        second_largest_index = find_index_of_largest_dig(battaries_arr[:largest_index])
        second_largest = battaries_arr[second_largest_index]
        return second_largest, battaries_arr[largest_index]

    after_largest_arr = battaries_arr[largest_index + 1:]
    second_largest_index = find_index_of_largest_dig(after_largest_arr)
    print("second largest index:", second_largest_index)
    second_largest = after_largest_arr[second_largest_index]
    return battaries_arr[largest_index], second_largest

    print(second_largest_after_largest, "\n")


def find_twelve_largest_batteries(bank):
    bank_arr = divide_str(bank, 1)

    # # find largest digit
    length = len(bank_arr)
    # bank_without_last_twelve = bank_arr[:length-12]
    # largest_before_twelve_index = find_index_of_largest_dig(bank_without_last_twelve)
    # largest_overall_index = find_index_of_largest_dig(bank_arr)
    #
    # # if largest is twelve before last, the largest is the final twelve
    # if bank_arr[largest_before_twelve_index] == bank_arr[-12]:
    #     return bank_arr[-12:]
    #
    # if largest_overall_index < length-12:
    #     without_tail = bank_arr[largest_overall_index:]
    #
    # if largest_overall_index > length-12:

    list_of_largest_combo_by_order = []
    for i in range(12, 0, -1):
        cut_last_i_min_one = bank_arr[:len(bank_arr) - i + 1]
        # print("from outside while loop cut_last_i_min_one:" , cut_last_i_min_one, "i:", i)
        largest_index_before_i = find_index_of_largest_dig(cut_last_i_min_one)

        if largest_index_before_i == len(cut_last_i_min_one) - 1:
            j = 0
            while len(list_of_largest_combo_by_order) != 12:
                cut_head = bank_arr[len(bank_arr) - i:]

                # print("from while loop j:", j)
                # print("from while loop length-j:", len(cut_last_i_min_one) - j)
                # print("from while loop new bank_arr:", bank_arr)
                # print("from while loop cut head:", cut_head)
                # print("from while loop what he appended until now:", list_of_largest_combo_by_order,"\n")
                list_of_largest_combo_by_order.append(cut_head[j])
                j += 1
            return list_of_largest_combo_by_order

        list_of_largest_combo_by_order.append(bank_arr[largest_index_before_i])
        bank_arr = bank_arr[largest_index_before_i + 1:]
        # print("from outside while loop what he appended until now:", list_of_largest_combo_by_order)
        # print("from outside while loop new bank_arr:", bank_arr, "\n")
    return list_of_largest_combo_by_order


def is_paper_accessible(matrix, i, j, rows, columns):
    sum_of_ajesent_papers = 0
    directions = []
    directions.append([i + 1, j])
    directions.append([i - 1, j])
    directions.append([i, j + 1])
    directions.append([i, j - 1])
    directions.append([i + 1, j + 1])
    directions.append([i - 1, j - 1])
    directions.append([i + 1, j - 1])
    directions.append([i - 1, j + 1])
    for d in range(8):
        if directions[d][0] < 0 or directions[d][1] < 0:
            continue
        if directions[d][0] >= rows or directions[d][1] >= columns:
            continue
        if matrix[directions[d][0]][directions[d][1]] == '@':
            sum_of_ajesent_papers += 1
    if sum_of_ajesent_papers < 4:
        # print(directions)
        return 1
    return 0


def find_out_how_many_papers_accessible(matrix_of_papers):
    num_of_rows = len(matrix_of_papers)
    num_of_columns = len(matrix_of_papers[0])
    coordinates_of_removable_papers = []
    accessible_papers_sum = 0
    for i in range(num_of_rows):
        for j in range(num_of_columns):
            if matrix_of_papers[i][j] == '.':
                continue
            is_accessible = is_paper_accessible(matrix_of_papers, i, j, num_of_rows, num_of_columns)
            if is_accessible == 1:
                accessible_papers_sum += is_accessible
                coordinates_of_removable_papers.append([i, j])
    return accessible_papers_sum, coordinates_of_removable_papers


def remove_papers(matrix_of_papers, removable_papers):
    for poss in range(len(removable_papers)):
        row = removable_papers[poss][0]
        column = removable_papers[poss][1]
        matrix_of_papers[row][column] = '.'

    return matrix_of_papers


def split_into_ingredients_ranges_and_ids(ingredients):
    place_of_split = 0
    for index in range(len(ingredients)):
        if ingredients[index] == '':
            place_of_split = index
            break
    ranges = ingredients[:place_of_split]
    ids = ingredients[place_of_split + 1:]
    return ranges, ids


def str_range_to_top_and_bottom(range_str):
    return range_str.split('-')


def is_id_in_range(id, range):
    top_bottom_str = str_range_to_top_and_bottom(range)
    bottom = int(top_bottom_str[0])
    top = int(top_bottom_str[1])
    id_int = int(id)
    if bottom <= id_int <= top:
        return True
    return False


def is_id_in_any_range(id, ranges):
    for range_str in ranges:
        if is_id_in_range(id, range_str):
            return True
    return False


def how_many_ids_are_fresh(ranges):
    top_bottom_str = str_range_to_top_and_bottom(ranges)
    bottom = int(top_bottom_str[0])
    top = int(top_bottom_str[1])
    return top - bottom + 1


def add_ids_to_list(list_of_fresh_ids, range_str):
    top_bottom_str = str_range_to_top_and_bottom(range_str)
    bottom = int(top_bottom_str[0])
    top = int(top_bottom_str[1])
    for num in range(bottom, top + 1):
        if num not in list_of_fresh_ids:
            list_of_fresh_ids.append(num)
    list_of_fresh_ids.sort()
    return list_of_fresh_ids


def convert_str_ranges_to_int_ranges(str_ranges):
    int_ranges = []
    for range_strings in str_ranges:
        top_bottom_str = str_range_to_top_and_bottom(range_strings)
        bottom = int(top_bottom_str[0])
        top = int(top_bottom_str[1])
        int_ranges.append([bottom, top])
    return int_ranges


def add_range_to_list(all_fresh_ranges, curr_range):
    bottom = curr_range[0]
    top = curr_range[1]
    if not all_fresh_ranges:
        bottom_top = [bottom, top]
        all_fresh_ranges.append(bottom_top)
        return all_fresh_ranges

    for i in range(len(all_fresh_ranges)):
        # case 1: entire range is within them
        if (all_fresh_ranges[i][0] <= bottom <= all_fresh_ranges[i][1]) and (
                all_fresh_ranges[i][0] <= top <= all_fresh_ranges[i][1]):
            return all_fresh_ranges

        # case 2: bottom is within an existing range, top is outside of it
        if all_fresh_ranges[i][0] <= bottom <= all_fresh_ranges[i][1]:
            all_fresh_ranges[i][1] = top
            return all_fresh_ranges

        # case 3: top is within range, bottom is outside
        if all_fresh_ranges[i][0] <= top <= all_fresh_ranges[i][1]:
            all_fresh_ranges[i][0] = bottom
            return all_fresh_ranges

    bottom_top = [bottom, top]
    all_fresh_ranges.append(bottom_top)
    return all_fresh_ranges


def sum_lines_form_worksheet(full_worksheet):
    length_of_worksheet = len(full_worksheet[0])
    result = 0
    for i in range(length_of_worksheet):
        num1 = int(full_worksheet[0][i])
        num2 = int(full_worksheet[1][i])
        num3 = int(full_worksheet[2][i])
        num4 = int(full_worksheet[3][i])
        if full_worksheet[-1][i] == '+':
            result += (num1 + num2 + num3 + num4)

        if full_worksheet[-1][i] == '*':
            result += (num1 * num2 * num3 * num4)

    return result


def order_sheet_by_numbers(full_worksheet):
    length_of_worksheet = len(full_worksheet[0])
    how_many_lines = len(full_worksheet)
    result = []
    for i in range(length_of_worksheet):
        column = []
        for j in range(how_many_lines):
            print(full_worksheet[j][i])
            column.append(full_worksheet[j][i])
        print(column)
        result.append(column)
    return result


def create_operator_arr(operators_str):
    str_to_arr = operators_str.split(' ')
    result = [i for i in str_to_arr if i != '']
    return result


def calc_line_with_operator(worksheet_full, operator_list):
    ""
    print(worksheet_full)
    print(operator_list)
    operator_list_index = 0
    sum_of_each_line_by_index = []

    for i in range(len(worksheet_full[0])):
        num_list = []
        empty_counter = 0
        operator = ''
        if operator_list[operator_list_index] == '+':
            operator = '+'
        if operator_list[operator_list_index] == '*':
            operator = '*'

        for j in range(len(worksheet_full)):
            if worksheet_full[j][i] == ' ':
                empty_counter += 1
            else:
                num_list.append(worksheet_full[j][i])

        if empty_counter == len(worksheet_full):
            operator_list_index += 1
            continue
        print(num_list)
        num_to_int = int(''.join(num_list))
        print(num_to_int)
        if len(sum_of_each_line_by_index) <= operator_list_index:
            sum_of_each_line_by_index.append(num_to_int)
            continue
        # if len(sum_of_each_line_by_index) == 0:
        #     sum_of_each_line_by_index.append(num_to_int)
        #     continue
        if operator == '+':
            sum_of_each_line_by_index[operator_list_index] += int(num_to_int)
        if operator == '*':
            sum_of_each_line_by_index[operator_list_index] *= int(num_to_int)
    return sum_of_each_line_by_index


def teleporter_activate(teleporter_list):
    num_of_splits = 0
    for i in range(len(teleporter_list)):
        if i == 0:
            for j in range(len(teleporter_list[0])):
                if teleporter_list[0][j] == 'S':
                    teleporter_list[1][j] = '|'

        if i != len(teleporter_list) - 2:
            for j in range(len(teleporter_list[i])):
                if teleporter_list[i][j] == '|' and teleporter_list[i + 1][j] == '^':
                    # if teleporter_list[i + 1][j - 1] == '|':
                    #     num_of_splits -= 1
                    # if teleporter_list[i + 1][j + 1] == '|':
                    #     num_of_splits -= 1

                    teleporter_list[i + 1][j - 1] = '|'
                    teleporter_list[i + 1][j + 1] = '|'
                    num_of_splits += 2

                if teleporter_list[i][j] == '|' and teleporter_list[i + 1][j] == '.':
                    teleporter_list[i + 1][j] = '|'

        print(teleporter_list[i])

    return num_of_splits


if __name__ == '__main__':
    # rotations = read_file_to_list("input_rotations.txt")
    # num_of_rotations = len(rotations)
    # num_of_zeros = 0
    # for i in range(num_of_rotations):
    #     print(dial, " rotation: ", rotations[i], "zeros: ", num_of_zeros)
    #     rotation = rotate(rotations[i], dial)
    #     dial = rotation[0]
    #     num_of_zeros += rotation[1]
    #
    # print(dial)
    # print("num of zeros is: ", num_of_zeros)
    #
    # print("part 2")
    # ids = read_ranges_to_list("input_ids.txt")
    # print(ids)
    # sum = 0
    # for range_of_IDs in ids:
    #     invalids = IDs_finder(range_of_IDs)
    #     for j in range(len(invalids)):
    #         sum += invalids[j]
    #
    # print(sum)
    #
    # print("part 3")
    # banks = read_file_to_list("banks_input.txt")
    # sum = 0
    # for bank in banks:
    #     batteries_to_activate = find_twelve_largest_batteries(bank)
    #     final_digs = ''.join(batteries_to_activate)
    #     print("finale:", final_digs, '\n')
    #     sum += int(final_digs)
    #     print(batteries_to_activate)
    #
    # print("sum of batteries:", sum, "\n")
    #
    # print("part 4")
    # papers = read_file_to_list("input_papers.txt")
    # papers_matrix = []
    # for paper in papers:
    #     papers_matrix.append(divide_str(paper, 1))
    #
    # for paper_roll in papers_matrix:
    #     print(paper_roll)
    #
    # total_removed = 0
    # while True:
    #     how_many_accessible = find_out_how_many_papers_accessible(papers_matrix)[0]
    #     if how_many_accessible == 0:
    #         break
    #     removables = find_out_how_many_papers_accessible(papers_matrix)[1]
    #     removed_papers_metrix = remove_papers(papers_matrix, removables)
    #     papers_matrix = removed_papers_metrix
    #     total_removed += how_many_accessible
    # print("total_removed:", total_removed)
    #
    # print("day 5")
    # ingredients = read_file_to_list("input_ingredients.txt")
    # all_ranges, ids = split_into_ingredients_ranges_and_ids(ingredients)
    # all_ranges.sort()
    # print(all_ranges)
    #
    # # sum_of_fresh_ingredients = 0
    # # for id in ids:
    # #     if is_id_in_any_range(id, all_ranges):
    # #         sum_of_fresh_ingredients += 1
    # # print(sum_of_fresh_ingredients)
    #
    # sum_of_fresh_ids = 0
    # all_ranges_int = convert_str_ranges_to_int_ranges(all_ranges)
    # fresh_ids = []
    # for range_int in all_ranges_int:
    #     fresh_ids = add_range_to_list(fresh_ids, range_int)
    #
    # new_fresh_ids = []
    # while True:
    #
    #     first_len = len(new_fresh_ids)
    #     for range_num in fresh_ids:
    #         new_fresh_ids = add_range_to_list(new_fresh_ids, range_num)
    #     second_len = len(new_fresh_ids)
    #     if first_len == second_len:
    #         print("from while:", fresh_ids)
    #         print("first and second len:", first_len, second_len)
    #         fresh_ids = new_fresh_ids
    #         break
    #     fresh_ids = new_fresh_ids
    #
    #
    #
    # # print(fresh_ids)
    #
    # for range_int in fresh_ids:
    #     sum_of_fresh_ids += range_int[1] - range_int[0] + 1
    #
    # print(sum_of_fresh_ids)

    # print("day 6")
    # worksheet = read_file_to_list("input_worksheet.txt")
    # # print(worksheet)
    # for i in range(len(worksheet)):
    #     if worksheet[i][-1] == '\n':
    #         worksheet[i] = worksheet[i][:-1]
    # # print(worksheet)
    # operator_list = create_operator_arr(worksheet[-1])
    # # print(operator_list)
    # worksheet_solution = calc_line_with_operator(worksheet[:-1], operator_list)
    # print(worksheet_solution)
    # print(sum(worksheet_solution))
    #
    # # worksheets_lines = []
    # # for i in range(4):
    # #     line = worksheet[i].split(' ')
    # #     line_without_space = []
    # #     for element in line:
    # #         if element != '':
    # #             line_without_space.append(element)
    # #     worksheets_lines.append(line_without_space)
    # # for element in worksheets_lines:
    # #     print(element)
    # #
    # # reshaped_worksheet = order_sheet_by_numbers(worksheets_lines)
    # # print(reshaped_worksheet)
    #
    # # sum_of_all_worksheet = sum_lines_form_worksheet(worksheets_lines)
    # # print(sum_of_all_worksheet)

    # print("day 7")
    # teleporter_str = read_file_to_list("input_teleporter_copy.txt")
    # teleporter = []
    # for i in range(len(teleporter_str)):
    #     teleporter.append(list(teleporter_str[i]))
    #
    # for line in teleporter:
    #     print(line)
    # s_index = 0
    # for j in range(len(teleporter[0])):
    #     if teleporter[0][j] == 'S':
    #         s_index += 1
    #
    #
    # print("\n")
    # splits = teleporter_activate(teleporter)
    # print(splits)
    #
    # for line in teleporter:
    #     print(line)

    print("day 8")
