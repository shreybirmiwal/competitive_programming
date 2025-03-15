class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        overal_dict = {}
        for word in strs:
            cur_dict = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for char in word:
                cur_dict[ord(char)-96] = cur_dict[ord(char)-96] + 1
            
            if(tuple(cur_dict) in overal_dict):
                overal_dict[tuple(cur_dict)].append(word)
            else:
                overal_dict[tuple(cur_dict)] = []
                overal_dict[tuple(cur_dict)].append(word)


        
        ar = []
        for key in overal_dict:
            ar.append(overal_dict[key])


        return ar
        