class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s) == 0 or len(s) == 1:
            return len(s)

        current_set = set(s[0])

        lPoint = 0
        rPoint = 0
        largestSub = 0

        while True:

            print("current set", s[lPoint: rPoint+1])
            print("current_set ar", current_set)
            
            if len(s) > rPoint+1:
                if s[rPoint+1] not in current_set:
                    current_set.add(s[rPoint+1])
                    rPoint += 1
                    largestSub = max(largestSub, rPoint+1-lPoint)

                else:
                    # we need to move l point
                    largestSub = max(largestSub, rPoint+1-lPoint)
                    
                    while s[rPoint+1] in current_set:
                        current_set.remove(s[lPoint])
                        lPoint += 1
                    

            else:
                return largestSub


        