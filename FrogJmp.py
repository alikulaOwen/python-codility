# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    diff = Y - X
    jumps = diff // D
    if X == Y:
        return 0
    else:
        if diff % D == 0:
            return jumps
        else:
            jumps += 1
    return jumps
    pass
