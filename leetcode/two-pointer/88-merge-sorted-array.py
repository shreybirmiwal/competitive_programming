class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ar1 = nums1[0:m]

        nums1_pointer = 0
        nums2_pointer = 0

        for i in range(0, len(nums1)):
            
            if nums1_pointer < m and nums2_pointer < n:

                if ar1[nums1_pointer] < nums2[nums2_pointer]:
                    nums1[i] = ar1[nums1_pointer]
                    nums1_pointer += 1
                else:
                    nums1[i] = nums2[nums2_pointer]
                    nums2_pointer += 1
            
            elif nums1_pointer < m:
                nums1[i] = ar1[nums1_pointer]
                nums1_pointer += 1

            elif nums2_pointer < n:
                nums1[i] = nums2[nums2_pointer]
                nums2_pointer += 1

            else:
                return