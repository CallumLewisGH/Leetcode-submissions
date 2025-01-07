public class Solution {
    public int MaxProfit(int[] prices)
    {
        int maxProfit = 0;
        for(int sell = 1, buy = 0; sell < prices.Length; sell++)
        {
            if(prices[buy] < prices[sell])
            {
               maxProfit = prices[sell] - prices[buy] > maxProfit ? prices[sell] - prices[buy] : maxProfit;  
            }
            else
            {
                buy = sell;
            }
        }
        return maxProfit;
    }
}