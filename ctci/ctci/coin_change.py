class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        x =self.helper(coins,amount,memo=dict())
        if x == None:
            return -1
        return len(x)
        
    def helper(self,coins,amount,memo):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return []
        if amount < 0:
            return None
        shortest = None
        for num in coins:
            rem = amount - num
            l = self.helper(coins,rem,memo)
            if l is not None:
                comb=l+[num]
                if not shortest or shortest and len(comb)<len(shortest):
                    shortest = comb
        memo[amount] = shortest
        return memo[amount]