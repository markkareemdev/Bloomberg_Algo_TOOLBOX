"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""

def move_zeros(nums):

    l = len(nums)

    for i in range(l):

        if nums[i] == 0:
            nxt = i+1

            while nxt <= l-1:
                if nums[nxt] != 0:
                    nums[i] = nums[nxt]
                    nums[nxt] = 0
                    i = nxt
                    nxt = i+1
                else:
                    nxt += 1

    return nums


n = [0]
print(move_zeros(n))