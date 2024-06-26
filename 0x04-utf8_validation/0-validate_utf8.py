#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Determines if a given data set represents
        a valid UTF-8 encoding """
    number_bytes = 0

    for byte in data:

        mask = 1 << 7

        if number_bytes == 0:

            while byte & mask:
                number_bytes += 1
                mask = mask >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False

        number_bytes -= 1

    return number_bytes == 0
