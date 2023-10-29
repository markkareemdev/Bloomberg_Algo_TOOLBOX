"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

def move_zeroes(arr):


    # get the length of the array
    l = len(arr)

    # loop through the array
    for i in range(l-1):

        # check if the element at the index is 0
        if arr[i] == 0:
            nxt = i+1
            while nxt <= l-1:
                if arr[nxt] != 0:
                    arr[i] =  arr[nxt]
                    arr[nxt] = 0

                    i = nxt
                    nxt = i+1
                else:
                    nxt += 1


    return arr

inputnums = [0,100,1,0,3,99,0,13,12]
print(move_zeroes(inputnums))