class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        leftPoint = 0
        rightPoint = len(numbers)-1
        sum_ = numbers[leftPoint] + numbers[rightPoint]

        while ( not sum_ == target):
            if sum_ < target:
                leftPoint += 1
            if sum_ > target:
                rightPoint -= 1

            sum_ = numbers[leftPoint] + numbers[rightPoint]

        return [leftPoint+1, rightPoint+1]
        