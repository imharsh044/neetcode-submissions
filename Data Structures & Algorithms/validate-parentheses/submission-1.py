class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_pairs and len(stack) > 0:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0
