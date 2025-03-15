class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]
        for i in range(0, len(nums)-1):
            prefix.append(prefix[i] * nums[i])

        print(prefix)

        # now add the final postfix
        mult_cur = 1
        for i in range(len(prefix)-2, -1, -1):
            print(prefix[i])
            mult_cur *= nums[i+1]
            prefix[i] *= mult_cur
            print(nums[i])

        return prefix
        