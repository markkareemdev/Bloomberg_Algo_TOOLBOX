"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List


def coin_change(coins: List, amount):
    print(coins)
    l = len(coins)

    t_coins = []
    coins.sort(reverse=True)

    for coin in coins:
        while amount >= coin and amount >= 0:
            # print(amount)
            # print(coin)
            amount -= coin
            t_coins.append(coin)


    if amount == 0:
        return(len(t_coins))
    else:
        return -1

input_coins = [1,2,5]
input_amount = 264
coinnchangee = coin_change(input_coins, input_amount)
print(coinnchangee)
    