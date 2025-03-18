class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix[0]) == 0:
            return False

        
        subArrayIndex = 0
        lPoint = 0
        rPoint = len(matrix)-1
        while True:

            middleIndex = int((rPoint-lPoint)/2) + lPoint
            middleValueMin = matrix[middleIndex][0]
            middleValueMax = matrix[middleIndex][-1]
 
            if middleValueMin <= target and middleValueMax >= target:
                subArrayIndex = middleIndex
                break
            
            if target < middleValueMin:
                rPoint = middleIndex - 1

            if target > middleValueMax:
                lPoint = middleIndex + 1

            if (lPoint == rPoint):
                subArrayIndex = lPoint
                break
        

        print(subArrayIndex)

        nums = matrix[subArrayIndex]
        lPoint = 0
        rPoint = len(nums)-1
        
        while True:
            middleIndex = int((rPoint - lPoint - 1)/2) + lPoint
            middleVal = nums[middleIndex]

            if middleVal == target:
                return True

            if middleVal > target:
                rPoint = middleIndex -1

            if middleVal < target:
                lPoint = middleIndex + 1

            if (rPoint - lPoint) == 1:
                if nums[lPoint] == target:
                    return True
                else:
                    return False 