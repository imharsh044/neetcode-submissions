class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for element in strs:
            anagram_key = ''.join(sorted(element))

            if anagram_key in anagram_dict:
                anagram_dict[anagram_key].append(element)
            else:
                anagram_dict[anagram_key] = [element]

        return list(anagram_dict.values())
