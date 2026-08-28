class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedP = {']': '[', '}': '{', ')': '('}

        for c in s:
            if c in closedP:
                if stack and stack[-1] == closedP[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False