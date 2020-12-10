#!/usr/bin/python3


def canUnlockAll(boxes):

    canUnlockAll = False
    keys = {0: True}
    n_boxes = len(boxes)
    while(True):

        n_keys = len(keys)

        for box in range(len(boxes)):
            if boxes[box] and keys.get(box, False):
                for key in boxes[box]:
                    if key < n_boxes:
                        keys[key] = True
                    boxes[box] = None

        if not(len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
