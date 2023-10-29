class Solution:
    def minSteps(self, s: str, t: str) -> int:
        import collections 
        memo = collections.defaultdict(int)
        # saving the number of occurance of characters in s
        for char in s:
            memo[char] += 1
			
        count = 0
        for char in t:
            if memo[char]:
                memo[char] -=1   # if char in t is also in memo, substract that from the counted number
            else:
                count += 1
        # return count #or
        return sum(memo.values())