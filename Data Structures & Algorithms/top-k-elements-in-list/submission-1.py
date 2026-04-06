from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] * i for i in range(len(nums) + 1)]

        for key, count in counter.items():
            freq[count].append(key)

        result = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
