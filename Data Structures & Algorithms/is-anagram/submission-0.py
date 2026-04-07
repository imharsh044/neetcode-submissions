class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_set = set(t)

        for ch in s:
            if ch not in t_set:
                return False

        return True
