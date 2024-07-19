class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        minimum=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-minimum 
            maximum=max(profit,maximum)
            minimum=min(minimum,prices[i])
        return maximum 