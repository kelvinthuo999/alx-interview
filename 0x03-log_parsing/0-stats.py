#!/usr/bin/python3
'''function to parse log'''

import sys
import signal


def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def parse_line(line):
    parts = line.split()
    if len(parts) < 9 or parts[8] != '"GET' or not parts[7].isdigit():
        return None, None
    return int(parts[7]), int(parts[8])

def main():
    total_size = 0
    status_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            file_size, status_code = parse_line(line)
            if file_size is None:
                continue

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
