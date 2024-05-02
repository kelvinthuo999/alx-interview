#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def parse_line(line):
    parts = line.split()
    if len(parts) < 9:
        return None, None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if not (status_code.isdigit() and file_size.isdigit()):
        return None, None
    return status_code, int(file_size)

def main():
    total_size = 0
    status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line.strip())
            if status_code is None:
                continue
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        pass
    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
