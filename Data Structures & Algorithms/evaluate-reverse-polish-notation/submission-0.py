class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if not tokens: return 0

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                num1 = stack.pop()
                num2 = stack.pop()
                res = eval(f"{num1} {token} {num2}")
                stack.append(res)
            else:
                stack.append(token)

        return stack.pop()
