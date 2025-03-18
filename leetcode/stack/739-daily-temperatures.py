class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # initialize output array w 0s
        outputArray = []
        for i in range(len(temperatures)):
            outputArray.append(0)
        

        stack = []
        
        for i in range(0, len(temperatures)):
            temp_ar = [temperatures[i], i]

            while ((len(stack) != 0) and (stack[-1])[0] < temperatures[i] ):
                x = stack.pop()
                outputArray[x[1]] = i-x[1]
            stack.append(temp_ar)
        
        return outputArray