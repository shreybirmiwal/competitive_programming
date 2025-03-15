class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = []
        for i in range(len(height)):
            if i == 0:
                max_left.append(0)
            else:
                max_left.append(max(max_left[i-1], height[i-1]))

        max_right = []
        for i in range(len(max_left)):
            max_right.append(0)

        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                max_right[i] = 0
            else:
                max_right[i] = max(max_right[i+1], height[i+1])
        
        print(max_left)
        print(max_right)

        ret_sum = 0
        for i in range(len(max_left)):
            val = min(max_right[i], max_left[i]) - height[i]
            ret_sum += max(val, 0)

        return ret_sum
        