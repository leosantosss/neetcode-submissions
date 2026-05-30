class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        pairs = {']':'[','}':'{',')':'('}
        for p in s:
            if p in pairs:
                if stack and pairs[p] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(p)
        if stack:
            return False
        else:
            return True