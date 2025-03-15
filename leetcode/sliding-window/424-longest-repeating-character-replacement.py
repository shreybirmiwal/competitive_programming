class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        lPoint = 0
        rPoint = 0
        counts = {}
        longestSub = 0
        counts[s[0]] = 1


        while True:
            most_common = 0
            for i in counts:
                most_common = max(most_common, counts[i])
                
            space = rPoint + 1 - lPoint
            isValid = (space-most_common) <= k
            
            if isValid:
                longestSub = max(longestSub, space)

                if (rPoint < len(s)-1):
                    rPoint += 1
                    counts[s[rPoint]] = counts.get(s[rPoint], 0) + 1
                else:
                    return longestSub
                
            else:
                counts[s[lPoint]] = counts[s[lPoint]] - 1
                lPoint += 1

        
