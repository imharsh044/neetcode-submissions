from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        result = []

        for key, freq in counter.items():
            if freq >= k:
                result.append(key)

        return result
