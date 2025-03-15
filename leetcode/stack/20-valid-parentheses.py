class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if not len(s)%2 == 0:
            return False
        
        if len(s) == 0:
            return True
        
        for char in s:
            if char == '[':
                stack.append(1)
            if char == '(':
                stack.append(2)
            if char == '{':
                stack.append(3)

            if char == ']':
                if(len(stack) > 0):
                    val = stack.pop() 
                    if not val == 1:    
                        return False
                else:
                    return False

            if char == ')':
                if len(stack) > 0:
                    val = stack.pop()
                    if not val == 2:
                        return False
                else:
                    return False

            if char == '}':
                if len(stack) > 0:
                    val = stack.pop()
                    if not val == 3:
                        return False
                else:
                    return False

            print(stack)

        if len(stack) == 0:
            return True   
        else:
            return False