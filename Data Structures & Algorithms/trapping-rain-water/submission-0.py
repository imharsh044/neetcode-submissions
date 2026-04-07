class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        result = 0

        for idx in range(1, n):
            maxLeft[idx] = max(maxLeft[idx - 1], height[idx])
        
        for idx in range(n-2, 0, -1):
            maxRight[idx] = max(maxRight[idx + 1], height[idx])

        for idx in range(n):
            water = min(maxLeft[idx], maxRight[idx]) - height[idx]
            if water >= 0:
                result += water

        return result
