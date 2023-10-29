"""
Write a function to crush candy in one dimensional board. In candy crushing games, groups of like items are removed from the board. In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. This process should be repeated as many time as possible. You should greedily remove characters from left to right.
"""

def crush_candy(arr):

    # get the length of the input array
    l = len(arr)

    # create an empty stack to store each letter and its count
    results = []

    # add the first leter and its count into the results list
    results.append( [arr[0], 1] )

    # loop through the input array
    for i in range(1, l):

        prev = i-1
        
        # chec if value at current index is same as previous value in previous index
        # if not the same
        if arr[i] != arr[prev]:

            # check if the count of the previous value >= 3
            if results[-1][1] >= 3:

                # remove the element from the result stack
                results.pop() 
            
            # check if there is a value for value at the current index in the results array
            # if there is a value for the current index, incerase the cout
            if results and results[-1][0] == arr[i]:
                results[-1][1] += 1
            # if there is no value, create the entry
            else:
                results.append([arr[i], 1])

        # if the current and previous values are the same 
        else:
            results[-1][1] += 1

    
    # handle the remaining items in the results stack
    # using list comprehension
    leftovers = [ r[0] for r in results ]

    # using for loop
    lft = []
    for n in results:
        # n[0]
        lft.append(n[0])

    return ''.join(lft)

userInput = "aabbbacd"
print(crush_candy(userInput))



