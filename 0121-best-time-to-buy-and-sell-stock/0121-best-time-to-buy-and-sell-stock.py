class Solution(object):
    def maxProfit(self, prices):
        lowestValue = prices[0]
        maxProfit = 0

        for i in prices:
            if i < lowestValue:
                lowestValue = i

            if i - lowestValue > maxProfit:
                maxProfit = i - lowestValue
            
        return(maxProfit)