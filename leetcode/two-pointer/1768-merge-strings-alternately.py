class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l = 0
        r = 0
        out = ""

        for i in range(0, min(len(word1), len(word2))):
            out += word1[i]
            out += word2[i]

        
        if len(word1) > len(word2):
            out += word1[len(word2):]

        else:
            out += word2[len(word1):]

        return out