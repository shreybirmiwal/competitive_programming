class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashset = {}

        for i in range(0, len(nums)):
            num = nums[i]

            if not num in hashset:
                hashset[num] = i

            else:
                if (i-hashset[num]) <= k:
                    return True

                hashset[num] = i

        return False