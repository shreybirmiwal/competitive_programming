class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        leftPointer = 0
        rightPointer = len(s)-1

        while leftPointer < rightPointer:
            while(not s[leftPointer].isalnum() and leftPointer < rightPointer):
                leftPointer += 1

            while(not (s[rightPointer]).isalnum() and leftPointer < rightPointer):
                rightPointer -= 1

            print(s[leftPointer], "-", s[rightPointer])

            if not s[leftPointer] == s[rightPointer]:
                return False
            
            leftPointer += 1
            rightPointer -=1 

        return True

        