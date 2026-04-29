class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {')': '(', '}': '{', ']': '['}
        bracket_stack = []
        
        for char in s:
            if char in bracket_pairs:
                if bracket_stack and bracket_stack[-1] == bracket_pairs[char]:
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(char)
        
        return len(bracket_stack) == 0
