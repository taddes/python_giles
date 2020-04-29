"""
Example of Recursion


 |       |       |
 <>      |       |
 <=>     |       |
 <==>    |       |
 <===>   |       |
 <====>  |       |
=====================

-Three posts: source, spare, target
-n disks
-Disks are stacked largest (bottom) to smallest (top) and can only be in correct order
-Must move from source post to target post
a = [5, 4, 3, 2, 1]
b = []
c = []
"""


def hanoi(n, source, target, spare):
    global count
    if n > 0:
        # Move n-1 disks (all but bottom) from source tto spare, so they are out of the way
        hanoi(n - 1, source, spare, target)
        # Move the nth (last) disk from source to target
        target.append(source.pop())
        count += 1

        # Move the n - 1 disks from spare to target
        hanoi(n-1, spare, target, source)

num_moves = []
for x in range(1, 25):
    a = list(range(x, 0, -1))
    b = []
    c = []
    count = 0
    hanoi(x, a, b, c)
    num_moves.append(count)
print(num_moves)