class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in {'-','+','/','*'}:
                stack.append(int(s))
            else:
                first = stack[-1]
                second = stack[-2]
                if s == '+':
                    stack.pop()
                    stack.pop()
                    stack.append(second + first)
                elif s == '-':
                    stack.pop()
                    stack.pop()
                    stack.append(second - first)
                elif s == '*':
                    stack.pop()
                    stack.pop()
                    stack.append(second * first)
                elif s == '/':
                    stack.pop()
                    stack.pop()
                    stack.append(int(second / first))

        return stack[-1]