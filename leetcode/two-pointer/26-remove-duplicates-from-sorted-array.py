class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writePointer = 0
        seen = set()

        for i in range(len(nums)):

            if nums[i] not in seen:
                seen.add(nums[i])
                nums[writePointer] = nums[i]
                writePointer += 1

        return writePointer