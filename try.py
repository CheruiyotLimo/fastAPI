import re

def maxProfit(prices: list[int]) -> int:
        k, j = 0, 0
        for i in range(len(prices)):
            if prices[i] <= prices[k]:
                k = i
                j = i
            
        for x in range(j+1, len(prices)):
            if prices[x] >= prices[j]:
                j = x
        
        if prices[k] == prices[j]:
            return 0
        return prices[j] - prices[k]

print(maxProfit(prices = [2, 1, 4, 1]))