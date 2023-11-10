#!/usr/bin/python3
""" define a function """


import sys
import re
import signal

# Define a dictionary to store status code counts
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Variable to store the total file size
total_file_size = 0

# Variable to keep track of the line count
line_count = 0

# Function to print the metrics
def print_metrics():
    """ function to print the metrics """
    print("Total file size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")

# Signal handler for CTRL+C
def signal_handler(sig, frame):
    """ signal handler for CTRL+C """
    print_metrics()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Regular expression to match the input format
pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)')

try:
    for line in sys.stdin:
        # Attempt to match the line with the regular expression
        match = pattern.match(line)
        if match:
            ip_address, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()

except KeyboardInterrupt:
    print_metrics()
