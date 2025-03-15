class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_of_visited = {}
        for i in range(len(nums)):
            num = nums[i]
            target_sum = target - num
            if target_sum in map_of_visited:
                return [map_of_visited[target_sum], i]
            else:
                map_of_visited [num] = i

        return