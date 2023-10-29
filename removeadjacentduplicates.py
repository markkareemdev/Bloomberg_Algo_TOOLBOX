"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
"""


def removeDuplicates(s: str, k: int) -> str:

    # create a stack to store the character and the count
    stk = []

    # loop through the characters in the string
    for i in s:

        # check if the stack exists AND if the last elemnt is the current character
        if stk and stk[-1][0] == i:
            stk[-1][1] += 1
        else:
            stk.append([i, 1])

        if stk[-1][1] == k:
            stk.pop()

    leftovers = [r*n for r,n in stk]
    return ''.join(leftovers)

s = "deeedbbcccbdaa"
k = 3

print(removeDuplicates(s, k))