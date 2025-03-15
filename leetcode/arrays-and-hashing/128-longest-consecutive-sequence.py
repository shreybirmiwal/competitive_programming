class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        map1 = {}
        for num in nums:
            map1[num] = 1
        
        max_val = 0
        for num in map1:
            if not (num-1) in map1:
                #candidate

                cur_sum = 0
                val = num
                while val in map1:
                    cur_sum += 1
                    val = val + 1
            
                if cur_sum > max_val:
                    max_val = cur_sum

        return max_val


        # map1 = {}

        # for num in nums:

        #     if num in map1:
        #         continue

        #     elif num+1 in map1 and num-1 in map1:
        #         print("BOTH", num)
        #         map1[num+1] = map1[num+1] + map1[num-1] + 1
        #         map1[num-1] = map1[num+1]
        #         map1[num] = map1[num+1]
            
        #     elif num+1 in map1:
        #         print("+1", num)
        #         map1[num+1] = map1[num+1]
        #         map1[num] = map1[num+1]
            
        #     elif num-1 in map1:
        #         print("-1", num)
        #         map1[num-1] = map1[num-1]
        #         map1[num] = map1[num-1]
            
        #     else:
        #         print("neither", num)
        #         map1[num] = 1

        #     print(map1)
        
        # print(map1)
        # maxval = 0
        # for keys in map1:
        #     if map1[keys] > maxval:
        #         maxval = map1[keys]


        # return maxval