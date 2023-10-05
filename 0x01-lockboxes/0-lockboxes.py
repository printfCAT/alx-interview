#!/usr/bin/python3
""" define a function """


def canUnlockAll(boxes):
    """ the lockbox problem """
    n = len(boxes)
    visited = [False] * n
    stack = [0]
    visited[0] = True

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                stack.append(key)
                visited[key] = True

    return all(visited)