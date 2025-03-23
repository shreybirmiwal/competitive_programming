class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        if len(arr) == 0:
            return []

        if len(arr) == 1:
            return [-1]

        cur_max = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            old_curMax = cur_max
            cur_max = max(arr[i], cur_max) 

            arr[i] = old_curMax

        return arr

        