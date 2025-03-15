class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for char in tokens:
            if char == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)

            elif char == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)

            elif char == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b/a)

            elif char == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)   
            else:
                stack.append(int(char))

        print(stack)
        return int(stack[0])