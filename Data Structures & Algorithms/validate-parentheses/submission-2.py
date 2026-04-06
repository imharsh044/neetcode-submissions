class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_pairs.keys():
                curr_brace = bracket_pairs[char]
                if len(stack) > 0 and stack[-1] == curr_brace:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
