class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        target_map = {}

        for num, idx in enumerate(numbers, start=1):
            diff = target - num

            if diff in target_map:
                return [target_map[diff], idx]
            else:
                target_map[num] = idx