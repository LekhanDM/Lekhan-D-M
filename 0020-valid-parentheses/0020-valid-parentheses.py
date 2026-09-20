class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in "([{":
                stack.append(x)
            elif not stack or ")]}".index(x) != "([{".index(stack.pop()):
                return False
        return not stack