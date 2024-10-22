#!/usr/bin/python3
import sys
import re

# Dictionary to store status code counts
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

# Regular expression to match log format
log_pattern = r'(\d+\.\d+\.\d+\.\d+) - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'

def print_stats():
    """Prints the statistics collected so far."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

try:
    for line in sys.stdin:
        match = re.match(log_pattern, line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            total_file_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle the case when CTRL + C is pressed
    print_stats()
    sys.exit(0)

# Print stats at the end if the loop completes
print_stats()
