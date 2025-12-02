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


if __name__ == '__main__':
    rotations = read_file_to_list("input_rotations.txt")
    num_of_rotations = len(rotations)
    num_of_zeros = 0
    for i in range(num_of_rotations):
        print(dial, " rotation: ", rotations[i], "zeros: ", num_of_zeros)
        rotation = rotate(rotations[i], dial)
        dial = rotation[0]
        num_of_zeros += rotation[1]

    print(dial)
    print("num of zeros is: ", num_of_zeros)
