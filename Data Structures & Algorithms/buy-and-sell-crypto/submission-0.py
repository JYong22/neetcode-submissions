class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        
        for r in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[r] - prices[l])

            while prices[l] > prices[r]:
                l+=1
        

        return maxProfit