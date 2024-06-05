#!/usr/bin/python3
"""Script to unlock a list of lists."""


def can_unlock_all(boxes):
    """Determine if all boxes can be unlocked.
    
    Arguments:
    boxes -- a list of lists where each sublist contains keys to other boxes

    Returns:
    True if all boxes can be unlocked, False otherwise.
    """
    keys = [0]
    keys_set = set(keys)
    [
        keys.append(boxKey) 
        for key in keys
        for boxKey in boxes[key]
        if boxKey not in keys_set and boxKey < len(boxes) 
        and not keys_set.add(boxKey)
    ]
    return len(keys_set) == len(boxes)
