'''Find the best times to buy and sell a stock. You have an array for which the ith element is the price of a given stock on day "i". If you are only allowed to 
buy one share of the stock and sell one 
share of the stock, make a program to find the best times to buy and sell.'''




# Python3 implementation of the approach
 
# Function to return the maximum profit
# that can be made after buying and
# selling the given stocks


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        lp, p = prices[0], 0
      
        for i in range(1, len(prices)):
            p = max(p, prices[i]-lp)
            lp = min(lp, prices[i])
                
        return p
