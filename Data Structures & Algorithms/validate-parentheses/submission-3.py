class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        thisDict = {']': '[', '}': '{', ')': '('}

        for c in s:
            if stack and c in thisDict and stack[-1] == thisDict[c]:
                print(stack[-1])
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
        