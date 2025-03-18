class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        leftIndex = 0
        rightIndex = len(nums)-1

        while True:

            print(nums[leftIndex:rightIndex+1])

            if len(nums[leftIndex:rightIndex+1]) == 1:
                if nums[leftIndex] == target:
                    return leftIndex
                else:
                    return -1
            elif len(nums[leftIndex:rightIndex+1]) < 1:
                return -1
    

            partionIndex = int((rightIndex-leftIndex)/2) + leftIndex
            partionValue = nums[partionIndex]

            print("partion index, value", partionIndex, partionValue)

            if target > partionValue:
                leftIndex = partionIndex + 1
                print("target > partion")
            elif target < partionValue:
                rightIndex = partionIndex-1
                print("Target < partion")
            else:
                print("target found")
                return partionIndex

