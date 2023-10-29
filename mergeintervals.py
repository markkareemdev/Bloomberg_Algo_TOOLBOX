"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:

    # check the length of the list
    if len(intervals) < 2:
        return intervals

    # sort the list
    intervals.sort()

    # create an array to store the result
    result = []

    # loop through the remaining chars in the array
    for start, end in intervals[1:]:

        # check if the current start is greater than the previous end
        if start > result[-1][1]:

            # add the start and end of the current guy to the result
            result.append([start, end])

        # check if the end of the current guy is greater than the end of the previous guy
        elif end > result[-1][1]:
            
            # update the end of the previous guy
            result[-1][1] = end


