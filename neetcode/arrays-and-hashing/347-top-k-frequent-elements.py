class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = {}
        for num in nums:
            occurances[num] = occurances.get(num, 0) + 1
        print(occurances)

        ar = [[] for _ in range(len(nums))]


        for key in occurances:
            print("key", key, "occurances[key]", occurances[key])
            print("cur val " , ar[occurances[key] -1])
            print("total ar", ar)
            temp = ar[occurances[key]-1]
            print("temp OG", temp)
            temp.append(key)
            print("temp post", temp)
            ar[occurances[key]-1] = temp
            print("ar post", ar)

        print(occurances)
        print(ar)
        
        out = []
        index = len(ar)-1
        while len(out) != k and not index < 0:
            if ar[index] != [None]:
                for item in ar[index]:
                    out.append(item)
            index -= 1
        
        return out


 
        