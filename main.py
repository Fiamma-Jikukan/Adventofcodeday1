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
    top_range = range_IDs[dash_index+1:]
    return int(bottom_range), int(top_range)

def is_valid_id(id):
    id_str = str(id)
    if len(id_str) % 2 != 0:
        return True
    half_point = int(len(id_str) / 2)
    for i in range(half_point):
        if id_str[i] != id_str[half_point + i]:
            return True
    return False

def IDs_finder(range_IDs):
    top_and_bottom = find_top_and_bottom(range_IDs)
    top_range = top_and_bottom[1]
    bottom_range = top_and_bottom[0]
    invalid_ids = []
    for i in range(bottom_range, top_range+1):
        valid_id = is_valid_id(i)
        if not valid_id:
            invalid_ids.append(i)
    return invalid_ids





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
    print("part 2")
    ids = read_ranges_to_list("input_ids.txt")
    print(ids)
    sum = 0
    for range_of_IDs in ids:
        invalids = IDs_finder(range_of_IDs)
        print(invalids)
        for j in range(len(invalids)):
            sum += invalids[j]

    print(sum)

