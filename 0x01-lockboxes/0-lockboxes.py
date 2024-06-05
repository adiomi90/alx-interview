#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    keys = [0]
    keys_set = set(keys)
    [keys.append(boxKey) for key in keys
        for boxKey in boxes[key]
        if boxKey not in keys_set and boxKey < len(boxes)
        and not keys_set.add(boxKey)]
    return len(keys_set) == len(boxes)
