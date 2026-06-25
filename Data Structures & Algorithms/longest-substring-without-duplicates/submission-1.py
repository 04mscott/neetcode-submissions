class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 1
        max_len = 1

        seen = {s[l]}
        while l <= r and r < len(s):
            if s[r] not in seen:
                max_len = max(max_len, r - l + 1)
                seen.add(s[r])
                r += 1

            else:
                seen.discard(s[l])
                l += 1
            

        return max_len