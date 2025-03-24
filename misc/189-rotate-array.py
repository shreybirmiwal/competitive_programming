class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        nums = [1,2,3,4,5,6,7], k = 3

        """

        seenIndex = set()
        oldvals = {}

        i = 0
        while True:

            i = i % (len(nums))

            if i in seenIndex:
                i+=1
                continue
            else:
                seenIndex.add(i)

                newIndex = (i + k)%(len(nums))

                oldvals[newIndex] = nums[newIndex]

                if i in oldvals:
                    nums[newIndex] = oldvals[i]
                else:
                    nums[newIndex] = nums[i]


               # print("i", i, "new i", newIndex)


                i = newIndex



            if len(seenIndex) == len(nums):
                return


           # print(nums, oldvals, seenIndex)
        