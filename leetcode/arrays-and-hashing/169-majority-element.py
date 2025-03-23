class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority_map = {}

        for num in nums:
            majority_map[num] = majority_map.get(num, 0) + 1

            if float(majority_map[num]) > (len(nums)/2):
                return num

        return 0
        