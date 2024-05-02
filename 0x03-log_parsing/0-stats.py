#!/usr/bin/python3
'''function to parse log'''

import sys


def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print(f"File size: {total_file_size}")
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print(f"{key}: {val}")


def process_lines(lines):
    total_file_size = 0
    code = 0
    counter = 0
    dict_sc = {"200": 0,
               "301": 0,
               "400": 0,
               "401": 0,
               "403": 0,
               "404": 0,
               "405": 0,
               "500": 0}

    for line in lines:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if code in dict_sc:
                    dict_sc[code] += 1

            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

    if counter != 0:
        print_msg(dict_sc, total_file_size)


if __name__ == "__main__":
    try:
        process_lines(sys.stdin)
    except KeyboardInterrupt:
        pass
