class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        search_perm = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0,'z':0}
        for char in s1:
            search_perm[char] = search_perm[char] + 1

        for i in range(0, len(s2)-len(s1)+1):
            print("sub", s2[i:i+len(s1)])
            cur_perm = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0,'z':0}

            for char in s2[i:i+len(s1)]:
                cur_perm[char] = cur_perm[char]+1
            
            if cur_perm == search_perm:
                return True
        
        return False