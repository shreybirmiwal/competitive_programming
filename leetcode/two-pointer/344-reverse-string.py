class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0 or len(s) ==1:
            return s

        l = 0
        r = len(s)-1

        while l <r:

            oldL = s[l]
            s[l] = s[r]
            s[r] = oldL

            l+=1
            r-=1
