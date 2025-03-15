class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        leftPoint = 0
        rightPoint = len(heights)-1

        while True:
            if(leftPoint >= rightPoint):
                return maxArea
            
            maxArea = max(maxArea, (rightPoint-leftPoint)*min(heights[leftPoint], heights[rightPoint]))
            print((rightPoint-leftPoint), min(heights[leftPoint], heights[rightPoint]))

            if (heights[leftPoint] < heights[rightPoint]):
                leftPoint += 1
            else:
                rightPoint -= 1

        return maxArea       