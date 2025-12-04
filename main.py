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

    print("part 3")
    banks = read_file_to_list("banks_input.txt")
    sum = 0
    for bank in banks:
        batteries_to_activate = find_twelve_largest_batteries(bank)
        final_digs = ''.join(batteries_to_activate)
        print("finale:", final_digs, '\n')
        sum += int(final_digs)
        print(batteries_to_activate)

    print("sum of batteries:", sum, "\n")
