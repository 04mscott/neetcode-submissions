from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            s_dict = defaultdict(int)
            for c in s:
                s_dict[c] += 1
            char_freqs = tuple(sorted((c, v) for c, v in s_dict.items()))
            anagrams[char_freqs].append(s)
        
        return list(anagrams.values())