class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = dict()
        counter_t = dict()

        for char in s:
            counter_s[char] = counter_s.get(char, 0) + 1
        
        for char in t:
            counter_t[char] = counter_t.get(char, 0) + 1

        for char_key in counter_s:
            if counter_t.get(char_key) != counter_s[char_key]:
                return False

        return True
