class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        
        if len(prices) <= 1:
            return profit
        

        pointL = 0
        pointR = 1
        profit = 0

        while(True):

            profit = max(prices[pointR]-prices[pointL], profit)

            if( prices[pointL] > prices[pointR]):
                pointL = pointR    


            elif (pointR < len(prices)-1):
                pointR += 1
                
            else:

                return profit        