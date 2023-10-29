

def crush_candy(arr):


    # get the length of the array
    l = len(arr)
    
    # create an empty array to store reults
    results = []
    
    # add the first element of the array with its count
    results.append([arr[0], 1])

    # loop through the original array
    for i in range(1, l):

        # get the index of the previous element
        prev = i-1

        # check if prev and current are the same

        # not same
        if arr[i] != arr[prev]:

            # check if count > 3
            if results[-1][1] >= 3:
                results.pop()

            if results and results[-1][0] == arr[i]:
                results[-1][1] += 1
            else:
                results.append([arr[i], 1])

        else:

            results[-1][1] += 1

    if results[-1][1] >= 3:
        results.pop()

    leftovers = [r[0] for r in results]
    c = ''.join(leftovers)
    return c






a= 'aabbccddeeedcbazz'
s = crush_candy(a)
print(s)