class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counter = dict()
        result = 0

        left = 0
        for right in range(len(s)):
            char_counter[s[right]] = 1 + char_counter.get(s[right], 0)

            if (right - left + 1) - max(char_counter.values()) > k:
                char_counter[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
