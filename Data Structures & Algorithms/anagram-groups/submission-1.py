class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create list of char frequency tuples
        anagrams = defaultdict(list)
        for s in strs:
            char_freqs = tuple(sorted((c, s.count(c)) for c in s))
            anagrams[char_freqs].append(s)
        
        return list(anagrams.values())