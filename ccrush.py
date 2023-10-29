"""
Write a function to crush candy in one dimensional board. In candy crushing games, groups of like items are removed from the board. In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. This process should be repeated as many time as possible. You should greedily remove characters from left to right.
"""

def crush_candy(arr):

    # get the length of the array
    l = len(arr)

    # create a results array to store the characters and their count
    results = []
    results.append([arr[0], 1])

    # loop through the original array starting from the first character (zeroth char already in results)
    for i in range(1, l):
        
        # get the previous index
        prev = i-1

        # check if curr and prev are the same
        if arr[i] != arr[prev]:

            # # check the prev guy in the result
            # if results[-1][0] != arr[prev]:

            # check if the value is >= 3# check the prev guy in the result
            # if r
            if results[-1][1] >= 3:
                results.pop()
            
            # check if the value already exists, add to it OR create its conunt
            if results and results[-1][0] == arr[i]:
                results[-1][1] += 1
            else:
                results.append([arr[i], 1])
        
        else:
            results[-1][1] += 1

    # check the count of the last element in results
    if results[-1][1] >= 3:
        results.pop()

    print(results)
    leftovers = [r[0] for r in results]
    return ''.join(leftovers)





a= 'aaabbbc'
s = crush_candy(a)
print(s)


