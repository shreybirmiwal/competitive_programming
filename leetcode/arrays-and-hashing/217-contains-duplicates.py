class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for num in nums:
            if num in x:
                return True

            x.add(num)

        return False
         