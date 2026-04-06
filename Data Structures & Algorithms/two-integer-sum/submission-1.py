class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = dict()
        result = []

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diff_map:
                result = [idx, diff_map[diff]] if idx < diff_map[diff] else [diff_map[diff], idx]
                break
            else:
                diff_map[num] = idx

        return result
