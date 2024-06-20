#!/usr/bin/python3
""" A script for parsing HTTP request logs. """
import re


def group_input(line):
    """ Groups sections of a line of an HTTP request log. """
    gp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    ret = {
        'status_code': 0,
        'file_size': 0,
    }
    pattern = '{}\\-{}{}{}{}\\s*'.format(gp[0], gp[1], gp[2], gp[3], gp[4])
    matched = re.fullmatch(pattern, line)
    if matched:
        status_code = matched.group('status_code')
        file_size = int(matched.group('file_size'))
        ret['status_code'] = status_code
        ret['file_size'] = file_size
    return ret


def print_statistics(total_file_size, status_codes_stats):
    """ Prints accumulated statistics of the HTTP request log """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """ Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    """
    info = group_input(line)
    status_code = info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + info['file_size']


def main():
    """ Starts the log parser. """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    main()
