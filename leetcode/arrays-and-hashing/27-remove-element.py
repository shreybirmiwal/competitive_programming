class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) == 0:
            return 0

        writeIndex = 0
        readIndex = 0

        count = 0

        while True:
            if nums[readIndex] == val:
                readIndex += 1
            else:
                count += 1
                nums[writeIndex] = nums[readIndex]
                readIndex += 1
                writeIndex += 1

            if readIndex == len(nums) or writeIndex == len(nums):
                return count


        