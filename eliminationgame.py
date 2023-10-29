"""
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

    Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
    Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
    Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer n, return the last number that remains in arr.
"""

def elimination_game(n: int):

    # get the left and right index
    l = 1
    r = n

    # initialize a step
    step = 1

    # initialize a turn
    turn = True

    # as long as the integer is +ve
    while n > 1:

        # start from the left
        if turn:
            
            # increase the left side by the step
            l += step

            # take care of the right side
            if n%2:

                # reduce the right side by the step
                r -= step
            else:
                r = r

        # move to the right side
        else:

            # reduce the right side by the step
            r -= step

            # take care of the left side
            if n%2:

                # increase the left side by the step
                l += step

            else:
                l = l

        # flip the turn
        turn = not turn

        # for every move, reduce the value of n
        n = n//2

        # for every move, increase the step
        step *= 2

    return l

print(elimination_game(0))