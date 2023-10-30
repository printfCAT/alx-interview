#!/bin/usr/python3
""" define a function """


def validUTF8(data):
    """ checks if data passed is UTF-8 valid """
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow > 0:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_follow -= 1
        else:
            if (byte >> 7) == 0:
                bytes_to_follow = 0
            elif (byte >> 5) == 0b110:
                bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_follow = 3
            else:
                return False
    return True
