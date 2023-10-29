"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def bestbuy(prices):

    # get the length of the array
    n = len(prices)

    # initialize a maxprofit
    maxprofit = 0

    # loop through the prices array
    for i in range(n-1):
        
        # get the index of the next guy
        nxt = i+1

        # get your values
        buy = prices[i]
        sell = prices[nxt]

        # do the algorithm
        while nxt <= n-1:
            profit = sell - buy
            if profit > maxprofit:
                maxprofit = profit
            if nxt == n-1:
                break
            nxt += 1
            sell = prices[nxt]

    return maxprofit

inputPrices = [7, 1, 5, 3, 6, 4, 19]
print(bestbuy(inputPrices))
            

            
# """
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# """


# def bestbuy(prices):

#     # get the length of the array
#     n = len(prices)

#     # initialize a maxprofit
#     maxprofit = 0

#     # loop through the prices array
#     for i in range(n):
        
#         # get the index of the next guy
#         nxt = i+1

#         # get your values
#         buy = prices[i]
#         sell = prices[nxt]

#         while nxt <= n:
#             if buy <= sell:
#                 profit = sell - buy
#                 if profit > maxprofit:
#                     maxprofit = profit
#                 if nxt == n:
#                     break
#                 nxt += 1
#                 sell = prices[nxt]
#             else:
#                 nxt += 1
#                 if nxt == n:
#                     break
#                 sell = prices[nxt]
                


#     return maxprofit

# inputPrices = [7, 1, 5, 3, 6, 4]
# print(bestbuy(inputPrices))
            

            