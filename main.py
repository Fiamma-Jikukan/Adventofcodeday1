import os


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



if __name__ == '__main__':
    print("hahaha")
    rotations = read_file_to_list("input_rotations.txt")
    print(rotations)