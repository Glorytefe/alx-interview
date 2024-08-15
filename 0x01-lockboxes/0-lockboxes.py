#!/usr/bin/python3

"""
Lockboxes
"""


def canUnlockAll(boxes):
    n = len(boxes)
    opened_boxes = set([0])
    keys = boxes[0][:]

    while len(keys):
        key = keys.pop()
        if key < n and key not in opened_boxes:
            new_keys = boxes[key]
            keys.extend(new_keys)
            opened_boxes.add(key)
            if len(opened_boxes) == n:
                return True

    return n == len(opened_boxes)
