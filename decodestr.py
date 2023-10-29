"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
"""

def decodestring(s):

    # find the length of the string
    n = len(s)

    # create a stack to store the decoded string
    stackk = []

    # loop through the original list
    for i in s:

        # get a variable to store the results in the bracket and the number multiplier
        results = ""
        num = ""

        # check if the current element is a closing bracket
        if i != ']':

            # add the element to the stack
            stackk.append(i)
        
        else:

            while stackk[-1] != '[':

                # create a variable to store the values being popped
                res = stackk.pop()
                results = res + results

            # remove the '['
            stackk.pop()

            while stackk and stackk[-1].isdigit():
                k_num = stackk.pop()
                num = str(k_num) + num

            stackk.append(int(num) * results)

    return ''.join(stackk)


m = "3[a]2[bc]"
print(decodestring(m))